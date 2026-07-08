# ETHAGT07 — Referências

> Todas as fontes utilizadas na preparação e apresentação da aula.

---

## Canônicas (fundação do curso)

### 1. GraphRAG: From Local to Global — A Graph RAG Approach to Query-Focused Summarization
- **Autores**: Darren Edge, Ha Trinh, Newman Cheng, Joshua Bradley, Alex Chao, Apurva Mody, Steven Truitt, Jonathan Larson
- **Instituição**: Microsoft
- **Data**: abril 2024
- **arXiv**: 2404.16130
- **Resumo**: Introduz GraphRAG — construção de knowledge graph de entidades, detecção de comunidades (Leiden) e sumarização hierárquica. Define Local search (perguntas específicas) e Global search (perguntas amplas via map-reduce). Base direta das Seções E da aula.
- **Importância**: Canônica
- **Slides que referenciam**: 6, 38, 39, 40, 41, 42, 43, 44, 45, 46, 48

### 2. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (RAG original)
- **Autores**: Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, Sebastian Riedel, Douwe Kiela
- **Venue**: NeurIPS 2020
- **arXiv**: 2005.11401
- **Resumo**: Introduz RAG — retrieve + generate. Fundamento de toda a evolução até GraphRAG. Contexto histórico do Slide 6.
- **Importância**: Canônica
- **Slides que referenciam**: 6

### 3. Unifying Large Language Models and Knowledge Graphs: A Roadmap
- **Autores**: Shirui Pan, Linhao Luo, Yufei Wang, Chen Chen, Jiapu Wang, Xindong Wu
- **Data**: junho 2023
- **arXiv**: 2306.08302
- **Resumo**: Survey unificando LLMs e knowledge graphs — categorias de integração (KG-enhanced LLMs, LLM-augmented KGs). Base teórica para a Seção D e E.
- **Importância**: Canônica
- **Slides que referenciam**: 6, 27, 33, 34

---

## Importantes (complementam e aprofundam)

### 4. Efficient and Robust Approximate Nearest Neighbor Search Using Hierarchical Navigable Small World Graphs (HNSW)
- **Autores**: Yu. A. Malkov, D. A. Yashunin
- **Data**: 2016 (atualizado 2018)
- **arXiv**: 1603.09320
- **Resumo**: Introduz HNSW — o algoritmo dominante de ANN em vector DBs modernos. Fundamento do Slide 11.
- **Importância**: Importante
- **Slides que referenciam**: 11

### 5. Qdrant — Documentation
- **URL**: https://qdrant.tech/documentation/
- **Resumo**: Vector DB em Rust com filtering otimizado e sparse vectors nativos. Base dos Slides 19 e 15.
- **Importância**: Importante
- **Slides que referenciam**: 15, 19, 24

### 6. Milvus — Documentation
- **URL**: https://milvus.io/docs
- **Resumo**: Vector DB distribuído, cloud-native, para escala massiva. Base do Slide 20.
- **Importância**: Importante
- **Slides que referenciam**: 20, 24, 64

### 7. Weaviate — Documentation
- **URL**: https://weaviate.io/developers/weaviate
- **Resumo**: Vector DB com modules integrados (generative, Q&A, multi-modal). Base do Slide 21.
- **Importância**: Importante
- **Slides que referenciam**: 21, 24

### 8. pgvector — GitHub
- **URL**: https://github.com/pgvector/pgvector
- **Resumo**: Extensão PostgreSQL para vector search (HNSW e IVFFlat). Base do Slide 23.
- **Importância**: Importante
- **Slides que referenciam**: 23, 24

### 9. Neo4j — Graph Data Platform
- **URL**: https://neo4j.com/docs/
- **Resumo**: Graph database nativa (Labeled Property Graph) com linguagem Cypher. Base das Seções D e E.
- **Importância**: Importante
- **Slides que referenciam**: 30, 31, 46

### 10. Microsoft GraphRAG — Implementation
- **URL**: https://github.com/microsoft/graphrag
- **Resumo**: Implementação de referência do GraphRAG (Python). Base da DEMO do Slide 46.
- **Importância**: Importante
- **Slides que referenciam**: 39, 46

### 11. LangChain LLMGraphTransformer
- **URL**: https://python.langchain.com/docs/use_cases/graph/constructing/
- **Resumo**: Ferramenta para extração de entidades/relações com LLM e construção de knowledge graph. Base do Slide 33.
- **Importância**: Importante
- **Slides que referenciam**: 33

---

## Complementares (leitura opcional)

### 12. Chroma — Documentation
- **URL**: https://docs.trychroma.com/
- **Resumo**: Vector DB minimalista para prototipagem. Base do Slide 22.
- **Slides que referenciam**: 22, 24

### 13. Memgraph — Documentation
- **URL**: https://memgraph.com/docs
- **Resumo**: Graph database in-memory, alternativa ao Neo4j para latência baixa.
- **Slides que referenciam**: 30

### 14. ArangoDB — Documentation
- **URL**: https://www.arangodb.com/docs/
- **Resumo**: Graph database multi-modelo (grafo + documento + chave-valor).
- **Slides que referenciam**: 30

### 15. Product Quantization for Nearest Neighbor Search (PQ)
- **Autores**: Hervé Jégou, Matthijs Douze, Cordelia Schmid
- **Venue**: IEEE TPAMI 2011
- **Resumo**: Algoritmo de quantização para comprimir vetores. Base do Slide 67.
- **Slides que referenciam**: 12, 67

### 16. GLiNER — Generalist and Lightweight Model for Named Entity Recognition
- **URL**: https://github.com/urchade/GLiNER
- **Resumo**: NER sem LLM (mais rápido que LLM para extração de entidades). Alternativa mencionada no Slide 33.
- **Slides que referenciam**: 33

### 17. Vespa — Documentation
- **URL**: https://docs.vespa.ai/
- **Resumo**: Platform de search enterprise com vector + grafo. Complementar ao comparativo.
- **Slides que referenciam**: 24

### 18. LangGraph — TNT-LLM Tutorial
- **URL**: https://github.com/langchain-ai/langgraph/tree/main/tutorials/tnt-llm
- **Resumo**: Exemplo de graph + LLM (topic naming + tagging). Caso prático de knowledge graph com LLM.
- **Slides que referenciam**: 33, 55

### 19. Linked Open Data (LOD) e RDF/SPARQL
- **URL**: https://www.w3.org/standards/semanticweb/
- **Resumo**: Paradigma W3C de knowledge graphs (RDF, SPARQL, ontologias). Alternativa ao LPG mencionada no Slide 30.
- **Slides que referenciam**: 30

### 20. Reciprocal Rank Fusion (RRF)
- **URL**: https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf
- **Resumo**: Método simples e robusto para fundir rankings de múltiplas trilhas de retrieval. Base do Slide 16.
- **Slides que referenciam**: 16, 54

---

## Ficha de Pesquisa

- **Arquivo**: `20-Research/ETHAGT07-pesquisa.md`
- **Última consulta**: Julho 2026
- **Revalidação**: Janeiro 2027 (vector DBs e GraphRAG evoluem rápido)
