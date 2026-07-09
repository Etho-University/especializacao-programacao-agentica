---
password: Etho-Prof-2026
---
# ETHAGT11 — Gabarito

> Restrito a mentores. Cada resposta justificada com referência à apostila.

## Múltipla escolha

1. **b)** — Durable execution significa que o estado do workflow persiste entre crashes, permitindo que o workflow retome exatamente do ponto de falha após recuperação (Capítulo 4 — Durable execution para agentes).

2. **b)** — No padrão Saga, a compensação desfaz ações já executadas quando uma etapa posterior falha, realizando um rollback semântico (ex.: se creditar falhar, reembolsar o débito) (Capítulo 5.3 — Compensação/saga).

3. **a)** — Exactly-once garante entrega única (sem duplicatas); at-least-once pode entregar duplicatas, exigindo idempotência no consumidor para lidar com elas (Capítulo 6.1 — Exactly-once vs at-least-once).

4. **b)** — Kafka é preferível quando se precisa de ordering por partição, alto throughput e log persistente (event sourcing). RabbitMQ é melhor para routing complexo com exchanges (Capítulo 2 — Mensageria).

## Verdadeiro ou Falso (justificado)

1. **Falso.** Event-driven é mais escalável em muitos cenários (desacoplamento, paralelismo), mas adiciona complexidade de debugging, ordering e consistência eventual. Para sistemas simples ou interativos, orquestração síncrona pode ser mais apropriada (Capítulo 1.3 — Trade-off).

2. **Verdadeiro (na prática).** Exactly-once verdadeiro é difícil de garantir end-to-end; na prática, usa-se at-least-once com idempotência. Mesmo em sistemas que alegam exactly-once, bordas podem produzir duplicatas, então idempotência é defesa essencial (Capítulo 6.1).

3. **Verdadeiro.** Backoff exponencial space as retries de forma crescente, evitando que todos os clientes tentem simultaneamente quando um serviço cai (thundering herd) e permite recuperação gradual (Capítulo 5.1 — Retries com backoff).

4. **Verdadeiro.** Temporal persiste o estado do workflow e permite replays — executar novamente o workflow passo a passo para investigar onde e por que falhou (Capítulo 4.4 — Replays e debug temporal).

## Código curto

1. **Saga compensatória:**
```python
def transfer(from_acc, to_acc, amount):
    debit(from_acc, amount)          # ação
    try:
        credit(to_acc, amount)       # ação
    except Failure:
        refund(from_acc, amount)     # compensação: desfaz débito
        raise
```
Referência: Capítulo 5.3 (Saga pattern).

2. **Retry com backoff exponencial:**
```python
import time
def retry_with_backoff(func, max_retries=3, base=1):
    for attempt in range(max_retries):
        try:
            return func()
        except Exception:
            if attempt == max_retries - 1:
                raise
            time.sleep(base * (2 ** attempt))
```
Referência: Capítulo 5.1 (Retries com backoff).

3. **Circuit breaker:**
```python
class CircuitBreaker:
    def __init__(self, threshold=5, timeout=60):
        self.threshold = threshold
        self.timeout = timeout
        self.failures = 0
        self.open_until = 0

    def call(self, func):
        if time.time() < self.open_until:
            raise Exception("Circuit open")
        try:
            result = func()
            self.failures = 0
            return result
        except Exception:
            self.failures += 1
            if self.failures >= self.threshold:
                self.open_until = time.time() + self.timeout
            raise
```
Referência: Capítulo 5.4 (Circuit breakers).

## Análise de trade-off

1. **Temporal vs. Kafka puro:** Temporal vale a pena para orquestração de agentes de longa duração que precisam de durable execution, retries, compensação e replays. Kafka puro é infraestrutura de mensageria — exige construir a orquestração por cima. Temporal abstrai isso (Capítulo 3 e 4).

2. **At-least-once + idempotência vs. exactly-once:** At-least-once com idempotência é mais simples de implementar e suficiente para a maioria dos casos (a idempotência absorve duplicatas). Exactly-once é mais complexo e nem sempre necessário — só vale quando o custo da idempotência é proibitivo (Capítulo 6.1).

3. **Código (Temporal/Prefect) vs. agente supervisor:** Código é melhor quando o fluxo é determinístico e conhecido (previsibilidade). Agente supervisor é melhor quando o fluxo precisa de decisão dinâmica do LLM a cada etapa. Híbrido é comum: orquestração determinística com agentes em pontos de decisão (Capítulo 3.4).

## Debug / diagnóstico

1. **Diagnóstico:** Falta de idempotência — o consumidor processa cada mensagem sem verificar se já foi processada. **Correção:** adicionar chave de idempotência (message_id ou request_id) e verificar/deduplicar antes de executar a ação (Capítulo 5.2).

2. **Causas de não retomar:**
   - **Worker não reiniciou:** O processo do worker morreu e não foi reiniciado pelo orquestrador. Verificar restart policy.
   - **Activity com side-effect não determinístico:** Um activity não é replay-safe (ex.: usa timestamp atual). Temporal não consegue replay corretamente. Correção: usar APIs determinísticas do Temporal (Capítulo 4.3).
