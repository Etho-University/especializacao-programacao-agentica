# ETHAGT14 — Exercícios

> Exercícios para aula e para casa.
> Organizados por tipo: em aula, individual, em duplas, projeto.

---

## Exercícios em Aula

### E1 — Quando Cache Semântico Falha (Votação Rápida)
**Slide**: 29
**Tempo**: 2 min
**Formato**: Individual, votação de mão levantada

**Enunciado**: Para cada cenário abaixo, vote: cache semântico FUNCIONA (F) ou FALHA (X)?

1. "Preço das ações da Apple hoje"
2. "Qual a capital da França?"
3. "Resuma o último email recebido"
4. "Como fazer um loop em Python?"
5. "Qual a previsão do tempo amanhã?"

**Gabarito**:
1. **X** (temporal — preço muda)
2. **F** (estável — geografia não muda)
3. **X** (contextual — depende do email)
4. **F** (estável — conceito de programação)
5. **X** (temporal — previsão muda)

**Lição**: Cache semântico funciona para conhecimento ESTÁVEL. Falha para TEMPORAL (preço, previsão) ou CONTEXTUAL (último email, histórico pessoal).

---

### E2 — Threshold Ideal (Discussão em Duplas)
**Slide**: 20
**Tempo**: 2 min
**Formato**: Duplas, 2 min discussão

**Enunciado**: Discutam em duplas:
1. Em que tipo de sistema você usaria threshold baixo (0.80)?
2. Em que tipo de sistema você usaria threshold alto (0.95)?
3. Dê um exemplo de cada.

**Gabarito**:
1. **Threshold baixo (0.80)**: FAQs gerais, conhecimento estável, baixo risco de falso positivo (e.g., "como reiniciar servidor"). Hit rate alto, erros toleráveis.
2. **Threshold alto (0.95)**: Dados numéricos/sensíveis, dados pessoais, preços. Hit rate menor mas falsos positivos seriam graves (e.g., "preço do iPhone 15" vs "preço do iPhone 14").

---

### E3 — Qual Modelo para Qual Tarefa (Votação)
**Slide**: 38
**Tempo**: 2 min
**Formato**: Individual, votação

**Enunciado**: Para cada tarefa, vote: Haiku (H), Sonnet (S) ou Opus (O)?

1. "Classificar este ticket como bug/feature/question"
2. "Resolver este bug complexo de concorrência"
3. "Resumir este documento de 5 páginas"
4. "Planejar arquitetura de sistema multi-agente"
5. "Extrair entidades deste email"
6. "Decidir qual tool chamar e por quê"

**Gabarito**:
1. **H** (classificação direta, estruturada)
2. **O** (raciocínio profundo sobre concorrência)
3. **H** (sumarização, tarefa bem definida)
4. **O** (arquitetura complexa, multi-step)
5. **H** (extração estruturada)
6. **S** (decisão com tools, raciocínio moderado)

**Lição**: A maioria das tarefas é Haiku. Use Opus com parcimônia.

---

### E4 — Stateless é Sempre Preferível? (Duplas)
**Slide**: 47
**Tempo**: 2 min
**Formato**: Duplas, 2 min discussão

**Enunciado**: Discutam em duplas:
1. "Stateless é sempre preferível? Justifique."
2. Pensem em um caso onde stateful é claramente melhor.
3. Como você tornaria um agente stateful mais "stateless-friendly"?

**Gabarito**:
1. **Falso**. Há casos legítimos para stateful.
2. **Casos stateful**: sessões longas com contexto acumulado (manter em memória evita re-buscar a cada request), WebSockets/streaming (conexão persistente), caches em memória para baixa latência (<5ms vs 50ms do Redis).
3. **Stateless-friendly**: checkpoint externo (Redis/Postgres) + restore on-demand. Se a réplica cai, outra pode restaurar o estado e continuar.

---

### E5 — Circuit Breaker de Custo (Duplas)
**Slide**: 62
**Tempo**: 4 min (3 código + 2 compartilhar)
**Formato**: Duplas, código

**Enunciado**: Cenário: sistema multi-tenant com orçamento de R$100/usuário/mês.

