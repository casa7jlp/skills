# AUTOMAÇÃO DE ENTREGA E NUTRIÇÃO - Low Ticket

## Imersão: Atualização em Medicina da Dor (gravação) - Dr. Renato Zaneti

Sequência de e-mail (ActiveCampaign) + WhatsApp (ManyChat) que entrega o acesso, nutre o comprador na voz do Renato e o aquece para o retargeting da Imersão Microfat (hands-on, high ticket). Pipeline Casa 7. Identidade e tom do DNA v2. Compliance CFM aplicado.

Papel estratégico: o low ticket é a porta de entrada (SLO). Esta automação faz três trabalhos - entregar bem (reduz reembolso), nutrir (gera consumo e confiança) e qualificar/aquecer o comprador para a esteira (entra no pixel e na lista quente de retargeting da imersão hands-on, vendida por application funnel).

---

## 1. Arquitetura e stack

- **Checkout:** Hotmart (oferta a R$ 97).
- **E-mail:** ActiveCampaign (plataforma oficial Casa 7).
- **WhatsApp:** ManyChat (automação e broadcast). Conversa humana de venda do high ticket fica no número do closer (Jonathan), não na automação.
- **Gatilho de entrada:** postback de "compra aprovada" da Hotmart -> cria/atualiza contato no ActiveCampaign com a tag `comprador-imersao-lowticket` e, se houver opt-in de WhatsApp, dispara o fluxo no ManyChat.
- **Pixel:** o comprador passa pela página de obrigado com o Pixel da Meta instalado, entrando no público de retargeting da Imersão Microfat. `[NECESSÁRIO FORNECER pixel ID]`.

Regra de duração de acesso: usar sempre "acesso imediato". Nunca prometer duração ("vitalício" proibido).

---

## 2. Mapa do fluxo

```
COMPRA APROVADA (Hotmart postback)
   |
   +-> ActiveCampaign: cria contato + tag comprador-imersao-lowticket
   |       |
   |       +-> Automação de E-MAIL (E0 a E5) - entrega + nutrição + ponte
   |
   +-> Pagina de obrigado com Pixel Meta -> publico de retargeting da Imersao Microfat
   |
   +-> [se opt-in WhatsApp] ManyChat: fluxo W0 a W3 - entrega + engajamento + teaser
           |
           +-> quem demonstra interesse no proximo nivel recebe a tag lead-quente-microfat
                   |
                   +-> entra na LISTA QUENTE de retargeting + (futuro) application funnel do hands-on
```

Princípio: a automação aquece e qualifica, mas NÃO vende o high ticket por aqui. A venda da Imersão Microfat acontece por application funnel + closer humano (fora desta aba). Aqui a gente só identifica quem levanta a mão e o entrega aquecido para o retargeting.

---

## 3. Sequência de E-MAIL (ActiveCampaign)

Tom: mentor prático, professoral empático, coloquial, direto. Sem promessa de faturamento, cura ou resultado clínico garantido. Sem sensacionalismo. Hífen comum, sem emoji decorativo.

Remetente sugerido: `Dr. Renato Zaneti <[NECESSÁRIO FORNECER e-mail]>`.

---

### E0 - Imediato - ENTREGA DO ACESSO

**Assunto:** Seu acesso à Imersão já está liberado
**Pré-cabeçalho:** Entra aqui e começa quando quiser.

Cara, seja bem-vindo.

Sua inscrição na Imersão: Atualização em Medicina da Dor está confirmada e o acesso já está liberado. É só entrar e começar quando quiser, no seu tempo.

Acessar a imersão: `[NECESSÁRIO FORNECER link da área de membros / gravação]`

O que tem lá dentro:
- As 4 horas completas, divididas em 4 módulos (Mesoterapia, Proloterapia e regenerativas, Protocolos e raciocínio clínico, Aplicação ética e conforme o CFM).
- Bônus 1: MasterClass de Ácido Hialurônico na Medicina da Dor.
- Bônus 2: Checklist Premium de Aplicação.
- Seu certificado digital, disponível ao final.

