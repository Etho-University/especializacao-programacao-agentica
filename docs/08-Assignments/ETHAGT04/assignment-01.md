# ETHAGT04 — Avaliação do Módulo

> Curso: Reasoning & Planning (do CoT ao inference-time reasoning) · Nota mínima de aprovação: 3,0

## Composição da nota (4 pilares)

| Pilar | Peso | Instrumento |
|---|---|---|
| Técnico | 40% | Projeto (agente GAIA com ≥3 padrões de raciocínio) + prova de padrões |
| Consultivo | 30% | Apresentação comparativa para especialista |
| Comportamental | 20% | Code review |
| Prático | 10% | Demo: padrão escolhido resolvendo caso |

**Nota final** = Σ(pilar × peso).

---

## Rubrica — Pilar Técnico (40%)

O projeto exige implementar um agente que resolve um subconjunto de GAIA usando pelo menos 3 padrões de raciocínio (ex.: ReAct, Plan-and-Execute, Reflexion, ToT, LATS), comparando resultados e justificando a escolha.

| Critério | Peso | 1 (muito abaixo) | 3 (esperado) | 5 (referência) |
|---|---|---|---|---|
| Correção técnica | 25% | Agente não resolve nenhum caso de GAIA | Resolve subconjunto com ≥3 padrões funcionais; success rate mensurado | ≥3 padrões completos + casos de borda (orçamento de tokens estourado, loop detectado, re-planejamento acionado) |
| Qualidade arquitetural | 25% | Padrões acoplados; sem separação planner/executor/reflector | Separação razoável entre estratégia de raciocínio e agent loop | Padrões como estratégias intercambiáveis; ADR justifica escolha de reasoning model vs prompting |
| Profundidade | 20% | Superficial; não entende as estratégias | Compara success rate entre padrões; discute custo × qualidade × latência | Discute trade-offs (quando ToT vale vs CoT, quando reasoning model substitui ToT), analisa falhas por classe de problema |
| Produção-ready | 15% | Só roda em notebook | Roda em ambiente controlado com Docker; benchmark reproduzível | Docker + orçamento de tokens/passos configurável + benchmark reproduzível em subset GAIA + ADR de estratégia |
| Avaliação/observabilidade | 15% | Sem benchmark | Success rate por padrão + custo/latência básicos | Benchmark com traces por padrão, detecção/quebra de loops documentada, análise de convergência (Reflexion) |

**Prova de padrões** (parte do Pilar Técnico): mapear classes de problema a estratégias, explicar ReWOO vs ReAct em custo, estrutura de memória de Reflexion, quando reasoning model nativo substitui prompting. Peso: 40% do pilar técnico.

---

## Critérios dos demais pilares

- **Consultivo (30%):** Apresentação comparativa dos padrões para um especialista (banca).
  - *1:* Apresenta resultados sem análise crítica.
  - *3:* Compara ≥3 padrões com dados (success rate, custo) e recomenda um.
  - *5:* Articula trade-offs com evidência, discute limites de cada padrão, identifica cenários onde a recomendação mudaria.

- **Comportamental (20%):** Code review do projeto de um colega.
  - *1:* Comentários ausentes ou genéricos.
  - *3:* ≥5 observações sobre lógica de raciocínio, orçamento de tokens e tratamento de loops.
  - *5:* Identifica bugs de re-planejamento, sugere estratégias alternativas, avalia robustez do Reflexion memory.

- **Prático (10%):** Demo: padrão escolhido resolvendo um caso de GAIA ao vivo.
  - *1:* Agente não resolve o caso ou entra em loop.
  - *3:* Resolve o caso em tempo aceitável, mostrando o raciocínio.
  - *5:* Mostra traces do plano, detecta/quebra loop, justifica a estratégia em tempo real.

---

## Regras

- Entrega: repositório Git com código, benchmark, ADR de estratégia (`./docs/adr-001-reasoning.md`) e traces.
- **Integridade acadêmica:** success rates devem ser reais e reproduzíveis. Fabricação de resultados resulta em nota 1,0 e processo disciplinar.
- Atraso: -0,5 ponto por dia útil, até 3 dias.
