# ETHAGT11 — Lab 1: Agente com Kafka

> Curso: Event-Driven Agents & Workflow Orchestration · Carga: 25h · Pré-req: ETHAGT10

## Objetivo
Implementar dois agentes que se coordenam exclusivamente via tópicos Kafka, com ordering por chave, e demonstrar desacoplamento assíncrono entre produtores e consumidores.

## Preparação
- Ambiente: Python 3.11+, `pip install aiokafka`, Docker + Docker Compose
- Dados/recursos: `docker-compose.yml` com Kafka + Zookeeper
- Leitura prévia: Apostila ETHAGT11, Unidade 2 (Mensageria)

## Roteiro
### Passo 1 — Subir o Kafka
Crie `docker-compose.yml`:

```yaml
services:
  kafka:
    image: bitnami/kafka:3.7
    ports:
      - "9092:9092"
    environment:
      KAFKA_CFG_NODE_ID: 1
      KAFKA_CFG_PROCESS_ROLES: controller,broker
      KAFKA_CFG_LISTENERS: PLAINTEXT://:9092
      KAFKA_CFG_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092
      KAFKA_CFG_CONTROLLER_QUORUM_VOTERS: 1@localhost:9093
      KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP: CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT
      KAFKA_CFG_CONTROLLER_LISTENER_NAMES: CONTROLLER
      KAFKA_KRAFT_CLUSTER_ID: "$(random)"
```

```bash
docker compose up -d
```

**Checkpoint:** Kafka acessível em `localhost:9092`; tópicos podem ser criados.

### Passo 2 — Criar os tópicos
Defina os tópicos de comunicação entre agentes:

```python
TOPICS = {
    "analysis-requests": "Agente A → Agente B: pedidos de análise",
    "analysis-results": "Agente B → Agente A: resultados de análise",
    "errors": "Qualquer agente → monitor: erros"
}
```

**Checkpoint:** 3 tópicos criados via admin client ou CLI.

### Passo 3 — Definir o schema de mensagem
Modele a mensagem com versionamento:

```python
from pydantic import BaseModel
from datetime import datetime
import uuid

class AgentMessage(BaseModel):
    id: str = str(uuid.uuid4())
    version: str = "1.0"
    timestamp: datetime
    source: str  # agent name
    target: str  # agent name or "broadcast"
    type: str    # "request", "result", "error"
    payload: dict
    correlation_id: str  # para rastrear requisição/resposta
```

**Checkpoint:** schema serializa/deserializa em JSON corretamente.

### Passo 4 — Agente A: produtor
Implemente o Agente A que publica pedidos de análise:

```python
from aiokafka import AIOKafkaProducer
import asyncio, json

async def agent_a():
    producer = AIOKafkaProducer(bootstrap_servers="localhost:9092")
    await producer.start()
    try:
        for task in tasks:
            msg = AgentMessage(timestamp=datetime.now(), source="agent_a",
                             target="agent_b", type="request",
                             payload={"question": task},
                             correlation_id=str(uuid.uuid4()))
            # Key = correlation_id para garantir ordering por chave
            await producer.send_and_wait("analysis-requests",
                key=msg.correlation_id.encode(),
                value=msg.model_dump_json().encode())
    finally:
        await producer.stop()
```

**Checkpoint:** Agente A publica mensagens no tópico `analysis-requests`.

### Passo 5 — Agente B: consumidor + produtor
Implemente o Agente B que consome, processa e publica resultados:

```python
async def agent_b():
    consumer = AIOKafkaConsumer("analysis-requests",
        bootstrap_servers="localhost:9092", group_id="agent-b")
    producer = AIOKafkaProducer(bootstrap_servers="localhost:9092")
    await consumer.start()
    await producer.start()
    try:
        async for record in consumer:
            msg = AgentMessage(**json.loads(record.value))
            # Processar com LLM
            result = call_llm(msg.payload["question"])
            # Publicar resposta
            reply = AgentMessage(timestamp=datetime.now(), source="agent_b",
                               target="agent_a", type="result",
                               payload={"answer": result},
                               correlation_id=msg.correlation_id)
            await producer.send_and_wait("analysis-results",
                key=reply.correlation_id.encode(),
                value=reply.model_dump_json().encode())
    finally:
        await consumer.stop()
        await producer.stop()
```

**Checkpoint:** Agente B consome, processa e publica resultados de volta.

### Passo 6 — Validar ordering por chave
Envie 5 mensagens com a mesma correlation_id e verifique que chegam em ordem:

```python
# Todas com mesma key (correlation_id)
for i in range(5):
    await producer.send("analysis-requests",
        key=b"same-key", value=f"msg-{i}".encode())
```

**Checkpoint:** consumidor recebe msg-0, msg-1, msg-2... em ordem.

### Passo 7 — Tratar falhas
Adicione error handling: se o LLM falha, publique no tópico de erros:

```python
try:
    result = call_llm(msg.payload["question"])
except Exception as e:
    error_msg = AgentMessage(timestamp=datetime.now(), source="agent_b",
                           target="monitor", type="error",
                           payload={"error": str(e), "original": msg.model_dump()},
                           correlation_id=msg.correlation_id)
    await producer.send_and_wait("errors",
        value=error_msg.model_dump_json().encode())
```

**Checkpoint:** erro no LLM produz mensagem no tópico `errors`.

### Passo 8 — Análise do desacoplamento
Documente as propriedades do sistema event-driven:

```markdown
## Propriedades observadas
- **Desacoplamento temporal**: Agente A não espera Agente B responder
- **Escalabilidade**: múltiplas instâncias de B no mesmo group_id
- **Resiliência**: se B cai, mensagens ficam no Kafka até serem consumidas
- **Ordering**: garantida por partition key (correlation_id)

## Trade-offs
- Complexidade de debugging aumentou
- Latência adicional do Kafka
- Infraestrutura extra
```

**Checkpoint:** análise em `event_driven_analysis.md`.

## Desafios extras
- Adicione um 3º agente (Agente C) que consome `analysis-results` e agrega estatísticas
- Implemente exactly-once semantics com transações Kafka
- Adicione dead letter queue para mensagens que falham após N retries
- Compare Kafka com NATS usando o mesmo cenário

## Entrega
- Repositório com `docker-compose.yml`, `agent_a.py`, `agent_b.py`, `event_driven_analysis.md`
- Commit no padrão `ETHAGT11: lab-1 implementar agentes com kafka`

## Rubrica
Avaliado pela rubrica em `08-Assignments/ETHAGT11/assignment-01.md` (Pilar Comportamental 20%: colaboração em labs).
