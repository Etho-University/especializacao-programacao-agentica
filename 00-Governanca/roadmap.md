# Roadmap de Desenvolvimento do Material

Plano de produção da Especialização em sprints. Cada sprint entrega **material versionado, revisável e navegável**, com rastreabilidade competência → módulo → avaliação.

## Visão geral

```
S0 Aprovação ──► S1 Fundação ──► S2 Syllabus ──► S3 Fase A ──► S4 Fase B
                                                                  │
   ◄── Publicação final ◄── S8 ◄── S7 Capstone ◄── S6 Fase D ◄── S5 Fase C
```

| Sprint | Duração | Entregável principal | MCPs principais |
|---|---|---|---|
| **S0** | — | Proposta aprovada (concluído) | Confluence (leitura) |
| **S1** | 1-2 sessões | **Fundação**: governança, currículo, matriz, glossário, templates, checklists, esqueleto navegável | Confluence (leitura), zai (diagramas) |
| **S2** | 1-2 sessões | Syllabus dos 16 cursos + Capstone (1 arquivo por curso, completo) | Confluence, zread |
| **S3** | 3-4 sessões | **Fase A completa** (`ETHAGT01-03`): apostila + slides + labs + exercícios + avaliação + gabaritos | github (code search), web-reader, zai |
| **S4** | 4-5 sessões | **Fase B** (`ETHAGT04-07`) + Biblioteca de Padrões v1 (23 padrões) + Workflows (5 Anthropic + variantes) | github, zread (LangGraph examples) |
| **S5** | 4-5 sessões | **Fase C** (`ETHAGT08-11`) + Biblioteca de Arquiteturas (12 topologias) + MCP profundo + RAG patterns | zread (MCP repo, framework repos), web-search |
| **S6** | 4-5 sessões | **Fase D** (`ETHAGT12-16`) + Research KB completa (papers/benchmarks/frameworks) + Catálogo de Ferramentas + AgentOps | web-search, web-reader, github |
| **S7** | concluído | **Capstone** (`ETHAGT90`) completo + Certification blueprint + Exams (provas + gabaritos) + Diagramas finais (C4/UML/sequência) | todos |
| **S8** | pendente | Revisão final, site docs (mkdocs), handoff, certificação de qualidade | — |

## Entregáveis por sprint (detalhe)

### S1 — Fundação (atual)
- [x] README raiz do repositório
- [x] `00-Governanca`: missão/visão/princípios, roadmap, ADR-001
- [x] `01-Curriculum`: grade curricular, matriz de competências, mapa de fases, rastreabilidade
- [x] `22-Glossary`: glossário técnico
- [x] `24-Templates`: syllabus, ADR, rubrica de avaliação, eval report, PDI agêntico
- [x] `25-Checklists`: produção de módulo, security de agente, code review
- [x] Esqueleto navegável (README em todos os diretórios)

### S2 — Syllabus ✓ (concluído)
- [x] 16 arquivos `02-Syllabus/ETHAGT0x-syllabus.md` preenchidos
- [x] 1 arquivo `02-Syllabus/ETHAGT90-capstone-syllabus.md`

### S3 — Fase A (Fundamentos Agênticos) ✓ (concluído)
- [x] `04-Apostilas/ETHAGT01/` — cognitive architecture, augmented LLM, agent loop, ReAct
- [x] `04-Apostilas/ETHAGT02/` — tool calling, ACI
- [x] `04-Apostilas/ETHAGT03/` — 5 workflows Anthropic + composição
- [x] Labs (6), projetos (3), exercícios+gabaritos (3), avaliações (3)
- [x] `03-Slides/ETHAGT0{1,2,3}-slides.md`
- [x] `12-Diagrams/ETHAGT0{1,2,3}/`: augmented-llm, agent-loop, 5-workflows, ACI, HITL, risk-matrix

### S4 — Fase B (Razão, Memória, Conhecimento) ✓ (concluído)
- [x] `ETHAGT04` — Reasoning & Planning (CoT, ReAct, Plan-and-Execute, ReWOO, ToT, LATS, Reflexion, Self-Discover)
- [x] `ETHAGT05` — Memória (working/episódica/semântica/procedural, checkpointer)
- [x] `ETHAGT06` — RAG Agêntico (Adaptive, CRAG, Self-RAG, Agentic)
- [x] `ETHAGT07` — Knowledge Graphs & Vector DBs (GraphRAG, híbridos)
- [x] `11-AgentPatterns/` — catálogo com 23 padrões
- [x] `03-Slides/ETHAGT0{4,5,6,7}-slides.md`
- [x] `23-Exams/ETHAGT0{4,5,6,7}/prova.md`
- [x] `13-Workflows/` — 8 workflows documentados
- [x] `15-RAG/` — 8 padrões documentados (naive, adaptive, corrective, self, agentic, graph, multimodal, eval)
- [x] `16-Memory/` — 6 padrões documentados (checkpointer, summarization, vector-recall, entity-memory, consolidation, eviction)

