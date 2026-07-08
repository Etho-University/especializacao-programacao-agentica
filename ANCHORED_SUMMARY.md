# Anchored Summary — Especialização em Programação Agêntica (Etho)

> Última atualização: Julho 2026 · Sprints S9-S11 concluídos · Site MkDocs funcional · Pronto para versionamento

---

## Goal
Criar a Especialização em Programação Agêntica completa para a Universidade Etho (conteúdo programático, currículo, grade, planos de ensino, laboratórios, projetos, avaliações, bibliotecas de padrões/arquiteturas/ferramentas, Capstone e certificação).

## Constraints & Preferences
- **Público-alvo**: Engenheiros de Software, Arquitetos, Cientistas de Dados, Engenheiros de IA, Pesquisadores, Devs Python experientes
- **Conteúdo em português** com termos técnicos em inglês mantidos
- **Foco em arquitetura, não framework**: Augmented LLM (Anthropic) como bloco fundamental; SDKs como instanciação
- **Ênfase em multi-agentes e pesquisa autônoma** como diferenciação curricular
- **7 pendências pós-handoff eliminadas nesta sessão** (arquivos individuais, papers, exemplos, MCP docs, ortografia)
- **Convenções Etho**: prefixo `ETHAGT`, 5 fases (Onboarding→Liderança), Fase 4 (Especialização), 4 pilares (Técnico 40%/Consultivo 30%/Comportamental 20%/Prático 10%), aprovação ≥3.0, certificação ≥4.0
- **Pré-requisito**: `ETHDEV07` + `ETHML01` + Python Intermediário
- **Destino**: repositório local — não publicar no Confluence
- **Qualidade pós-graduação lato sensu**: profundo, baseado em papers/benchmarks/repositórios reais

## Progress

### S9 — Apostilas + material didático (esta sessão)
- **Descoberta crítica:** `04-Apostilas/`, `05-Labs/`, `06-Projects/`, `07-Exercises/`, `08-Assignments/` estavam TODOS VAZIOS (apenas READMEs), apesar de HANDOFF/README afirmarem que o conteúdo existia.
- **Ação:** Produzido o material didático completo:
  - **16 apostilas** (`04-Apostilas/ETHAGT0x/apostila.md`), nível pós-graduação lato sensu, ~7-9 capítulos cada, ~322 KB / ~3.100 linhas, ancoradas nos syllabi + Research KB + slides.
  - **32 labs** (`05-Labs/`, 2 por curso) com roteiro passo-a-passo + checkpoints.
  - **16 projetos** (`06-Projects/`) com cenário realista + critérios mensuráveis.
  - **16 listas de exercícios + 16 gabaritos** (`07-Exercises/`).
  - **16 avaliações com rubricas** (`08-Assignments/`, 4 pilares Etho).
  - **16 provas modulares + 16 gabaritos** (`23-Exams/ETHAGT0x/`).
- **Docs corrigidos:** README.md (Status), HANDOFF.md (números finais + pendências) agora refletem o estado real.

### S10 — Revisão geral de qualidade (esta sessão)
- **Revisão por 5 agentes paralelos:** integridade de links, correção de questões/gabaritos (exercícios + provas), erros de código em labs, consistência de fontes (arXiv IDs).
- **Corrigido:**
  - **Fontes (syllabi):** 6 arXiv IDs trocados (Reflexion 2303.11366; Gorilla 2305.15334; Plan-and-Solve 2305.04091; ReWOO 2305.18323; LLMCompiler 2312.04511) + autor ReWOO (Zhou→Xu) + título corrompido ReWOO na apostila ETHAGT04.
  - **Provas:** ETHAGT10 Q3 (2 respostas válidas→1), ETHAGT07 Q7 (`nlist` é IVF não HNSW, em gabarito+apostila), ETHAGT04 Q5 (latência Plan-and-Execute média, não baixa).
  - **Exercícios:** ETHAGT05 V/F4 (caracteres chineses + gabarito que contradizia a apostila, reformulada), typo "agosto"→"agente", ETHAGT09 A2A 2024→2025, ETHAGT11 circuit breaker (atributos não armazenados).
  - **Links:** ETHAGT03 apostila (2 diagramas inexistentes→parallelization.mmd consolidado).
  - **Labs (sistemático):** `pip install asyncio` removido (4 labs — asyncio é stdlib), "Meja"→"Meça" (8 labs).
  - **Labs (bugs bloqueantes):** ETHAGT16-02 (erro de sintaxe f-string + await em nível de módulo + parsing de score), ETHAGT04-02 (`correct_answer` indefinido), ETHAGT07-02 (Cypher sem interpolação + injeção), ETHAGT03-02 (serial vs paralelo), ETHAGT10-01 (`TeamState` indefinido + fan-out sem barreira), ETHAGT11-02 (Ellipsis como argumento).
