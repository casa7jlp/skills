# DESIGN SYSTEM - Página de Vendas Low Ticket

## Imersão: Atualização em Medicina da Dor (gravação completa) - Dr. Renato Zaneti

Pipeline Casa 7 - Etapa 2 (design-system). Entrada: COPY-PAGINA-LOWTICKET-ATUALIZACAO-RENATO.md (17 peças, estrutura morna). Saída alimenta a etapa 3 (casa7-pagina-vendas-03-direcao) e a construção (casa7-pagina-vercel ou casa7-pagina-figma).

Metodologia: Júlia Wolf Cruz - PROSP (adaptada Casa 7). Identidade visual extraída do DNA oficial do projeto (Brand Book Médico da Dor 2.0 v2, 2026-05-20). Estrutura/ritmo extraídos das referências reais de página de venda de ingresso da base de conhecimento Casa 7.

---

## Insumos consumidos

- Identidade: DNA-Renato-Zaneti.md (v2) + Brand Book Médico da Dor 2.0 v2. Paleta, tipografia, CTA Cobalto, proibições de cor e compliance CFM vêm daqui e vencem qualquer convenção de referência.
- Copy: COPY-PAGINA-LOWTICKET-ATUALIZACAO-RENATO.md (17 peças).
- Referência de estrutura (swipe file Casa 7 - 02. PAGINAS / Venda de Ingresso):
  - Imersão TMAP - Dr. Ícaro Ramalho (R$ 197, profissional de saúde) - referência primária, avatar análogo (insegurança à referência, raciocínio clínico, agenda lotada, certificado, mentor, FAQ).
  - Imersão Apareça & Venda - Suellen Warmling (R$ 37) - padrão de bloco "por que tão barato" (justificativa de SLO honesta) e vozes da cabeça.
  - Workshop Inglês - Eli Sato (R$ 27) - padrão de badges de credibilidade e estrutura "para você que / mas não é para você".

## Decisões de escopo (validadas com a Poliana)

- As duas dobras de prova social (peças 5 e 13 da copy) ficam FORA deste wireframe até existir depoimento ou print real e rastreável. Serão reintroduzidas num passe futuro. A numeração de dobras abaixo já reflete a remoção (13 dobras).
- Componente de escassez honesta desenhado e DESLIGADO por default. A página roda como SLO perpétuo a R$ 97 sem relógio regressivo. O componente fica documentado, pronto para ligar caso a oferta passe a rodar por janela (pendência nº 6).
- Compliance CFM aplicado: sem countdown sensacionalista, sem "106% vendido", sem promessa de faturamento ou de resultado clínico. Estatística (DATASUS) sempre com fonte e ano visíveis.

---

# A - DESIGN SYSTEM TÉCNICO

