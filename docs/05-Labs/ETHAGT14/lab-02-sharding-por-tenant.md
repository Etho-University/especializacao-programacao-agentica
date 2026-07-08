# ETHAGT14 — Lab 2: Sharding por tenant

> Curso: Escalabilidade & Sistemas Distribuídos de Agentes · Carga: 30h · Pré-req: ETHAGT14 Lab 1

## Objetivo
Distribuir um agente multi-tenant usando sharding por tenant, garantindo isolamento de dados, memória e estado entre tenants, e medir o throughput sob carga concorrente.

## Preparação
- Ambiente: Python 3.11+, `pip install redis openai`, Docker
- Dados/recursos: 5 tenants simulados (tenant-001 a tenant-005), cada um com dados próprios
- Leitura prévia: Apostila ETHAGT14, Unidade 4 (Distribuição) e Unidade 6 (FinOps)

## Roteiro
### Passo 1 — Modelar multi-tenancy
Defina o modelo de isolamento por tenant:

```python
@dataclass
class TenantConfig:
    tenant_id: str
    redis_db: int        # DB isolado no Redis
    vector_collection: str  # Collection isolada no Qdrant
    model: str           # Modelo alocado (mini para free, full para paid)
    rate_limit: int      # Requests/min
    budget_usd: float    # Orçamento mensal

TENANTS = {
    "tenant-001": TenantConfig("tenant-001", redis_db=1, vector_collection="t001",
                               model="gpt-4o-mini", rate_limit=10, budget_usd=100),
    "tenant-002": TenantConfig("tenant-002", redis_db=2, vector_collection="t002",
                               model="gpt-4o", rate_limit=30, budget_usd=500),
    # ... 3 tenants a mais
}
```

**Checkpoint:** 5 tenants configurados com isolamento de recursos.

### Passo 2 — Sharding de memória
Cada tenant tem seu próprio espaço de memória (Redis DB ou prefix):

```python
class TenantMemoryStore:
    def __init__(self, tenant_id):
        self.tenant = TENANTS[tenant_id]
        self.redis = redis.Redis(host="localhost", port=6379,
                                 db=self.tenant.redis_db, decode_responses=True)

    def get(self, key):
        return self.redis.get(f"mem:{key}")

    def set(self, key, value, ttl=3600):
        self.redis.setex(f"mem:{key}", ttl, value)
```

**Checkpoint:** tenant-001 não consegue ler dados do tenant-002 (DBs diferentes).

### Passo 3 — Sharding de vector store
Cada tenant tem sua própria collection no Qdrant:

```python
from qdrant_client import QdrantClient

class TenantVectorStore:
    def __init__(self, tenant_id):
        self.client = QdrantClient("localhost", port=6333)
        self.collection = TENANTS[tenant_id].vector_collection
        # Garantir que a collection existe
        try:
            self.client.create_collection(self.collection,
                vectors_config={"size": 1536, "distance": "Cosine"})
        except:
            pass  # já existe

    def search(self, query_vec, limit=5):
        return self.client.search(self.collection, query_vec=query_vec, limit=limit)
```

**Checkpoint:** busca no tenant-001 não retorna documentos do tenant-002.

### Passo 4 — Rate limiting e budget por tenant
Implemente controle de uso:

```python
from time import time

class TenantGovernor:
    def __init__(self, tenant_id):
        self.tenant = TENANTS[tenant_id]
        self.usage_file = f"usage_{tenant_id}.json"

    def check_rate_limit(self):
        now = time()
        recent = load_recent_calls(self.usage_file, window=60)
        if len(recent) >= self.tenant.rate_limit:
            raise RateLimitError(f"Tenant {self.tenant.tenant_id} rate limited")

    def check_budget(self, cost):
        spent = load_total_spent(self.usage_file)
        if spent + cost > self.tenant.budget_usd:
            raise BudgetExceededError(f"Tenant {self.tenant.tenant_id} budget exceeded")

    def record_usage(self, cost):
        record_call(self.usage_file, cost=cost, timestamp=time())
```

**Checkpoint:** 11ª chamada em 1 minuto para tenant-001 (rate_limit=10) é rejeitada.

### Passo 5 — O agente multi-tenant
Combine tudo em um agente que respeita o isolamento:

```python
class MultiTenantAgent:
    def run(self, tenant_id, query):
        config = TENANTS[tenant_id]
        governor = TenantGovernor(tenant_id)
        memory = TenantMemoryStore(tenant_id)
        vectors = TenantVectorStore(tenant_id)

        # 1. Rate limit + budget check
        governor.check_rate_limit()
        governor.check_budget(estimated_cost)

        # 2. Retrieval isolado
        query_vec = embed(query)
        docs = vectors.search(query_vec)

        # 3. LLM call com modelo do tenant
        response = call_llm(f"Context: {docs}\nQ: {query}",
                           model=config.model)

        # 4. Registrar uso
        governor.record_usage(calculate_cost(response))
        return response
```

**Checkpoint:** agente usa recursos isolados por tenant e respeita limites.

### Passo 6 — Teste de isolamento
Verifique que não há vazamento entre tenants:

```python
# tenant-001 armazena documento secreto
agent.run("tenant-001", "Remember: my secret code is 1234")

# tenant-002 tenta acessar
result = agent.run("tenant-002", "What is the secret code?")
# NÃO deve conter "1234"
assert "1234" not in result
```

**Checkpoint:** teste de isolamento passa — nenhum vazamento entre tenants.

### Passo 7 — Benchmark de concorrência
Simule carga concorrente de múltiplos tenants:

```python
import asyncio

async def simulate_tenant_load(tenant_id, n_requests=20):
    for i in range(n_requests):
        agent.run(tenant_id, f"Question {i} from {tenant_id}")

async def main():
    # 5 tenants, 20 requests cada, em paralelo
    await asyncio.gather(*[
        simulate_tenant_load(tid) for tid in TENANTS
    ])
```

Meça throughput e latência:

| Métrica | Valor |
|---|---|
| Requests totais | 100 |
| Throughput (req/s) | |
| Latência p50 (ms) | |
| Latência p95 (ms) | |
| Rate limits acionados | |
| Budgets excedidos | |

**Checkpoint:** benchmark executado e métricas registradas.

### Passo 8 — FinOps dashboard
Crie um relatório de uso por tenant:

```markdown
## FinOps Report — Multi-Tenant Agent

| Tenant | Requests | Tokens | Custo (USD) | % do Budget |
|---|---|---|---|---|
| tenant-001 | | | | |
| tenant-002 | | | | |
| tenant-003 | | | | |
| tenant-004 | | | | |
| tenant-005 | | | | |
| **Total** | | | | |
```

**Checkpoint:** relatório FinOps em `finops_report.md`.

## Desafios extras
- Implemente auto-scaling: adicionar workers quando throughput cai
- Adicione cache semântico (Lab 1) por tenant e meça economia
- Implemente tier migration: tenant que excede rate limit é upgradado para tier maior
- Compare sharding por DB Redis vs sharding por prefix (trade-offs)

## Entrega
- Repositório com `multi_tenant_agent.py`, `benchmark_results.md`, `finops_report.md`
- Commit no padrão `ETHAGT14: lab-2 implementar sharding por tenant`

## Rubrica
Avaliado pela rubrica em `08-Assignments/ETHAGT14/assignment-01.md` (Pilar Comportamental 20%: colaboração em labs).
