# ETHAGT12 — Prova do Módulo: AgentOps, Observabilidade & Avaliação

> Universidade Etho · Versão 1.0 · Julho 2026
> Duração: ~60 min · 10 questões · closed book · Pilar Técnico (40%)

Esta prova avalia **rigor experimental** em agentes: observar (traces), medir (métricas), avaliar (LLM-as-judge, golden cases, benchmarks) e iterar com confiança.

---

## Parte 1 — Conceitos (Q1-4)

**1. (Múltipla escolha)** A diferença central entre *log estruturado* e *trace distribuído* é:
- (a) Logs são sempre mais baratos; traces são só para LLMs.
- (b) Traces modelam spans hierárquicos com contexto/causalidade (bags); logs são eventos isolados.
- (c) Não há diferença prática.

**2. (V/F justificado)** "Bom score num benchmark canônico (ex.: SWE-bench) garante bom desempenho em produção."

**3. (Múltipla escolha)** Qual NÃO é um viés típico do *LLM-as-judge*?
- (a) Viés de posição (preferir a primeira opção).
- (b) Viés de verbosidade (preferir respostas mais longas).
- (c) Viés de custo (preferir sempre a opção mais barata).

**4. (V/F justificado)** "Você só confia numa mudança se mediu antes e depois em um conjunto de regressão."

---

## Parte 2 — Aplicação e trade-off (Q5-8)

**5. (Trade-off)** Liste 3 motivos pelos quais agentes são particularmente difíceis de avaliar em relação a um LLM isolado.

**6. (Debug)** Um LLM-as-judge dá nota 4,5/5 a uma resposta que um humano avaliou como errada. Cite 2 causas prováveis e 2 mitigações.

**7. (Análise)** Diferencie métricas de **tarefa** (success rate, partial credit) de métricas de **processo** (steps, loops, tool misuse). Por que ambas importam?

**8. (Trade-off)** Quando vale usar um **benchmark canônico** (GAIA, τ-bench) vs construir um **benchmark custom**?

---

## Parte 3 — Projeto curto (Q9-10)

**9. (Projeto)** Escreva um **golden case** (input, expected, critério de sucesso mensurável) para um agente que cancela um pedido de e-commerce.

**10. (Projeto)** Liste 3 sinais de **contaminação de benchmark** e como detectá-los.

---

## Critérios de correção (resumo)

| Parte | Questões | Peso |
|---|---|---|
| Conceitos | 1, 2, 3, 4 | 40% |
| Aplicação/trade-off | 5, 6, 7, 8 | 40% |
| Projeto curto | 9, 10 | 20% |

**Conversão**: cada questão vale 10 pts; total 100 pts → nota 1-5.
- 90+: 5,0 · 80-89: 4,5 · 70-79: 4,0 · 60-69: 3,5 · 50-59: 3,0 (mínimo) · <50: reprovação.

Gabarito comentado em [`gabarito.md`](gabarito.md).