```
# DESIGN SYSTEM - PÁGINA LOW TICKET ATUALIZAÇÃO EM MEDICINA DA DOR

CORES:
  Primary   #0A2540  (Azul Profundo - institucional, autoridade médica de elite)
  Secondary #1F4E79  (Azul-Médio Clínico - hierarquia secundária, hovers escuros)
  Accent/CTA #0066CC (Cobalto - botões, links, números e valores destacados)
  Regen     #0EA5B7  (Teal Bioma - acento de medicina regenerativa, usar só em PRP/regenerativa)
  BG        #F7F4EE  (Off-White Quente - canvas principal, substitui branco puro)
  Surface   #FFFFFF  (cards e blocos elevados sobre o off-white)
  Text      #1B1F24  (Grafite Quente - texto principal, substitui preto puro)
  Muted     #5B6770  (Cinza-Aço - texto secundário, captions, labels)
  Border    #E4DDCC  (areia clara dessaturada para bordas de card sobre off-white)
  Success   #0EA5B7  (reaproveita Teal Bioma para selos de garantia/checks)
  Error     #B23A3A  (vermelho contido - só validação de formulário, nunca como cor de marca)
  Temperatura: fria-neutra com base quente no canvas. Calibrada para autoridade clínica sem frieza hospitalar.
  Proporção 60-30-10: 60% Off-White / 30% Azul Profundo + Azul-Médio + Grafite / 10% Cobalto + Teal (Cobalto dominando).

TIPOGRAFIA:
  Títulos: DM Serif Display - import https://fonts.google.com/specimen/DM+Serif+Display - peso 400 - escala dramática
  Corpo:  Inter - import https://fonts.google.com/specimen/Inter - 17px / weight 400-500 (liberada por ser fonte oficial do projeto)
  Acento técnico: JetBrains Mono - import https://fonts.google.com/specimen/JetBrains+Mono - usar em "2.0", "R$ 97", "4h", "7 dias", datas, número DATASUS, labels de módulo (01-04)
  Mobile  -> H1:32px H2:26px H3:20px body:16px caption:13px CTA:17px
  Desktop -> H1:54px H2:38px H3:24px body:18px caption:14px CTA:18px
  Comportamentos: H1/H2 em DM Serif com grifo Cobalto em palavra-chave; labels e números em JetBrains Mono caixa alta; corpo em Inter; sem itálico decorativo
  Hero split override: H1 clamp(30px, 4.2vw, 54px)

ESPAÇAMENTOS:
  Container: 1080px
  Padding x mobile: 20px - desktop: 24px
  Section py mobile: 64px - desktop: 96px
  Card gap: 20px mobile / 24px desktop

BORDAS E RAIOS:
  Btn: 8px - Card: 12px - Input: 8px - Img: 12px - Badge: 999px (pílula)
  Border padrão: 1px solid #E4DDCC (em dobra escura: 1px solid rgba(255,255,255,0.12))

SOMBRAS:
  SM: 0 1px 2px rgba(10,37,64,0.06)
  MD: 0 6px 20px rgba(10,37,64,0.10)
  LG: 0 16px 48px rgba(10,37,64,0.14)
  CTA hover: 0 10px 28px rgba(0,102,204,0.32)
  Glow: nenhum (proibido no projeto)

BOTÃO PRIMARY:
  Mobile: h 56px / width 100% / pad 0 24px / radius 8px / bg #0066CC / text #FFFFFF / Inter 600 17px
  hover: bg #0A5BB8 + shadow CTA hover + translateY(-2px) / transition 180ms ease-out
  Desktop: auto width / pad 0 40px / 18px
  Microcopy sob o botão em JetBrains Mono 13px #5B6770: "Acesso imediato - garantia de 7 dias"

BOTÃO SECONDARY (WhatsApp / dúvidas):
  outline 1px solid #0A2540 / bg transparente / text #0A2540 / hover bg rgba(10,37,64,0.06)

CARDS:
  pad 28px / radius 12px / bg #FFFFFF / border 1px #E4DDCC / shadow MD
  Grid: 1col mobile - 2col tablet 24px gap - 4col desktop (módulos) / 2col desktop (bônus, entregáveis)

INPUTS: h 52px / border 1px #E4DDCC / radius 8px / focus: border #0066CC + shadow 0 0 0 3px rgba(0,102,204,0.15)

ÍCONES: Iconify Solar Outline (preferencial) ou Phosphor - 24px - cor #0A2540 (checks em #0EA5B7) - PROIBIDO Lucide

IMAGENS - SISTEMA GLOBAL:
  Emoção: método + autoridade clínica contemporânea
  Luz: natural neutra com leve viés frio nas sombras (definição do DNA)
  Contraste: médio - Temperatura: fria-neutra - Saturação: contida (sem cor estourada)
  Fotos do Renato em ambiente real (consultório, sala de procedimento, sala de aula)
  Fundo estúdio (mockups) -> filter: brightness(1.02) contrast(1.03)
  Overlay em camadas sobre foto em dobra escura (NUNCA opacity simples):
    linear-gradient(to right, #0A2540 0%, rgba(10,37,64,0.85) 45%, rgba(10,37,64,0.55) 70%, transparent)
    + linear-gradient(to top, #0A2540 0%, transparent 28%)
    + linear-gradient(to bottom, rgba(10,37,64,0.30) 0%, transparent 20%)

ELEMENTO DE ASSINATURA:
  "Linha de atualização" Cobalto - filete fino Cobalto #0066CC (2px) usado como divisor de seção
  e sublinhado de palavra-chave. Substitui a "incisão cobre" da v1 (descartada).

ANIMAÇÕES:
  Fade-in: opacity 0->1 / 480ms ease-out
  Slide-up: translateY(24px)->0 / 480ms - Stagger: 80ms delay entre cards
  Hover botões: translateY(-2px) + shadow / Hover cards: shadow MD->LG + border #0066CC
  Especiais: contador numérico animado no número DATASUS (count-up ao entrar na viewport). Sem parallax, sem floating, sem grain pesado (grain só 3% opcional nas dobras escuras).

CSS VARS:
:root {
  --color-primary:#0A2540; --color-secondary:#1F4E79; --color-accent:#0066CC;
  --color-regen:#0EA5B7; --color-bg:#F7F4EE; --color-surface:#FFFFFF;
  --color-text:#1B1F24; --color-muted:#5B6770; --color-border:#E4DDCC;
  --font-heading:'DM Serif Display'; --font-body:'Inter'; --font-mono:'JetBrains Mono';
  --container-max:1080px; --padding-x-m:20px; --padding-x-d:24px;
  --section-py-m:64px; --section-py-d:96px;
  --radius-btn:8px; --radius-card:12px;
  --shadow-sm:0 1px 2px rgba(10,37,64,0.06);
  --shadow-md:0 6px 20px rgba(10,37,64,0.10);
  --shadow-lg:0 16px 48px rgba(10,37,64,0.14);
  --shadow-cta:0 10px 28px rgba(0,102,204,0.32);
}
```

