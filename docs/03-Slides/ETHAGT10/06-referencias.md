# ETHAGT10 — Referências

> Todas as fontes utilizadas na preparação e apresentação da aula.

---

## Canônicas (fundação do curso)

### 1. MetaGPT: Meta Programming for Multi-Agent Collaborative Framework
- **Autores**: Sirui Hong, Ming Zhong, Steven Ka Shing Yau, et al.
- **Venue**: ICLR 2024
- **arXiv**: 2308.00352
- **URL**: https://arxiv.org/abs/2308.00352
- **Resumo**: Framework multi-agente baseado em SOPs (Standard Operating Procedures). Codifica papéis de uma software house (PM → Architect → Engineer → QA) em agentes. Base direta dos Slides 26 (MetaGPT SOPs) e 57 (caso de estudo).
- **Importância**: Canônica
- **Slides que referenciam**: 6, 26, 57

### 2. AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors
- **Autores**: Weize Chen, Yusheng Su, Jingwei Cheng, et al.
- **arXiv**: 2308.10848
- **URL**: https://arxiv.org/abs/2308.10848
- **Resumo**: Framework para assembling agents como montar uma equipe humana. Conceito de crew formation. Base do Slide 27 (Crew Formation).
- **Importância**: Canônica
- **Slides que referenciam**: 6, 27

### 3. AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation
- **Autores**: Qingyun Wu, Gagan Bansal, Jieyu Zhang, et al.
- **arXiv**: 2308.08155
- **URL**: https://arxiv.org/abs/2308.08155
- **Resumo**: Framework Microsoft baseado em conversação multi-agente. Usa conceitos de actor model. Base do Slide 43 (Actor Model).
- **Importância**: Canônica
- **Slides que referenciam**: 6, 43

---

## Importantes (complementam e aprofundam)

### 4. OpenAI Swarm
- **Data**: 2024
- **URL**: https://github.com/openai/swarm
- **Resumo**: Framework de agentes leves com handoffs (`transfer()`). Topologia swarm descentralizada sem orquestrador. Base direta dos Slides 30-33 (Swarm e handoffs).
- **Importância**: Importante
- **Slides que referenciam**: 6, 30, 31, 32, 33

### 5. LangGraph Multi-Agent Examples
- **URL**: https://github.com/langchain-ai/langgraph
- **Resumo**: Implementação de referência de supervisor (`multi-agent-collaboration`) e hierarchical (`hierarchical_agent_teams`). Base direta dos Slides 18-20 (Supervisor e Hierarchical).
- **Importância**: Importante
- **Slides que referenciam**: 18, 19, 20, 24

### 6. Agentic AI: Architectures, Taxonomies, and Evaluation of LLM Agents
- **Autores**: Arunkumar V, Gangadharan G.R., Rajkumar Buyya
- **Data**: janeiro 2026
- **arXiv**: 2601.12560
- **Resumo**: Survey com taxonomia unificada de arquiteturas multi-agente. Base do Slide 8 (grid de 12 topologias).
- **Importância**: Importante
- **Slides que referenciam**: 6, 8

### 7. Anthropic — Building Effective Agents
- **Autores**: Erik Schluntz, Barry Zhang
- **Data**: dezembro 2024
- **URL**: https://www.anthropic.com/engineering/building-effective-agents
- **Resumo**: Define orchestrator-workers como padrão distinto de supervisor. Base do Slide 37 (Orchestrator-Workers). Pré-requisito: ETHAGT01.
- **Importância**: Importante
- **Slides que referenciam**: 11, 37

### 8. LATS: Language Agent Tree Search
- **Autores**: Andy Zhou, Yanjun Ma, et al.
- **arXiv**: 2310.01757
- **Resumo**: Aplica MCTS (Monte Carlo Tree Search) a agentes LLM. Base do Slide 48 (Tree of Agents).
- **Importância**: Importante
- **Slides que referenciam**: 48

### 9. Hewitt, C. — A Universal Modular Actor Formalism for AI
- **Data**: 1973
- **Resumo**: Origem do actor model. Fundação teórica de sistemas distribuídos (Akka, Erlang). Base do Slide 43 (Actor Model).
- **Importância**: Importante
- **Slides que referenciam**: 43

---

## Complementares (leitura opcional)

### 10. CrewAI Documentation
- **URL**: https://docs.crewai.com
- **Resumo**: Framework role-based para multi-agente. Conceito de crew (agentes + tarefas + processo). Base do Slide 27 (Crew Formation).
- **Slides que referenciam**: 27

### 11. Akka Documentation
- **URL**: https://akka.io
- **Resumo**: Implementação de actor model para JVM (Scala/Java). Referência para escalabilidade de atores.
- **Slides que referenciam**: 43

### 12. Weiss, G. — Multi-Agent Systems
- **Data**: 2ª edição, 2013 (MIT Press)
- **Resumo**: Livro clássico de sistemas multi-agente. Fundação teórica.
- **Slides que referenciam**: 6

### 13. Microsoft AutoGen Documentation
- **URL**: https://microsoft.github.io/autogen/
- **Resumo**: Docs oficiais do AutoGen com exemplos de GroupChat e hierarchical.
- **Slides que referenciam**: 20, 43

### 14. Hearsay-II
- **Autores**: Erman, L.D. et al.
- **Data**: 1971-1976
- **Resumo**: Origem do padrão blackboard em IA clássica. Base do Slide 45 (Blackboard).
- **Slides que referenciam**: 45

---

## Catálogo Interno

### 15. Catálogo de Arquiteturas (12 Topologias)
- **Arquivo**: `10-Architecture/architectures/catalog.md`
- **Resumo**: Catálogo consolidado das 12 topologias com estrutura, when-to-use, when-to-avoid, trade-offs. Base direta dos Slides 8-16 (catálogo).
- **Slides que referenciam**: 8, 9, 10, 11, 12, 13, 14, 15

### 16. Fichas Individuais de Topologias
- **Arquivos**: `10-Architecture/architectures/01-single-agent.md` a `12-hybrid.md`
- **Resumo**: Fichas detalhadas de cada topologia com exemplo runnable e anti-patterns.

---

## Diagramas Referenciados

| Arquivo | Slides |
|---|---|
| `12-Diagrams/ETHAGT10/supervisor-topology.mmd` | 18, 19, 10 |
| `12-Diagrams/ETHAGT10/hierarchical-topology.mmd` | 20, 10 |
| `12-Diagrams/ETHAGT10/swarm-topology.mmd` | 30, 12 |
| `12-Diagrams/ETHAGT10/decision-matrix.mmd` | 54 |

---

## Ficha de Pesquisa

- **Arquivo**: `20-Research/ETHAGT10-pesquisa.md`
- **Última consulta**: Julho 2026
- **Revalidação**: Janeiro 2027 (estado da arte evolui rápido)
