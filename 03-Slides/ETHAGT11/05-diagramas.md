# ETHAGT11 — Sugestões de Diagramas

> 24 diagramas referenciados no storyboard.
> 3 já existem em `12-Diagrams/ETHAGT11/`. 21 novos a produzir.

---

## Diagramas Existentes (3)

| # | Slide | Arquivo | Descrição |
|---|---|---|---|
| D1 | 9 | `event-driven.mmd` | Pipeline event-driven: producer → Kafka topics → consumers (agentes OCR, validate, index) → vector DB + DLQ |
| D17/D18 | 24, 51, 52 | `saga.mmd` | Saga pattern: iniciar → debitar → creditar → sucesso; falha em creditar → compensar (estornar) |
| D12/D14 | 31, 38 | `durable-execution.mmd` | Durable execution: workflow com activities, checkpoints, HITL via signal, recovery após crash |

---

## Diagramas Novos (21)

### D2 — O Log Imutável (Slide 15)

**Tipo**: Flowchart horizontal
**Descrição**: Log append-only com offsets (0, 1, 2, 3...) e múltiplos consumers lendo em posições diferentes
**Mermaid**:
```mermaid
flowchart LR
    subgraph Log["Log Imutável (append-only)"]
        direction LR
        O0["offset 0"]
        O1["offset 1"]
        O2["offset 2"]
        O3["offset 3"]
        O4["offset 4"]
        O0 --- O1 --- O2 --- O3 --- O4
    end
    P[Producer] -->|append| O4
    C1["Consumer A<br/>offset=2"] -.lê.- O1
    C2["Consumer B<br/>offset=4"] -.lê.- O3
```
**Estilo**: Log em `etho-accent`; consumers em cores diferentes.

---

### D3 — Kafka: Arquitetura (Slide 16)

**Tipo**: Flowchart
**Descrição**: Topic com 3 partições, cada partição é um log; producers e consumer group
**Mermaid**:
```mermaid
flowchart TB
    P1[Producer] --> T["Topic: agent-tasks"]
    P2[Producer] --> T
    T --> P0["Partition 0<br/>(log)"]
    T --> P1p["Partition 1<br/>(log)"]
    T --> P2p["Partition 2<br/>(log)"]
    P0 --> C1[Consumer 1]
    P1p --> C2[Consumer 2]
    P2p --> C3[Consumer 3]
    C1 --- CG["Consumer Group"]
    C2 --- CG
    C3 --- CG
```

---

### D4 — Kafka: Particionamento e Ordering por Chave (Slide 17)

**Tipo**: Diagrama de chaves
**Descrição**: 3 partições com mensagens coloridas por agent_id (mesma cor = mesma partição)
**Mermaid**:
```mermaid
flowchart LR
    subgraph Part0["Partition 0"]
        A1["agent_1: msg"]
        A1b["agent_1: msg"]
    end
    subgraph Part1["Partition 1"]
        A2["agent_2: msg"]
        A2b["agent_2: msg"]
    end
    subgraph Part2["Partition 2"]
        A3["agent_3: msg"]
        A3b["agent_3: msg"]
    end
    H["hash(agent_id) % 3"] --> Part0
    H --> Part1
    H --> Part2
```
**Estilo**: Mesmo agent_id em mesma cor (azul, verde, laranja).

---

### D5 — Kafka: Consumer Groups e Escala Horizontal (Slide 18)

**Tipo**: Diagrama de atribuição
**Descrição**: 3 partições → 3 consumers em um group, com setas de atribuição
**Mermaid**:
```mermaid
flowchart LR
    P0["Partition 0"] --> C1["Consumer 1"]
    P1["Partition 1"] --> C2["Consumer 2"]
    P2["Partition 2"] --> C3["Consumer 3"]
    subgraph CG["Consumer Group 'processors'"]
        C1
        C2
        C3
    end
```

---

### D6 — RabbitMQ: Exchanges, Bindings, Queues (Slide 19)

