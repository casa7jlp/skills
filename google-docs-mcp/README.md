# google-docs-mcp

Servidor **MCP** próprio que edita Google Docs **no lugar** (in-place), usando a
API oficial do Google Docs (`documents.batchUpdate`). Resolve a limitação do
conector nativo do Claude, que só lê e cria arquivos novos.

👉 **Para instalar sem saber programar, siga o [PASSO-A-PASSO.md](./PASSO-A-PASSO.md).**

## Ferramentas expostas

| Ferramenta     | O que faz                                              |
| -------------- | ------------------------------------------------------ |
| `find_docs`    | Procura documentos pelo nome                           |
| `read_doc`     | Lê o texto de um documento                             |
| `replace_text` | Acha um trecho e troca por outro (edição no lugar)     |
| `append_text`  | Adiciona texto ao final do documento                   |
| `insert_text`  | Insere texto numa posição específica                   |
| `create_doc`   | Cria um documento novo                                 |

## Resumo técnico

- **Linguagem:** Python (SDK `mcp` / FastMCP).
- **Auth:** OAuth de aplicativo Desktop (`InstalledAppFlow`). Login feito uma vez
  com `python authorize.py`, token salvo em `token.json`.
- **Escopos:** `documents` (editar Docs) e `drive` (procurar arquivos).
- **Transporte:** stdio — pensado para o Claude Desktop. Para usar no Claude web
  seria preciso hospedar como servidor remoto com OAuth.

## Arquivos

- `server.py` — o servidor MCP e as ferramentas.
- `authorize.py` — faz o login do Google uma vez e gera `token.json`.
- `requirements.txt` — dependências.
- `credentials.json` — **você baixa do Google** (não vai para o git).
- `token.json` — gerado no primeiro login (não vai para o git).

## Instalação rápida (para quem já manja)

```bash
pip install -r requirements.txt
# coloque o credentials.json (OAuth Desktop) nesta pasta
python authorize.py
# adicione ao claude_desktop_config.json apontando para server.py
```
