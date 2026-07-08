# ETHAGT14 — Lab 1: Cache semântico

> Curso: Escalabilidade & Sistemas Distribuídos de Agentes · Carga: 30h · Pré-req: ETHAGT11

## Objetivo
Adicionar cache semântico (baseado em similaridade de embeddings) a um agente existente, medir a redução de custo e latência, e analisar os trade-offs de consistência.

## Preparação
- Ambiente: Python 3.11+, `pip install openai redis numpy`, Docker (para Redis)
- Dados/recursos: agente ReAct ou RAG de labs anteriores; 30 perguntas de teste (algumas semelhantes)
- Leitura prévia: Apostila ETHAGT14, Unidade 2 (Caching)

## Roteiro
### Passo 1 — Subir o Redis
```bash
docker run --name agent-redis -p 6379:6379 -d redis:7 redis-server --save 60 1
```

**Checkpoint:** Redis acessível em `localhost:6379`.

### Passo 2 — Implementar cache exato (baseline)
Comece com cache de match exato (exact match):

```python
import redis, hashlib, json

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

def exact_cache_get(query):
    key = hashlib.sha256(query.encode()).hexdigest()
    cached = r.get(f"exact:{key}")
    return json.loads(cached) if cached else None

def exact_cache_set(query, response, ttl=3600):
    key = hashlib.sha256(query.encode()).hexdigest()
    r.setex(f"exact:{key}", ttl, json.dumps(response))
```

**Checkpoint:** mesma pergunta retorna resposta cacheada sem chamar o LLM.

### Passo 3 — Medir hit rate do cache exato
Rode 30 perguntas (algumas repetidas/intencionais) e meça o hit rate:

```python
hits, misses = 0, 0
for q in test_questions:
    cached = exact_cache_get(q)
    if cached:
        hits += 1
    else:
        response = agent.run(q)
        exact_cache_set(q, response)
        misses += 1
print(f"Exact cache hit rate: {hits}/{hits+misses}")
```

**Checkpoint:** hit rate do cache exato registrado (esperado: baixo, só repetições exatas).

### Passo 4 — Implementar cache semântico
Use embeddings para encontrar perguntas semanticamente similares:

```python
from openai import OpenAI
client = OpenAI()

def semantic_cache_get(query, threshold=0.92):
    query_vec = embed(query)
    # Buscar todas as queries cacheadas e comparar similaridade
    for key in r.keys("semantic:*"):
        cached = json.loads(r.get(key))
        similarity = cosine_similarity(query_vec, cached["embedding"])
        if similarity >= threshold:
            return cached["response"]
    return None

def semantic_cache_set(query, response, ttl=3600):
    key = hashlib.sha256(query.encode()).hexdigest()
    r.setex(f"semantic:{key}", ttl, json.dumps({
        "query": query, "embedding": embed(query), "response": response
    }))
```

**Checkpoint:** pergunta similar (mas não idêntica) encontra resposta no cache semântico.

### Passo 5 — Otimizar busca com Redis Vector
Para escala, use Redis com busca vetorial (RediSearch):

```python
from redis.commands.search.query import Query
from redis.commands.search.field import VectorField, TextField

# Criar índice
schema = [TextField("query"), VectorField("embedding", "FLAT",
           {"TYPE": "FLOAT32", "DIM": 1536, "DISTANCE_METRIC": "COSINE"})]
r.ft("semantic_cache").create_index(schema)

def fast_semantic_cache_get(query, threshold=0.92):
    query_vec = embed(query)
    q = Query(f"(*)=>[KNN 1 @embedding $vec AS score]") \
        .add_sort_desc("score") \
        .return_fields("query", "response", "score") \
        .dialect(2)
    results = r.ft("semantic_cache").search(q, query_params={"vec": query_vec})
    if results.docs and float(results.docs[0].score) < (1 - threshold):
        return results.docs[0].response
    return None
```

**Checkpoint:** busca vetorial no Redis retorna em <5ms para 1000 entradas.

### Passo 6 — Agente com cache integrado
Integre o cache no fluxo do agente:

```python
def cached_agent(query):
    # 1. Tentar cache semântico
    cached = fast_semantic_cache_get(query)
    if cached:
        return cached, "cache_hit"
    # 2. Executar agente normalmente
    response = agent.run(query)
    # 3. Armazenar no cache
    fast_semantic_cache_set(query, response)
    return response, "cache_miss"
```

**Checkpoint:** agente verifica cache antes de chamar o LLM.

### Passo 7 — Benchmark antes vs depois
Rode as 30 perguntas com e sem cache e compare:

| Métrica | Sem cache | Com cache exato | Com cache semântico |
|---|---|---|---|
| Latência média (ms) | | | |
| Custo total (tokens) | | | |
| Hit rate | 0% | ?% | ?% |
| Latência em cache hit (ms) | N/A | | |

**Checkpoint:** tabela preenchida em `cache_benchmark.md`.

### Passo 8 — Análise de consistência
Teste casos onde o cache semântico pode ser problemático:

1. Perguntas similares com respostas diferentes ("Qual a população de SP?" vs "Qual a área de SP?")
2. Informação que muda com o tempo ("Quem é o presidente?")
3. Perguntas com negação sutil ("O que NÃO fazer?")

```python
# Ajustar threshold ou adicionar TTL curto para dados voláteis
def smart_cache_set(query, response):
    ttl = 300 if is_volatile(query) else 3600  # 5 min vs 1 hora
    ...
```

**Checkpoint:** análise de edge cases documentada com soluções propostas.

## Desafios extras
- Adicione cache de embeddings (não recalcular embedding da mesma query)
- Implemente cache invalidation por domínio (novos dados invalidam cache de um tópico)
- Compare cache semântico vs cache de tool results
- Meça o break-even point: quantas queries para o cache pagar seu custo de infra?

## Entrega
- Repositório com `semantic_cache.py`, `cached_agent.py`, `cache_benchmark.md`
- Commit no padrão `ETHAGT14: lab-1 implementar cache semântico`

## Rubrica
Avaliado pela rubrica em `08-Assignments/ETHAGT14/assignment-01.md` (Pilar Comportamental 20%: colaboração em labs).
