# Retrieval Agent

> Padrão 14/23 · Categoria D — Informação e Memória

## Intenção
Especialista em RAG — decide o quê/quando recuperar, refina queries.

## Estrutura
Loop com tools `search_kb`, `search_web`, `lookup_entity`.

## Quando usar
RAG agêntico multi-hop.

## Anti-patterns
- Parar cedo demais
- Sem re-ranking

## Custo
Variável (N hops).

## Referências
- Adaptive RAG / CRAG / Self-RAG
- ETHAGT06 — RAG Agêntico
