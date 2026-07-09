---
password: Etho-Prof-2026
---
# Mapa de Rastreabilidade — Competências × Módulos × Avaliações

> Este é o documento que **garante** que toda competência declarada é desenvolvida em ao menos um módulo e medida em ao menos uma avaliação. Sustenta o Pilar Técnico (40%) e habilita o cálculo de progresso de PDI.

## Legenda

- **Competências** (C1-C6): ver [`matriz-competencias.md`](matriz-competencias.md).
- **Nível desenvolvido**: B/I/A.
- **Itens de avaliação** (A1-A4): A1=Técnico(40%) · A2=Consultivo(30%) · A3=Comportamental(20%) · A4=Prático(10%).

## Matriz Módulo → Competências

| Módulo | C1 Agêntica | C2 Multi-Agent | C3 MCP/Tools | C4 Memória | C5 AgentOps | C6 Security | Avaliação principal |
|---|---|---|---|---|---|---|---|
| `ETHAGT01` Arquitetura Cognitiva | **I** | — | B | B | B | — | A1 (prova) + A4 (lab ReAct) |
| `ETHAGT02` Tool Calling & ACI | **I** | — | **I** | — | B | B | A1 + A4 (construção de tools) |
| `ETHAGT03` Workflows | **I** | B | B | — | B | — | A1 + A2 (análise de trade-offs) + A4 |
| `ETHAGT04` Reasoning & Planning | **I** | B | — | B | B | — | A1 (prova) + A4 (implementar 3 padrões) |
| `ETHAGT05` Memória | **A** | — | — | **I** | B | B | A1 + A4 (checkpointer) |
| `ETHAGT06` RAG Agêntico | **A** | — | B | **I** | **I** | — | A1 + A4 (eval de RAG) + A2 |
| `ETHAGT07` KG & Vector DBs | **A** | — | B | **A** | **I** | — | A1 + A4 ( KG + vector pipeline) |
| `ETHAGT08` MCP | **A** | B | **A** | — | B | **I** | A1 + A4 (MCP server custom) + A2 |
| `ETHAGT09` A2A / Coordenação | **A** | **I** | B | B | B | — | A1 + A4 (2 agentes coordenados) |
| `ETHAGT10` Topologias Multi-Agent | **A** | **A** | B | B | B | B | A1 + A2 (justificar topologia) + A4 |
| `ETHAGT11` Event-Driven & Orquestração | **A** | **A** | B | B | **I** | — | A1 + A4 (Kafka/NATS/Temporal) |
| `ETHAGT12` AgentOps & Avaliação | **A** | B | — | B | **A** | B | A1 + A2 (estudo comparativo) + A4 |
| `ETHAGT13` Segurança & Governança | **A** | B | **A** | — | **I** | **A** | A1 + A2 (threat model) + A4 (red team) |
| `ETHAGT14` Escalabilidade & Distribuído | **A** | **A** | B | **A** | **A** | B | A1 + A2 (ADR de escala) + A4 |
| `ETHAGT15` Meta-Agentes | **A** | **A** | B | **A** | B | **I** | A1 + A4 (agent que cria agent) + A2 |
| `ETHAGT16` Sociedades / Pesquisa | **A** | **A** | B | **A** | **I** | **I** | A1 + A2 (paper review) + A4 |
| `ETHAGT90` Capstone | **A** | **A** | **A** | **A** | **A** | **A** | **A1+A2+A3+A4** (defesa por painel) |

## Cobertura reversa: Competência → Módulos

| Competência | Desenvolvida em (módulos) | Medida em (avaliações) |
|---|---|---|
| **C1 Programação Agêntica** | 01, 02, 03, 04, 05, 06, 07, 08, 11, 12, 14, 90 | A1 (todos), A4 (todos os labs) |
| **C2 Multi-Agent Systems** | 03, 04, 08, 09, 10, 11, 14, 15, 16, 90 | A1, A2 (trade-offs), A4 (sistemas) |
| **C3 MCP & Tool Use** | 02, 03, 06, 07, 08, 13, 90 | A1, A4 (MCP server custom) |
| **C4 Agent Memory** | 01, 04, 05, 06, 07, 09, 10, 14, 15, 16, 90 | A1, A4 (checkpointer, KG) |
| **C5 AgentOps & Avaliação** | 01, 02, 06, 07, 11, 12, 13, 14, 16, 90 | A1, A2 (comparativos), A4 (eval) |
| **C6 Agent Security** | 02, 05, 08, 10, 13, 15, 16, 90 | A1, A2 (threat model), A4 (red team) |

**Verificação de cobertura**: todas as 6 competências têm ≥ 4 módulos desenvolvendo-as e ≥ 2 modalidades de avaliação medindo-as. ✓

## Pesos por fase interna (contribuição ao Pilar Técnico 40%)

| Fase interna | Peso no Pilar Técnico | Justificativa |
|---|---|---|
| A — Fundamentos | 15% | Base sem a qual nada se sustenta |
| B — Razão/Memória/Conhecimento | 25% | Diferencial cognitivo |
| C — Multi-Agentes/Ferramentas | 30% | **Ênfase** — diferenciação da Especialização |
| D — Produção/Fronteira | 20% | Maturidade de produção |
| Capstone | 10% | Integração validada |

> Os 60% restantes do Pilar Técnico podem vir de `ETHML02` e outras competências técnicas adjacentes.

---

*Relacionado: [`matriz-competencias.md`](matriz-competencias.md) · [`grade-curricular.md`](grade-curricular.md) · Avaliações (Confluence `UE`)*
