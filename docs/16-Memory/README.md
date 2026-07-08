# 16 — Memory

Padrões de **memória de agentes** — além da context window. Suporte ao curso `ETHAGT05`.

## Taxonomia

- **Working memory** — sessão atual (context window)
- **Episodic** — eventos passados (vector store + timestamps)
- **Semantic** — fatos/conhecimento (KB, knowledge graph)
- **Procedural** — como fazer tarefas (skills, ferramentas)

## Padrões

- `checkpointer.md` — persistência de estado (Postgres, SQLite, Redis)
- `summarization.md` — comprimir histórico
- `vector-recall.md` — recuperar memórias por similaridade
- `entity-memory.md` — memória por entidade (estilo MemGPT/Zep)
- `consolidation.md` — promover episódica → semântica
- `eviction.md` — políticas de expurgo

## Tópicos avançados

- Consistência em sistemas multi-agente
- Privacidade e PII em memória
- Custo de memória vs benefício
