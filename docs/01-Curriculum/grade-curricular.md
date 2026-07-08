# Grade Curricular — Especialização em Programação Agêntica

> **Prefixo**: `ETHAGT` · **Carga total**: ~440 h · **Fase Etho**: Especialização (Fase 4) · **Duração típica**: 12-18 meses

## Pré-requisitos de entrada

| Tipo | Requisito |
|---|---|
| Curso Etho | `ETHDEV07` Introdução à Programação Agêntica |
| Curso Etho | `ETHML01` Introdução a Machine Learning (ou equivalência demonstrada) |
| Conhecimento | Python Intermediário · APIs REST · Git |

---

## Fase A — Fundamentos Agênticos (80 h)

| Código | Curso | Carga | Pré-req | Origem |
|---|---|---|---|---|
| `ETHAGT01` | Arquitetura Cognitiva de Agentes LLM | 25 h | `ETHDEV07` | Especialização |
| `ETHAGT02` | Tool Calling e Agent-Computer Interface (ACI) | 25 h | `ETHAGT01` | Especialização |
| `ETHAGT03` | Padrões de Workflow Agêntico | 30 h | `ETHAGT01` | Especialização |

**Objetivo da fase**: estabelecer o bloco fundamental (Augmented LLM), o agent loop e a distinção crítica entre **workflow** (previsibilidade) e **agente** (flexibilidade).

## Fase B — Razão, Memória e Conhecimento (115 h)

| Código | Curso | Carga | Pré-req | Origem |
|---|---|---|---|---|
| `ETHAGT04` | Reasoning & Planning | 30 h | `ETHAGT03` | Especialização |
| `ETHAGT05` | Memória de Agentes | 25 h | `ETHAGT04` | Especialização |
| `ETHAGT06` | RAG Agêntico | 30 h | `ETHAGT04` | Especialização |
| `ETHAGT07` | Knowledge Graphs & Vector Databases | 30 h | `ETHAGT06` | Especialização |

**Objetivo da fase**: dotar o agente de **razão, memória e conhecimento** — os três pilares cognitivos que distinguem um agente útil de um chatbot.

## Fase C — Multi-Agentes, Ferramentas e Orquestração (105 h)

| Código | Curso | Carga | Pré-req | Origem |
|---|---|---|---|---|
| `ETHAGT08` | MCP — Model Context Protocol | 25 h | `ETHAGT02` | Especialização |
| `ETHAGT09` | Comunicação e Coordenação Multi-Agente | 25 h | `ETHAGT04` | Especialização |
| `ETHAGT10` | Padrões de Arquitetura Multi-Agente | 30 h | `ETHAGT09` | Especialização |
| `ETHAGT11` | Event-Driven Agents & Workflow Orchestration | 25 h | `ETHAGT10` | Especialização |

**Objetivo da fase**: passar do agente isolado para **sistemas de agentes** coordenados, com ferramentas padronizadas (MCP) e orquestração robusta (eventos, durable execution).

## Fase D — Produção, Governança e Fronteira (115 h)

| Código | Curso | Carga | Pré-req | Origem |
|---|---|---|---|---|
| `ETHAGT12` | AgentOps, Observabilidade & Avaliação | 30 h | `ETHAGT11` | Especialização |
| `ETHAGT13` | Segurança & Governança de Agentes | 25 h | `ETHAGT12` | Especialização |
| `ETHAGT14` | Escalabilidade & Sistemas Distribuídos | 30 h | `ETHAGT11` | Especialização |
| `ETHAGT15` | Meta-Agentes & Sistemas Autoaprendentes | 15 h | `ETHAGT10` | Especialização |
| `ETHAGT16` | Sociedades de Agentes & Autonomous Research | 15 h | `ETHAGT15` | Especialização |

**Objetivo da fase**: levar a produção com rigor (AgentOps, segurança, escala) e atingir a **fronteira** (meta-agentes, sociedades, pesquisa autônoma) — a diferenciação da Especialização.

## Capstone (60 h)

| Código | Curso | Carga | Pré-req | Origem |
|---|---|---|---|---|
| `ETHAGT90` | Capstone — Plataforma de Pesquisa Autônoma | 60 h | Todos os 16 módulos | Especialização |

**Objetivo**: integrar todos os módulos em uma plataforma multi-agente estilo AutoResearch, com topologia Hierarchical + Orchestrator-Workers + Evaluator-Optimizer, MCP servers customizados, memória de longo prazo, event-driven, guardrails e observabilidade completa.

---

## Eletivos (não contam na carga mínima)

| Código | Curso | Carga |
|---|---|---|
| `ETHAGT-E1` | Agentes Embutidos / Robotics | 20 h |
| `ETHAGT-E2` | Coding Agents (estilo SWE-bench) | 25 h |
| `ETHAGT-E3` | Computer Use & Browser Agents | 20 h |
| `ETHAGT-E4` | Agentes para Enterprise (SAP / Salesforce / GCP) | 25 h |

---

## Fluxograma de progressão

```
ETHDEV07 (Tronco) ──► ETHAGT01 ──► ETHAGT02 ──► ETHAGT03 ──┐
                                                            │
                              ┌─────────────────────────────┘
                              ▼
                            ETHAGT04 (Reasoning/Planning)
                              │
                   ┌──────────┼──────────┐
                   ▼          ▼          ▼
              ETHAGT05    ETHAGT06    ETHAGT07
              (Memória)   (RAG)       (KG/Vector)
                   │          │          │
                   └──────────┼──────────┘
                              ▼
                            ETHAGT08 (MCP)        ETHAGT09 (A2A)
                              │                       │
                              └──────────┬────────────┘
                                         ▼
                                   ETHAGT10 (Topologias)
                                         │
                                         ▼
                                   ETHAGT11 (Event-driven)
                                         │
                              ┌──────────┼──────────┐
                              ▼          ▼          ▼
                         ETHAGT12    ETHAGT13    ETHAGT14
                         (AgentOps) (Security)  (Escala)
                              │          │          │
                              └──────────┼──────────┘
                                         ▼
                                   ETHAGT15 (Meta-Agentes)
                                         │
                                         ▼
                                   ETHAGT16 (Sociedades)
                                         │
                                         ▼
                                   ETHAGT90 (CAPSTONE)
```

## Convenção de códigos

- `ETHAGT0[1-9]` e `ETHAGT1[0-6]`: cursos obrigatórios da Especialização.
- `ETHAGT-E[N]`: eletivos.
- `ETHAGT90`: Capstone.
- `ETHAGT9[1-9]`: reservado para futuros projetos integradores.

---

*Relacionado: [`matriz-competencias.md`](matriz-competencias.md) · [`mapa-fases.md`](mapa-fases.md) · [`mapa-competencias-modulos.md`](mapa-competencias-modulos.md)*
