# Vector DBs

| DB | Linguagem | Força | Quando escolher | Quando evitar |
|---|---|---|---|---|
| **Qdrant** | Rust | filtering potente, performance, API limpa | produção, filtros complexos | simplicidade extrema |
| **Milvus** | Go/C++ | escala horizontal, ecossistema | volumes enormes (bilhões) | setup complexo |
| **Weaviate** | Go | modules (embeddings, rerank nativos), GraphQL | protótipo rápido, híbrido | performance extrema |
| **Chroma** | Python | simplicidade, embedded | protótipo, dev local | produção em volume |
| **pgvector** | C (ext. Postgres) | operacional, transacional | já tem Postgres, volume médio | volume muito alto |
| **Vespa** | Java | escala, features avançadas | enterprise, search pesado | complexidade |
| **Pinecone** | SaaS | managed, sem ops | sem querer operar | custo em escala |

## Critérios de decisão

- **Volume**: bilhões → Milvus/Vespa; milhões → qualquer um.
- **Multi-tenancy**: todos suportam; Qdrant é referência.
- **Filtering**: Qdrant.
- **Híbrido nativo**: Weaviate, Qdrant.
- **Operação**: já tem Postgres? pgvector elimina um sistema.
- **Custo**: SaaS é caro em escala.

## Quando NÃO usar vector DB

- Poucos milhares de documentos: JSON + similarity in-memory.
- Dados puramente estruturados: relacional.
- Dados puramente relacionais: knowledge graph.

## Referências

- Documentação oficial de cada.
- Artigo *Vector DB bake-off* (comparativos).
