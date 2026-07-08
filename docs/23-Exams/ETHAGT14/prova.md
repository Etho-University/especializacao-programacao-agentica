# ETHAGT14 — Prova do Módulo: Escalabilidade & Sistemas Distribuídos de Agentes

> Universidade Etho · Versão 1.0 · Julho 2026
> Duração: ~60 min · 10 questões · closed book · Pilar Técnico (40%)

Esta prova avalia levar sistemas de agentes a **escala de produção**: identificar gargalos, caching, model routing, distribuição (sharding/replica) e FinOps de agentes.

---

## Parte 1 — Conceitos (Q1-4)

**1. (Múltipla escolha)** Em sistemas de agentes em escala, o gargalo dominante costuma ser:
- (a) A rede entre microsserviços.
- (b) A latência e o custo do LLM (crescendo com o contexto).
- (c) O disco local dos workers.

**2. (V/F justificado)** "Streaming de tokens reduz a latência total da requisição."

**3. (Múltipla escolha)** *Cache semântico* difere do cache de prompt (exact match) porque:
- (a) Usa embedding para casar perguntas semanticamente equivalentes, não só idênticas.
- (b) Sempre é mais rápido que exact match.
- (c) Só funciona para tools, não para prompts.

**4. (V/F justificado)** "Workers stateless são sempre preferíveis a stateful."

---

## Parte 2 — Aplicação e trade-off (Q5-8)

**5. (Trade-off)** Dê 2 situações em que o **cache semântico falha** (retorna resposta errada/stale) e como mitigar.

**6. (Debug)** O custo de um agente cresceu 5× após adicionar mais tools ao contexto. Diagnóstico + 2 correções concretas.

**7. (Análise)** Para **model routing** por complexidade: como medir a complexidade da pergunta? Descreva 2 abordagens e um risco de cada.

**8. (Trade-off)** Justifique o trade-off **custo × latência × qualidade** e dê 1 alavanca que move dois deles favoravelmente ao custo.

---

## Parte 3 — Projeto curto (Q9-10)

**9. (Projeto)** Escreva o esqueleto de um **orçamento por execução** com *circuit breaker*: se o custo acumulado exceder o limite, a execução aborta com erro.

**10. (Projeto)** Descreva uma estratégia de **sharding por tenant** para um agente multi-tenant: como particionar, onde fica o estado, e como garantir isolamento.

---

## Critérios de correção (resumo)

| Parte | Questões | Peso |
|---|---|---|
| Conceitos | 1, 2, 3, 4 | 40% |
| Aplicação/trade-off | 5, 6, 7, 8 | 40% |
| Projeto curto | 9,10 | 20% |

**Conversão**: cada questão vale 10 pts; total 100 pts → nota 1-5.
- 90+: 5,0 · 80-89: 4,5 · 70-79: 4,0 · 60-69: 3,5 · 50-59: 3,0 (mínimo) · <50: reprovação.

Gabarito comentado em [`gabarito.md`](gabarito.md).
