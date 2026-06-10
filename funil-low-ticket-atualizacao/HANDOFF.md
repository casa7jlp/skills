# HANDOFF - Funil Low Ticket Renato Zaneti

Resumo para retomar em outra sessão. Cole isto no início de uma aba nova.

## Contexto
- Projeto: funil **low ticket** do Dr. Renato Zaneti (Médico da Dor 2.0). Produto: **Imersão: Atualização em Medicina da Dor** - gravação 4h, 4 módulos, **R$ 97**, Hotmart.
- Função do funil: tráfego frio-morno de médicos -> página low ticket -> comprador entra no pixel e alimenta o retargeting da **Imersão Microfat** (high ticket).
- Identidade: **DNA-Renato-Zaneti v2** + **Brand Book Médico da Dor 2.0 v2** (paleta Azul Profundo #0A2540, Cobalto #0066CC, Teal #0EA5B7, Off-White #F7F4EE; fontes DM Serif Display + Inter + JetBrains Mono).
- Regras sempre: zero invenção (nada de número/depoimento/case não rastreável); compliance CFM (sem promessa de faturamento/cura, sem antes/depois com garantia, sem paciente identificável); anti-IA na copy (sem em-dash, sem aspas curly).
- Avatar: médico CRM ativo, 35-60, consultório; exausto de plantão, refém de convênio, equipamento parado.
- Ângulos do Renato: A1 "não é cobrar caro, é cobrar certo"; A2 Ferrari/equipamento parado; A3 "eu só ensino o que eu vivo".

## Onde está tudo
- Git: repo `casa7jlp/skills`, branch **`claude/renato-low-ticket-sales-gsopoa`**, pasta `funil-low-ticket-atualizacao/` (+ `pagina-vendas/index.html`).
- Drive: pasta **funil-low-ticket-atualizacao** (id `1FxxRuiWVoIzVhOhrhb4k_MeSADdjXbZo`). Cada doc tem `.md` + Google Doc `(leitura)`.

## Entregue (7 itens, todos commitados e no Drive salvo onde indicado)
1. **Design system da página** (etapa 2) - Drive + git (.md/.docx).
2. **Direção: persona + frase-norte** (etapa 3) - validado.
3. **Página de vendas HTML** padrão Vercel/Casa 7 - git `pagina-vendas/index.html` (placeholders de imagem nomeados; Cloudinary cloud `dlypuyaxt`).
4. **Automação entrega + nutrição** (e-mail + WhatsApp) - Drive + git.
5. **Mapa de assets reais (fotos Renato)** - git. Fonte principal: pasta Drive `FOTOS RENATO / Fotos Profissionais` (id `15bAk5qU9hPsQrAg-JRmfc01KEEtlObZz`); alternativa `DR. RENATO ZANETI GRAVAÇÃO fotos` (id `19eYiUIF2nhRie27ALAw_TNUGaChyjps_`). Slots: `img-hero-renato-clinica` e `img-autoridade-renato-retrato`. NÃO consegui avaliar as fotos visualmente (MCP não renderiza imagem). Subpasta `IA` = não usar.
6. **Criativos etapa 1: 50 copies** (`casa7-criativos-01-copy`) - Drive + git. 10 categorias x 5: GERAIS, DORES, DESEJOS, ANGULO1/2/3, ENTREGAVEIS-GERAL, ENTREGAVEIS (um a um), BONUS, RMKT. Cada um com ID, nível de consciência, gatilho, chamada <=10 palavras, sub, CTA, direção de imagem.
7. **Criativos etapa 2: brand guide + motor copy->imagem** (`casa7-criativos-02-brandguide`) - Drive + git. Story 9:16; tipos A-G mapeados aos 50 IDs; motor pré-preenchido pronto pra etapa 3. Derivado da identidade (sem biblioteca de ads ainda; itens [inferido]).

## Próximo passo
**Criativos etapa 3 (`casa7-criativos-03-prompts`)**: gerar prompt de imagem por ID dos 50.
- Bloqueio parcial: criativos COM o Renato exigem foto de referência real (regra "pessoa sem referência não gera"). Os SEM pessoa (Tipo A dado, DORES com objeto, fundo sólido, parte de educação) podem ser gerados já.
- Opções: (A) etapa 3 só dos sem-pessoa agora; (B) usuário passa IDs dos frames do Renato -> etapa 3 completa + apontar fotos no index.html; (C) pausar.

## Pendências do cliente (para publicar e rodar tráfego)
Oferta Hotmart R$ 97 + link de checkout; link de acesso da gravação; pixel Meta + postback Hotmart->ActiveCampaign; WhatsApp comercial + ManyChat; dados legais do rodapé + e-mail remetente; CRM/RQE do Renato; **2-3 fotos escolhidas** (hero + autoridade); ano da fonte DATASUS; valores de referência dos bônus; prova social real (depoimento de médico); **resolver conflito de dados da Imersão Microfat** (Chapecó/turma 2-3/10-jul vs SP/turma 15-20 no briefing).
