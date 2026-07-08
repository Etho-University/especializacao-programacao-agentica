# ETHAGT05 — Roteiro da Apresentação

> Universidade Etho · Especialização em Programação Agêntica
> Fase B — Memória, Contexto e Persistência · 25 h

---

## Metadados

| Campo | Valor |
|---|---|
| Código | ETHAGT05 |
| Título | Memória de Agentes (working · episódica · semântica · procedural) |
| Duração | 90 min (2 blocos de 45 min) |
| Total de slides | 70 |
| Competências | C1 (A), C4 (I), C5 (B), C6 (B) |
| Pré-requisitos | ETHAGT04 (Reasoning Patterns) |
| Fontes canônicas | Packer et al. *MemGPT* (arXiv:2310.08560); Park et al. *Generative Agents* (arXiv:2304.03442); Shinn et al. *Reflexion* (arXiv:2303.11366); LangGraph docs |

---

## Fluxo da Aula

### BLOCO 1 — 45 min

| Seção | Slides | Tempo | Objetivo |
|---|---|---|---|
| A — Abertura | 1-6 | 8 min | Engajar, estabelecer objetivos, contextualizar a era da memória |
| B — Tipos de Memória | 7-16 | 12 min | As 4 camadas (working, episódica, semântica, procedural) + MemGPT |
| C — Checkpointer e Estado Persistente | 17-29 | 15 min | Backends, resume/replay/branching, DEMO ao vivo |
| D — Gerenciamento de Contexto | 30-40 | 10 min | Custo, sumarização, eviction, entity-centric memory |
| Intervalo | — | 5 min | — |

### BLOCO 2 — 45 min

| Seção | Slides | Tempo | Objetivo |
|---|---|---|---|
| E — Memória Vetorial para Recall | 41-50 | 12 min | Embedding, metadata filtering, re-ranking, pipeline, Lab 2 |
| F — Memória Semântica e Grafos | 51-57 | 8 min | Consolidação, knowledge graph, Generative Agents |
| G — Produção | 58-63 | 8 min | Consistência, PII, direito ao esquecimento, custo, observabilidade |
| H — Fechamento | 64-70 | 12 min | Boas práticas, anti-patterns, resumo, quiz, projeto, Q&A |
| Q&A extra | — | 5 min | Perguntas abertas |

---

## Pontos de Engajamento

| Slide | Tipo | Interação |
|---|---|---|
| 5 | Mão levantada | "Quanto contexto você acha que um assistente pessoal precisa reter?" |
| 9 | Discussão rápida | "Já notaram o agente 'esquecendo' o início da conversa?" |
| 15 | Votação | "Inspiração cognitiva: framework de design ou modelo neural?" |
| 22 | Comparação | "Qual backend você usaria para seu projeto hoje?" |
| 28 | DEMO ao vivo | Checkpointer em Postgres — interromper e retomar agente |
| 29 | Duplas (2 min) | "O que acontece se o modelo foi atualizado entre sessões?" |
| 39 | Trios (3 min) | Escrever política de eviction combinando relevância e idade |
| 49 | Discussão aberta | "Embedding ou metadata? 3 cenários para escolher" |
| 56 | Grupo | "A arquitetura de memória é a identidade do agente? Concordam?" |
| 67-69 | Quiz individual | 3 perguntas de múltipla escolha |

---

## Materiais Necessários

- [ ] Projetor / tela de compartilhamento
- [ ] VS Code aberto com `05-Labs/ETHAGT05/Lab1-Checkpointer-Postgres/`
- [ ] Postgres local rodando (Docker: `docker run -p 5432:5432 postgres:16`)
- [ ] Python 3.11+ com `langgraph`, `langgraph-checkpoint-postgres`, `openai`, `qdrant-client`
- [ ] `OPENAI_API_KEY` configurada
- [ ] Acesso ao repositório da especialização
- [ ] Quadro branco (para diagramar as 4 camadas de improviso)
- [ ] Handout: storyboard impresso (opcional)
- [ ] Qdrant rodando (Docker) para Lab 2 preview

---

## Riscos e Planos B

| Risco | Plano B |
|---|---|
| Postgres indisponível na DEMO (Slide 28) | Mostrar screenshot do resume pré-gravado + logs |
| API LLM indisponível | Usar SQLite no lugar de Postgres (fallback local) |
| Alunos sem ETHAGT04 (reasoning) | Revisar StateGraph em 5 min antes da Seção C |
| Tempo estourado no Bloco 1 | Cortar exercício do Slide 39 (eviction), mover para homework |
| Tempo estourado no Bloco 2 | Reduzir quiz para 2 perguntas (Slides 67-68); referências como leitura |
| Vector DB confuso na turma | Simplificar: focar só em embedding + cosine similarity |

---

## Avaliação da Aula

- Quiz ao final (Slides 67-69): ≥2 acertos = compreensão básica
- Exercício de política de eviction (Slide 39): discussão em trios
- Perguntas de discussão (arquivo `08-perguntas-discussao.md`): profundidade das respostas
- DEMO (Slide 28): verificar se alunos percebem o "resume" acontecendo
- Feedback informal: "Um tipo de memória que você não conhecia antes de hoje"