---

# B - WIREFRAME DOBRA A DOBRA

```
DOBRA 01 - HERO (PROMESSA)
══════════════════════════════════════════════════
NARRATIVA: posiciona a atualização técnica como atalho. Responde a dúvida não-dita "isso é sério ou é mais um curso online?" com autoridade médica e badge de exclusividade.
COMPOSIÇÃO: entrada -> kicker + badge / percurso -> H1 promessa / chegada -> CTA + foto Renato

LAYOUT DESKTOP:
 ┌─────────────────────────────────────┐
 │ 60% texto (esq) | 40% foto Renato   │
 └─────────────────────────────────────┘
 Container 1080px - py 96px

MOBILE: foto abaixo do bloco de texto, empilhado. Badge acima do H1. CTA largura total.

BG: #0A2540 (Azul Profundo, dobra escura de abertura) / foto Renato com overlay em camadas / grain 3%
 Ritmo: abre escuro para dar peso institucional.

IMAGENS: 1
 img-hero-renato-clinica.jpg -> tipo 01 Especialista / função: autoridade de quem faz / posição: coluna direita full-height / proporção: 4:5 vertical
 tratamento: foto real do Renato em ambiente clínico, overlay Azul Profundo em camadas / luz natural viés frio / mobile: reduz para 16:9 topo

KICKER (JetBrains Mono, Cobalto): "IMERSÃO - ATUALIZAÇÃO EM MEDICINA DA DOR"
BADGE (pílula): "Exclusivo para médicos com CRM ativo"
H1 (DM Serif): Domine os protocolos de [Mesoterapia e Proloterapia] para tratar dor sem cirurgia, com raciocínio clínico pronto para o consultório
   (grifo Cobalto em "Mesoterapia e Proloterapia")
SUBHEAD (Inter): Quatro horas de atualização técnica, direto ao ponto, para o médico que quer parar de só encaminhar e passar a ter o que oferecer antes da cirurgia.
ÍCONES: não
ANIMAÇÃO: fade-in no bloco de texto, slide-up no CTA
CTA: sim -> "QUERO MINHA ATUALIZAÇÃO AGORA" / primary / abaixo do subhead
   microcopy: "R$ 97 - acesso imediato - garantia de 7 dias" (JetBrains Mono)
ALERTA: foto do Renato deve vir da pasta FOTOS RENATO (real). Sem foto aprovada, usar briefing img-hero.
══════════════════════════════════════════════════

DOBRA 02 - VOZES DA CABEÇA (IDENTIFICAÇÃO DA DOR)
══════════════════════════════════════════════════
NARRATIVA: espelha o monólogo interno do médico para gerar identificação. Fecha com a virada "não é falta de capacidade, é falta de repertório".
COMPOSIÇÃO: entrada -> frase de contexto / percurso -> grade de balões de objeção / chegada -> frase-virada em destaque

LAYOUT DESKTOP: bloco de texto centrado 760px + grade 2col de "balões" de aspas
MOBILE: balões empilhados 1col

BG: #F7F4EE (claro, contraste com a hero escura) / sólido / linha de atualização Cobalto como divisor superior
 Ritmo: claro após escuro.

IMAGENS: 0 (composição tipográfica)
ÍCONES: aspas estilizadas em Solar Outline #5B6770 em cada balão
ANIMAÇÃO: stagger fade-in nos balões
CTA: não
COPY: 6 falas reais do avatar (da copy peça 2) + virada: "Não é falta de capacidade. É falta de um repertório atualizado que ninguém te entregou na residência."
══════════════════════════════════════════════════

DOBRA 03 - A OPORTUNIDADE (DADO DE MERCADO)
══════════════════════════════════════════════════
NARRATIVA: mostra que a fila de pacientes já existe. Dado com fonte para credibilidade e compliance.
COMPOSIÇÃO: entrada -> headline / percurso -> card de número DATASUS / chegada -> frase "quem domina primeiro atende a fila que já existe"

LAYOUT DESKTOP: 2col - texto (esq) | card de número grande (dir)
MOBILE: card acima do texto

BG: #F7F4EE (claro) / sólido / card interno surface #FFFFFF com borda
IMAGENS: 0 (card de dado, sem foto)
NÚMERO (JetBrains Mono, Cobalto, count-up): "~12 milhões" + label "brasileiros com osteoartrite"
   fonte visível em caption: "Fonte: DATASUS [ano a confirmar]" -> [NECESSÁRIO CONFIRMAR ano da fonte]
ÍCONES: ícone de dado/gráfico de linha Solar Outline
ANIMAÇÃO: count-up do número ao entrar na viewport
CTA: não
══════════════════════════════════════════════════

DOBRA 04 - A SOLUÇÃO
══════════════════════════════════════════════════
NARRATIVA: nomeia a saída (atualização técnica de verdade) contra o vilão (curso genérico de fim de semana).
COMPOSIÇÃO: entrada -> contraste vilão x solução / chegada -> frase "aprender o que fazer é metade"

LAYOUT DESKTOP: bloco centrado 820px, frase-chave em destaque DM Serif
MOBILE: igual, empilhado

BG: #0A2540 (escuro) / sólido com linha de atualização Cobalto / grain 3%
 Ritmo: escuro para marcar virada de argumento.
IMAGENS: 0
ÍCONES: não (ou um ícone de bússola/raciocínio Solar Outline opcional)
ANIMAÇÃO: fade-in
CTA: não
══════════════════════════════════════════════════

DOBRA 05 - MECANISMO: OS 4 MÓDULOS
══════════════════════════════════════════════════
NARRATIVA: mostra o conteúdo das 4 horas como percurso estruturado. Padrão "o que você vai aprender" da referência Ícaro/TMAP, adaptado a 4 módulos.
COMPOSIÇÃO: entrada -> headline "O que você percorre nas 4 horas" / percurso -> 4 cards numerados / chegada -> CTA intermediário

LAYOUT DESKTOP: grade 4col de cards (ou 2x2) com label de módulo em JetBrains Mono
MOBILE: 1col empilhado

BG: #F7F4EE (claro) / cards surface #FFFFFF
IMAGENS: 0 fotos - 4 ícones de módulo
 Módulo 01 Mesoterapia -> ícone de seringa/ponto de aplicação (Solar Outline)
 Módulo 02 Proloterapia e regenerativa -> ícone de célula/regeneração (acento Teal Bioma #0EA5B7)
 Módulo 03 Protocolos e raciocínio clínico -> ícone de fluxo/checklist
 Módulo 04 Aplicação ética e CFM -> ícone de escudo/balança
LABELS (JetBrains Mono): "01" "02" "03" "04"
ÍCONES: Solar Outline 32px, módulo 02 em Teal Bioma (regenerativa), demais em Azul Profundo
ANIMAÇÃO: stagger slide-up nos 4 cards
CTA: sim (intermediário) -> "QUERO MINHA ATUALIZAÇÃO AGORA" / primary
══════════════════════════════════════════════════

DOBRA 06 - ENTREGÁVEIS (O QUE VOCÊ RECEBE)
══════════════════════════════════════════════════
NARRATIVA: materializa o produto digital (gravação + certificado). Remove qualquer mecânica de evento ao vivo.
COMPOSIÇÃO: entrada -> headline "Tudo que você recebe" / percurso -> 2 cards com mockup / chegada -> reforço de acesso imediato

LAYOUT DESKTOP: 2col - card gravação | card certificado
MOBILE: 1col

BG: #F7F4EE (claro)
IMAGENS: 2 (tipo 03 Entregável)
 img-entregavel-gravacao-mockup.jpg -> mockup de área de membros/player com 4 módulos, em notebook + celular / fundo estúdio off-white
 img-entregavel-certificado.jpg -> mockup do certificado digital com selo Médico da Dor 2.0 e assinatura
ÍCONES: check Solar Outline Teal Bioma nos bullets
ANIMAÇÃO: fade-in
CTA: não
COPY: "Acesso imediato à gravação completa das 4 horas" + "Certificado digital com carga horária e conteúdo programático". NÃO usar "vitalício".
══════════════════════════════════════════════════

DOBRA 07 - BÔNUS
══════════════════════════════════════════════════
NARRATIVA: empilha valor com 2 bônus reais já produzidos.
COMPOSIÇÃO: entrada -> "E você ainda leva junto" / percurso -> 2 cards de bônus / chegada -> transição para ancoragem

LAYOUT DESKTOP: 2col - MasterClass | Checklist
MOBILE: 1col

BG: #0A2540 (escuro) / cards surface translúcido rgba(255,255,255,0.06) com borda clara / acento Teal Bioma (tema regenerativo do ácido hialurônico)
 Ritmo: escuro para destacar os bônus como bloco premium.
IMAGENS: 2 (tipo 03 Entregável)
 img-bonus-masterclass-ah.jpg -> capa/mockup da MasterClass "Ácido Hialurônico na Medicina da Dor"
 img-bonus-checklist-premium.jpg -> mockup do PDF Checklist Premium de Aplicação
BADGE: "BÔNUS 01" / "BÔNUS 02" (JetBrains Mono, Teal Bioma)
ÍCONES: não (mockups fazem o trabalho)
ANIMAÇÃO: slide-up
CTA: não
══════════════════════════════════════════════════

DOBRA 08 - PARA QUEM É
══════════════════════════════════════════════════
NARRATIVA: qualifica o público (médico com consultório) e auto-seleciona o lead certo.
COMPOSIÇÃO: entrada -> "Esta imersão é para você, médico, que..." / percurso -> lista de checks / chegada -> regra "2 itens = é para você"

LAYOUT DESKTOP: lista 2col de itens com check
MOBILE: 1col

BG: #F7F4EE (claro)
IMAGENS: 0
ÍCONES: check Solar Outline Teal Bioma por item
ANIMAÇÃO: stagger fade-in
CTA: não
══════════════════════════════════════════════════

DOBRA 09 - ANCORAGEM DE VALOR
══════════════════════════════════════════════════
NARRATIVA: soma o valor de referência antes de revelar o preço, para fazer R$ 97 parecer pequeno.
COMPOSIÇÃO: entrada -> "Recapitulando o que você recebe" / percurso -> tabela de itens com valores / chegada -> total riscado

LAYOUT DESKTOP: tabela/lista centrada 640px, valores em JetBrains Mono
MOBILE: igual

BG: #F7F4EE (claro)
IMAGENS: 0
VALORES (JetBrains Mono): R$ 147 gravação / R$ 97 MasterClass [valor de referência - confirmar] / R$ 47 Checklist [confirmar] / Certificado incluso / TOTAL R$ 291 valor de referência
ÍCONES: não
ANIMAÇÃO: fade-in
CTA: não
ALERTA: valores de bônus marcados [NECESSÁRIO CONFIRMAR na Hotmart].
══════════════════════════════════════════════════

DOBRA 10 - OFERTA + PREÇO + CTA
══════════════════════════════════════════════════
NARRATIVA: o momento da conversão. Quebra de preço (R$ 291 -> R$ 97) + como funciona em 3 passos.
COMPOSIÇÃO: entrada -> "Você não vai pagar R$ 291" / percurso -> caixa de oferta / chegada -> CTA grande + selos

LAYOUT DESKTOP: caixa de oferta central 720px, preço em destaque, 3 passos em linha
MOBILE: caixa largura total, 3 passos empilhados

BG: #0A2540 (escuro) / caixa de oferta surface #FFFFFF elevada (shadow LG) / linha de atualização Cobalto no topo
 Ritmo: escuro de fundo, caixa clara saltando = foco total na oferta.
IMAGENS: 0 (selos de pagamento como ícones/SVG)
PREÇO (JetBrains Mono, Cobalto): "R$ 97 à vista" + "ou parcelado no cartão [confirmar parcelamento Hotmart]"
SELOS: "Acesso imediato" / "Garantia de 7 dias" / "Compra 100% segura (Hotmart)"
3 PASSOS: 1 compra na Hotmart / 2 acesso no e-mail na hora / 3 assiste e baixa os bônus
ÍCONES: cadeado, raio, check Solar Outline
ANIMAÇÃO: fade-in na caixa
CTA: sim -> "QUERO MINHA ATUALIZAÇÃO AGORA" / primary grande
COMPONENTE OPCIONAL (DESLIGADO): barra de escassez honesta acima da caixa, ex "Preço de entrada por tempo limitado" sem countdown regressivo. Ativar só por decisão de janela (pendência nº 6).
══════════════════════════════════════════════════

DOBRA 11 - GARANTIA
══════════════════════════════════════════════════
NARRATIVA: remove o risco. Garantia incondicional de 7 dias via Hotmart.
COMPOSIÇÃO: entrada -> selo de garantia / percurso -> texto / chegada -> frase "o risco é todo meu"

LAYOUT DESKTOP: selo (esq) + texto (dir), bloco centrado 820px
MOBILE: selo acima, texto abaixo

BG: #F7F4EE (claro)
IMAGENS: 1 (tipo 08 visual)
 img-selo-garantia-7dias.svg -> selo "Garantia 7 dias" em Azul Profundo + Cobalto (vetor, pode ser SVG/CSS, não foto)
ÍCONES: escudo Solar Outline
ANIMAÇÃO: fade-in
CTA: não
══════════════════════════════════════════════════

DOBRA 12 - AUTORIDADE (QUEM CONDUZ)
══════════════════════════════════════════════════
NARRATIVA: apresenta o Dr. Renato como mentor prático ("eu só ensino o que eu vivo"). Credenciais marcadas para confirmar.
COMPOSIÇÃO: entrada -> foto Renato / percurso -> bio + frase-assinatura / chegada -> CTA

LAYOUT DESKTOP: 40% foto (esq) | 60% texto (dir)
MOBILE: foto topo, texto abaixo

BG: #0A2540 (escuro) / foto com overlay em camadas / grain 3%
 Ritmo: escuro, fecha o argumento de autoridade com peso.
IMAGENS: 1
 img-autoridade-renato-retrato.jpg -> tipo 01 Especialista / retrato profissional do Renato, jaleco ou ambiente clínico / luz natural viés frio / fonte: pasta FOTOS RENATO
FRASE-ASSINATURA (DM Serif): "Eu só ensino o que eu vivo. E não é cobrar caro, é cobrar certo."
ÍCONES: não
ANIMAÇÃO: fade-in
CTA: sim -> "QUERO MINHA ATUALIZAÇÃO AGORA" / primary
   microcopy: "R$ 97 à vista - acesso imediato - garantia de 7 dias"
ALERTA: [NECESSÁRIO CONFIRMAR] CRM, RQE, titulações e qualquer número antes de publicar. Sem "referência nacional" ou número de alunos sem fonte. Bloco de bio desenhado para acomodar as credenciais quando confirmadas.
══════════════════════════════════════════════════

DOBRA 13 - SUPORTE + FAQ + RODAPÉ
══════════════════════════════════════════════════
NARRATIVA: tira a última objeção (WhatsApp), responde dúvidas (FAQ) e fecha com rodapé legal e disclaimer educativo.
COMPOSIÇÃO: entrada -> bloco WhatsApp / percurso -> acordeão FAQ / chegada -> rodapé legal

LAYOUT DESKTOP: bloco WhatsApp centrado + FAQ acordeão 760px + rodapé full-width
MOBILE: empilhado

BG: #F7F4EE (claro) / rodapé em faixa #0A2540 (escuro) ao final
IMAGENS: 0 (logo Médico da Dor 2.0 no rodapé)
WHATSAPP: botão secondary "CONVERSAR NO WHATSAPP" -> [NECESSÁRIO FORNECER número/link comercial]
FAQ: 7 perguntas da copy peça 16, em acordeão (Solar Outline chevron)
RODAPÉ: "Dr. Renato Zaneti - Médico da Dor 2.0" / disclaimer "Conteúdo educativo destinado a médicos. Não substitui avaliação clínica individualizada." / [NECESSÁRIO FORNECER razão social, CNPJ, cidade/estado, e-mail] / Todos os direitos reservados
ÍCONES: WhatsApp + chevron Solar Outline
ANIMAÇÃO: acordeão expand/collapse 240ms
CTA: secondary (WhatsApp)
══════════════════════════════════════════════════

COMPONENTE GLOBAL - BARRA FIXA DE CTA (STICKY)
══════════════════════════════════════════════════
Aparece após a dobra 01 sair da viewport. Mobile: barra inferior fixa largura total com preço + botão. Desktop: barra superior fina ou botão flutuante canto inferior direito.
Conteúdo: "Imersão: Atualização em Medicina da Dor - R$ 97" + botão "QUERO AGORA" (Cobalto).
BG: #0A2540 com botão Cobalto. Sombra LG. Sem countdown.
══════════════════════════════════════════════════
```

