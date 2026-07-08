# ETHAGT09 — Sugestões de Diagramas

> 18 diagramas necessários para a apresentação.
> 4 canônicos em `12-Diagrams/ETHAGT09/`. 14 novos a produzir.

---

## Diagramas Canônicos (4)

| # | Slide | Arquivo | Descrição |
|---|---|---|---|
| D6 | 22 | `handoff.mmd` | Handoff (Swarm) — transferência de controle |
| D8 | 29 | `blackboard.mmd` | Padrão blackboard — espaço compartilhado |
| D9 | 36 | `actor-model.mmd` | Actor model — atores com mailboxes |
| D12 | 49 | `negotiation.mmd` | Negociação — bargaining flow |

---

### handoff.mmd

**Tipo**: Flowchart
**Descrição**: Triager transfere controle para Sales/Billing/Support via handoff.

```mermaid
flowchart LR
    User([Usuário]) --> Triager["Triager Agent"]
    Triager -->|"handoff: vendas"| Sales["Sales Agent"]
    Triager -->|"handoff: cobrança"| Billing["Billing Agent"]
    Triager -->|"handoff: suporte"| Support["Support Agent"]
    Sales --> Done([Resolvido])
    Billing --> Done
    Support --> Done

    style Triager fill:#1B3A5E,color:#fff
    style Sales fill:#E85D2F,color:#fff
    style Billing fill:#E85D2F,color:#fff
    style Support fill:#E85D2F,color:#fff
```

---

### blackboard.mmd

**Tipo**: Flowchart
**Descrição**: 3 agentes conectados a um blackboard central; leem e escrevem sem comunicação direta.

```mermaid
flowchart TD
    A1["Agente 1<br/>(Pesquisador)"]
    A2["Agente 2<br/>(Analista)"]
    A3["Agente 3<br/>(Redator)"]
    BB[("Blackboard<br/>facts · hypotheses<br/>partial results")]

    A1 -->|"write"| BB
    A2 -->|"write"| BB
    A3 -->|"write"| BB
    BB -->|"read"| A1
    BB -->|"read"| A2
    BB -->|"read"| A3

    style BB fill:#1B3A5E,color:#fff
    style A1 fill:#E85D2F,color:#fff
    style A2 fill:#E85D2F,color:#fff
    style A3 fill:#E85D2F,color:#fff
```

---

### actor-model.mmd

**Tipo**: Flowchart
**Descrição**: 3 atores com mailboxes individuais; comunicação assíncrona via mensagens; estado privado encapsulado.

```mermaid
flowchart LR
    subgraph A1["Ator A"]
        MB1["mailbox"]
        ST1["estado privado"]
    end
    subgraph A2["Ator B"]
        MB2["mailbox"]
        ST2["estado privado"]
    end
    subgraph A3["Ator C"]
        MB3["mailbox"]
        ST3["estado privado"]
    end

    MB1 -->|"msg"| MB2
    MB2 -->|"msg"| MB3
    MB3 -->|"msg"| MB1
    MB1 -.-> ST1
    MB2 -.-> ST2
    MB3 -.-> ST3

    style A1 fill:#1B3A5E,color:#fff
    style A2 fill:#1B3A5E,color:#fff
    style A3 fill:#1B3A5E,color:#fff
```

---

### negotiation.mmd

**Tipo**: Flowchart
**Descrição**: Comprador propõe 100 → Vendedor contrapropõe 150 → convergem em 120; fallback de timeout.

```mermaid
flowchart TD
    Start([Início]) --> P1["Comprador propõe: 100"]
    P1 --> P2["Vendedor contrapropõe: 150"]
    P2 --> P3{"Comprador aceita?"}
    P3 -- "Não" --> P4["Comprador propõe: 120"]
    P4 --> P5{"Vendedor aceita?"}
    P5 -- "Sim" --> Deal([Acordo: 120])
    P5 -- "Não" --> Round{"Round < max?"}
    Round -- "Sim" --> P2
    Round -- "Não" --> Timeout([Timeout / Escalar mediator])

    style Deal fill:#2D8659,color:#fff
    style Timeout fill:#C0392B,color:#fff
    style P1 fill:#E85D2F,color:#fff
    style P2 fill:#1B3A5E,color:#fff
    style P4 fill:#E85D2F,color:#fff
```

---

## Diagramas Novos (14)

### D1 — Topologias: Broadcast vs P2P vs Pub/Sub (Slide 9)

**Tipo**: Grid 1x3
**Descrição**: 3 topologias canônicas lado a lado.

```mermaid
flowchart LR
    subgraph BC["Broadcast"]
        B1[Sender] --> B2[Agente]
        B1 --> B3[Agente]
        B1 --> B4[Agente]
    end
    subgraph PP["P2P"]
        P1[Agente A] <--> P2[Agente B]
    end
    subgraph PS["Pub/Sub"]
        PA1[Produtor] --> Topic[(Tópico)]
        Topic --> SC1[Consumidor 1]
        Topic --> SC2[Consumidor 2]
    end
```

