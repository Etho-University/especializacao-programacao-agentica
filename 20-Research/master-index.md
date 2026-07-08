# Research KB — Base de Conhecimento Estruturada

> v1: índice master das fontes que sustentam a Especialização. Cada entrada: fonte · tipo · ano · importância · módulos onde é citada. As fichas detalhadas estão em `21-Papers/` e nos diretórios temáticos deste `20-Research/`.

## Como usar

- Procure por tema ou módulo.
- Importância: 🏛 canônica (base) · ⭐ importante · 📖 complementar.
- Sempre verifique a data; revalide a cada 6 meses (estado da arte evolui).

---

## Papers canônicos (índice master)

### Foundational reasoning
| arXiv | Título | Autores | Ano | Imp | Módulos |
|---|---|---|---|---|---|
| 2201.11903 | Chain-of-Thought | Wei et al. | 2022 | 🏛 | ETHAGT04 |
| 2203.11171 | Self-Consistency | Wang et al. | 2023 | ⭐ | ETHAGT04 |
| 2210.03629 | ReAct | Yao et al. | 2023 | 🏛 | ETHAGT01, 04 |
| 2305.10601 | Tree of Thoughts | Yao et al. | 2023 | 🏛 | ETHAGT04 |
| 2303.11366 | Reflexion | Shinn et al. | 2023 | 🏛 | ETHAGT04 |
| 2305.04091 | Plan-and-Solve | Wang et al. | 2023 | ⭐ | ETHAGT03, 04 |
| 2305.18323 | ReWOO | Xu et al. | 2023 | ⭐ | ETHAGT03, 04 |
| 2310.01757 | LATS | Zhou et al. | 2024 | 🏛 | ETHAGT04 |
| 2402.03620 | Self-Discover | Major et al. | 2024 | ⭐ | ETHAGT04 |

### Tools & tool use
| arXiv | Título | Autores | Ano | Imp | Módulos |
|---|---|---|---|---|---|
| 2302.04761 | Toolformer | Schick et al. | 2023 | 🏛 | ETHAGT01, 02 |
| 2305.15334 | Gorilla | Patil et al. | 2023 | ⭐ | ETHAGT02 |
| 2307.16789 | ToolLLM | Qin et al. | 2023 | ⭐ | ETHAGT02 |

### RAG
| arXiv | Título | Autores | Ano | Imp | Módulos |
|---|---|---|---|---|---|
| 2005.11401 | RAG (original) | Lewis et al. | 2020 | 🏛 | ETHAGT06, 07 |
| 2310.11511 | Self-RAG | Asai et al. | 2024 | 🏛 | ETHAGT06 |
| 2401.15884 | Corrective RAG (CRAG) | Yan et al. | 2024 | 🏛 | ETHAGT06 |
| 2404.16130 | GraphRAG | Edge et al. (MS) | 2024 | 🏛 | ETHAGT07 |
| 2306.08302 | LLMs + KG (survey) | Pan et al. | 2023 | ⭐ | ETHAGT07 |
| 2212.10496 | HyDE | Gao et al. | 2022 | ⭐ | ETHAGT06 |

### Memory
| arXiv | Título | Autores | Ano | Imp | Módulos |
|---|---|---|---|---|---|
| 2310.08560 | MemGPT | Packer et al. | 2023 | 🏛 | ETHAGT05 |
| 2304.03442 | Generative Agents | Park et al. | 2023 | 🏛 | ETHAGT05, 16 |

### Multi-agent
| arXiv | Título | Autores | Ano | Imp | Módulos |
|---|---|---|---|---|---|
| 2308.08155 | AutoGen | Wu et al. | 2023 | 🏛 | ETHAGT09, 10 |
| 2303.17760 | CAMEL | Li et al. | 2023 | ⭐ | ETHAGT09 |
| 2308.00352 | MetaGPT | Hong et al. | 2024 | 🏛 | ETHAGT09, 10 |
| 2308.10848 | AgentVerse | Chen et al. | 2023 | ⭐ | ETHAGT09, 10, 16 |
| 2402.01680 | LLM Multi-Agents Survey | Guo et al. | 2024 | ⭐ | ETHAGT09 |

### Meta-agentes & frontier
| arXiv | Título | Autores | Ano | Imp | Módulos |
|---|---|---|---|---|---|
| 2310.03714 | DSPy | Khattab et al. | 2024 | 🏛 | ETHAGT15 |
| 2309.16797 | Promptbreeder | Fernando et al. | 2023 | ⭐ | ETHAGT15 |
| 2305.16291 | Voyager | Wang et al. | 2023 | 🏛 | ETHAGT15, 16 |
| 2408.06292 | AI Scientist | Lu et al. (Sakana) | 2024 | 🏛 | ETHAGT15, 16 |
| 2311.11402 | Meta-Prompting | Hu et al. | 2024 | ⭐ | ETHAGT15 |

