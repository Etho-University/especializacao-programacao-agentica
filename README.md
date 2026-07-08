# Especialização em Programação Agêntica

> **Universidade Etho** · Escola de Tecnologia · Área de Inteligência Artificial
> Trilha de **Especialização (Fase 4)** · Prefixo `ETHAGT` · ~440 h · 12-18 meses

Formar **arquitetos de sistemas de agentes autônomos**, não usuários de framework. O framework é consequência; o **princípio de arquitetura** permanece.

Esta Especialização representa o **estado da arte em Programação Agêntica** e foi projetada para superar formações disponíveis no mercado (DeepLearning.AI, HuggingFace Agents, LangGraph, CrewAI, AutoGen, OpenAI Agents SDK, Google ADK, Semantic Kernel, PydanticAI, Agno, OpenHands/OpenDevin, etc.) em **profundidade arquitetural**, **rigor de produção** e **cobertura de fronteira** (multi-agentes, sociedades de agentes, pesquisa autônoma).

---

## Para quem é

Engenheiros de Software, Arquitetos, Cientistas de Dados, Engenheiros de IA, Pesquisadores e Desenvolvedores Python experientes. **Não assume** conhecimento prévio de agentes — a porta de entrada é `ETHDEV07` (Introdução à Programação Agêntica, no Tronco Comum).

## O que o aluno torna-se capaz de

Projetar arquiteturas de agentes · construir sistemas multi-agente · criar agentes especializados e autônomos · arquitetar memória de longo prazo · implementar planejamento, reflexão e autoaprendizado · aplicar MCP, RAG, tool calling, bancos vetoriais e grafos de conhecimento · construir sistemas distribuídos orientados a eventos · orquestrar hierarquias e sociedades de agentes · criar agentes que criam agentes · implementar governança, observabilidade, avaliação (AgentOps) e segurança · levar plataformas completas a produção.

## Pré-requisitos de entrada

- `ETHDEV07` — Introdução à Programação Agêntica (Tronco Comum)
- `ETHML01` — Introdução a Machine Learning (ou equivalente)
- Python Intermediário + APIs REST + Git

## Estrutura curricular resumida

| Fase | Cursos | Carga |
|---|---|---|
| **A — Fundamentos Agênticos** | `ETHAGT01-03` | 80 h |
| **B — Razão, Memória e Conhecimento** | `ETHAGT04-07` | 115 h |
| **C — Multi-Agentes, Ferramentas e Orquestração** | `ETHAGT08-11` | 105 h |
| **D — Produção, Governança e Fronteira** | `ETHAGT12-16` | 115 h |
| **Capstone** | `ETHAGT90` | 60 h |
| **Total** | **16 + 1** | **~440 h** |

Detalhes em [`01-Curriculum/grade-curricular.md`](01-Curriculum/grade-curricular.md).

## Como navegar neste repositório

| Diretório | Propósito |
|---|---|
| [`00-Governanca/`](00-Governanca) | Missão, princípios, roadmap, ADRs |
| [`01-Curriculum/`](01-Curriculum) | Grade, matriz de competências, mapa de fases, rastreabilidade |
| [`02-Syllabus/`](02-Syllabus) | Um syllabus por curso `ETHAGT0x` |
| [`03-Slides/`](03-Slides) | Slides (markdown/reveal) por curso |
| [`04-Apostilas/`](04-Apostilas) | Material textual aprofundado (nível pós-graduação) |
| [`05-Labs/`](05-Labs) | Laboratórios guiados hands-on |
| [`06-Projects/`](06-Projects) | Projetos práticos por módulo |
| [`07-Exercises/`](07-Exercises) | Listas de exercícios + soluções |
| [`08-Assignments/`](08-Assignments) | Trabalhos avaliativos com rubricas |
| [`09-CaseStudies/`](09-CaseStudies) | Estudos de caso reais (Anthropic, Coinbase, Intercom…) |
| [`10-Architecture/`](10-Architecture) | Biblioteca de arquiteturas + ADRs |
| [`11-AgentPatterns/`](11-AgentPatterns) | 23 padrões de projeto de agentes |
| [`12-Diagrams/`](12-Diagrams) | C4, UML, sequência, fluxos |
| [`13-Workflows/`](13-Workflows) | Biblioteca de workflows agênticos |
| [`14-MCP/`](14-MCP) | Model Context Protocol — guias e servers |
| [`15-RAG/`](15-RAG) | Padrões RAG agêntico |
| [`16-Memory/`](16-Memory) | Padrões de memória + checkpointer |
| [`17-PromptLibrary/`](17-PromptLibrary) | Prompts por padrão e domínio |
| [`18-Tools/`](18-Tools) | Catálogo comparativo de ferramentas |
| [`19-Examples/`](19-Examples) | Exemplos de referência runnable |
| [`20-Research/`](20-Research) | Base de conhecimento (papers, frameworks, benchmarks) |
| [`21-Papers/`](21-Papers) | PDFs e fichas de leitura |
| [`22-Glossary/`](22-Glossary) | Glossário técnico PT + EN |
| [`23-Exams/`](23-Exams) | Provas + gabaritos |
| [`24-Templates/`](24-Templates) | Syllabus, ADR, rubrica, eval report, PDI |
| [`25-Checklists/`](25-Checklists) | Produção, security, code review |
| [`26-Capstone/`](26-Capstone) | Projeto final + rubrica de defesa |
| [`27-Certification/`](27-Certification) | Critérios, blueprint do exame |
| [`docs/`](docs) | Site estático (mkdocs/docusaurus) |

## Modelo de avaliação

Alinhado ao modelo de **4 pilares** da Universidade Etho:

- **Técnico** 40% · **Consultivo** 30% · **Comportamental** 20% · **Prático** 10%
- Aprovação por módulo: nota final ≥ **3,0**
- **Certificação**: nota ≥ **4,0** + capstone aprovado + 8 mentorias + todos módulos concluídos · validade **2 anos**

## Princípios pedagógicos

1. **Aprender Fazendo** — todo conceito tem laboratório e projeto.
2. **Arquitetura primeiro, framework depois** — `ETHAGT01` estabelece os blocos fundamentais antes de qualquer SDK.
3. **Rastreabilidade** — cada módulo mapeia competências → avaliações (Pilar Técnico 40%).
4. **Pesquisa viva** — conteúdo ancorado em fontes canônicas (arXiv, Anthropic, docs oficiais, repositórios). Ver `20-Research/`.
5. **Equilíbrio + fronteira** — cobertura igual das dimensões, com ênfase em **multi-agentes** e **pesquisa autônoma** (fronteira do estado da arte).

## Status

Conteúdo de referência entregue: governança, currículo, **16 syllabi**, **16 apostilas** (`04-Apostilas/ETHAGT01..16/apostila.md`, nível pós-graduação, ~7-9 capítulos cada), **32 labs** (`05-Labs/`, 2 por curso), **16 projetos** (`06-Projects/`), **16 listas de exercícios + 16 gabaritos** (`07-Exercises/`), **16 avaliações com rubricas** (`08-Assignments/`), slides, diagramas (59), casos de estudo (17), bibliotecas de padrões/arquiteturas/workflows, MCP guide, Research KB, catálogo de ferramentas, capstone, certificação e exames.

**Pendente:** revisão ortográfica final recomendada; expansão opcional de exemplos runnable em `19-Examples/`.

---

*Mantido por: Escola de Tecnologia — Universidade Etho · Versão: 1.0 · Última atualização: Julho 2026*
