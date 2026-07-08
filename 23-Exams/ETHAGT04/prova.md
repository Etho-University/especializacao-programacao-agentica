# ETHAGT04 — Prova do Módulo: Reasoning & Planning

> Universidade Etho · Versão 1.0 · Julho 2026
> Duração: ~60 min · 10 questões · closed book · Pilar Técnico (40%)

Esta prova avalia estratégias de raciocínio e planejamento para agentes: CoT, Plan-and-Execute, ReWOO, Tree of Thoughts, Reflexion, Self-Discover e inference-time reasoning nativo.

---

## Parte 1 — Conceitos (Q1-4)

**1. (Múltipla escolha)** Organize CoT, Plan-and-Execute e Reflexion segundo o eixo "estrutura": qual é linear, qual adiciona auto-correção?
- (a) CoT = árvore; Plan-and-Execute = linear; Reflexion = árvore
- (b) CoT = linear sem reflexão; Plan-and-Execute = linear sem reflexão; Reflexion = adiciona auto-correção
- (c) Todos são lineares
- (d) CoT = árvore; Plan-and-Execute = árvore; Reflexion = linear

**2. (V/F justificado)** "CoT melhora a precisão em qualquer tarefa, incluindo recuperação factual simples como 'qual a capital da França?'."

**3. (Múltipla escolha)** Por que o ReWOO reduz custo comparado ao ReAct?
- (a) Usa modelos menores
- (b) O planner gera o plano inteiro de uma vez ("cego"), sem re-raciocinar entre passos, e executa em paralelo
- (c) Não usa ferramentas
- (d) Faz cache dos resultados

**4. (V/F justificado)** "Com um reasoning model nativo (o1/o3), você ainda deve promptar 'pense passo a passo' para maximizar a qualidade."

---

## Parte 2 — Aplicação e trade-off (Q5-8)

**5. (Trade-off)** Compare ReAct, Plan-and-Execute e ReWOO em latência, custo (tokens) e robustez a planos errados. Use uma tabela.

**6. (Análise de estratégia)** Dê 2 critérios para decidir se vale a pena usar Tree of Thoughts (ToT) em um problema, dado que é "artilharia pesada".

**7. (Debug de raciocínio)** Um agente Reflexion está re-planejando indefinidamente: falha → reflete → refaz → falha de novo → reflete... Qual é a defesa canônica para evitar isso?

**8. (V/F justificado)** "Self-Discover é sempre superior a CoT."

---

## Parte 3 — Projeto curto (Q9-10)

**9. (Projeto curto)** Escreva a estrutura (esqueleto em Python) de um agente Reflexion com 3 atores (Actor, Evaluator, Self-Reflection) e memória de erros acumulada entre tentativas.

**10. (Projeto curto)** Para estes 3 cenários, indique a estratégia de raciocínio mais adequada e justifique:
- (a) Resolver um problema de aritmética do GSM8K
- (b) Depurar um bug que pode levar 2 ou 20 passos
- (c) Problema tão novo que não há padrão conhecido

---

## Critérios de correção (resumo)

| Conceito | Questões | Peso |
|---|---|---|
| Tipologia & CoT | 1, 2 | 20% |
| Plan-and-Execute & ReWOO | 3, 5 | 20% |
| ToT & Reflexion | 6, 7, 9 | 25% |
| Reasoning nativo & Self-Discover | 4, 8 | 15% |
| Escolha de estratégia | 10 | 20% |

**Conversão**: cada questão vale 10 pts; total 100 pts. Nota 1-5.
- 90+ pts: 5,0
- 75-89: 4,0
- 60-74: 3,0 (mínimo aprovação)
- <60: reprovação.

Gabarito comentado em [`gabarito.md`](gabarito.md).
