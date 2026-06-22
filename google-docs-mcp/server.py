"""
Conector próprio (MCP) para editar Google Docs DIRETO no Drive.

Diferente do conector nativo do Claude (que só lê e cria arquivo novo),
este servidor usa a API oficial do Google Docs (documents.batchUpdate),
então ele edita o documento NO LUGAR, mantendo o mesmo link.

Ferramentas disponíveis para o Claude:
  - find_docs:     procura documentos pelo nome
  - read_doc:      lê o texto de um documento
  - replace_text:  acha um trecho e troca por outro (edição no lugar)
  - append_text:   adiciona texto no final do documento
  - insert_text:   insere texto numa posição específica
  - create_doc:    cria um documento novo

Configuração por variáveis de ambiente (opcional):
  GOOGLE_CREDENTIALS_FILE  -> caminho do credentials.json (padrão: ao lado deste arquivo)
  GOOGLE_TOKEN_FILE        -> onde guardar o login (padrão: token.json ao lado deste arquivo)
"""

import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from mcp.server.fastmcp import FastMCP

# Permissões pedidas ao Google: editar Docs + procurar arquivos no Drive.
SCOPES = [
    "https://www.googleapis.com/auth/documents",
    "https://www.googleapis.com/auth/drive",
]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CREDENTIALS_FILE = os.environ.get(
    "GOOGLE_CREDENTIALS_FILE", os.path.join(BASE_DIR, "credentials.json")
)
TOKEN_FILE = os.environ.get(
    "GOOGLE_TOKEN_FILE", os.path.join(BASE_DIR, "token.json")
)

mcp = FastMCP("google-docs")

# Cache simples dos serviços do Google para não reconstruir a cada chamada.
_services = {}


def _get_credentials() -> Credentials:
    """Carrega o login salvo ou abre o navegador para autorizar na primeira vez."""
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(CREDENTIALS_FILE):
                raise RuntimeError(
                    f"Não encontrei o arquivo de credenciais em '{CREDENTIALS_FILE}'. "
                    "Siga o PASSO-A-PASSO.md para baixar o credentials.json do Google."
                )
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, "w") as f:
            f.write(creds.to_json())
    return creds


def _docs():
    if "docs" not in _services:
        _services["docs"] = build("docs", "v1", credentials=_get_credentials())
    return _services["docs"]


def _drive():
    if "drive" not in _services:
        _services["drive"] = build("drive", "v3", credentials=_get_credentials())
    return _services["drive"]


@mcp.tool()
def find_docs(name_contains: str = "", limit: int = 10) -> str:
    """Procura documentos Google Docs pelo nome.

    name_contains: parte do nome do documento (deixe vazio para listar os mais recentes).
    limit: quantos resultados retornar.
    """
    query = "mimeType='application/vnd.google-apps.document' and trashed=false"
    if name_contains:
        safe = name_contains.replace("'", "\\'")
        query += f" and name contains '{safe}'"
    result = (
        _drive()
        .files()
        .list(
            q=query,
            pageSize=limit,
            fields="files(id,name,modifiedTime)",
            orderBy="modifiedTime desc",
        )
        .execute()
    )
    files = result.get("files", [])
    if not files:
        return "Nenhum documento encontrado."
    return "\n".join(f"- {f['name']} (id: {f['id']})" for f in files)


@mcp.tool()
def read_doc(document_id: str) -> str:
    """Lê e devolve o texto de um documento Google Docs."""
    doc = _docs().documents().get(documentId=document_id).execute()
    parts = []
    for element in doc.get("body", {}).get("content", []):
        paragraph = element.get("paragraph")
        if not paragraph:
            continue
        for run in paragraph.get("elements", []):
            text = run.get("textRun", {}).get("content")
            if text:
                parts.append(text)
    return "".join(parts) or "(documento vazio)"


@mcp.tool()
def replace_text(
    document_id: str, find: str, replace: str, match_case: bool = False
) -> str:
    """Acha um trecho de texto e troca por outro, NO LUGAR (mesmo documento/link).

    find: o texto exato que você quer substituir.
    replace: o texto novo.
    match_case: True para diferenciar maiúsculas/minúsculas.
    """
    requests = [
        {
            "replaceAllText": {
                "containsText": {"text": find, "matchCase": match_case},
                "replaceText": replace,
            }
        }
    ]
    result = (
        _docs()
        .documents()
        .batchUpdate(documentId=document_id, body={"requests": requests})
        .execute()
    )
    changed = (
        result.get("replies", [{}])[0]
        .get("replaceAllText", {})
        .get("occurrencesChanged", 0)
    )
    if not changed:
        return f'Não encontrei o texto "{find}" no documento. Nada foi alterado.'
    return f'Pronto! {changed} ocorrência(s) de "{find}" trocada(s) por "{replace}".'


@mcp.tool()
def append_text(document_id: str, text: str) -> str:
    """Adiciona texto no FINAL do documento, mantendo o resto intacto."""
    doc = _docs().documents().get(documentId=document_id).execute()
    content = doc.get("body", {}).get("content", [])
    end_index = content[-1].get("endIndex", 1) if content else 1
    insert_at = max(1, end_index - 1)
    requests = [{"insertText": {"location": {"index": insert_at}, "text": text}}]
    _docs().documents().batchUpdate(
        documentId=document_id, body={"requests": requests}
    ).execute()
    return "Texto adicionado ao final do documento."


@mcp.tool()
def insert_text(document_id: str, text: str, index: int = 1) -> str:
    """Insere texto numa posição específica (index 1 = começo do documento)."""
    requests = [{"insertText": {"location": {"index": max(1, index)}, "text": text}}]
    _docs().documents().batchUpdate(
        documentId=document_id, body={"requests": requests}
    ).execute()
    return f"Texto inserido na posição {index}."


@mcp.tool()
def create_doc(title: str, text: str = "") -> str:
    """Cria um documento Google Docs novo e devolve o link."""
    doc = _docs().documents().create(body={"title": title}).execute()
    doc_id = doc["documentId"]
    if text:
        _docs().documents().batchUpdate(
            documentId=doc_id,
            body={"requests": [{"insertText": {"location": {"index": 1}, "text": text}}]},
        ).execute()
    return (
        f"Documento criado: {title}\n"
        f"Link: https://docs.google.com/document/d/{doc_id}/edit"
    )


if __name__ == "__main__":
    mcp.run()