**Tipo**: Flowchart AMQP
**Descrição**: Exchange → bindings → múltiplas queues → consumers
**Mermaid**:
```mermaid
flowchart LR
    P[Producer] --> EX["Exchange<br/>(topic)"]
    EX -->|routing_key: agent.*| Q1["Queue: agent_tasks"]
    EX -->|routing_key: validation.*| Q2["Queue: validation"]
    EX -->|routing_key: *.error| Q3["Queue: errors"]
    Q1 --> C1[Consumer A]
    Q2 --> C2[Consumer B]
    Q3 --> C3[Consumer C]
    Q1 -.falhas.- DLQ["Dead Letter<br/>Exchange"]
```

---

### D7 — Comparação Kafka vs RabbitMQ vs NATS (Slide 21)

**Tipo**: Tabela 3 colunas
**Descrição**: Tabela comparativa colorida nos eixos principais
**Mermaid**:
```mermaid
flowchart LR
    subgraph Kafka["Kafka"]
        K1["Modelo: Log"]
        K2["Ordering: por partição"]
        K3["Throughput: altíssimo"]
    end
    subgraph Rabbit["RabbitMQ"]
        R1["Modelo: Filas (AMQP)"]
        R2["Ordering: por fila"]
        R3["Throughput: médio"]
    end
    subgraph NATS["NATS"]
        N1["Modelo: Stream"]
        N2["Ordering: por stream"]
        N3["Throughput: alto"]
    end
```

---

### D8 — CQRS (Slide 23)

**Tipo**: Flowchart
**Descrição**: Command → event store → read model → query
**Mermaid**:
```mermaid
flowchart LR
    Cmd[Command] --> WS["Write Side<br/>(commands)"]
    WS --> ES[("Event Store")]
    ES --> RS["Read Side<br/>(queries)"]
    RS --> VM["Views Materializadas"]
    VM --> Q[Query]
```

---

### D9 — CloudEvent (JSON Exemplo) (Slide 25)

**Tipo**: Code block
**Descrição**: JSON de um CloudEvent com campos destacados
**Mermaid**:
```json
{
  "specversion": "1.0",
  "id": "evt-12345",
  "source": "/agents/extractor",
  "type": "com.etho.document.extracted",
  "time": "2026-07-07T10:30:00Z",
  "subject": "doc-67890",
  "data": {
    "document_id": "doc-67890",
    "fields": {"name": "João", "value": 1500}
  }
}
```

---

### D10 — Temporal: Arquitetura (Slide 30)

**Tipo**: Flowchart
**Descrição**: Client → Server → Task Queue → Worker
**Mermaid**:
```mermaid
flowchart LR
    Client["Temporal Client<br/>(start workflow)"] --> TS["Temporal Server<br/>(persiste histórico)"]
    TS --> TQ["Task Queue"]
    TQ --> W1["Worker 1"]
    TQ --> W2["Worker 2"]
    W1 -->|executa activity| TS
    W2 -->|executa activity| TS
```

---

### D11 — Comparação Temporal vs Prefect vs Airflow (Slide 35)

**Tipo**: Tabela
**Descrição**: Comparação nos eixos: durable execution, HITL, timers, replay, agendamento
**Mermaid**:
```mermaid
flowchart LR
    subgraph Temporal["Temporal"]
        T1["Durability: Máximo"]
        T2["HITL: Nativo"]
        T3["Replay: Sim"]
    end
    subgraph Prefect["Prefect"]
        P1["Durability: Médio"]
        P2["HITL: Limitado"]
        P3["Replay: Limitado"]
    end
    subgraph Airflow["Airflow"]
        A1["Durability: Baixo"]
        A2["HITL: Não"]
        A3["Replay: Não"]
    end
```

---

### D13 — HITL via Timers e Signals (Slide 40)

**Tipo**: Sequência
**Descrição**: Workflow → pause (await signal) → humano aprova → resume; com timeout
**Mermaid**:
```mermaid
sequenceDiagram
    participant WF as Workflow
    participant H as Humano
    participant T as Timer (24h)
    WF->>WF: Activity: agente gera email
    WF->>H: await signal (aprovado/rejeitado)
    WF->>T: iniciar timeout 24h
    alt Humano aprova
        H-->>WF: signal: aprovado
        WF->>WF: Activity: enviar email
    else Humano rejeita
        H-->>WF: signal: rejeitado
        WF->>WF: Activity: voltar ao agente
    else Timeout
        T-->>WF: timeout expirado
        WF->>WF: Activity: escalar para gerente
    end
```