- **Residual aceitável:** labs avançados referenciam funções auxiliares (call_llm, embed) definidas em labs anteriores — scaffolding legítimo.

### S11 — Revisão ortográfica + Site (esta sessão)
- **Revisão ortográfica por 5 agentes paralelos** cobrindo apostilas, labs, exercícios/provas, projetos/assignments.
- **~40 correções ortográficas** aplicadas: acentuação (`agentica`→`agêntica`, `confrança`→`confiança`), typos (`tráfese`→`tráfego`, `decomõe`→`decompõe`, `Meje`→`Meça`, `Perggunta`→`Pergunta`), concordância (`compõe`→`compõem`, `veto`→`veta`), PT-PT→PT-BR (`arquitectural`→`arquitetural`, `facturação`→`faturação`), anglicismos (`hierarchy`→`hierarquia`).
- **Caracteres CJK que vazaram** erradicados (16 ocorrências). Varredura final: 0 caracteres não-latinos.
- Termo corrompido "Talinated Agent" corrigido para `ConversableAgent`/`GroupChat`.
- **Site MkDocs reestruturado:** conteúdo movido de `docs/material/` para `docs/` (root), 27 diretórios numerados copiados diretamente. Links do overlay antigo (`bibliotecas/`, `sobre/`, `curriculo/`, `pesquisa/`, `avaliacao/`) corrigidos via `../../`→`../` (21 arquivos). `index.md` link `cursos/` redirecionado para syllabus. Nav liberado do prefixo `material/`.
- **Build:** 126→7 warnings (6 pre-existentes em `18-Tools/README.md`). Geração em 11.72s, ~424 páginas. Site funcional com todas as apostilas, labs, exames, projetos, exercícios.

### S0 — Aprovação da Estrutura
- Pesquisa estado da arte (arXiv:2601.12560, Anthropic *Building Effective Agents*, LangGraph)
- Gap analysis vs cursos existentes
- Proposta 16 módulos + Capstone (~440 h)
- 6 competências (B/I/A) para Framework Etho
- Arquitetura repositório + roadmap S0-S8

### S1 — Fundação
- Governança (missão/visão/princípios, roadmap, ADR-001)
- Curriculum (grade, matriz competências, mapa fases, rastreabilidade)
- Glossário (~70 termos)
- Templates (syllabus, ADR, rubrica, eval report, PDI agêntico)
- Checklists (produção, security, code review)
- Esqueleto com READMEs em 31+ diretórios

### S2 — Syllabus
- 17 syllabi (16 cursos + Capstone), 16 seções cada
- ~40 papers canônicos referenciados

### S3 — Fase A (ETHAGT01-03)
- 3 apostilas aprofundadas (8-9 capítulos/cada)
- 6 labs runnable (2 por módulo)
- 3 projetos + exercícios+gabarito
- 3 avaliações+rubricas (4 pilares)
- 3 slides outlines
- 13 diagramas Mermaid
- 3 casos de estudo reais (SWE-bench, ACI redesign, suporte produção)
- 3 fichas de pesquisa

### S4 — Fase B (ETHAGT04-07)
- 4 módulos: Reasoning & Planning, Memória, RAG Agêntico, KG & Vector DBs
- Slides outlines, provas modulares
- **Biblioteca de Workflows** (5 canônicos + 3 variações)
- **Biblioteca de Padrões** (23 padrões, 6 categorias)
- **Padrões RAG** (8 arquivos em `15-RAG/`)
- **Padrões de Memória** (6 arquivos em `16-Memory/`)

