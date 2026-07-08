# `ETHAGT05` — Memória de Agentes

> Fase B · Carga 25 h · Versão 1.0 · Julho 2026

## 1. Identificação

| Campo | Valor |
|---|---|
| Código | `ETHAGT05` |
| Título | Memória de Agentes (working · episódica · semântica · procedural) |
| Fase interna | B |
| Carga horária | 25 h |
| Pré-requisitos | `ETHAGT04` |
| Módulos que dependem deste | `ETHAGT07`, `ETHAGT09`, `ETHAGT14`, `ETHAGT15` |

## 2. Objetivos

**Objetivo geral**: Capacitar o aluno a **arquitetar sistemas de memória** que dão a agentes persistência, contexto acumulado e aprendizado — para além da context window.

**Objetivos específicos**:
1. Distinguir tipos de memória (working, episódica, semântica, procedural) e quando cada é necessária.
2. Implementar persistência via checkpointer (Postgres/SQLite/Redis).
3. Gerenciar a janela de contexto: sumarização, eviction, janela deslizante.
4. Construir memória vetorial para recall episódico.
5. Lidar com consistência, privacidade e custo de memória.

## 3. Competências desenvolvidas

| Competência | Nível ao final |
|---|---|
| C1 Programação Agêntica | **A** |
| C4 Agent Memory | **I** |
| C5 AgentOps & Avaliação | B |
| C6 Agent Security | B |

## 4. Conteúdo programático

### Unidade 1 — Tipos de memória (3 h)
- Working memory (context window): limites e estratégias
- Episódica (eventos passados, com timestamp)
- Semântica (fatos, conhecimento)
- Procedural (como fazer; skills)
- Inspiração cognitiva sem literalismo

### Unidade 2 — Checkpointer e estado persistente (5 h)
- LangGraph checkpointer: modelo de estado serializável
- Implementações: Postgres, SQLite, Redis
- Resume, replay, branching (time travel)
- Versionamento de schema de estado

### Unidade 3 — Gerenciamento de contexto (4 h)
- Custo cresce quadraticamente? linearmente? visão crítica
- Sumarização em cascata
- Eviction por relevância ou tempo
- Entity-centric memory (estilo MemGPT, Zep)

### Unidade 4 — Memória vetorial para recall (5 h)
- Embedding de eventos/passados
- Recall por similaridade semântica
- Metadata filtering (por sessão, usuário, tempo)
- Pós-recuperação: re-ranking

### Unidade 5 — Memória semântica e grafos (4 h)
- Quando promover episódica → semântica (consolidação)
- Knowledge graph como memória estruturada
- Integração com KG (profundidade em `ETHAGT07`)

### Unidade 6 — Produção: consistência, privacidade, custo (4 h)
- Consistência em sistemas multi-agente (eventual, ordenação)
- PII em memória: redação, retenção, direito ao esquecimento
- Custo de memória vs benefício (quando *não* memorizar)
- Observabilidade de memória (quem acessou, quando)

## 5. Bibliografia

### Fundamental
- Packer, C. *MemGPT: Towards LLMs as Operating Systems* (arXiv:2310.08560).
- Park, J.S. *Generative Agents* (arXiv:2304.03442).
- LangGraph docs — *Persistence* e *Memory*.

### Complementar
- Zep (long-term memory para agentes).
- *A-MEM: Agentic Memory* (2024).

## 6. Papers canônicos

- `arXiv:2310.08560` — MemGPT
- `arXiv:2304.03442` — Generative Agents (Stanford, "Smallville")
- `arXiv:2303.11366` — Reflexion (memória de falhas)

## 7. Laboratórios

- **Lab 1** (4 h): "Checkpointer em Postgres". Agente interrompido e retomado dias depois, preservando estado.
- **Lab 2** (5 h): "Memória episódica". Agente recorda interações anteriores relevantes via recall vetorial; comparar com/sem memória.

## 8. Projeto do módulo

**Descrição**: projetar a memória de um agente pessoal de longo prazo (assistentes de produtividade) com as 4 camadas; justificar trade-offs.
**Entrega**: implementação + ADR de memória + política de privacidade/evicção.
**Critério de sucesso**: agente demonstra memória útil em sessões espaçadas; política documentada.

## 9. Exercícios

1. Para 5 cenários, indique quais tipos de memória são necessários.
2. Quando uma memória vetorial é pior que uma relacional?
3. Escreva uma política de eviction por combinação de relevância e idade.
4. Como lidar com um fato que muda ao longo do tempo?
5. Liste 3 riscos de privacidade em memória de longo prazo.

## 10. Avaliação

| Pilar | Peso | Instrumento |
|---|---|---|
| Técnico | 40% | Projeto + prova |
| Consultivo | 30% | Defesa do ADR de memória |
| Comportamental | 20% | Code review |
| Prático | 10% | Demo: memória cross-sessão |

**Nota mínima**: 3,0.

## 11. Slides

- Slides: `03-Slides/ETHAGT05-slides.md` (~70 slides).

## 12. Leitura complementar

- *Generative Agents* paper; Zep blog; LangSmith *Memory*.

## 13. Ferramentas

- Python, LangGraph (checkpointer), Postgres, Redis, Qdrant, MemGPT-lib.

## 14. Diagramas

- Diagramas: `12-Diagrams/ETHAGT05/` — memory-layers.mmd, checkpointer-resume.mmd, eviction-flow.mmd.

## 15. Estudo de caso

- agentes com personalidade persistente (Generative Agents).

## 16. Ficha de pesquisa

- Ficha: `20-Research/ETHAGT05-pesquisa.md`.

---

*Mantido por: Universidade Etho · Versão 1.0 · Julho 2026*
