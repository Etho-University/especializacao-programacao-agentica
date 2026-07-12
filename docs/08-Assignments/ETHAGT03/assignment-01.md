# ETHAGT03 — Avaliação do Módulo

> Curso: Padrões de Workflow Agêntico (os 5 da Anthropic + composições) · Nota mínima de aprovação: 3,0

## Composição da nota (4 pilares)

| Pilar | Peso | Instrumento |
|---|---|---|
| Técnico | 40% | Projeto (workflow composto) + prova de trade-offs |
| Consultivo | 30% | Defesa do ADR para "cliente" |
| Comportamental | 20% | Code review em duplas |
| Prático | 10% | Demo: workflow escolhido rodando |

**Nota final** = Σ(pilar × peso).

---

## Rubrica — Pilar Técnico (40%)

O projeto exige projetar e implementar o workflow mais adequado para síntese de relatório a partir de múltiplas fontes, comparando 2 abordagens (ex.: prompt chaining vs orchestrator-workers) em qualidade, custo e latência.

| Critério | Peso | 1 (muito abaixo) | 3 (esperado) | 5 (referência) |
|---|---|---|---|---|
| Correção técnica | 25% | Workflow não produz relatório; gates ausentes | Workflow funcional com gates programáticos; 2 abordagens implementadas e comparáveis | 2 abordagens completas + casos de borda (fonte indisponível, gate falha, composição routing→parallelization→evaluator) |
| Qualidade arquitetural | 25% | Sem separação de stages; estado global mutável | Separação razoável de stages com estado explícito (LangGraph state) | Padrões canônicos claros, gates injetáveis, composição justificada em ADR |
| Profundidade | 20% | Superficial; não distingue os 5 workflows | Compara as 2 abordagens em ≥3 dimensões (qualidade, custo, latência) | Discute trade-offs de cada workflow, identifica quando composição vira agente, justifica escolha vs agente autônomo |
| Produção-ready | 15% | Só roda em notebook | Roda em ambiente controlado com Docker; benchmark em ≥20 casos | Docker + profiler de custo/latência próprio + benchmark reproduzível em ≥20 casos |
| Avaliação/observabilidade | 15% | Sem medições | Métricas básicas (custo, latência, qualidade subjetiva) | Benchmark automatizado com métricas comparativas (custo/case, latência p50/p95, quality score) documentadas |

**Prova de trade-offs** (parte do Pilar Técnico): para 5 cenários, indicar o workflow mais adequado e justificar; explicar gates, voting vs sectioning, condição de parada de evaluator-optimizer. Peso: 40% do pilar técnico.

---

## Critérios dos demais pilares

- **Consultivo (30%):** Defesa do ADR para "cliente" (banca simulada) justificando a escolha de workflow.
  - *1:* ADR ausente ou genérico; não justifica a escolha.
  - *3:* ADR coerente com ≥3 critérios; defende a escolha frente a perguntas.
  - *5:* Usa dados do benchmark para justificar; articula sinais de que a escolha precisaria evoluir; recomendação acionável.

- **Comportamental (20%):** Code review em duplas do workflow do colega.
  - *1:* Comentários ausentes ou genéricos.
  - *3:* ≥5 observações sobre correção de gates, estrutura de state e edge cases.
  - *5:* Sugere simplificação (princípio "comece simples"), identifica complexidade prematura, propõe refactor de composição.

- **Prático (10%):** Demo: workflow escolhido rodando em um caso ao vivo.
  - *1:* Workflow não roda ou falha na demo.
  - *3:* Workflow produz relatório coerente com tempo aceitável.
  - *5:* Mostra gates disparando, mede custo/latência em tempo real, lida com fonte indisponível.

---

## Regras

- Entrega: repositório Git com código, benchmark, ADR (`./docs/adr-001-workflow.md`) e dados de comparação.
- **Integridade acadêmica:** assistência de IA é permitida e deve ser declarada. Medições devem ser reais (não inventadas). Plágio ou fabricação de dados resulta em nota 1,0.
- Atraso: -0,5 ponto por dia útil, até 3 dias.