### Benchmarks & eval
| arXiv | Título | Autores | Ano | Imp | Módulos |
|---|---|---|---|---|---|
| 2310.06770 | SWE-bench | Jimenez et al. | 2023 | 🏛 | ETHAGT12 |
| 2311.12983 | GAIA | Mialon et al. | 2023 | 🏛 | ETHAGT12 |
| 2404.44529 | τ-bench | Yao et al. | 2024 | 🏛 | ETHAGT12 |
| 2308.03688 | AgentBench | Liu et al. | 2023 | ⭐ | ETHAGT12 |
| 2307.13854 | WebArena | Zhou et al. | 2023 | ⭐ | ETHAGT12 |
| 2310.04451 | AgentDojo | Debnath et al. | 2024 | ⭐ | ETHAGT13 |
| 2406.18510 | InjecAgent | Zhan et al. | 2024 | ⭐ | ETHAGT13 |

### Security
| arXiv | Título | Autores | Ano | Imp | Módulos |
|---|---|---|---|---|---|
| 2302.12173 | Indirect prompt injection | Greshake et al. | 2023 | 🏛 | ETHAGT13 |

### Surveys
| arXiv | Título | Autores | Ano | Imp |
|---|---|---|---|---|
| 2601.12560 | Agentic AI survey | Arunkumar et al. | 2026 | 🏛 |
| 2308.11432 | LLM Autonomous Agents survey | Wang et al. | 2023 | ⭐ |

### Coding agents
| arXiv | Título | Autores | Ano | Imp |
|---|---|---|---|---|
| 2405.15793 | SWE-agent | Yang et al. | 2024 | ⭐ |
| 2404.05427 | AutoCodeRover | Zhang et al. | 2024 | 📖 |

---

## Frameworks estudados

| Framework | Repo | Foco | Módulos |
|---|---|---|---|
| LangGraph | langchain-ai/langgraph | estado + grafo | ETHAGT01-16 |
| OpenAI Agents SDK | openai/openai-agents-python | SDK minimalista | ETHAGT01 |
| CrewAI | crewAIInc/crewAI | role-based | ETHAGT10 |
| AutoGen | microsoft/autogen | multi-agent conversation | ETHAGT09 |
| PydanticAI | pydantic/pydantic-ai | typed, Pydantic | ETHAGT02 |
| Agno | agno-agi/agno | performance | ETHAGT10 |
| Semantic Kernel | microsoft/semantic-kernel | enterprise | ETHAGT10 |
| Google ADK | google/adk | Google ecosystem | ETHAGT10 |
| OpenAI Swarm | openai/swarm | handoffs lightweight | ETHAGT09 |
| OpenHands | All-Hands-AI/OpenHands | coding agent | ETHAGT-E2 |
| OpenCode | sst/opencode | agentic IDE | ETHAGT08 |

## MCP

- Spec oficial: <https://modelcontextprotocol.io/specification> (versão 2025-11-25)
- Python SDK (FastMCP), TypeScript SDK
- Cloudflare Remote MCP, Auth0 analysis

## Benchmarks

Ver tabela acima; implementações oficiais no GitHub de cada.

## Livros

- Kleppmann, *Designing Data-Intensive Applications* (O'Reilly) — fundamentos distribuídos
- Richards & Ford, *Fundamentals of Software Architecture* (O'Reilly)
- Narkhede et al., *Kafka: The Definitive Guide* (O'Reilly)
- Tulving, *Episodic and Semantic Memory* (1972) — fundamentos cognitivos
- Hewitt, *Actor Model* (1973) — clássico
- Weiss, *Multi-Agent Systems* (MIT Press) — clássico

## Blogs / talks canônicos

- Anthropic Engineering Blog (*Building Effective Agents*, *Contextual Retrieval*)
- Karpathy talks (*Software 3.0*, *Thinking clearly*)
- Hamel Husain (*Evals for LLMs*)
- Eugene Yan blog
- Pat McGuinness Substack (série workflows)

## RFCs / specs

- MCP Specification (Anthropic, nov/2024 → atualizações 2025)
- OpenTelemetry GenAI semantic conventions
- CloudEvents (CNCF)
- A2A Protocol (Google, 2025)

## Standards / compliance

- OWASP Top 10 for LLM Applications (2025)
- NIST AI RMF
- EU AI Act
- LGPD (Brasil), GDPR (UE)

---

## Revalidação

Estado da arte evolui rápido. Política:
- Revalidar a cada **6 meses** (próxima: janeiro 2027).
- Mudanças que afetam princípios → ADR novo.
- Mudanças que afetam conteúdo → atualizar em ficha detalhada.

**Última revalidação**: Julho 2026.