---

### D15 — Non-Determinism Quebrando Replay (Slide 42)

**Tipo**: Comparação
**Descrição**: Replay quebrado (non-determinism) vs replay correto
**Mermaid**:
```mermaid
flowchart TB
    subgraph Broken["✗ Replay Quebrado"]
        B1["Workflow usa datetime.now()"]
        B2["Replay gera timestamp diferente"]
        B3["Sequência diverge do histórico"]
        B4["❌ Replay falha"]
        B1 --> B2 --> B3 --> B4
    end
    subgraph Correct["✓ Replay Correto"]
        C1["Workflow usa workflow.now()"]
        C2["Replay usa valor do histórico"]
        C3["Sequência coincide"]
        C4["✅ Replay funciona"]
        C1 --> C2 --> C3 --> C4
    end
```

---

### D16 — Determinismo: Código Correto vs Quebrado (Slide 43)

**Tipo**: Code comparison
**Descrição**: Dois snippets lado a lado
**Mermaid**:
```python
# ✗ Quebrado (non-determinístico)
@workflow
async def bad_workflow():
    now = datetime.now()      # NON-DETERMINISTIC
    time.sleep(5)              # BLOQUEIA, não é durable
    result = requests.get(...)  # I/O direto no workflow
```

```python
# ✓ Correto (determinístico)
@workflow
async def good_workflow():
    now = workflow.now()       # DETERMINISTIC (seeded)
    await workflow.sleep(5)    # Durable, não bloqueia
    result = await workflow.execute_activity(
        fetch_data             # I/O vai em activity
    )
```

---

### D19 — Circuit Breaker (State Machine) (Slide 53)

**Tipo**: State diagram
**Descrição**: Estados Closed → Open → Half-Open → Closed/Open
**Mermaid**:
```mermaid
stateDiagram-v2
    [*] --> Closed
    Closed --> Open: N falhas consecutivas
    Open --> HalfOpen: timeout expira
    HalfOpen --> Closed: sucesso na tentativa
    HalfOpen --> Open: falha na tentativa
```

---

### D20 — Exactly-once vs At-least-once vs At-most-once (Slide 56)

**Tipo**: Comparação visual
**Descrição**: 3 modelos de delivery com exemplos
**Mermaid**:
```mermaid
flowchart TB
    subgraph ALO["At-Least-Once (padrão)"]
        A1["Pode chegar 1+ vezes"]
        A2["Solução: idempotência"]
        A3["Ex: Kafka, Temporal"]
    end
    subgraph AMO["At-Most-Once"]
        M1["Pode se perder"]
        M2["Fire and forget"]
        M3["Ex: logs não críticos"]
    end
    subgraph EO["'Exactly-Once' (mito)"]
        E1["Não existe com falhas"]
        E2["= at-least-once + idempotência"]
        E3["= 'effectively once'"]
    end
```

---

### D21 — Sharding de Consumidores (Slide 57)

**Tipo**: Diagrama de paralelismo
**Descrição**: Múltiplas partições → múltiplos consumers em paralelo
**Mermaid**:
```mermaid
flowchart TB
    subgraph Partitions
        P0["Partition 0<br/>agents 1-100"]
        P1["Partition 1<br/>agents 101-200"]
        P2["Partition 2<br/>agents 201-300"]
        P3["Partition 3<br/>agents 301-400"]
    end
    P0 --> C0["Consumer 0"]
    P1 --> C1["Consumer 1"]
    P2 --> C2["Consumer 2"]
    P3 --> C3["Consumer 3"]
```

---

### D22 — Distributed Tracing (Slide 58)

**Tipo**: Timeline de spans
**Descrição**: Trace distribuído com spans em múltiplos serviços
**Mermaid**:
```mermaid
flowchart TB
    Root["Trace (root span)"]
    Root --> S1["Producer: publish event<br/>2ms"]
    S1 --> S2["Kafka: broker<br/>5ms"]
    S2 --> S3["Consumer A: agente OCR<br/>1200ms"]
    S3 --> S4["LLM API call<br/>1100ms"]
    S3 --> S5["Consumer B: validate<br/>300ms"]
    S5 --> S6["Consumer C: index<br/>150ms"]
```
**Estilo**: Cada span em cor diferente por serviço.

