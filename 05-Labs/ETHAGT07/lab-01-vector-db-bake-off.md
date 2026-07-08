# ETHAGT07 — Lab 1: Vector DB bake-off

> Curso: Knowledge Graphs & Vector Databases para Agentes · Carga: 30h · Pré-req: ETHAGT06

## Objetivo
Carregar o mesmo corpus em três vector databases (Qdrant, pgvector e Chroma), executar um benchmark de latência e recall, e produzir uma tabela comparativa que justifique a escolha por cenário.

## Preparação
- Ambiente: Python 3.11+, `pip install qdrant-client psycopg2-binary chromadb numpy`, Docker
- Dados/recursos: corpus de 1000+ documentos curtos (`corpus.json`); 50 queries de teste com ground truth
- Leitura prévia: Apostila ETHAGT07, Unidade 1 (Vector DBs: modelo mental) e Unidade 2 (Comparativo)

## Roteiro
### Passo 1 — Preparar corpus e ground truth
Gere ou carregue 1000+ documentos e 50 queries com resultados esperados:

```python
corpus = load_corpus("corpus.json")  # [{"id": "...", "text": "..."}]
queries = load_queries("queries.json")  # [{"query": "...", "expected_ids": ["d1", "d5"]}]
```

**Checkpoint:** corpus com 1000+ docs e 50 queries com ground truth.

### Passo 2 — Gerar embeddings
Pré-compute embeddings para todo o corpus (uma vez, reutilizar nos 3 DBs):

```python
from openai import OpenAI
client = OpenAI()

def embed_batch(texts, batch_size=100):
    all_embeddings = []
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i+batch_size]
        resp = client.embeddings.create(input=batch, model="text-embedding-3-small")
        all_embeddings.extend([d.embedding for d in resp.data])
    return all_embeddings

embeddings = embed_batch([d["text"] for d in corpus])
```

**Checkpoint:** 1000+ embeddings gerados e salvos.

### Passo 3 — Carregar no Qdrant
```python
from qdrant_client import QdrantClient
qdrant = QdrantClient("localhost", port=6333)
qdrant.create_collection("bench", vectors_config={"size": 1536, "distance": "Cosine"})
qdrant.upsert("bench", points=[
    {"id": i, "vector": embeddings[i], "payload": {"text": corpus[i]["text"]}}
    for i in range(len(corpus))
])
```

**Checkpoint:** Qdrant tem 1000+ pontos indexados.

### Passo 4 — Carregar no pgvector
```sql
CREATE EXTENSION IF NOT EXISTS vector;
CREATE TABLE docs (id TEXT PRIMARY KEY, embedding vector(1536), text TEXT);
CREATE INDEX ON docs USING hnsw (embedding vector_cosine_ops);
```

```python
import psycopg2
conn = psycopg2.connect("postgresql://postgres:pass@localhost/agents")
for i, doc in enumerate(corpus):
    conn.execute("INSERT INTO docs VALUES (%s, %s, %s)",
                 (doc["id"], embeddings[i], doc["text"]))
```

**Checkpoint:** pgvector tem 1000+ linhas com índice HNSW.

### Passo 5 — Carregar no Chroma
```python
import chromadb
chroma = chromadb.PersistentClient(path="./chroma_data")
coll = chroma.create_collection("bench")
coll.add(ids=[d["id"] for d in corpus],
         embeddings=embeddings,
         documents=[d["text"] for d in corpus])
```

**Checkpoint:** Chroma tem 1000+ documentos.

### Passo 6 — Benchmark de latência
Meça o tempo de query para cada DB nas 50 queries:

```python
import time

def benchmark_db(search_fn, queries, n_runs=3):
    latencies = []
    for q in queries:
        q_vec = embed(q["query"])
        for _ in range(n_runs):
            start = time.perf_counter()
            results = search_fn(q_vec, limit=10)
            latencies.append(time.perf_counter() - start)
    return {"p50": np.percentile(latencies, 50),
            "p95": np.percentile(latencies, 95),
            "mean": np.mean(latencies)}
```

**Checkpoint:** latências medidas para os 3 DBs.

### Passo 7 — Benchmark de recall
Meça recall@10 (fração dos docs esperados que aparecem no top-10):

```python
def recall_at_k(search_fn, queries, k=10):
    recalls = []
    for q in queries:
        q_vec = embed(q["query"])
        results = search_fn(q_vec, limit=k)
        retrieved_ids = {r.id for r in results}
        expected_ids = set(q["expected_ids"])
        if expected_ids:
            recalls.append(len(retrieved_ids & expected_ids) / len(expected_ids))
    return np.mean(recalls)
```

**Checkpoint:** recall@10 calculado para os 3 DBs.

### Passo 8 — Tabela comparativa
Produza a tabela final:

| DB | Recall@10 | Latência p50 (ms) | Latência p95 (ms) | Setup complexity | Filtering |
|---|---|---|---|---|---|
| Qdrant | | | | Baixa | Forte |
| pgvector | | | | Média (SQL) | SQL nativo |
| Chroma | | | | Muito baixa | Básico |

**Checkpoint:** tabela preenchida em `bakeoff_results.md` com recomendação por cenário.

## Desafios extras
- Adicione metadata filtering ao benchmark e Meça o impacto na latência
- Teste com 10k e 100k documentos e veja como a escala afeta cada DB
- Compare HNSW vs IVF no Qdrant
- Adicione Milvus ou Weaviate como 4º competidor

## Entrega
- Repositório com `bakeoff.py`, `bakeoff_results.md`, `corpus.json`, `queries.json`
- Commit no padrão `ETHAGT07: lab-1 executar vector db bakeoff`

## Rubrica
Avaliado pela rubrica em `08-Assignments/ETHAGT07/assignment-01.md` (Pilar Comportamental 20%: colaboração em labs).
