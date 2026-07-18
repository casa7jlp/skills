# Guia: instalar o Estúdio CCB Reels no seu computador

> Para quem não é técnico. Siga na ordem. A Poliana só participa do Passo 2, uma única vez.
> Depois disso você edita Reels sozinho, sem depender de ninguém.

---

## Passo 1 — Instalar o Claude Code no seu computador (você faz sozinho)

**No Mac:**
1. Abra o programa **Terminal** (aperte `Cmd + Espaço`, digite "Terminal", Enter).
2. Cole este comando e aperte Enter:
   ```
   curl -fsSL https://claude.ai/install.sh | bash
   ```
3. Quando terminar, digite `claude` e aperte Enter. Ele vai pedir login — entre com a conta Claude da empresa.

**No Windows:**
1. Abra o **PowerShell** (menu Iniciar, digite "PowerShell", Enter).
2. Cole este comando e aperte Enter:
   ```
   irm https://claude.ai/install.ps1 | iex
   ```
3. Depois digite `claude`, Enter, e faça login com a conta da empresa.

> ⚠️ Importante: se o PC da Poliana for Mac e o seu for Windows (ou vice-versa),
> avise o Claude no Passo 3 — ele adapta a instalação, mas pode dar um pouco mais de trabalho.

---

## Passo 2 — Pedir 1 cópia pra Poliana (única vez que precisa dela)

Peça pra ela **compactar (zipar) duas pastas** do computador dela e te mandar
(Google Drive, HD externo ou pendrive — o banco de mídia pode ser pesado):

| O que | Onde fica no PC dela |
|---|---|
| O estúdio inteiro | `Documentos/CCB-Reels` (a pasta toda: INBOX, conteudos, banco, engine) |
| A skill de edição | `~/.claude/skills/editar-reel-brolls` (pasta oculta `.claude` na pasta pessoal dela) |

No seu computador, **descompacte nos mesmos lugares**:
- `CCB-Reels` dentro da sua pasta **Documentos**
- `editar-reel-brolls` dentro de `~/.claude/skills/` (se a pasta `skills` não existir, crie)

Só isso. Modelos de transcrição, ffmpeg e o resto o Claude baixa sozinho no passo seguinte
(são públicos, não precisam vir dela).

> 💡 Dica pra nunca mais precisar disso: peça pra Poliana subir a skill e o estúdio
> (sem os vídeos pesados) neste repositório `casa7jlp/skills` no GitHub.
> Aí qualquer computador novo baixa de lá.

---

## Passo 3 — Deixar o Claude terminar a instalação sozinho

No seu computador, abra o Claude Code (Terminal → `claude`) e **cole este texto**:

```
Acabei de copiar o estúdio CCB Reels do computador da Poliana para este.
As pastas já estão em: ~/Documents/CCB-Reels (estúdio) e
~/.claude/skills/editar-reel-brolls (skill). Sua missão é deixar tudo
funcionando nesta máquina:

1. Leia ~/Documents/CCB-Reels/BEM-VINDO.md e o SKILL.md + PIPELINE.md da skill.
2. Instale o que faltar: ffmpeg, whisper.cpp (whisper-cli) e Node.js.
3. Baixe os modelos de transcrição para ~/.cache/whisper/:
   ggml-large-v3-turbo.bin e ggml-small.bin (são ~1,5 GB, pode demorar).
4. Rode npm install na engine Remotion do estúdio.
5. Valide tudo: transcreva um áudio curto de teste e faça um render de teste
   da engine. Só me diga que está pronto quando os dois testes passarem.

Sou leigo: me avise em linguagem simples se precisar que eu aprove alguma coisa.
```

O Claude vai pedir permissão pra instalar coisas — pode aprovar. No final ele te diz "está pronto".

---

## Como usar no dia a dia (depois de instalado)

1. Coloque o vídeo bruto em `Documentos/CCB-Reels/INBOX/`.
2. Abra o Claude Code no seu computador (não pelo site!) e cole a missão de edição
   (aquele texto "Missão: editar meu Reel..." — junto com o roteiro do vídeo,
   qual expert/projeto é, e qual pasta de b-rolls usar).
3. O Claude transcreve, corta, te mostra o plano de edição pra aprovar,
   monta e entrega o `REEL-final.mp4` na pasta do conteúdo em `a-postar`.

> ⚠️ Regra de ouro: a edição tem que rodar no **Claude Code do computador**
> (Terminal ou app). Pelo site claude.ai a conversa roda na nuvem e não enxerga
> suas pastas — foi exatamente o que aconteceu na primeira tentativa.