Uma dica: não tenta ver tudo de uma vez. Começa pelo Módulo 1, com calma, com o caderno do lado. Essa imersão foi feita pra você rever quantas vezes precisar antes de levar pro consultório.

Qualquer problema de acesso, é só responder este e-mail.

Dr. Renato Zaneti
Médico da Dor 2.0

---

### E1 - +1 dia - BOAS-VINDAS + COMO APROVEITAR

**Assunto:** Por onde começar (pra não se perder)
**Pré-cabeçalho:** O caminho que eu faria no seu lugar.

Você já entrou na imersão?

Se ainda não, esse é o empurrão. Se já entrou, deixa eu te dar o caminho que eu faria no seu lugar.

Comece pelo Módulo 1 (Mesoterapia). Não é a parte mais sofisticada, é a base que sustenta todo o resto. Quando você entende o princípio farmacológico e a indicação certa, o resto da imersão para de parecer técnica solta e vira raciocínio.

Depois siga na ordem. O Módulo 3 (Protocolos e raciocínio clínico) é onde a ficha cai pra maioria dos médicos, porque é onde a técnica vira conduta.

Eu montei essa imersão do jeito que eu queria ter aprendido: sem enrolação, com o que eu uso no consultório de verdade. Eu só ensino o que eu vivo.

Bons estudos. Volto em breve com uma parte que quase ninguém ensina.

Dr. Renato Zaneti

---

### E2 - +3 dias - NUTRIÇÃO 1 (aplicação na prática)

**Assunto:** O que fazer na segunda de manhã
**Pré-cabeçalho:** Repertório sem aplicação não muda nada.

A diferença entre o médico que se atualiza e o que muda de verdade não está em quanto ele assiste. Está em quanto ele aplica.

Repertório parado é igual aparelho parado na sala: não resolve o problema de ninguém e ainda pesa na consciência.

Então, antes de seguir, pega o Checklist Premium de Aplicação (está nos seus bônus) e olha o próximo paciente da sua agenda com ele na mão. Não precisa ser o caso mais complexo. Precisa ser o primeiro.

E se você ainda tem dúvida sobre quando indicar ácido hialurônico, separa a MasterClass de bônus. Ela mostra por que nem todo ácido hialurônico é igual, os três tipos e quando cada um faz sentido. É a aula que organiza uma decisão que muita gente toma no chute.

Aplica. Depois me conta.

Dr. Renato Zaneti

---

### E3 - +5 dias - NUTRIÇÃO 2 (mentor / cobrar certo)

**Assunto:** Não é cobrar caro, é cobrar certo
**Pré-cabeçalho:** A parte que não está no protocolo.

Tem uma objeção que aparece em quase todo médico que começa a aplicar essas técnicas: "meu paciente não vai pagar por isso".

Quase sempre não é o paciente. É o médico que ainda não acredita no que entrega.

Quando você domina o protocolo, entende a indicação e sabe explicar o porquê, o preço deixa de ser um problema e vira consequência. Não é sobre cobrar caro. É sobre cobrar certo pelo que resolve.

Isso não é papo de venda. É o que separa o médico que vive de plantão do que faz o consultório virar a fonte principal. E está dentro do que o CFM permite, desde que você comunique com ética. A imersão tem um módulo inteiro sobre isso por um motivo.

Revê o Módulo 4 com essa lente. Muda tudo.

Dr. Renato Zaneti

---

### E4 - +8 dias - PONTE PARA O PRÓXIMO NÍVEL (teaser Microfat)

**Assunto:** O degrau seguinte (quando você estiver pronto)
**Pré-cabeçalho:** Onde a medicina regenerativa fica séria de verdade.

A essa altura você já viu que medicina da dor sem cirurgia não é promessa, é ferramenta. Mesoterapia, proloterapia, ácido hialurônico: isso resolve uma fatia enorme da sua agenda.

