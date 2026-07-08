# `ETHAGT10` — Padrões de Arquitetura Multi-Agente

> Fase C · Carga 30 h · Versão 1.0 · Julho 2026

## 1. Identificação

| Campo | Valor |
|---|---|
| Código | `ETHAGT10` |
| Título | Padrões de Arquitetura Multi-Agente (topologias) |
| Fase interna | C |
| Carga horária | 30 h |
| Pré-requisitos | `ETHAGT09` |
| Módulos que dependem deste | `ETHAGT11`, `ETHAGT14`, `ETHAGT15`, `ETHAGT90` |

## 2. Objetivos

**Objetivo geral**: Dominar as **topologias de arquitetura multi-agente** — quando usar cada, trade-offs, e como escolher com base em requisitos de consistência, latência, custo e flexibilidade.

**Objetivos específicos**:
1. Caracterizar 12 topologias: Single Agent, Supervisor, Hierarchical, Blackboard, Actor Model, Pipeline, Event-Driven, Swarm, Tree of Agents, Recursive, Agent Mesh, Hybrid.
2. Justificar a escolha de topologia via ADR.
3. Implementar ao menos 4 topologias em um mesmo domínio.
4. Medir trade-offs entre elas (custo, latência, qualidade).
5. Identificar sinais de que a topologia precisa evoluir.

## 3. Competências desenvolvidas

| Competência | Nível ao final |
|---|---|
| C1 Programação Agêntica | **A** |
| C2 Multi-Agent Systems | **A** |
| C3 MCP & Tool Use | B |
| C4 Agent Memory | B |
| C6 Agent Security | B |

## 4. Conteúdo programático

### Unidade 1 — Catálogo de topologias (5 h)
Panorama das 12 topologias (ver `10-Architecture/`). Para cada: topologia, when-to-use, when-to-avoid.

### Unidade 2 — Supervisor e Hierarchical (5 h)
- Supervisor pattern (LangGraph): supervisor como roteador com tool calls
- Hierarchical: árvore de supervisor → workers → sub-workers
- Quando escalar hierarquia (3 níveis) vs flat
- Casos de falha: supervisor gargalo, workers redundantes

### Unidade 3 — Swarm e handoffs (4 h)
- OpenAI Swarm: agentes leves com transfer
- Quando transfer é melhor que roteamento central
- Limites: coordenação complexa

### Unidade 4 — Pipeline e Orchestrator-Workers (4 h)
- Pipeline fixo vs dinâmico
- Orchestrator-Workers revisitado em multi-agente
- Composição com hierarchical

### Unidade 5 — Event-Driven e Actor Model (4 h)
- Event-driven em multi-agente (preview; profundidade em `ETHAGT11`)
- Actor model como fundação de escalabilidade
- Mesh de agentes

### Unidade 6 — Tree, Recursive, Mesh (4 h)
- Tree of Agents (LATS em sistema)
- Recursive (meta-agents, preview `ETHAGT15`)
- Agent Mesh: topologia flat peer-to-peer

### Unidade 7 — Escolha e ADR (4 h)
- Matriz de decisão: consistência × latência × custo × flexibilidade
- ADR de topologia
- Sinais de evolução

## 5. Bibliografia

### Fundamental
- Hong, S. et al. *MetaGPT: Meta Programming for Multi-Agent Collaborative Framework* (arXiv:2308.00352).
- LangGraph *Multi-Agent* examples (`hierarchical_agent_teams`, `multi-agent-collaboration`).
- OpenAI Swarm (repo, 2024).

### Complementar
- Chen, W. et al. *AgentVerse: Facilitating Multi-Agent Collaboration* (arXiv:2308.10848).
- ConversableAgent / Microsoft AutoGen docs.

## 6. Papers canônicos

- `arXiv:2308.00352` — MetaGPT
- `arXiv:2308.10848` — AgentVerse
- `arXiv:2308.08155` — AutoGen

## 7. Laboratórios

- **Lab 1** (5 h): "Hierarchical teams". Implementar topologia hierarchical com supervisor + 2 workers + sub-worker.
- **Lab 2** (5 h): "Swarm vs Supervisor". Mesma tarefa nas duas topologias; medir.

## 8. Projeto do módulo

**Descrição**: dada uma tarefa complexa (ex.: revisão de PR com especialistas), projetar e implementar a topologia mais adequada, justificada em ADR.
**Entrega**: código + ADR + benchmark comparando topologia escolhida com ao menos 1 alternativa.
**Critério de sucesso**: ADR coerente; medições reais; topologia justificada.

## 9. Exercícios

1. Para 6 cenários, proponha a topologia mais adequada.
2. Quando hierarchical supera swarm?
3. Quando recursive é *anti-pattern*?
4. Escreva o esqueleto de um ADR de topologia.
5. Verdadeiro/falso: "Mesh é sempre a topologia mais escalável."

## 10. Avaliação

| Pilar | Peso | Instrumento |
|---|---|---|
| Técnico | 40% | Projeto + ADR + benchmark |
| Consultivo | 30% | Defesa do ADR para painel |
| Comportamental | 20% | Code review |
| Prático | 10% | Demo: topologia rodando |

**Nota mínima**: 3,0.

## 11. Slides

- Slides: `03-Slides/ETHAGT10-slides.md` (~100 slides; um conjunto por topologia).

## 12. Leitura complementar

- MetaGPT; LangGraph hierarchical teams notebook.

## 13. Ferramentas

- LangGraph, AutoGen, OpenAI Agents SDK, CrewAI, Agno, PydanticAI.

## 14. Diagramas

- Diagramas: `12-Diagrams/ETHAGT10/` — 12 topologias (C4 + fluxo).

## 15. Estudo de caso

- MetaGPT em simulação de software house.

## 16. Ficha de pesquisa

- Ficha: `20-Research/ETHAGT10-pesquisa.md`.

---

*Mantido por: Universidade Etho · Versão 1.0 · Julho 2026*
