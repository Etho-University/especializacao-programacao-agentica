---
password: Etho-Prof-2026
---
# ETHAGT01 — Prova do Módulo: Arquitetura Cognitiva de Agentes LLM

> Universidade Etho · Versão 1.0 · Julho 2026
> Duração: ~60 min · 10 questões · closed book · Pilar Técnico (40%)

Esta prova avalia os fundamentos da programação agêntica: o Augmented LLM, o agent loop ReAct, a distinção workflow vs agente e a observabilidade desde o primeiro dia.

---

## Parte 1 — Conceitos (Q1-4)

**1. (Múltipla escolha)** A decomposição canônica do "Augmented LLM" (Anthropic) inclui quatro extensões. Qual alternativa lista corretamente as quatro?
- (a) Prompt · modelo · fine-tuning · RAG
- (b) Retrieval · Tools · Memory · Loop de controle
- (c) Percepção · Brain · Planning · Collaboration
- (d) Chain-of-Thought · function calling · caching · guardrails

**2. (V/F justificado)** "Toda aplicação de LLM deveria ser um agente autônomo."

**3. (Múltipla escolha)** A taxonomia unificada (arXiv:2601.12560) decompõe um agente em seis componentes. Qual NÃO é uma delas?
- (a) Perception
- (b) Brain
- (c) Fine-tuning
- (d) Collaboration

**4. (V/F justificado)** "A recuperação (retrieval) no Augmented LLM é estática e externa ao modelo, exatamente como no RAG ingênuo."

---

## Parte 2 — Aplicação e trade-off (Q5-8)

**5. (Trade-off)** Um colega propõe começar um projeto de atendimento ao cliente diretamente com um agente totalmente autônomo. Cite o princípio de Anthropic que ele está violando e dê 2 riscos concretos dessa decisão.

**6. (Debug de trace)** Um agente ReAct produz o seguinte trace e entra em loop infinito:
```
Thought: Preciso buscar o preço.
Action: search_price
Action Input: {"product": "laptop"}
Observation: ERRO: Ferramenta 'search_price' não existe.
Thought: Vou tentar novamente.
Action: search_price
Action Input: {"product": "laptop"}
Observation: ERRO: Ferramenta 'search_price' não existe.
```
Identifique 2 problemas e proponha correções.

**7. (Análise de trade-off)** Compare usar ReAct em Python puro vs LangGraph para um agente de produção. Liste 1 vantagem do Python puro e 2 do LangGraph.

**8. (V/F justificado)** "O custo do contexto (working memory) cresce quadraticamente com o número de tokens na maioria dos provedores, tornando contextos longos proibitivos."

---

## Parte 3 — Projeto curto (Q9-10)

**9. (Projeto curto)** Escreva o esqueleto de um agent loop ReAct em Python (função `run_agent`) com: (a) limite de iterações, (b) tratamento de ferramenta inexistente que devolve mensagem útil, (c) condição de parada. Não precisa implementar o LLM — use `llm(mensagens)` como abstração.

**10. (Projeto curto)** Você deve arquitetar um agente de "research assistant". Justifique em 3-4 frases: (a) workflow ou agente? (b) quais tools mínimas? (c) qual métrica de observabilidade você monitoraria desde o dia 1?

---

## Critérios de correção (resumo)

| Conceito | Questões | Peso |
|---|---|---|
| Augmented LLM & taxonomia | 1, 3, 4 | 25% |
| Workflow vs agente | 2, 5 | 20% |
| Agent loop (ReAct) | 6, 9 | 25% |
| Implementação & trade-offs | 7, 8 | 15% |
| Arquitetura & observabilidade | 10 | 15% |

**Conversão**: cada questão vale 10 pts; total 100 pts. Nota 1-5.
- 90+ pts: 5,0
- 75-89: 4,0
- 60-74: 3,0 (mínimo aprovação)
- <60: reprovação.

Gabarito comentado em [`gabarito.md`](gabarito.md).
