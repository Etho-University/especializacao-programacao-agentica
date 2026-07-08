# ETHAGT07 — Gabarito

> Restrito a mentores. Cada resposta justificada com referência à apostila.

## Múltipla escolha

1. **b)** — HNSW (Hierarchical Navigable Small World) é um algoritmo de busca aproximada de vizinhos mais próximos (ANN) que oferece boa relação entre latência e recall, amplamente usado em vector DBs (Capítulo 1 — Vector DBs: modelo mental).

2. **b)** — Local search responde sobre entidades específicas e suas vizinhanças diretas; Global search sintetiza informações em nível de comunidade/tema, usando a sumarização hierárquica construída no pré-processamento (Capítulo 4 — GraphRAG).

3. **b)** — pgvector é preferível quando já se usa PostgreSQL e a escala de vetores é moderada, pois aproveita operações ACID, joins com dados relacionais e simplifica a stack operacional (Capítulo 2 — Comparativo de vector DBs).

4. **b)** — Uma tripla representa uma relação na forma (sujeito, predicado, objeto), ex.: (PessoaX, CO_AUTOR_DE, PessoaY). É a unidade fundamental de um knowledge graph (Capítulo 3 — Knowledge Graphs).

## Verdadeiro ou Falso (justificado)

1. **Falso.** Pipelines híbridos adicionam custo de construção (extração de entidades, manutenção de grafo) e latência. Só vale quando o problema genuinamente exige raciocínio multi-hop estruturado. Para perguntas factuais simples, vector DB puro é suficiente e mais barato (Capítulo 5 e exercícios do syllabus).

2. **Verdadeiro.** GraphRAG exige extração de entidades/relações com LLM, construção de comunidades e sumarização hierárquica — um pré-processamento caro que justifica o custo apenas para corpora onde raciocínio multi-hop é frequente (Capítulo 4.4 — Custos de construção).

3. **Verdadeiro.** Metadata filtering (payloads) permite filtrar por atributos (tenant, data, tipo) armazenados junto aos vetores, sem precisar reprocessar ou recomputar embeddings (Capítulo 1.3 — Metadata filtering).

4. **Falso.** Extração de entidades/relações com LLM é não-determinística — varia entre execuções. É necessário validação, pós-processamento e possivelmente múltiplas amostras com reconciliação (Capítulo 3.4).

## Código curto

1. **Query Cypher para co-autores:**
```cypher
MATCH (x:Person {name: "PesquisadorX"})-[:CO_AUTHORED_WITH]-(coauthor:Person)
RETURN DISTINCT coauthor.name
```
Referência: Capítulo 3 (Knowledge Graphs, Neo4j/Cypher).

2. **RetrievalAgent (decisão vector vs grafo):**
```python
def retrieval_agent(query):
    q_type = classify_query(query)  # "entity" | "topic" | "factual"
    if q_type == "entity":
        return graph_search(query)   # multi-hop estruturado
    else:
        return vector_search(query)  # similaridade semântica
```
Referência: Capítulo 5 (Pipelines híbridos).

3. **Busca híbrida (BM25 + densa):**
```python
def hybrid_search(query, k=5):
    sparse_results = bm25_search(query, k=k*2)
    dense_results = vector_search(embed(query), k=k*2)
    fused = reciprocal_rank_fusion(sparse_results, dense_results)
    return fused[:k]
```
Referência: Capítulo 1.4 (Híbrido: sparse + dense).

## Análise de trade-off

1. **Vector DB vs KG por cenário:**
   - **FAQ:** Vector DB (similaridade semântica entre pergunta e resposta).
   - **Rede de co-autores:** Knowledge graph (traversal de relações estruturadas).
   - **Perguntas factuais simples:** Vector DB (recuperação por similaridade).
   Referência: Capítulo 2 e 3.

2. **GraphRAG local vs. vector RAG (multi-hop):** GraphRAG supera quando a pergunta exige encadear múltiplas relações (ex.: "quem são os co-autores dos alunos de X?"). Vector RAG falha porque cada chunk é isolado e não captura a estrutura relacional (Capítulo 4.3).

3. **Qdrant vs. pgvector (10M vetores, multi-tenant):** Qdrant é melhor para escala massiva e filtering otimizado (escrito em Rust). pgvector é melhor se já há PostgreSQL, dados relacionais precisam de joins com vetores, e a operação quer simplificar a stack. A escolha depende do contexto operacional existente (Capítulo 2).

## Debug / diagnóstico

1. **Diagnóstico:** O filtro de tenant não está sendo aplicado na query — a busca retorna vetores de todos os tenants. **Correção:** sempre incluir `filter={"tenant_id": current_tenant}` na query ao vector DB (Capítulo 1.3).

2. **Diagnóstico:** A sumarização hierárquica de comunidades não foi construída ou o Global search não está usando o nível de comunidade adequado. **Correção:** verificar o pipeline de indexação do GraphRAG e garantir que a etapa de detecção de comunidades (ex.: algoritmo de Leiden) e sumarização foi executada (Capítulo 4.2).