Em duplas, escrevam a lógica de um circuit breaker que:
1. Verifica o custo acumulado do mês para o usuário antes de cada chamada de LLM
2. Bloqueia a execução se o custo + custo estimado da próxima chamada exceder o orçamento
3. Emite exceção amigável para o usuário
4. Loga + alerta para monitoramento

**Bônus**: O que acontece se o orçamento for compartilhado entre features (chat, RAG, code)?

**Exemplo de resposta**:
```python
class CostCircuitBreaker:
    def __init__(self, budget_per_user_month: float, redis_client):
        self.budget = budget_per_user_month
        self.redis = redis_client

    def check(self, user_id: str, estimated_cost: float):
        key = f"cost:user:{user_id}:month"
        current = float(self.redis.get(key) or 0)
        if current + estimated_cost > self.budget:
            self._alert(user_id, current, estimated_cost)
            raise BudgetExceededError(
                f"Orçamento mensal de R${self.budget} excedido para este usuário. "
                f"Consumido: R${current:.2f}. Tente novamente próximo mês."
            )

    def add(self, user_id: str, actual_cost: float):
        key = f"cost:user:{user_id}:month"
        self.redis.incrbyfloat(key, actual_cost)

    def _alert(self, user_id, current, estimated):
        logger.warning(f"Budget exceeded: user={user_id}, current={current}, attempted={estimated}")
        send_slack_alert(f"User {user_id} hit monthly budget")
```

**Bônus (orçamento compartilhado)**: Use pesos por feature (chat=1x, RAG=2x, code=3x) ou segregue orçamento por feature (chat R$40, RAG R$30, code R$30).

---

## Exercícios Individuais (para casa)

### E6 — Cálculo de Custo em Escala
**Tempo estimado**: 15 min
**Formato**: Individual, cálculo

**Enunciado**: Um agente tem as seguintes características:
- Custo médio por execução: R$0,08
- Passos médios por execução: 5
- Tokens por step: 2.000 input + 500 output
- Usuários ativos: 500
- Consultas por usuário/dia: 8

Calcule:
1. Custo por step
2. Custo por execução
3. Custo diário total
4. Custo mensal total
5. Com 60% de redução via caching + routing, qual o novo custo mensal?

**Gabarito**:
1. R$0,08 / 5 = R$0,016/step
2. R$0,08/execução (dado)
3. R$0,08 × 500 × 8 = R$320/dia
4. R$320 × 30 = R$9.600/mês
5. R$9.600 × 0,40 = R$3.840/mês (economia de R$5.760/mês)

---

### E7 — Estratégia de Cache em Camadas
**Tempo estimado**: 20 min
**Formato**: Individual, diagrama + texto

**Enunciado**: Desenhe (em texto ou ASCII) uma arquitetura de cache em 3 camadas (L1/L2/L3) para um agente de suporte corporativo. Para cada camada:
1. Onde reside (memória local, Redis compartilhado, provider-side)
2. Latência esperada
3. TTL recomendado
4. Tipo de invalidação

**Exemplo de resposta**:
- **L1 — Memória local (por pod)**: latência ~1ms, TTL 5min, invalidação por restart do pod. Cacheia respostas frequentes dentro de uma sessão.
- **L2 — Redis compartilhado**: latência ~5ms, TTL 30min, invalidação por TTL + event-driven (doc atualizada → invalida). Cacheia respostas entre pods e sessões.
- **L3 — Prompt caching do provider (Anthropic)**: latência ~50ms (mas reduz custo de processamento), TTL gerenciado pelo provider. Cacheia prefixo (system prompt + tools).

---

### E8 — Plano de Otimização
**Tempo estimado**: 30 min
**Formato**: Individual, documento

**Enunciado**: Você é responsável por um agente em produção com as características:
- 2.000 usuários ativos
- Custo mensal atual: R$20.000
- Latência p95: 15s
- Taxa de erro: 4%
- Sem caching, sem routing, sempre Sonnet

Escreva um plano de otimização em 4 semanas para reduzir custo em ≥40% sem perder qualidade. Estruture:
1. Ordem de implementação (técnica por semana)
2. Impacto esperado por técnica
3. Métricas para validar
4. Riscos e mitigações

**Exemplo de resposta**:

| Semana | Técnica | Impacto Esperado | Métrica |
|---|---|---|---|
| 1 | Cache semântico (threshold 0.92, Redis) | −30% custo, −40% latência | cache hit rate ≥50% |
| 2 | Model routing (Haiku para 70%) | −25% custo adicional | % queries em Haiku ≥65% |
| 3 | Batching de embeddings + tool results | −10% latência adicional | latência p95 <8s |
| 4 | FinOps (circuit breaker + dashboard) | Sustentabilidade | alertas configurados, orçamento por usuário |

**Total esperado**: −55% custo (R$20k → R$9k), −65% latência (15s → 5s), erro mantido em ~4%.

**Riscos**: Cache stale (mitigação: TTL por categoria), routing errado (mitigação: cascata Haiku→Sonnet), resistência da equipe (mitigação: ADR documentado).

---

### E9 — Verdadeiro/Falso Justificado
**Tempo estimado**: 15 min
**Formato**: Individual, escrito

**Enunciado**: Responda V ou F e justifique em 2-3 frases:

1. "Cache semântico substitui completamente o exact match."
2. "Streaming reduz a latência total de uma resposta."
3. "Stateless é sempre preferível a stateful."
4. "Caching de tool results deve ser aplicado a todas as tools."
5. "Orçamento só precisa ser agregado mensal."

**Gabarito**:
1. **F** — São complementares. Exact match captura prompts idênticos (mais rápido, sem custo de embedding). Cache semântico captura variações linguísticas. Use ambos em camadas.
2. **F** — Streaming reduz a latência PERCEBIDA (usuário vê tokens em 500ms), mas a latência TOTAL é a mesma — o LLM ainda gera os mesmos tokens no mesmo tempo.
3. **F** — Há casos legítimos para stateful: sessões longas com contexto acumulado, WebSockets, caches em memória para baixa latência. Solução híbrida (stateless-friendly com checkpoint externo) é geralmente ideal.
4. **F** — Só tools idempotentes (GET, search) devem ser cacheadas. Tools que mutam estado (POST, PUT, DELETE) nunca devem ser cacheadas — causaria bugs sutis.
5. **F** — Orçamento agregado mensal descobre o estouro tarde demais. Precisa de orçamento por execução (para parar loops em tempo real) e por usuário/tenant (para conter abuso individual).

---

## Projeto do Módulo

### P1 — Otimização de Custo/Latência em Sistema Existente
**Prazo**: 2 semanas
**Formato**: Individual ou em duplas
**Carga**: ~10h

**Descrição**: Otimizar custo/latência de um sistema agêntico existente em **≥40%** sem perder qualidade mensurável.

**Requisitos**:
1. Escolher um sistema agêntico existente (próprio, open-source, ou fornecido pelo professor)
2. Medir baseline (antes): custo por execução, latência p95, success rate
3. Aplicar otimizações (mínimo 3 técnicas da aula)
4. Medir resultado (depois)
5. Validar que qualidade foi mantida (success rate ±2%)

**Entregáveis**:
- **Before/After**: tabelas com métricas (custo, latência, success rate)
- **ADR (Architecture Decision Record)**: documento justificando cada otimização (contexto, decisão, consequências)
- **FinOps Dashboard**: mockup ou implementação (Grafana, Streamlit, etc.) mostrando custo por feature/tenant/modelo
- **Demo**: gravação ou apresentação ao vivo do sistema otimizado

**Técnicas aplicáveis (mínimo 3)**:
- Cache semântico
- Model routing
- Batching de requests
- Streaming (para latência percebida)
- Sharding por tenant
- Circuit breaker de custo
- Otimização de prompt (reduzir contexto)

**Critério de sucesso**:
- Redução de custo ≥40% **OU** latência ≥40%
- Success rate mantido (±2%)
- ADR claro e justificado
- Dashboard funcional ou mockup detalhado

**Avaliação** (rubrica de 4 pilares):

| Pilar | Peso | Critério |
|---|---|---|
| Técnico | 40% | Otimizações implementadas, before/after mensurado, qualidade mantida |
| Consultivo | 30% | ADR claro, justificativa de trade-offs, defesa para "CTO" |
| Comportamental | 20% | Code review de um colega |
| Prático | 10% | Demo: antes/depois ao vivo ou em vídeo |

**Nota mínima de aprovação**: 3.0