### S5 — Fase C (Multi-Agentes, Ferramentas, Orquestração) ✓ (concluído)
- [x] `ETHAGT08` — MCP (spec, servers, clients, governança)
- [x] `ETHAGT09` — A2A, blackboard, actor model, handoff, negociação
- [x] `ETHAGT10` — Topologias multi-agente (Supervisor, Hierarchical, Swarm, Mesh)
- [x] `ETHAGT11` — Event-driven (Kafka, NATS, Temporal, sagas)
- [x] `10-Architecture/` — catálogo de 12 topologias
- [x] `03-Slides/ETHAGT0{8,9,10,11}-slides.md`
- [x] `23-Exams/ETHAGT0{8,9,10,11}/prova.md`
- [x] `14-MCP/` — guia (intro, spec, transports)

### S6 — Fase D (Produção, Governança, Fronteira) ✓ (concluído)
- [x] `ETHAGT12` — AgentOps (traces, eval, benchmarks)
- [x] `ETHAGT13` — Segurança (prompt injection, red team, HITL, policy-as-code)
- [x] `ETHAGT14` — Escalabilidade (cache, routing, FinOps)
- [x] `ETHAGT15` — Meta-Agentes (DSPy, Promptbreeder, Voyager)
- [x] `ETHAGT16` — Sociedades de Agentes & Autonomous Research (Generative Agents, AI Scientist)
- [x] `18-Tools/` — catálogo comparativo (6 fichas)
- [x] `03-Slides/ETHAGT1{2,3,4,5,6}-slides.md`
- [x] `23-Exams/ETHAGT1{2,3,4,5,6}/prova.md`
- [x] `20-Research/` — Knowledge Base (master-index + 16 fichas)

### S7 — Capstone + Certificação ✓ (concluído)
- [x] `26-Capstone/`: enunciado detalhado + arquitetura de referência + marcos (M1-M8) + guia de defesa + rubrica + starter
- [x] `27-Certification/`: blueprint do exame + exame modelo v1 + gabarito + recertificação
- [x] `23-Exams/`: provas modulares ETHAGT01-16 + prova final integradora (20 questões) + gabarito comentado
- [x] `17-PromptLibrary/`: 15 prompts em 7 categorias
- [x] `12-Diagrams/ETHAGT90/`: 5 diagramas (C4 Context, C4 Container, C4 Component, execution-flow, topology)

### S8 — Revisão e handoff ✓ (concluído)
- [x] Site docs (mkdocs) — `mkdocs.yml` + ~40 páginas de navegação em `docs/`
- [x] `.gitignore` para `site/`
- [x] Revisão dos checklists e Definition of Done
- [x] Roadmap atualizado com todos os sprints (S1-S7) marcados como concluídos
- [x] Revisão cruzada (placeholders, links, terminologia, estrutura de syllabi)
- [x] Correção de 3+ inconsistências (slide paths, syllabi estrutura, ETHAGT90 missing files)
- [x] `HANDOFF.md` — documento de transição para equipe de produção

## Critério de "pronto" (Definition of Done) por módulo

Um curso `ETHAGT0x` está **pronto** quando possui os 16 artefatos:

1. Syllabus · 2. Apostila · 3. Slides · 4. Laboratórios · 5. Projeto · 6. Exercícios · 7. Avaliação · 8. Gabarito · 9. Bibliografia · 10. Papers · 11. Leitura complementar · 12. Ferramentas · 13. Diagramas · 14. Estudo de caso · 15. Rubrica de avaliação · 16. Ficha de pesquisa (`20-Research/`)

E a rastreabilidade competência → módulo → avaliação está completa em `01-Curriculum/mapa-competencias-modulos.md`.

## Governança de mudança

- Mudanças em **princípios** ou **estrutura curricular**: exigem ADR novo + aprovação.
- Mudanças em **conteúdo de módulo**: via PR, com revisão de pelo menos 1 especialista da área.
- Atualização de **papers/benchmarks**: contínua, registrada em `20-Research/` com data.

---

*Relacionado: [`missao-visao-principios.md`](missao-visao-principios.md) · [`adr/ADR-001`](adr/ADR-001-fundacoes-especializacao.md)*
