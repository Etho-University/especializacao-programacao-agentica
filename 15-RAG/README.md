# 15 — RAG

Padrões de **Retrieval-Augmented Generation** no contexto agêntico. Suporte ao curso `ETHAGT06`.

## Padrões cobertos

- `naive-rag.md` — baseline (chunks + embed + retrieve)
- `adaptive-rag.md` — decide quando/quanto recuperar
- `corrective-rag.md` (CRAG) — avalia e corrige retrieved docs
- `self-rag.md` — modelo decide recuperar e criticar
- `agentic-rag.md` — agente dirige todo o processo
- `graph-rag.md` — RAG com knowledge graph
- `multimodal-rag.md` — texto + imagem + tabela
- `eval.md` — como avaliar RAG (faithfulness, relevance, context recall)

## Anti-patterns

- "Vector database resolve tudo"
- Sem re-ranking
- Sem eval
- Chunking ingênuo