### S5 — Fase C (ETHAGT08-11)
- 4 módulos: MCP (spec 2025-11-25, Streamable HTTP), A2A/Comunicação, Topologias Multi-Agente (12), Event-Driven/Orquestração
- Slides outlines, provas modulares
- **Biblioteca de Arquiteturas** (12 topologias)
- **Guia MCP** (intro, spec, transports, building-servers)

### S6 — Fase D (ETHAGT12-16)
- 5 módulos: AgentOps, Segurança, Escalabilidade, Meta-Agentes, Sociedades & Pesquisa Autônoma
- Slides outlines, provas modulares
- **Research KB** (master-index com ~40 papers, 11 frameworks, 7 benchmarks, specs MCP/A2A, compliance)
- **Catálogo de Ferramentas** (6 fichas comparativas)

### S7 — Capstone + Certificação + Exames
- **Capstone** (ETHAGT90): enunciado detalhado, arquitetura C4 (5 diagramas Mermaid), marcos M1-M8, guia de defesa, rubrica detalhada, starter code structure
- **Certificação**: blueprint + exame-v1 (35 questões) + gabarito + recertificação
- **Provas**: 16 modulares + prova final integradora (20 questões)
- **Prompt Library**: 15 prompts em 7 categorias

### S8 — Revisão e Handoff
- Revisão cruzada (placeholders, links, terminologia, estrutura syllabi)
- Correções: slide paths em 3 syllabi, seções 11-16 em 12 syllabi, `20-Research/ETHAGT90-pesquisa.md` e `03-Slides/ETHAGT90/README.md`
- Site MkDocs estruturado e build verificado
- `.gitignore` + `HANDOFF.md` criados

## Key Decisions
| Decisão | Detalhe |
|---------|---------|
| Prefixo `ETHAGT` | Convenção Etho (`ETH<AREA>`), área Programação Agêntica |
| Foco em arquitetura | Augmented LLM em loop, não SDK. Frameworks = instanciações (ADR-001) |
| 4 fases internas (A/B/C/D) + Capstone | A (fundamentos), B (razão/memória/conhecimento), C (multi-agentes/orquestração), D (produção/fronteira) |
| 6 novas competências | Programação Agêntica, Multi-Agent Systems, MCP & Tool Use, Agent Memory, AgentOps & Avaliação, Agent Security (B/I/A) |
| Rastreabilidade total | Cada competência: ≥4 módulos + ≥2 modalidades de avaliação |
| Capstone obrigatório | Nota ≥4,0 em **todos** os 4 pilares (não média); pré-requisito de certificação |
| 4 pilares | Técnico 40%, Consultivo 30%, Comportamental 20%, Prático 10% |
| Certificação 2 anos | Recertificação via eletivos, contribuição, mentoria ou reexame |
| Fontes canônicas | Toda afirmação técnica com fonte registrada |
| MkDocs como site | `docs/` com 27 diretórios numerados + overlay curado; build com mkdocs-material |

