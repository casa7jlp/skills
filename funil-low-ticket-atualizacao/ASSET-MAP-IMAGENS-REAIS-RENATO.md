# MAPA DE ASSETS REAIS - Imagens da Página Low Ticket

## Dr. Renato Zaneti - Imersão: Atualização em Medicina da Dor

Conecta os slots de imagem nomeados (design system, etapa 2) às pastas e arquivos REAIS de foto do Renato no Drive. Regra Casa 7: usar foto real e rastreável; prompt de IA só como fallback quando não houver asset. Quem finaliza a camada visual é a Vitória (definição do DNA).

Limitação técnica desta sessão: a avaliação visual frame a frame não foi possível pelo ambiente remoto (o leitor de imagem do MCP retorna vazio e o download em base64 é inviável em contexto). O inventário e o mapeamento abaixo estão confirmados por listagem; a escolha do melhor frame de cada pasta deve ser feita por quem abre o Drive (Vitória/Poliana) ou puxando IDs específicos sob demanda.

---

## 1. Inventário das fontes reais

### Pasta `FOTOS RENATO` (id 1Euy0YGWEwcTTQB7IkKp-HtFNi5FlOSB4)
Subpastas:
- **Fotos Profissionais** (id 15bAk5qU9hPsQrAg-JRmfc01KEEtlObZz) - sessão profissional, 11+ retratos editados ("Cópia de NNN_IMG_XXXX.jpg"). FONTE PRINCIPAL para hero e autoridade.
- Fotos não Profissionais - registro casual (uso eventual, menor prioridade).
- Fotos Cirurgias - contexto de procedimento (uso com cautela CFM, sem paciente identificável).
- Método SIS / Hydrogel - contexto técnico de técnicas (apoio, não retrato).
- insta - recortes para redes (formatos variados).
- IA - imagens geradas (NÃO usar como foto real do Renato).
- Família, Videos YT, Vídeos Youtube - fora de escopo da página.

### Pasta `DR. RENATO ZANETI GRAVAÇÃO fotos` (id 19eYiUIF2nhRie27ALAw_TNUGaChyjps_)
- ~9 JPGs de evento/gravação (001_IMG_7944 a 241_IMG_8221) + subpasta Fotos Cirurgias. CONTEXTO de aula/ensino - boa fonte alternativa para o hero (Renato em ambiente de sala/aula, reforça "mentor prático").

---

## 2. Mapa slot -> asset real

| Slot (nome no design system) | Dobra | Fonte real recomendada | O que procurar (do briefing) |
|---|---|---|---|
| `img-hero-renato-clinica.jpg` | 01 Hero | Fotos Profissionais (1a opção) ou GRAVAÇÃO fotos (contexto aula) | meio corpo, 4:5 vertical, terço esquerdo livre para overlay; luz natural viés frio; ambiente clínico/aula; sem paciente identificável |
| `img-autoridade-renato-retrato.jpg` | 12 Autoridade | Fotos Profissionais | retrato meio corpo, 4:5, postura de mentor, fundo neutro integrável ao Azul Profundo |
| `img-entregavel-gravacao-mockup.jpg` | 06 | screenshot real da área de membros/Hotmart (quando montada) | mockup de player com 4 módulos; sem texto/numero inventado |
| `img-entregavel-certificado.jpg` | 06 | template real do certificado do produto | selo Médico da Dor 2.0, carga horária |
| `img-bonus-masterclass-ah.jpg` | 07 | frame real da MasterClass de Ácido Hialurônico (pasta do lançamento) | capa/thumb, acento Teal, sem imagem de paciente |
| `img-bonus-checklist-premium.jpg` | 07 | export real do Checklist Premium (pasta do lançamento) | mockup do PDF |
| `img-selo-garantia-7dias` | 11 | vetor/SVG (não é foto) | selo 7 dias Azul Profundo + Cobalto |

Apoio opcional (se quiser enriquecer dobras): `Fotos Cirurgias`, `Método SIS`, `Hydrogel` dão contexto técnico real - usar só com conformidade CFM (sem antes/depois com tom de garantia, sem paciente identificável).

---

## 3. Tratamento (do design system, para manter unidade)

- Luz global: natural neutra com leve viés frio nas sombras, saturação contida, sem glow.
- Foto em dobra escura (hero, autoridade): overlay Azul Profundo em camadas (nunca opacity simples).
- Hospedagem na construção: Cloudinary (cloud `dlypuyaxt`, padrão das páginas Casa 7/Vercel) - subir o frame escolhido e referenciar pelo nome do slot.

---

## 4. Próximo passo da camada visual

1. Vitória (ou Poliana) abre `FOTOS RENATO/Fotos Profissionais` e escolhe 1 frame para o hero (4:5 com espaço lateral) e 1 para a autoridade.
2. Sobe os dois no Cloudinary com os nomes dos slots.
3. Troca os placeholders nomeados do `index.html` pelas URLs do Cloudinary.
4. Mockups de entregável/bônus: usar assets reais do produto quando existirem; até lá, gerar via fluxo GPT com os prompts dos briefings (etapa 2).

Alternativa: me passe os IDs (ou nomes) dos frames escolhidos que eu já deixo o HTML apontando para eles.

---

Zero invenção. Pasta IA contém imagens geradas - não usar como foto real do expert. Conformidade CFM em qualquer imagem de procedimento.