---

### D2 — Schema de Mensagem A2A (Slide 10)

**Tipo**: Código
**Descrição**: Exemplo de JSON schema para mensagem A2A com versionamento.

```json
{
  "message_id": "msg_abc123",
  "sender": "agent://researcher-01",
  "receiver": "agent://writer-02",
  "message_type": "task_result",
  "version": "1.2.0",
  "timestamp": "2026-07-07T14:30:00Z",
  "payload": {
    "task_id": "task_xyz",
    "result": "Resumo encontrado: ...",
    "confidence": 0.87
  },
  "in_reply_to": "msg_def456"
}
```

---

### D3 — 3 Padrões de Conversação (Slide 17)

**Tipo**: Grid 1x3
**Descrição**: Two-agent (CAMEL), Group chat (AutoGen), Handoff (Swarm).

```mermaid
flowchart LR
    subgraph D["Two-Agent (CAMEL)"]
        DA["Assistente"] <--> DB["Usuário simulado"]
    end
    subgraph G["Group Chat (AutoGen)"]
        GM["Manager"] <--> GA[Agente A]
        GM <--> GB[Agente B]
        GM <--> GC[Agente C]
    end
    subgraph H["Handoff (Swarm)"]
        HT[Triager] -->|handoff| HS[Specialist]
    end
```

---

### D4 — CAMEL Role-Playing Trace (Slide 19)

**Tipo**: Console
**Descrição**: Trace de diálogo CAMEL com turnos alternados.

```
┌─────────────────────────────────────────────┐
│  Tarefa: Escrever artigo sobre energias     │
│  renováveis                                  │
├─────────────────────────────────────────────┤
│  [Usuário]   Turno 1: "Qual estrutura       │
│              você sugere?"                   │
│  [Assistente] Turno 2: "Introdução, 3        │
│              seções técnicas, conclusão."    │
│  [Usuário]   Turno 3: "Aprofunde a seção    │
│              solar."                         │
│  [Assistente] Turno 4: "Painéis fotovoltaic │
│              os convertem..."                │
└─────────────────────────────────────────────┘
```

---

### D5 — AutoGen GroupChat Hub-and-Spoke (Slide 20)

**Tipo**: Flowchart
**Descrição**: Manager no centro decide quem fala a seguir.

```mermaid
flowchart TD
    M["Group Chat<br/>Manager"]
    M -->|select| A1["Researcher"]
    M -->|select| A2["Coder"]
    M -->|select| A3["Reviewer"]
    A1 -->|speak| M
    A2 -->|speak| M
    A3 -->|speak| M

    style M fill:#1B3A5E,color:#fff
    style A1 fill:#E85D2F,color:#fff
    style A2 fill:#E85D2F,color:#fff
    style A3 fill:#E85D2F,color:#fff
```

---

### D7 — Pipeline MetaGPT SOPs (Slide 24 / 63)

**Tipo**: Pipeline
**Descrição**: Papéis MetaGPT com artefatos estruturados como comunicação.

```mermaid
flowchart LR
    PM["Product Manager"] -->|PRD| AR["Architect"]
    AR -->|Design Doc| EN["Engineer"]
    EN -->|Code| QA["QA Engineer"]
    QA -->|Test Report| Done([Entrega])

    style PM fill:#1B3A5E,color:#fff
    style AR fill:#2980B9,color:#fff
    style EN fill:#E85D2F,color:#fff
    style QA fill:#2D8659,color:#fff
```

---

### D10 — Thread+Lock vs Actor (Slide 38)

**Tipo**: Comparação
**Descrição**: Shared state com locks vs actor model com mailbox.

```mermaid
flowchart LR
    subgraph SS["Shared State (com locks)"]
        T1[Thread 1] --> LOCK[("Estado<br/>compartilhado")]
        T2[Thread 2] --> LOCK
        T3[Thread 3] --> LOCK
        LOCK -. "lock/cond" .- T1
    end
    subgraph AM["Actor Model (sem locks)"]
        AM1[Ator 1] --> MB1[mailbox]
        AM2[Ator 2] --> MB2[mailbox]
        MB1 -. "msg async" .- MB2
    end
```

---

### D11 — DEMO: 2 Arquiteturas Lado a Lado (Slide 43)

**Tipo**: Comparação
**Descrição**: Group chat vs blackboard para a mesma tarefa.

```mermaid
flowchart LR
    subgraph GC["AutoGen Group Chat"]
        GCM[Manager] <--> GA1[Researcher]
        GCM <--> GA2[Summarizer]
        GCM <--> GA3[Formatter]
    end
    subgraph BB["Blackboard"]
        BBA1[Researcher] --> BBX[("Blackboard")]
        BBA2[Summarizer] --> BBX
        BBA3[Formatter] --> BBX
        BBX --> BBA1
        BBX --> BBA2
        BBX --> BBA3
    end
```

---

