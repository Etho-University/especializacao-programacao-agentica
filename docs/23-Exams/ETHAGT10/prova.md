---
password: Etho-Prof-2026
---
# ETHAGT10 — Prova do Módulo: Padrões de Arquitetura Multi-Agente

> Universidade Etho · Versão 1.0 · Julho 2026
> Duração: ~60 min · 10 questões · closed book · Pilar Técnico (40%)

Esta prova avalia o domínio das **topologias multi-agente** (12 padrões), a justificativa da escolha via ADR e a leitura de trade-offs de consistência, latência, custo e flexibilidade.

---

## Parte 1 — Conceitos (Q1-4)

**1. (Múltipla escolha)** No padrão *Supervisor* (LangGraph), o supervisor é melhor descrito como:
- (a) Um agente que executa todas as tarefas dos workers.
- (b) Um roteador que decide, via tool calls, qual worker invocar a seguir.
- (c) Um broker pub/sub assíncrono.

**2. (V/F justificado)** "Mesh é sempre a topologia mais escalável."

**3. (Múltipla escolha)** Quando *recursive* (meta-agentes) é tipicamente um **anti-pattern**?
- (a) Quando a tarefa exige adaptação dinâmica e decomposição variável.
- (b) Sempre; recursive nunca é justificável.
- (c) Quando há recursão profunda sem cercas (orçamento, profundidade máxima, veto).
- (d) Quando há múltiplos especialistas com escopos sobrepostos.

**4. (V/F justificado)** "Hierarchical de 3 níveis deve ser preferida sempre que houver mais de 2 workers."

---

## Parte 2 — Aplicação e trade-off (Q5-8)

**5. (Trade-off)** Dê ≥ 3 critérios para decidir quando a topologia **hierarchical** supera a **swarm**.

**6. (Análise de arquitetura)** Para uma tarefa de "revisão de PR com especialistas (segurança, performance, estilo)", esboce qual topologia escolheria e por que rejeitaria as 2 alternativas mais próximas.

**7. (Debug)** Um supervisor vira gargalo: latência explode com 15 workers. Cite 2 causas e 2 correções estruturais (sem apenas "adicionar mais modelo").

**8. (Trade-off)** Matriz de decisão menciona consistência × latência × custo × flexibilidade. Para um sistema de baixa latência e alta flexibilidade (custo tolerável), qual topologia priorizar? Justifique.

---

## Parte 3 — Projeto curto (Q9-10)

**9. (Projeto)** Escreva o esqueleto de um **ADR de topologia** (Contexto, Decisão, Justificativa, Alternativas, Consequências) para um sistema de atendimento multi-tenant.

**10. (Projeto)** Diferencie **Tree of Agents** de **Recursive** em 3 linhas e dê 1 cenário próprio de cada.

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
