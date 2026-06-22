# 👶 Passo a passo (nível criança de 5 anos)

Este guia liga o conector que **edita seus Google Docs direto no Drive**, igual
sua sócia faz. Eu (Claude) já escrevi todo o programa. O que falta é a parte que
**só você pode fazer**: pegar a "chave" do Google e plugar no aplicativo.

> ⏱️ Leva uns **20 a 30 minutos** na primeira vez. Depois é pra sempre.
>
> 💻 Isso funciona no **Claude para computador (Claude Desktop)**, não no Claude
> do navegador. No final eu explico por quê.

Vá com calma, um passo de cada vez. Se travar em algum, me chama e me diz em qual
número você parou.

---

## PARTE 1 — Instalar o "motor" (Python) no computador

O programa que escrevi roda em cima do **Python**. É de graça.

1. Abra o site: **https://www.python.org/downloads/**
2. Clique no botão grande amarelo **"Download Python"**.
3. Abra o arquivo que baixou.
4. **MUITO IMPORTANTE (Windows):** na primeira tela, marque a caixinha embaixo
   escrito **"Add Python to PATH"** ✅ antes de clicar em "Install Now".
5. Clique em **Install** e espere terminar. Pode fechar.

---

## PARTE 2 — Pegar a "chave" do Google (a parte mais chatinha, mas é só seguir)

Aqui você cria uma chave que dá permissão para o programa editar SEUS documentos.

### 2.1 — Criar um projeto

1. Entre em **https://console.cloud.google.com/** com a conta
   **adm@soucasa7.com.br**.
2. Lá em cima, do lado do logo "Google Cloud", clique na **setinha/nome do
   projeto** → **"New Project"** (Novo Projeto).
3. Em "Project name" escreva: **editar-docs** → clique em **Create** (Criar).
4. Espere uns segundos e selecione esse projeto (aparece um aviso, clique em
   "Select Project").

### 2.2 — Ligar as APIs (as "tomadas" do Google Docs e do Drive)

1. Na barra de busca lá em cima, escreva **"Google Docs API"** e clique no
   resultado.
2. Clique no botão azul **"Enable"** (Ativar). Espere.
3. Busque de novo, agora **"Google Drive API"**, e clique em **"Enable"**.

### 2.3 — Dizer quem pode usar (tela de consentimento)

1. Na busca, escreva **"OAuth consent screen"** e abra.
2. Escolha **"External"** (Externo) → **Create**.
3. Preencha só o obrigatório:
   - **App name:** editar-docs
   - **User support email:** adm@soucasa7.com.br
   - **Developer contact email** (lá embaixo): adm@soucasa7.com.br
4. Clique **Save and Continue** nas próximas telas até o fim (pode pular as do
   meio clicando em "Save and Continue").
5. Numa etapa chamada **"Test users"**, clique em **"+ Add users"**, digite
   **adm@soucasa7.com.br** e salve. (Isso libera VOCÊ para usar.)

### 2.4 — Criar a chave (credentials.json)

1. Na busca, escreva **"Credentials"** e abra.
2. Clique em **"+ Create Credentials"** (lá em cima) → **"OAuth client ID"**.
3. Em **Application type**, escolha **"Desktop app"**.
4. Em "Name" pode deixar o que vier → **Create**.
5. Vai aparecer uma janelinha. Clique em **"Download JSON"** ⬇️.
6. Esse arquivo baixado é a sua **chave**. Guarde bem.

---

## PARTE 3 — Colocar a chave no lugar certo

1. Ache o arquivo que você baixou (nome tipo
   `client_secret_....json`).
2. **Renomeie** ele para exatamente: **`credentials.json`**
3. **Mova** ele para dentro da pasta do programa, que é a pasta
   **`google-docs-mcp`** (a mesma onde está este guia).

> 🔒 Essa chave é secreta, como a senha do banco. Não mande para ninguém e não
> suba para a internet. (O programa já está configurado para nunca subir ela.)

---

## PARTE 4 — Instalar as peças e fazer o login (uma vez só)

Agora vamos abrir o "terminal" (uma telinha preta de comandos). Calma, é só
copiar e colar.

**No Windows:** aperte a tecla Windows, escreva **cmd**, abra o "Prompt de
Comando".
**No Mac:** aperte Command+Espaço, escreva **Terminal**, abra.

Cole os comandos abaixo **um de cada vez** e aperte Enter:

1. Entrar na pasta do programa (troque o caminho pelo lugar onde você salvou a
   pasta `google-docs-mcp`; se não souber, me chama que eu te ajudo a achar):

   ```
   cd CAMINHO/DA/PASTA/google-docs-mcp
   ```

2. Instalar as peças que o programa precisa:

   ```
   pip install -r requirements.txt
   ```

   (Se der erro dizendo que "pip não foi encontrado", tente `pip3` no lugar de
   `pip`.)

3. Fazer o login no Google:

   ```
   python authorize.py
   ```

   - Vai **abrir o navegador** sozinho.
   - Escolha a conta **adm@soucasa7.com.br**.
   - Vai aparecer um aviso **"Google não verificou este app"** — é normal, o app
     é seu. Clique em **"Avançado"** → **"Acessar editar-docs (não seguro)"**.
   - Clique em **"Permitir"**.
   - Quando o terminal disser **"Autorizado com sucesso"**, está pronto. ✅

---

## PARTE 5 — Plugar no Claude Desktop

1. Instale o **Claude para computador** (se ainda não tem):
   **https://claude.ai/download**
2. Abra o Claude, clique no menu de **Configurações (Settings)** →
   **Developer** → **"Edit Config"**. Isso abre um arquivo de texto chamado
   `claude_desktop_config.json`.
3. Cole o conteúdo abaixo dentro dele. **Troque** `CAMINHO/DA/PASTA` pelo lugar
   real onde está a pasta `google-docs-mcp`:

   ```json
   {
     "mcpServers": {
       "google-docs": {
         "command": "python",
         "args": ["CAMINHO/DA/PASTA/google-docs-mcp/server.py"]
       }
     }
   }
   ```

   > Se já existir coisa escrita nesse arquivo, me mostra o que tem lá que eu te
   > digo exatamente onde encaixar — não dá pra ter dois `{` soltos.
   >
   > No Windows, o caminho usa barra invertida e precisa ser dobrada, assim:
   > `"C:\\Users\\voce\\google-docs-mcp\\server.py"`.

4. **Feche e abra o Claude Desktop de novo.**

---

## PARTE 6 — Testar 🎉

No Claude Desktop, escreva por exemplo:

> "Procure meu documento chamado PLANO-MIDIA e leia ele."

ou

> "No documento X, troque 'R$ 24.000' por 'R$ 30.000'."

Se ele editar e o link continuar o mesmo, **deu certo** — agora você edita igual
sua sócia. 🙌

---

## ❓ Por que não funciona no Claude do navegador?

O Claude do navegador (claude.ai) só aceita conectores que ficam ligados na
internet num servidor público — o que exige hospedar o programa em algum lugar
pago e configurar mais coisa. O **Claude Desktop** roda o programa direto no seu
computador, então é **muito mais simples** para começar. Se mais pra frente você
quiser usar no navegador também, me avisa que eu monto a versão hospedada.

---

## 🆘 Travou?

Me diga **em qual número** você parou e **o que apareceu na tela** (pode mandar
print). Eu te desencalho na hora.