---

### D23 — Caso de Estudo: Pipeline Enterprise (Slide 65)

**Tipo**: Flowchart de arquitetura completa
**Descrição**: Pipeline de processamento de documentos com todos os patterns
**Mermaid**:
```mermaid
flowchart LR
    Ingest["Ingestão<br/>(Kafka topic: raw)"] --> Classify["Agente<br/>Classificador<br/>(Temporal activity)"]
    Classify --> Extract["Agente<br/>Extrator<br/>(activity + circuit breaker)"]
    Extract --> HITL{"Precisa<br/>validação?"}
    HITL -- "sim" --> Wait["await signal<br/>(até 7 dias)"]
    Wait -- "aprovado" --> Publish["Publicação"]
    HITL -- "não" --> Publish
    Publish --> DB[("Vector DB")]
    Extract -.falha.- CB["Circuit Breaker"]
    Extract -.irreparável.- DLQ[("DLQ")]
    HITL -- "falha" --> Saga["Saga<br/>compensatória"]
    OTel["OpenTelemetry<br/>distributed tracing"] -.observa.- Classify
```

---

### D24 — Mapa da Especialização com ETHAGT11 (Slide 73)

**Tipo**: Mind map radial
**Descrição**: ETHAGT11 no centro com conexões para módulos futuros
**Mermaid**:
```mermaid
mindmap
  root((ETHAGT11))
    ETHAGT12
      AgentOps
      Distributed Tracing
      Observabilidade
    ETHAGT14
      Escalabilidade
      Sharding
      Produção em larga escala
    ETHAGT90
      Projeto Final
      Pipeline event-driven
```

---

## Resumo de Produção

| # | Nome | Tipo | Status | Slide |
|---|---|---|---|---|
| D1 | Pipeline event-driven | Flowchart | ✅ Existe | 9 |
| D2 | O Log imutável | Flowchart | 🆕 Novo | 15 |
| D3 | Kafka: arquitetura | Flowchart | 🆕 Novo | 16 |
| D4 | Kafka: particionamento e ordering | Diagrama | 🆕 Novo | 17 |
| D5 | Kafka: consumer groups | Diagrama | 🆕 Novo | 18 |
| D6 | RabbitMQ: exchanges/bindings | Flowchart | 🆕 Novo | 19 |
| D7 | Comparação Kafka/RabbitMQ/NATS | Tabela | 🆕 Novo | 21 |
| D8 | CQRS | Flowchart | 🆕 Novo | 23 |
| D9 | CloudEvent JSON | Código | 🆕 Novo | 25 |
| D10 | Temporal: arquitetura | Flowchart | 🆕 Novo | 30 |
| D11 | Comparação Temporal/Prefect/Airflow | Tabela | 🆕 Novo | 35 |
| D12 | Durable execution | Sequência | ✅ Existe | 31, 38 |
| D13 | HITL via timers e signals | Sequência | 🆕 Novo | 40 |
| D14 | Durable execution (crash) | Sequência | ✅ = D12 | 38 |
| D15 | Non-determinism quebrando replay | Comparação | 🆕 Novo | 42 |
| D16 | Determinismo: correto vs quebrado | Código | 🆕 Novo | 43 |
| D17 | Saga pattern | Flowchart | ✅ Existe | 24, 51 |
| D18 | Saga: transferência entre contas | Flowchart | ✅ = D17 | 52 |
| D19 | Circuit breaker | State diagram | 🆕 Novo | 53 |
| D20 | Exactly-once vs at-least-once | Comparação | 🆕 Novo | 56 |
| D21 | Sharding de consumidores | Diagrama | 🆕 Novo | 57 |
| D22 | Distributed tracing | Timeline | 🆕 Novo | 58 |
| D23 | Caso de estudo: pipeline enterprise | Flowchart | 🆕 Novo | 65 |
| D24 | Mapa da especialização | Mind map | 🆕 Novo | 73 |

**Total**: 3 existentes (reutilizados em 6 slides) + 21 novos = 24 diagramas referenciados.
