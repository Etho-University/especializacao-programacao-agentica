# `ETHAGT09` — Comunicação e Coordenação Multi-Agente

> Fase C · Carga 25 h · Versão 1.0 · Julho 2026

## 1. Identificação

| Campo | Valor |
|---|---|
| Código | `ETHAGT09` |
| Título | Comunicação e Coordenação Multi-Agente (A2A · blackboard · actor model) |
| Fase interna | C |
| Carga horária | 25 h |
| Pré-requisitos | `ETHAGT04` |
| Módulos que dependem deste | `ETHAGT10`, `ETHAGT11`, `ETHAGT15` |

## 2. Objetivos

**Objetivo geral**: Dominar os **modelos de comunicação e coordenação** entre agentes — de troca direta de mensagens a *blackboard* e *actor model* — e saber escolher conforme o problema.

**Objetivos específicos**:
1. Distinguir padrões de comunicação A2A (agent-to-agent).
2. Implementar troca estruturada de mensagens (com schemas).
3. Aplicar blackboard para coordenação com espaço compartilhado.
4. Aplicar actor model para concorrência e isolamento.
5. Lidar com negociação, conflito e consenso em sistemas multi-agente.

## 3. Competências desenvolvidas

| Competência | Nível ao final |
|---|---|
| C1 Programação Agêntica | **A** |
| C2 Multi-Agent Systems | **I** |
| C3 MCP & Tool Use | B |
| C4 Agent Memory | B |
| C5 AgentOps & Avaliação | B |

## 4. Conteúdo programático

### Unidade 1 — O espectro da comunicação A2A (3 h)
- Direta (request/response) vs assíncrona (eventos)
- Broadcast vs p2p vs pub/sub
- Schemas de mensagem (estrutura, versão)
- Erros: mensagens perdidas, duplicadas, fora de ordem

### Unidade 2 — Padrões de conversação (5 h)
- Two-agent dialogue (estilo CAMEL)
- Group chat (estilo AutoGen GroupChat)
- Handoff / transfer (estilo OpenAI Swarm)
- Selector / round-robin / dynamic

### Unidade 3 — Blackboard (4 h)
- Espaço compartilhado de estado
- Quando brilha: problema dinâmico, especialistas contribuem
- vs mensagens diretas
- Implementação (em memória + persistente)

### Unidade 4 — Actor Model (5 h)
- Atores encapsulam estado; só mensagens
- Localização transparente; concorrência sem locks
- Akka / Erlang / asyncio actors
- Aplicação a agentes distribuídos

### Unidade 5 — Negociação e conflito (4 h)
- Negociação entre agentes (Bargaining, Auction)
- Resolução de conflito (voting, mediator)
- Convergência e deadlock
- Exemplo: agentes com objetivos parcialmente conflitantes

### Unidade 6 — Protocolos e padrões emergentes (4 h)
- A2A Protocol (Google, 2024)
- MCP vs A2A: complementares ou competidores?
- Padrões de orquestração de workflow multi-agente
- Estado da padronização

## 5. Bibliografia

### Fundamental
- Wu, Q. et al. *AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation* (arXiv:2308.08155).
- Li, G. et al. *CAMEL: Communicative Agents for Mind Exploration* (arXiv:2303.17760).
- Hewitt, C. *Actor Model* (clássico, 1973).

### Complementar
- OpenAI Swarm (repo + paper técnico).
- Google *A2A Protocol* spec.

## 6. Papers canônicos

- `arXiv:2308.08155` — AutoGen
- `arXiv:2303.17760` — CAMEL
- `arXiv:2308.00352` — *Survey on LLM-based Multi-Agent Systems*

## 7. Laboratórios

- **Lab 1** (4 h): "Duas arquiteturas, um problema". Mesma tarefa em AutoGen-style group chat e em blackboard; comparar.
- **Lab 2** (4 h): "Actor model com handoffs". Implementar swarm com transferência de controle.

## 8. Projeto do módulo

**Descrição**: implementar um sistema de **negociação entre agentes** (ex.: comprador/vendedor, ou especialistas debatendo um diagnóstico).
**Entrega**: código + traces + análise de convergência.
**Critério de sucesso**: convergência em ≥ 80% dos casos; análise de falhas documentada.

## 9. Exercícios

1. Quando blackboard é preferível a mensagens diretas?
2. Escreva um schema de mensagem A2A com versionamento.
3. Diferencie handoff (Swarm) de delegação (supervisor).
4. Como evitar deadlock em negociação?
5. Verdadeiro/falso: "Actor model é mais lento que shared-state."

## 10. Avaliação

| Pilar | Peso | Instrumento |
|---|---|---|
| Técnico | 40% | Projeto + prova |
| Consultivo | 30% | Defesa arquitetural |
| Comportamental | 20% | Code review |
| Prático | 10% | Demo: agentes coordenando |

**Nota mínima**: 3,0.

## 11. Slides

- Slides: `03-Slides/ETHAGT09-slides.md` (~70 slides).

## 12. Leitura complementar

- AutoGen paper; CAMEL; A2A spec.

## 13. Ferramentas

- LangGraph (multi-agent), AutoGen, OpenAI Agents SDK, OpenSwarm-references, asyncio.

## 14. Diagramas

- Diagramas: `12-Diagrams/ETHAGT09/` — blackboard.mmd, actor-model.mmd, handoff.mmd, negotiation.mmd.

## 15. Estudo de caso

- MetaGPT em desenvolvimento de software multi-agente.

## 16. Ficha de pesquisa

- Ficha: `20-Research/ETHAGT09-pesquisa.md`.

---

*Mantido por: Universidade Etho · Versão 1.0 · Julho 2026*