---

# C - BRIEFINGS DE IMAGEM

Decisão de luz global: luz natural neutra com leve viés frio nas sombras, saturação contida, sem glow. Fotos do Renato saem da pasta FOTOS RENATO (real); os mockups podem ser gerados ou montados a partir dos assets reais (gravação, certificado, MasterClass, checklist) da pasta do lançamento.

```
BRIEFING - img-hero-renato-clinica.jpg
Dobra: 01 - Tipo: 01 Especialista - Função: autoridade de quem faz
Sujeito: Dr. Renato Zaneti em ambiente clínico real (consultório ou sala de procedimento)
Composição: meio corpo, olhar para a câmera ou em atendimento - Proporção: 4:5 vertical (mobile 16:9) - Enquadramento: terço esquerdo livre para overlay de texto
Luz: natural direcional suave / viés frio nas sombras / temperatura neutra
Estilo: editorial médico contemporâneo - Paleta: ambiente neutro que case com Azul Profundo no overlay - Foco: no Renato - Desfoque: fundo levemente desfocado
Fundo: ambiente clínico real, recebe overlay Azul Profundo em camadas - por quê: integra a foto à dobra escura sem perder o sujeito
Evitar: branco hospitalar estourado, sorriso de banco de imagem, jaleco genérico de stock, gradiente saturado
PROMPT IA (fallback se não houver foto real): "Editorial portrait of a Brazilian male orthopedic doctor in his 40s-50s in a real modern clinical office, natural soft directional light with cool shadows, neutral desaturated palette, shallow depth of field, confident calm expression, documentary medical photography, left third of frame empty for text overlay"
Alternativa real (preferencial): foto da pasta FOTOS RENATO em consultório, sem paciente identificável.

BRIEFING - img-entregavel-gravacao-mockup.jpg
Dobra: 06 - Tipo: 03 Entregável - Função: materializar o acesso à gravação
Sujeito: tela de área de membros mostrando os 4 módulos, em notebook + celular
Composição: notebook em destaque, celular ao lado mostrando o player - Proporção: 4:3 - Enquadramento: produto centralizado
Luz: estúdio neutra suave - Estilo: mockup limpo de produto digital - Paleta: UI em Azul Profundo + Cobalto sobre off-white - Foco: telas nítidas
Fundo: estúdio off-white #F7F4EE - por quê: o produto é digital, fundo limpo evidencia a interface - filter: brightness(1.02) contrast(1.03)
Evitar: telas de UI inventando depoimento ou número, marca de player concorrente
PROMPT IA: "Clean product mockup of an online course members area on a laptop and smartphone, showing 4 video modules, deep blue and cobalt UI on warm off-white studio background, soft neutral studio light, minimal, high-end digital product photography"
Alternativa real: screenshot real da área de membros/gravação na Hotmart quando a oferta estiver montada.

BRIEFING - img-entregavel-certificado.jpg
Dobra: 06 - Tipo: 03 Entregável - Função: prova do certificado digital
Sujeito: certificado digital com selo Médico da Dor 2.0, carga horária e assinatura do Dr. Renato
Composição: certificado em leve perspectiva - Proporção: 4:3 - Enquadramento: documento centralizado
Luz: estúdio neutra - Estilo: mockup de documento - Paleta: Azul Profundo + Cobalto + selo, tipografia DM Serif + JetBrains Mono nos números
Fundo: off-white estúdio - por quê: consistência com os demais entregáveis
Evitar: nomes/assinaturas inventados, brasão genérico de stock
PROMPT IA: "Mockup of a digital medical certificate, deep blue and cobalt accents, serif title typography, monospace technical labels for workload hours, warm off-white background, clean and credible, soft studio light"
Alternativa real: usar o template real de certificado do produto quando existir.

BRIEFING - img-bonus-masterclass-ah.jpg
Dobra: 07 - Tipo: 03 Entregável - Função: dar forma ao bônus 1
Sujeito: capa/mockup da MasterClass "Ácido Hialurônico na Medicina da Dor"
Composição: thumbnail de aula + título - Proporção: 16:9 - Enquadramento: capa de vídeo
Luz: estúdio neutra com acento Teal Bioma (tema regenerativo) - Estilo: capa de masterclass - Paleta: Azul Profundo + Teal Bioma
Fundo: card translúcido sobre dobra escura - por quê: a dobra 07 é escura e o tema regenerativo pede o Teal
Evitar: imagem clínica gráfica de procedimento, antes/depois de paciente
PROMPT IA: "Masterclass cover mockup titled about hyaluronic acid in pain medicine, deep blue with teal biotech accent, serif title, clean medical-education aesthetic, soft studio light, no patient imagery"
Alternativa real: frame real da MasterClass (material já produzido na pasta do lançamento).

BRIEFING - img-bonus-checklist-premium.jpg
Dobra: 07 - Tipo: 03 Entregável - Função: dar forma ao bônus 2
Sujeito: mockup do PDF Checklist Premium de Aplicação
Composição: páginas do PDF em leque ou em tablet - Proporção: 4:3 - Enquadramento: documento
Luz: estúdio neutra - Estilo: mockup de PDF premium - Paleta: Azul Profundo + Cobalto, checks em Teal
Fundo: card translúcido sobre dobra escura
Evitar: texto ilegível inventado, passos clínicos específicos falsos
PROMPT IA: "Premium PDF checklist mockup on a tablet, deep blue and cobalt layout with teal checkmarks, clean medical document design, soft studio light, dark elegant background"
Alternativa real: export real do Checklist Premium (material já produzido na pasta do lançamento).

BRIEFING - img-autoridade-renato-retrato.jpg
Dobra: 12 - Tipo: 01 Especialista - Função: ancorar a autoridade do mentor
Sujeito: retrato profissional do Dr. Renato Zaneti
Composição: retrato meio corpo, postura de mentor - Proporção: 4:5 - Enquadramento: terço para texto ao lado
Luz: natural direcional viés frio - Estilo: retrato editorial médico - Paleta: neutra integrável ao Azul Profundo
Fundo: ambiente clínico ou neutro com overlay Azul Profundo - por quê: dobra escura de autoridade
Evitar: pose de stock, fundo branco estourado
PROMPT IA (fallback): "Editorial half-body portrait of a Brazilian orthopedic doctor, white coat or clinical setting, natural cool-toned directional light, confident mentor posture, neutral desaturated palette, documentary style, space for text beside subject"
Alternativa real (preferencial): foto da pasta FOTOS RENATO.

NOTA: img-selo-garantia-7dias e os ícones de módulo/checks NÃO são imagens geradas - são vetor/SVG/Iconify Solar Outline montados na construção.
```

