---
password: Etho-Prof-2026
---
# ETHAGT14 — Gabarito

> Restrito a mentores. Cada resposta justificada com referência à apostila.

## Múltipla escolha

1. **b)** — A chamada ao LLM é tipicamente o gargalo dominante de latência em sistemas de agentes — inferência de LLM é ordens de magnitude mais lenta que queries a vector DB ou rede interna (Capítulo 1 — Onde agentes esbarram em escala).

2. **b)** — Cache semântico usa similaridade de embedding para detectar queries semanticamente equivalentes (mesmo com wording diferente), ampliado o hit rate vs. exact match (Capítulo 2.2 — Cache semântico).

3. **b)** — Model routing usa roteamento dinâmico entre modelos de diferentes capacidades (Haiku para fácil, Sonnet para difícil) para otimizar a relação custo/qualidade (Capítulo 3.1 — Roteamento por complexidade).

4. **a)** — Orçamento por execução limita o custo total de uma única execução do agente, agindo como circuit breaker financeiro que evita gastos descontrolados (Capítulo 6.1 — Orçamento por execução).

## Verdadeiro ou Falso (justificado)

1. **Falso.** Streaming reduz a latência *percebida* (o usuário vê tokens chegando mais cedo), mas a latência total (tempo até completar) não muda — o modelo ainda gera todos os tokens. É uma otimização de UX, não de throughput (Capítulo 3.4 e exercícios do syllabus).

2. **Falso.** Stateless workers escalam mais facilmente (qualquer worker atende qualquer request), mas muitos agentes são inerentemente stateful (memória de sessão, contexto acumulado). Para esses, stateful com sharding por sessão/usuário é necessário (Capítulo 4.1 — Stateless vs stateful).

3. **Verdadeiro.** Similaridade de embedding pode enganar — duas queries com alta similaridade semântica podem ter respostas diferentes (ex.: "preço do produto A" vs. "preço do produto B" são semanticamente próximas mas precisam de respostas diferentes). Threshold inadequado causa falsos positivos (Capítulo 2.3).

4. **Verdadeiro.** Sharding por tenant isola fisicamente os dados de cada cliente em shards separados, permitindo que cada tenant escale independentemente e garantindo isolamento de dados (Capítulo 4.2 — Sharding por usuário/sessão/domínio).

## Código curto

1. **Cache semântico:**
```python
def semantic_cache_lookup(query, threshold=0.95):
    query_emb = embed(query)
    result = cache_vector_db.search(query_emb, top_k=1)
    if result and result[0].score >= threshold:
        return result[0].response  # cache hit
    return None  # cache miss
```
Referência: Capítulo 2.2 (Cache semântico).

2. **Orçamento com circuit breaker:**
```python
def agent_with_budget(task, budget_usd=0.50):
    spent = 0
    while spent < budget_usd:
        response = llm(task)
        spent += estimate_cost(response)
        if is_done(response):
            return response
    raise BudgetExceeded(f"Spent ${spent:.2f}, budget ${budget_usd}")
```
Referência: Capítulo 6.1 (Orçamento por execução).

3. **Model routing:**
```python
def route_model(query):
    complexity = classify_complexity(query)  # "easy" | "hard"
    if complexity == "easy":
        return llm_haiku(query)
    return llm_sonnet(query)
```
Referência: Capítulo 3.1 (Roteamento por complexidade).

## Análise de trade-off

1. **Exact vs. semântico:** Exact match é determinístico (só retorna cache idêntico) mas tem baixo hit rate. Semântico tem hit rate maior mas pode falhar quando queries semanticamente próximas têm respostas diferentes. O semântico falha em casos onde nuances importam (IDs, nomes próprios, números) (Capítulo 2).

2. **Serverless vs. dedicado:** Serverless (Lambda, Cloud Run) brilha para tráfego esporádico, escala automática e baixo custo em baixo volume. Dedicado (Kubernetes) brilha para alto throughput, latência previsível, GPUs locais e controle fino. Escolher conforme padrão de tráfego e requisitos de latência (Capítulo 5.2).

3. **3 otimizações para reduzir custo em 40%:**
   - **Model routing:** Enviar tarefas fáceis ao Haiku (10x mais barato).
   - **Cache semântico:** Evitar recomputação de queries repetidas.
   - **Compressão de contexto:** Sumarização/eviction para reduzir tokens de entrada.
   Referência: Capítulos 2, 3 e 6.

## Debug / diagnóstico

1. **Diagnóstico:** O threshold do cache semântico está muito baixo — queries semanticamente próximas mas com respostas diferentes estão sendo servidas do cache. **Correção:** aumentar o threshold, ou adicionar validação pós-cache (verificar se a resposta cached ainda é válida para a query atual) (Capítulo 2.3).

2. **Diagnóstico:** Gargalo de contenção — todos os tenants compartilham o mesmo pool de workers ou a mesma instância de vector DB, e a carga crescente degrada a latência para todos. **Soluções:** (1) Sharding por tenant com pools independentes; (2) Read replicas para aliviar a carga de leitura no vector DB (Capítulo 4).
