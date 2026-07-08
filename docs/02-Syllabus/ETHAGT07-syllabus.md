# `ETHAGT07` — Knowledge Graphs & Vector Databases para Agentes

> Fase B · Carga 30 h · Versão 1.0 · Julho 2026

## 1. Identificação

| Campo | Valor |
|---|---|
| Código | `ETHAGT07` |
| Título | Knowledge Graphs & Vector Databases para Agentes |
| Fase interna | B |
| Carga horária | 30 h |
| Pré-requisitos | `ETHAGT06` |
| Módulos que dependem deste | `ETHAGT14`, `ETHAGT90` |

## 2. Objetivos

**Objetivo geral**: Capacitar o aluno a escolher, modelar e operar **vector databases** e **knowledge graphs** como infraestrutura cognitiva de agentes — incluindo *GraphRAG*.

**Objetivos específicos**:
1. Comparar vector databases (Qdrant, Milvus, Weaviate, Chroma, pgvector) por cenário.
2. Modelar knowledge graphs para raciocínio estruturado.
3. Implementar GraphRAG (local + global).
4. Construir pipelines híbridos (vector + grafo).
5. Avaliar custo/latência/escala em volumes realistas.

## 3. Competências desenvolvidas

| Competência | Nível ao final |
|---|---|
| C1 Programação Agêntica | **A** |
| C3 MCP & Tool Use | B |
| C4 Agent Memory | **A** |
| C5 AgentOps & Avaliação | **I** |

## 4. Conteúdo programático

### Unidade 1 — Vector DBs: modelo mental (4 h)
- ANN (Approximate Nearest Neighbor): HNSW, IVF
- Métricas: cosine, dot, euclidean; quando cada
- Metadata filtering (payloads)
- Híbrido: sparse + dense

### Unidade 2 — Comparativo de vector DBs (5 h)
- Qdrant (Rust, filtering forte), Milvus (escala), Weaviate (modules), Chroma (simples), pgvector (operacional)
- Multi-tenancy, escala horizontal, custo
- Quando escolher cada; quando *não* usar vector DB

### Unidade 3 — Knowledge Graphs (5 h)
- Modelo: triplas, propriedades, labels
- Neo4j / memgraph (Cypher)
- Modelagem para raciocínio: entidades, relações, inferência
- Extração de entidades/relações com LLM

### Unidade 4 — GraphRAG (6 h)
- Microsoft GraphRAG: comunidades, sumarização hierárquica
- Local vs Global search
- Quando GraphRAG supera vector RAG (raciocínio multi-hop)
- Custos de construção e manutenção

### Unidade 5 — Pipelines híbridos (5 h)
- Vector + grafo combinados
- RetrievalAgent que escolhe estratégia
- Manutenção: incremental update, lineage
- Caso: base de conhecimento técnica

### Unidade 6 — Operação em escala (5 h)
- Sharding, replicação, consistência
- Reindexação, drift de embeddings
- Custo de armazenamento e query
- Observabilidade

## 5. Bibliografia

### Fundamental
- Edge, D. et al. *GraphRAG: From Local to Global* (Microsoft, arXiv:2404.16130).
- Documentação Qdrant, Milvus, Weaviate, Neo4j.

### Complementar
- Pan, S. *Large Language Models and Knowledge Graphs* (survey).
- Lewis, P. *RAG original*.

## 6. Papers canônicos

- `arXiv:2404.16130` — GraphRAG (Microsoft)
- `arXiv:2005.11401` — RAG (base)
- `arXiv:2306.08302` — *Unifying Large Language Models and Knowledge Graphs* (Pan et al.)

## 7. Laboratórios

- **Lab 1** (4 h): "Vector DB bake-off". Mesmo corpus em Qdrant, pgvector e Chroma; comparar latência e recall.
- **Lab 2** (5 h): "GraphRAG em Neo4j". Construir KG a partir de um corpus; responder pergunta multi-hop.

## 8. Projeto do módulo

**Descrição**: construir pipeline híbrido (vector + grafo) para um corpus técnico, com agente que escolhe estratégia e justifica.
**Entrega**: sistema + benchmark (vector vs grafo vs híbrido) + ADR.
**Critério de sucesso**: híbrido melhora success rate em casos multi-hop sem explodir custo.

## 9. Exercícios

1. Para 5 cenários, vector DB ou knowledge graph?
2. Quando pgvector é melhor que Qdrant?
3. Escreva uma query Cypher para "co-autores de X".
4. Por que GraphRAG é caro? Justifique o custo.
5. Verdadeiro/falso: "Sempre preferir híbrido."

## 10. Avaliação

| Pilar | Peso | Instrumento |
|---|---|---|
| Técnico | 40% | Projeto + benchmark |
| Consultivo | 30% | Defesa do ADR |
| Comportamental | 20% | Code review |
| Prático | 10% | Demo: query multi-hop |

**Nota mínima**: 3,0.

## 11. Slides

- Slides: `03-Slides/ETHAGT07-slides.md` (~80 slides).

## 12. Leitura complementar

- Neo4j *GraphRAG*; Weaviate *modules*; Qdrant *filtering*.

## 13. Ferramentas

- Qdrant, Milvus, Weaviate, Chroma, pgvector, Neo4j, Cypher, LangGraph, Microsoft GraphRAG.

## 14. Diagramas

- Diagramas: `12-Diagrams/ETHAGT07/` — vector-vs-graph.mmd, graphrag-pipeline.mmd, hybrid-retrieval.mmd.

## 15. Estudo de caso

- GraphRAG em farmacêutica / jurídico.

## 16. Ficha de pesquisa

- Ficha: `20-Research/ETHAGT07-pesquisa.md`.

---

*Mantido por: Universidade Etho · Versão 1.0 · Julho 2026*
