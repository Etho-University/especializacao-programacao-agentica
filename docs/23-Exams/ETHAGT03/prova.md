---
password: Etho-Prof-2026
---
# ETHAGT03 — Prova do Módulo: Padrões de Workflow Agêntico

> Universidade Etho · Versão 1.0 · Julho 2026
> Duração: ~60 min · 10 questões · closed book · Pilar Técnico (40%)

Esta prova avalia os 5 padrões canônicos de workflow (Anthropic), suas composições e o critério de decisão entre workflow e agente autônomo.

---

## Parte 1 — Conceitos (Q1-4)

**1. (Múltipla escolha)** Qual é a diferença crucial entre Orchestrator-Workers e Parallelization?
- (a) Orchestrator-Workers é mais rápido
- (b) Na Parallelization a decomposição é fixa; no Orchestrator-Workers ela é dinâmica, decidida pelo LLM
- (c) Orchestrator-Workers usa modelos menores
- (d) Parallelization sempre tem votação

**2. (V/F justificado)** "Para 80% de perguntas fáceis e 20% difíceis, Routing por modelo (Haiku vs Sonnet) economiza custo mantendo qualidade."

**3. (Múltipla escolha)** Qual padrão implementa "gerar → avaliar → refinar até critério"?
- (a) Prompt Chaining
- (b) Routing
- (c) Evaluator-Optimizer
- (d) Orchestrator-Workers

**4. (V/F justificado)** "Orchestrator-Workers é sempre melhor que Parallelization."

---

## Parte 2 — Aplicação e trade-off (Q5-8)

**5. (Trade-off)** Diferencie Sectioning e Voting dentro de Parallelization. Dê um cenário onde cada brilha.

**6. (Análise de composição)** Descreva a composição `Routing → Parallelization → Evaluator-Optimizer` aplicada a suporte ao cliente. O que cada etapa faz?

**7. (Debug de workflow)** Um colega construiu um "workflow" com 40 `if/else` para tentar prever todos os caminhos possíveis de atendimento. A latência explodiu e o sistema falha em casos que um humano resolveria adaptando o caminho. Qual é o diagnóstico?

**8. (V/F justificado)** "Gates em Prompt Chaining devem ser implementados por LLM, nunca por código determinístico."

---

## Parte 3 — Projeto curto (Q9-10)

**9. (Projeto curto)** Escreva a condição de parada (3 critérios) de um loop Evaluator-Optimizer para tradução de documentação técnica, incluindo código.

**10. (Projeto curto)** Para os 3 cenários abaixo, indique o workflow mais adequado e justifique em uma frase:
- (a) Traduzir um documento de 50 páginas para 3 idiomas simultaneamente
- (b) Triar tickets de suporte em cobrança/técnico/cancelamento
- (c) Gerar um rascunho de artigo → validar se cobre tópicos obrigatórios → polir

---

## Critérios de correção (resumo)

| Conceito | Questões | Peso |
|---|---|---|
| Padrões canônicos | 1, 3, 5 | 30% |
| Composição & fronteira | 4, 6, 7 | 25% |
| Trade-offs (custo/latência/qualidade) | 2, 8 | 20% |
| Escolha de padrão | 10 | 15% |
| Implementação | 9 | 10% |

**Conversão**: cada questão vale 10 pts; total 100 pts. Nota 1-5.
- 90+ pts: 5,0
- 75-89: 4,0
- 60-74: 3,0 (mínimo aprovação)
- <60: reprovação.

Gabarito comentado em [`gabarito.md`](gabarito.md).