---

# RESUMO FINAL

```
Total dobras: 13 (após remoção das 2 dobras de prova social, por decisão de escopo)
Com imagem: 4 (hero, entregáveis x2 cards, bônus x2 cards, autoridade) | Com CTA: 5 (dobras 01, 05, 10, 12 + barra fixa)
Barra fixa CTA: sim (sticky) | Barra escassez: componente pronto e DESLIGADO (default perpétuo)

IMAGENS (nomes exatos - imutáveis a partir daqui):
 img-hero-renato-clinica.jpg          - dobra 01 - tipo 01 - autoridade de quem faz
 img-entregavel-gravacao-mockup.jpg   - dobra 06 - tipo 03 - acesso à gravação
 img-entregavel-certificado.jpg       - dobra 06 - tipo 03 - certificado digital
 img-bonus-masterclass-ah.jpg         - dobra 07 - tipo 03 - bônus 1 MasterClass
 img-bonus-checklist-premium.jpg      - dobra 07 - tipo 03 - bônus 2 Checklist
 img-autoridade-renato-retrato.jpg    - dobra 12 - tipo 01 - mentor
 (vetor) img-selo-garantia-7dias.svg  - dobra 11 - tipo 08 - selo de garantia

FONTES (Google Fonts):
 DM Serif Display: https://fonts.google.com/specimen/DM+Serif+Display
 Inter: https://fonts.google.com/specimen/Inter
 JetBrains Mono: https://fonts.google.com/specimen/JetBrains+Mono

ÍCONES: Iconify Solar Outline (preferencial) ou Phosphor. PROIBIDO Lucide.

ALERTAS CSS:
 [ ] Hero split -> H1 override clamp(30px, 4.2vw, 54px)
 [ ] Fundo estúdio (mockups) -> filter brightness(1.02) contrast(1.03)
 [ ] Foto em dobra escura -> overlay em camadas (nunca opacity simples)
 [ ] Grain 3% só nas dobras escuras (01, 04, 07, 10, 12)
 [ ] Linha de atualização Cobalto como divisor/sublinhado (elemento de assinatura)
 [ ] Count-up no número DATASUS ao entrar na viewport
 [ ] Componente de escassez honesta presente no CSS porém desligado por default

PENDÊNCIAS DE CONTEÚDO QUE NÃO BLOQUEIAM O VISUAL (resolver antes de publicar):
 - Prova social real (dobras 5 e 13 reintroduzíveis)
 - CRM, RQE, titulações e números do Renato (dobra 12)
 - Razão social, CNPJ, cidade/estado, e-mail (rodapé, dobra 13)
 - WhatsApp comercial (dobra 13)
 - Parcelamento e valores de referência dos bônus (dobras 09 e 10)
 - Ano da fonte DATASUS (dobra 03)
 - Decisão perpétuo x escassez honesta (dobra 10 - componente já previsto)

PRÓXIMOS PASSOS DO PIPELINE:
 -> Etapa 3 (casa7-pagina-vendas-03-direcao): refino do wireframe + geração das imagens nomeadas com os briefings acima
 -> Construção em casa7-pagina-vercel (HTML no padrão drahteacademy/Casa 7) ou casa7-pagina-figma
```

---

Documento gerado pela etapa 2 do pipeline Casa 7 (casa7-pagina-vendas-02-design-system). Identidade do projeto vence a referência. Zero invenção: depoimentos, credenciais e números ausentes ficam marcados [NECESSÁRIO FORNECER/CONFIRMAR] e não entram até serem rastreáveis.
