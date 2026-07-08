# ETHAGT07 — Knowledge Graphs & Vector Databases para Agentes — Slides

> Apresentação para aula síncrona · ~50 min · 13 slides

## Estrutura da aula
- Abertura (5 min): gancho/motivação
- Teoria (25 min): conceitos principais com diagramas de referência
- Demonstração (10 min): código ao vivo ou walkthrough de lab
- Exercício (5 min): questão rápida ou discussão
- Fechamento (5 min): conexão com próximo módulo, leitura recomendada

## Slides

### Slide 1 — Título
- ETHAGT07 — Knowledge Graphs & Vector Databases para Agentes
- Professor, data, Universität Etho
- Pré-requisito: ETHAGT06
- ~1 min

### Slide 2 — Agenda
1. Vector DBs: modelo mental (ANN, métricas, filtering)
2. Comparativo de vector DBs
3. Knowledge Graphs (modelo, modelagem, extração)
4. GraphRAG (local + global)
5. Pipelines híbridos
6. Operação em escala
- ~1 min

### Slide 3 — Gancho / Motivação
- Problema: vector search sozinho não captura relacionamentos entre entidades
- Exemplo: "Quais medicamentos interagem com o remédio que o Dr. Silva prescreveu para o paciente X?" — precisa de grafo
- A solução: vector DB + knowledge graph como infraestrutura cognitiva
- Pergunta: *Quando uma busca por similaridade não é suficiente?*
- ~3 min

### Slide 4 — Vector DBs: Modelo Mental
- ANN (Approximate Nearest Neighbor): HNSW, IVF
- Métricas: cosine, dot, euclidean — quando cada
- Metadata filtering (payloads, filtering antes ou depois?)
- Híbrido: sparse + dense
- Pergunta técnica: *Cosine vs dot — quando a diferença importa?*
- ~4 min

### Slide 5 — Comparativo de Vector DBs
- Qdrant (Rust, filtering forte): melhor filtering
- Milvus: escala, distribuição
- Weaviate: modules integrados (generative, Q&A)
- Chroma: simplicidade, prototipagem
- pgvector: operacional (já usa Postgres)
- Multi-tenancy, escala horizontal, custo
- Discussão: *Para um MVP, qual escolher? E para 1M de usuários?*
- ~4 min

### Slide 6 — Knowledge Graphs
- Modelo: triplas (sujeito → predicado → objeto), propriedades, labels
- Neo4j / Memgraph e Cypher
- Modelagem para raciocínio: entidades, relações, inferência
- Extração de entidades/relações com LLM (NER + relation extraction)
- Pergunta: *Qual a cardinalidade típica de um KG empresarial? Quantas relações por entidade?*
- ~4 min

### Slide 7 — GraphRAG
- Microsoft GraphRAG: comunidades, sumarização hierárquica
- Local search: busca em comunidade específica
- Global search: síntese entre comunidades
- Quando GraphRAG supera vector RAG: raciocínio multi-hop
- Custos de construção e manutenção (token caro)
- Diagrama: `12-Diagrams/ETHAGT07/graphrag-pipeline.mmd`
- ~5 min

### Slide 8 — DEMO: Vector DB Bake-off
- Código ao vivo: mesmo corpus em Qdrant, pgvector e Chroma
- Medir latência (p50, p99) e recall@10 nos 3 sistemas
- Mostrar diferença de filtering performance
- Referência: `05-Labs/ETHAGT07/Lab1-Vector-DB-Bake-off`
- Pergunta: *pgvector teve 2x a latência do Qdrant — vocês aceitariam?*
- ~5 min

### Slide 9 — Pipelines Híbridos
- Vector + grafo combinados: busca vetorial + travessia de grafo
- RetrievalAgent que escolhe estratégia (com base na pergunta)
- Manutenção: incremental update, lineage
- Caso: base de conhecimento técnica com docs + relacionamentos
- Diagrama: `12-Diagrams/ETHAGT07/hybrid-retrieval.mmd`
- ~4 min

### Slide 10 — Operação em Escala
- Sharding, replicação, consistência
- Reindexação e drift de embeddings (modelos novos)
- Custo de armazenamento (dimensões, quantização)
- Observabilidade: latência de query, taxa de cache hit
- ~3 min

### Slide 11 — Exercício: Vector DB ou Knowledge Graph?
- 5 cenários:
  1. Catálogo de produtos com busca por similaridade
  2. Base de conhecimento médica com relações entre doenças e tratamentos
  3. Documentos jurídicos com referências cruzadas
  4. Chatbot de RH com perguntas sobre políticas
  5. Sistema de recomendação de filmes
- Em grupos: vector, graph, ou híbrido? Justificar.
- ~4 min

### Slide 12 — Conexão com Próximo Módulo
- ETHAGT14 — Escalabilidade: vector DBs em produção multi-tenant
- ETHAGT90 — Capstone: integra tudo
- Leitura: Edge et al. *GraphRAG* (Microsoft, arXiv:2404.16130)
- Documentação Qdrant, Milvus, Neo4j
- ~2 min

### Slide 13 — Referências
- Edge, D. et al. *GraphRAG: From Local to Global* (Microsoft, arXiv:2404.16130)
- Documentação Qdrant, Milvus, Weaviate, Neo4j
- Pan, S. *Large Language Models and Knowledge Graphs* (survey)
- Lewis, P. *RAG original* (arXiv:2005.11401)
- ~1 min