## Critical Context
- **Repositório**: `C:\Users\jcfig\Prog_Agentica\especializacao-programacao-agentica\` — ~270 arquivos, 31 diretórios
- **MCP spec**: 2025-11-25; Streamable HTTP substituiu HTTP+SSE (março/2025)
- **Carga total**: ~440 h (16 cursos + 1 Capstone). Duração: 12-18 meses
- **Diagramas Mermaid**: 59 (55 S0-S7 + 5 Capstone)
- **Casos de estudo**: 17 (16 modulares + 1 capstone)
- **Slides**: 16 outlines + README guia para capstone
- **Provas**: 16 modulares + 1 final integradora + gabarito
- **Site MkDocs**: 403 páginas HTML (de 404 .md), build em 11.72s (7 warnings — 6 pre-existentes em `18-Tools/README.md`). `mkdocs serve` para preview; `mkdocs build` gera em `site/`.
- **Erro frequente já corrigido**: consolidação de múltiplos artefatos em diretório errado (especialmente `09-CaseStudies/` e `04-Apostilas/`). Verificar se novos arquivos vão para o local correto.
- **Pendências eliminadas**: 12 topologias individuais (`10-Architecture/`), 23 padrões individuais (`11-AgentPatterns/`), 23 fichas de papers (`21-Papers/`), 8 exemplos runnable (`19-Examples/`), 6 docs MCP faltantes (`14-MCP/`), apêndice ferramentas ETHAGT01, links quebrados corrigidos.

## Next Steps for Future Sessions
1. **Versionamento**: `git init && git add . && git commit -m "feat: material completo + site MkDocs funcional"` na raiz do repositório
2. **GitHub Pages**: criar repositório `etho/especializacao-programacao-agentica`, push, ativar Pages (branch `main`, diretório `site/` ou `mkdocs gh-deploy`)
3. **Manutenção contínua**: revalidar Research KB a cada 6 meses (próxima: jan/2027)
4. **Pendências finas**: completar exemplos MCP restantes (`14-MCP/examples/`), adicionar métricas empíricas aos padrões (`11-AgentPatterns/catalog.md`)
5. **Aplicação prática** (fora do escopo atual): oferta para turmas, mentoria, evolução com feedback

## Relevant Files (paths from repo root)
| Caminho | Conteúdo |
|---------|----------|
| `README.md` | Raiz do repositório |
| `00-Governanca/` | Missão/visão/princípios, roadmap S0-S8, ADR-001 |
| `01-Curriculum/` | Grade (16+1), matriz 6 competências, mapa fases, rastreabilidade |
| `02-Syllabus/` | 17 syllabi (ETHAGT01-16 + ETHAGT90) |
| `03-Slides/` | 16 outlines + ETHAGT90/README.md |
| `04-Apostilas/` | 16 apostilas (`apostila.md` por curso, 7-9 capítulos cada) — **entregues em S9** |
| `05-Labs/` | 32 labs (2 por módulo) — **entregues em S9** |
| `06-Projects/` | 16 projetos aplicados — **entregues em S9** |
| `07-Exercises/` | 16 listas + 16 gabaritos — **entregues em S9** |
| `08-Assignments/` | 16 rubricas (4 pilares) — **entregues em S9** |
| `09-CaseStudies/` | 17 casos de estudo reais |
| `10-Architecture/` | 12 topologias multi-agente (catálogo + 12 fichas individuais + 3 ADRs) |
| `11-AgentPatterns/` | 23 padrões em 6 categorias (catálogo + 23 fichas individuais) |
| `12-Diagrams/` | 59 diagramas Mermaid |
| `13-Workflows/` | 8 workflows documentados |
| `14-MCP/` | Guia MCP completo (intro, spec, transports, building-servers, building-clients, governance, security, oauth, examples) |
| `15-RAG/` | 8 padrões RAG |
| `16-Memory/` | 6 padrões de memória |
| `17-PromptLibrary/` | 15 prompts em 7 categorias |
| `18-Tools/` | 6 fichas comparativas |
| `19-Examples/` | 8 exemplos runnable (ReAct, CoT/ToT, MCP, Supervisor, Event-Driven, AgentOps, Guardrails, DSPy) |
| `20-Research/` | Master-index + 16 fichas modulares + ETHAGT90 |
| `21-Papers/` | 23 fichas de leitura (foundational, reasoning, rag, memory, multi-agent, meta-agentes, eval, security, surveys) |
| `22-Glossary/` | ~70 termos |
| `23-Exams/` | 16 provas modulares + final + gabarito |
| `24-Templates/` | 5 templates |
| `25-Checklists/` | 3 checklists |
| `26-Capstone/` | Enunciado, diagramas C4, marcos, guia defesa, rubrica, starter |
| `27-Certification/` | Blueprint + exame-v1 + gabarito + recertificação |
| `docs/` | Site MkDocs (403 páginas, todas as bibliotecas + material didático) |
| `mkdocs.yml` | Configuração do site |
| `HANDOFF.md` | Documento de transição |