### D13 — Eixo Tempo × Qualidade (Slide 52)

**Tipo**: Gráfico
**Descrição**: Zona de acordo entre agente de velocidade e agente de qualidade.

```
Qualidade ↑
    │
 Q2 ····················· · Agente de Qualidade
    │              ╔══════╗
    │              ║ ZONA ║
    │              ║ DE   ║
    │              ║ACORDO║
    │              ╚══════╝
 Q1 · · Agente de Velocidade
    │
    └────────────────────────→ Tempo
    T1                      T2
```

---

### D14 — A2A Protocol Sequência (Slide 55)

**Tipo**: Sequência
**Descrição**: Descoberta de Agent Card → Task → processamento → resultado.

```mermaid
sequenceDiagram
    participant A as Agente A
    participant B as Agente B
    A->>B: GET /.well-known/agent.json
    B-->>A: Agent Card (skills, endpoints)
    A->>B: POST /tasks (Task)
    B->>B: processa tarefa
    B-->>A: status: working (SSE stream)
    B-->>A: status: completed + result
```

---

### D15 — MCP vs A2A Venn (Slide 56)

**Tipo**: Venn
**Descrição**: MCP = agent↔system; A2A = agent↔agent. Complementares.

```mermaid
flowchart LR
    subgraph MCP["MCP — Agent ↔ System"]
        M1[Tools]
        M2[Data Sources]
        M3[Resources]
    end
    subgraph A2A["A2A — Agent ↔ Agent"]
        A1[Delegação]
        A2[Colaboração]
        A3[Negociação]
    end
    AGENT(("Agente")) <--> MCP
    AGENT <--> A2A
```

---

### D16 — 4 Topologias de Orquestração (Slide 57)

**Tipo**: Grid 2x2
**Descrição**: Centralizada, descentralizada, hierárquica, market-based.

```mermaid
flowchart TD
    subgraph CEN["Centralizada"]
        SUP[Supervisor] <--> C1[A]
        SUP <--> C2[B]
    end
    subgraph DES["Descentralizada"]
        D1[A] <--> D2[B]
        D2 <--> D3[C]
        D1 <--> D3
    end
    subgraph HIE["Hierárquica"]
        H1[Top] --> H2[Sub-1]
        H1 --> H3[Sub-2]
        H2 --> H4[A]
        H3 --> H5[B]
    end
    subgraph MKT["Market-based"]
        MK[Tasks] --> MB1[A: bid]
        MK --> MB2[B: bid]
        MK --> MB3[C: bid]
    end
```

---

### D17 — Mapa da Especialização (Slide 71)

**Tipo**: Mind map radial
**Descrição**: ETHAGT09 no centro com conexões para módulos dependentes.

```mermaid
mindmap
  root((ETHAGT09))
    Pré-requisito
      ETHAGT04
        Reasoning
        Planning
    Dependentes
      ETHAGT10
        Padrões de Arquitetura
      ETHAGT11
        Event-Driven Agents
      ETHAGT15
        Sociedades de Agentes
    Conceitos
      A2A
      Blackboard
      Actor Model
      Negociação
```

---

## Resumo de Produção

| # | Nome | Tipo | Status | Slide |
|---|---|---|---|---|
| D1 | Topologias (broadcast/p2p/pubsub) | Grid 1x3 | 🆕 Novo | 9 |
| D2 | Schema de mensagem A2A | Código JSON | 🆕 Novo | 10 |
| D3 | 3 padrões de conversação | Grid 1x3 | 🆕 Novo | 17 |
| D4 | CAMEL role-playing trace | Console | 🆕 Novo | 19 |
| D5 | AutoGen GroupChat hub-and-spoke | Flowchart | 🆕 Novo | 20 |
| D6 | Handoff (Swarm) | Flowchart | ✅ `handoff.mmd` | 22 |
| D7 | Pipeline MetaGPT SOPs | Pipeline | 🆕 Novo | 24/63 |
| D8 | Blackboard pattern | Flowchart | ✅ `blackboard.mmd` | 29 |
| D9 | Actor model | Flowchart | ✅ `actor-model.mmd` | 36 |
| D10 | Thread+lock vs Actor | Comparação | 🆕 Novo | 38 |
| D11 | DEMO: 2 arquiteturas | Comparação | 🆕 Novo | 43 |
| D12 | Negociação (bargaining) | Flowchart | ✅ `negotiation.mmd` | 49 |
| D13 | Eixo tempo × qualidade | Gráfico | 🆕 Novo | 52 |
| D14 | A2A Protocol sequência | Sequência | 🆕 Novo | 55 |
| D15 | MCP vs A2A (Venn) | Venn | 🆕 Novo | 56 |
| D16 | 4 topologias orquestração | Grid 2x2 | 🆕 Novo | 57 |
| D17 | Mapa da especialização | Mind map | 🆕 Novo | 71 |

**Total**: 4 canônicos (`.mmd`) + 13 novos = 17 diagramas a produzir/manter.