Mas existe um degrau acima, pra quem já pratica e quer dominar uma técnica regenerativa de maior complexidade, com a mão na massa: o Microfat, o microenxerto adiposo aplicado em joelho e articulações.

Isso não se aprende vendo vídeo. Se aprende fazendo, ao vivo, aplicando em paciente real sob supervisão, com protocolo, indicação e a parte ética bem amarrada. É por isso que eu trato isso numa imersão presencial, de turma pequena, e não num curso gravado.

Ainda não é a hora de te falar de data e de vaga. É a hora de você saber que esse caminho existe e que ele é o passo natural depois do que você está estudando agora.

Se você quer ser avisado em primeira mão quando a próxima turma abrir, responde este e-mail com a palavra MICROFAT. Eu separo a lista de quem está pronto pra esse nível.

Dr. Renato Zaneti

> Nota de copy: a resposta com "MICROFAT" (ou clique no link equivalente) aplica a tag `lead-quente-microfat`. Esse lead entra na lista quente e no público de retargeting da imersão hands-on. Sem preço, sem promessa de faturamento - só manifestação de interesse.

---

### E5 - +12 dias - REFORÇO + PORTA ABERTA

**Assunto:** O que você faz com isso agora
**Pré-cabeçalho:** Conhecimento sem ação envelhece rápido.

Já faz quase duas semanas que você entrou na imersão. Vale uma pergunta honesta: você já aplicou alguma coisa, ou ainda está só guardando?

Não tem julgamento aqui. Mas conhecimento médico que não vira conduta envelhece rápido, e o paciente que precisava da sua atualização continua na fila.

Se você travou em algum ponto, volta no módulo certo. Se você aplicou, repete e vai ganhando repertório. É assim que se constrói segurança: não em teoria, em quilometragem.

E quando você sentir que dominou o que está aqui e quer ir pro próximo nível, você já sabe qual é (te falei dele no último e-mail). A porta vai estar aberta.

Conta comigo.

Dr. Renato Zaneti

---

## 4. Sequência de WHATSAPP (ManyChat)

Só para quem deu opt-in. Tom mais curto e humano que o e-mail. Mensagens pensadas para resposta (engajamento qualifica o lead). Número/conta: `[NECESSÁRIO FORNECER número comercial / conta ManyChat]`.

---

**W0 - Imediato (entrega)**

Oi {{nome}}, aqui é da equipe do Dr. Renato.
Sua inscrição na Imersão: Atualização em Medicina da Dor está confirmada e o acesso já está liberado.
Entra por aqui: `[NECESSÁRIO FORNECER link]`
Qualquer dificuldade pra acessar, responde aqui que a gente resolve.

---

**W1 - +1 dia (início)**

{{nome}}, conseguiu acessar a imersão?
Dica do Dr. Renato: comece pelo Módulo 1, com calma. É a base que sustenta o resto.
Se aparecer qualquer dúvida no caminho, me chama.

---

**W2 - +4 dias (engajamento / qualificação)**

{{nome}}, me conta uma coisa rápida: qual módulo você já assistiu?
1 - Mesoterapia
2 - Proloterapia e regenerativas
3 - Protocolos e raciocínio clínico
4 - Aplicação ética e CFM
(Responde com o número. Quero entender por onde você está.)

> Regra ManyChat: a resposta serve para segmentar engajamento (tag `assistiu-em-andamento` / `assistiu-avancado`). Quem chega no Módulo 2 ou além é candidato natural ao teaser do hands-on.

---

**W3 - +8 dias (teaser Microfat / levantar a mão)**

{{nome}}, depois que o médico domina o que está nesta imersão, costuma aparecer a pergunta: e o próximo nível?
O degrau seguinte é o Microfat, o microenxerto adiposo aplicado em joelho e articulações. É hands-on, presencial, turma pequena, aplicando em paciente real. Não dá pra aprender vendo vídeo.
Quer ser avisado em primeira mão quando a próxima turma abrir?
[Botão: QUERO SER AVISADO] [Botão: AGORA NÃO]

