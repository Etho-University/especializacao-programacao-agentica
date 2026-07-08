# Handoff — Especialização em Programação Agêntica

> Documento de transição para a equipe de produção.
> **Data**: Julho 2026 · **Versão**: 1.0 · **Status**: Completo (S0-S8)

---

## 1. Resumo executivo

A Especialização em Programação Agêntica (prefixo `ETHAGT`) da Universidade Etho está **completa** — todos os 7 sprints de desenvolvimento (S0-S7) foram executados, mais a revisão final (S8). São **16 cursos obrigatórios + 1 Capstone**, totalizando ~440 horas, material completo para pós-graduação lato sensu.

### Números finais

| Métrica | Valor |
|---|---|
| Arquivos no repositório | ~490 |
| Cursos (ETHAGT01-16) | 16 |
| Capstone (ETHAGT90) | 1 |
| Apostilas | 16 (`04-Apostilas/ETHAGT01..16/apostila.md`, 7-9 capítulos cada) |
| Laboratórios | 32 (`05-Labs/`, 2 por curso) |
| Projetos | 16 (`06-Projects/`, 1 por curso) |
| Exercícios + Gabaritos | 16 + 16 (`07-Exercises/`) |
| Avaliações + Rubricas | 16 (`08-Assignments/`, 4 pilares) |
| Provas modulares | 16 (ETHAGT01-16) |
| Prova final integradora | 1 (20 questões) |
| Exame de certificação | 1 (35 questões) |
| Slides (outlines de aula) | 16 |
| Diagramas Mermaid | 59 |
| Casos de estudo | 17 |
| Padrões de agente (catálogo) | 23 |
| Arquiteturas (catálogo) | 12 |
| Workflows documentados | 8 |
| Padrões RAG | 8 |
| Padrões de memória | 6 |
| Prompts (biblioteca) | 15 |
| Fichas comparativas de ferramentas | 6 |
| Artigos na Research KB | ~40 papers + 11 frameworks + 7 benchmarks |
| Páginas do site (MkDocs) | ~40 |

---

## 2. Estrutura do repositório

```
especializacao-programacao-agentica/
├── 00-Governanca/        # Missão, roadmap, ADR-001
├── 01-Curriculum/        # Grade, competências, fases, rastreabilidade
├── 02-Syllabus/          # 16 syllabi + capstone (17 arquivos)
├── 03-Slides/            # 16 outlines de aula + capstone README
├── 04-Apostilas/         # 16 apostilas aprofundadas
├── 05-Labs/              # 32 laboratórios (2 por módulo)
├── 06-Projects/          # 16 projetos aplicados
├── 07-Exercises/         # 16 listas de exercícios + gabaritos
├── 08-Assignments/       # 16 avaliações com rubricas (4 pilares)
├── 09-CaseStudies/       # 17 estudos de caso reais
├── 10-Architecture/      # Catálogo de 12 arquiteturas/topologias
├── 11-AgentPatterns/     # Catálogo de 23 padrões de projeto
├── 12-Diagrams/          # 59 diagramas Mermaid versionáveis
├── 13-Workflows/         # 8 workflows canônicos + variantes
├── 14-MCP/               # Guia MCP (intro, spec, transports)
├── 15-RAG/               # 8 padrões RAG (naive a graph)
├── 16-Memory/            # 6 padrões de memória
├── 17-PromptLibrary/     # 15 prompts em 7 categorias
├── 18-Tools/             # 6 fichas comparativas de ferramentas
├── 19-Examples/          # [vazio — a produzir]
├── 20-Research/          # Research KB (master-index + 16 fichas)
├── 21-Papers/            # [vazio — a produzir]
├── 22-Glossary/          # Glossário técnico (~70 termos)
├── 23-Exams/             # 16 provas modulares + prova final integradora
├── 24-Templates/         # 5 templates (ADR, syllabus, rubrica, eval, PDI)
├── 25-Checklists/        # 3 checklists (produção, security, code review)
├── 26-Capstone/          # Enunciado + milestones + defesa + rubrica + starter
├── 27-Certification/     # Blueprint + exame v1 + gabarito + recertificação
├── docs/                 # Site MkDocs (~40 páginas de navegação)
├── mkdocs.yml            # Configuração do site
└── .gitignore
```

---

## 3. Pendências conhecidas

### 3.1 Conteúdo
| Item | Prioridade | Notas |
|------|-----------|-------|
| `19-Examples/` — mais exemplos runnable | Média | Já há 25 arquivos; pode expandir conforme padrões |
| `21-Papers/` — PDFs e notas de leitura | Baixa | Links e referências já existem nas apostilas e Research KB; PDFs podem violar copyright |
| `03-Slides/ETHAGT90/` — slides de defesa | Baixa | A produzir pelo aluno durante o Capstone; README guia existe |
| Revisão ortográfica completa | Feita | Revisão técnica (S10) + ortográfica (S11) concluídas: arXiv IDs, gabaritos, código de labs, links, acentuação, concordância e caracteres CJK que vazaram — todos corrigidos |

### 3.2 Qualidade
| Item | Notas |
|------|-------|
| Revisão ortográfica completa | Não realizada — recomenda-se passar todos os .md por corretor |
| Revisão de links internos (mkdocs) | Warnings existem para links que apontam para fora de `docs/` — comportamento esperado |
| Validação de consistência cross-módulo | Feita nesta S8 — nenhuma inconsistência grave encontrada |

### 3.3 Manutenção contínua
| Item | Frequência | Responsável |
|------|-----------|-------------|
| Revalidar Research KB | A cada 6 meses (próxima: jan/2027) | Área de IA |
| Atualizar MCP spec | A cada release da spec (próxima: ~2026-12) | Área de IA |
| Atualizar comparação de ferramentas | A cada 6 meses | Área de IA |
| Revisar benchmarks (SWE-bench, GAIA, τ-bench) | A cada 6 meses | Área de IA |

---

## 4. Decisões arquiteturais registradas

| ADR | Decisão | Status |
|-----|---------|--------|
| ADR-001 | Criar Especialização como Fase 4, prefixo ETHAGT, 16+1 cursos, architecture-first | Vigente |

Toda mudança em princípios ou estrutura curricular exige ADR novo + aprovação. Mudanças em conteúdo de módulo via PR com revisão de especialista.

---

## 5. Fluxo de publicação

1. **Revisão**: especialista da área revisa PR
2. **Site**: `mkdocs build` gera `site/` (estático)
3. **Publicação**: fazer deploy do conteúdo de `site/` no servidor Web da Etho ou GitHub Pages
4. **Commit**: mensagens no padrão `ETHAGT0x: <ação>`

---

## 6. Contatos

- **Manutenção**: Escola de Tecnologia — Universidade Etho
- **Área**: Inteligência Artificial
- **Pré-requisitos para alunos**: ETHDEV07 + ETHML01 + Python Intermediário

---

*Este documento completa o Sprint 8 (Revisão e Handoff) da Especialização em Programação Agêntica.*