> Regra ManyChat: o botão QUERO SER AVISADO aplica a tag `lead-quente-microfat` e adiciona o contato à lista quente de retargeting/application funnel da Imersão Microfat. AGORA NÃO mantém o lead na nutrição padrão, sem insistir.

---

## 5. Tags e segmentação

| Tag | Onde aplica | Uso |
|---|---|---|
| `comprador-imersao-lowticket` | entrada (Hotmart) | base de compradores, supressão em campanhas de aquisição |
| `acesso-confirmado` | clicou no link de acesso | quem não tem -> reforço de entrega |
| `assistiu-em-andamento` / `assistiu-avancado` | resposta W2 | segmenta engajamento |
| `lead-quente-microfat` | E4 (resposta MICROFAT) ou W3 (botão) | lista quente + retargeting do hands-on |
| `opt-out-microfat` | AGORA NÃO / não responde | mantém na nutrição, sem teaser repetido |

Supressão: quem tem `comprador-imersao-lowticket` sai dos anúncios de aquisição do low ticket (não pagar pra reimpactar quem já comprou).

---

## 6. Ponte para o retargeting da Imersão Microfat

O comprador do low ticket é exatamente o público que o high ticket quer: médico com CRM ativo, consultório, já praticando ou querendo praticar medicina da dor. Esta automação entrega esse público para a esteira de duas formas:

1. **Pixel (passivo):** todo comprador entra no público de retargeting da Imersão Microfat ao passar pela página de obrigado. Mesmo quem não levanta a mão alimenta o público de anúncios.
2. **Lista quente (ativo):** quem responde MICROFAT (e-mail) ou clica em QUERO SER AVISADO (WhatsApp) recebe a tag `lead-quente-microfat` e fica pronto para o application funnel quando a turma abrir.

O que esta automação NÃO faz (de propósito): não revela preço do hands-on, não promete faturamento, não tenta fechar venda. Isso é trabalho do application funnel + closer (Jonathan), fora desta aba.

---

## 7. Pendências [NECESSÁRIO FORNECER / CONFIRMAR]

- Link da área de membros / gravação (E0, E1, W0, W1).
- E-mail remetente oficial do Renato.
- Número comercial / conta ManyChat do WhatsApp.
- Pixel ID da Meta (página de obrigado).
- Postback da Hotmart configurado para o ActiveCampaign (oferta a R$ 97 confirmada).
- Confirmar opt-in de WhatsApp no checkout (LGPD) antes de disparar o fluxo ManyChat.
- Detalhes da Imersão Microfat (cidade, data, tamanho de turma): briefing v2 (20/mai) diz SP ou cidade-base, turma 15-20; handoff do funil cita Chapecó, turma 2-3, 10/jul/2026. CONFLITO - confirmar antes de qualquer peça que mencione especifico. Por isso o teaser aqui é só conceito, sem cravar dado.

---

## 8. Compliance CFM (aplicado em toda a sequência)

- Sem promessa de faturamento ou de resultado financeiro específico (nem nos e-mails de "cobrar certo": fala de precificação como consequência de domínio técnico, não como garantia de ganho).
- Sem promessa de cura ou resultado clínico garantido.
- Sem antes/depois de paciente com tom de garantia.
- Foco em atualização técnica, repertório, raciocínio clínico e ética.
- Estatística só com fonte (não há número de aluno ou depoimento inventado em nenhuma mensagem).
- "Acesso imediato" sem prometer duração.

---

Documento gerado na trilha de automação do funil low ticket (Casa 7). Zero invenção: links, números, dados e detalhes do hands-on ausentes ficam marcados e não entram até serem rastreáveis. Tom e identidade conforme DNA-Renato-Zaneti v2.
