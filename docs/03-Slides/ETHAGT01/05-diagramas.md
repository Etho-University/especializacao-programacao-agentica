# ETHAGT01 — Sugestões de Diagramas

> 15 diagramas necessários para a apresentação.
> 7 já existem em `12-Diagrams/ETHAGT01/`. 8 novos a produzir.

---

## Diagramas Existentes (7)

| # | Slide | Arquivo | Descrição |
|---|---|---|---|
| D2 | 12 | `augmented-llm.mmd` | LLM + retrieval + tools + memory |
| D6 | 18 | `agent-loop.mmd` | Thought → Action → Observation em loop |
| D7 | 24 | `workflow-vs-agent.mmd` | Árvore de decisão workflow vs agente |
| D12 | 31/32 | `framework-comparison.mmd` | Python puro vs Framework (estrutura) |

> **Nota**: Os 4 diagramas existentes cobrem 4 dos 15 necessários. Os demais (D1, D3, D4, D5, D8, D9, D10, D11, D13, D14, D15) são novos.

---

## Diagramas Novos (8)

### D1 — Taxonomia Unificada (Slide 9)

**Tipo**: Mind map radial
**Descrição**: Hexágono com Brain no centro e 5 componentes ao redor (Perception, Planning, Action, Tool Use, Collaboration)
**Mermaid**:
```mermaid
mindmap
  root((Agent))
    Brain
      LLM
      Reasoning
      Generation
    Perception
      Input
      Tool Results
      Environment
    Planning
      Goal Decomposition
      Sub-task Selection
    Action
      Tool Calls
      API Calls
      Code Execution
    Tool Use
      Selection
      Execution
      Validation
    Collaboration
      Human-in-the-Loop
      Multi-Agent Comm
```
**Estilo**: Cada ramo em cor diferente. Centro em `etho-primary`.

---

### D3 — RAG Fixo vs RAG Agêntico (Slide 13)

**Tipo**: Comparação lado a lado
**Descrição**: Esquerda: pipeline linear (query → retrieve → generate). Direita: loop com decisão (query → modelo decide → retrieve ou resposta → generate)
**Mermaid**:
```mermaid
flowchart LR
    subgraph Fixo["RAG Tradicional (fixo)"]
        Q1[query] --> R1[retrieve] --> G1[generate]
    end
    subgraph Agentic["RAG Agêntico (in-loop)"]
        Q2[query] --> D{precisa recuperar?}
        D -- Sim --> R2[retrieve]
        R2 --> G2[generate]
        D -- Não --> G2
        G2 --> D2{precisa mais?}
        D2 -- Sim --> R2
        D2 -- Não --> A[answer]
    end
```

---

### D4 — Fluxo de Tool Calling (Slide 14)

**Tipo**: Diagrama de sequência
**Descrição**: LLM → tool_call (JSON) → execução → observation → LLM
**Mermaid**:
```mermaid
sequenceDiagram
    participant U as Usuário
    participant L as LLM
    participant T as Tool
    U->>L: "Quanto é 123 * 456?"
    L->>L: Thought: preciso calcular
    L->>T: tool_call: calculator(a=123, b=456, op="*")
    T->>T: executa 123 * 456
    T-->>L: Observation: 56088
    L->>L: Thought: agora somar 789
    L->>T: tool_call: calculator(a=56088, b=789, op="+")
    T-->>L: Observation: 56877
    L-->>U: "123 * 456 + 789 = 56877"
```

---

### D5 — Working vs Persistente Memory (Slide 15)

**Tipo**: Comparação
**Descrição**: Duas caixas: Context Window (efêmera) ↔ Checkpointer (persistente)
**Mermaid**:
```mermaid
flowchart LR
    subgraph WM["Working Memory (Context Window)"]
        direction TB
        W1["• Efêmera"]
        W2["• Limitada (128k-200k tokens)"]
        W3["• Custo cresce com tamanho"]
        W4["• Some ao fim da sessão"]
    end
    subgraph PM["Persistent Memory (Checkpointer)"]
        direction TB
        P1["• Durável"]
        P2["• Postgres / Redis / SQLite"]
        P3["• Serializada entre sessões"]
        P4["• Permite resumir e retomar"]
    end
    WM <-->|"summarize / evict"| PM
```

---

### D8 — 5 Workflows Canônicos (Slide 25)

**Tipo**: Grid de mini-diagramas
**Descrição**: 5 padrões em grade 2x3 (cada um com fluxo simples)
**Mermaid** (cada um separado):

**Prompt Chaining**:
```mermaid
flowchart LR
    A[Step 1] --> B[Gate?] --> C[Step 2] --> D[Output]
```

**Routing**:
```mermaid
flowchart TD
    I[Input] --> C{Classify} --> A[Handler A]
    C --> B[Handler B]
    C --> D[Handler C]
```

**Parallelization**:
```mermaid
flowchart TD
    I[Input] --> A[LLM A]
    I --> B[LLM B]
    I --> C[LLM C]
    A --> Agg[Aggregate]
    B --> Agg
    C --> Agg
```

**Orchestrator-Workers**:
```mermaid
flowchart TD
    O[Orchestrator] --> W1[Worker 1]
    O --> W2[Worker 2]
    O --> W3[Worker N]
    W1 --> S[Synthesize]
    W2 --> S
    W3 --> S
```

**Evaluator-Optimizer**:
```mermaid
flowchart LR
    G[Generate] --> E[Evaluate] --> F{Good enough?}
    F -- No --> G
    F -- Yes --> O[Output]
```

---

### D9 — Árvore de Decisão Detalhada (Slide 26)

**Tipo**: Fluxograma de decisão
**Descrição**: Árvore detalhada para decidir workflow vs agente vs agente+HITL
**Mermaid**:
```mermaid
flowchart TD
    Q([Preciso de sistema com LLM]) --> S{Consigo listar<br/>os passos?}
    S -- "Sim" --> W["WORKFLOW<br/>previsível, controlado"]
    S -- "Não" --> P{O nº de passos<br/>é previsível?}
    P -- "Sim, mas variável" --> O{Posso confiar<br/>no modelo sem HITL?}
    P -- "Não" --> A
    O -- "Sim" --> A["AGENTE<br/>flexível, dirigido pelo modelo"]
    O -- "Não" --> AH["AGENTE + HITL forte<br/>checkpoints críticos"]
```

> **Nota**: Este diagrama já existe como `workflow-vs-agent.mmd`. Reutilizar.

---

### D10 — Pirâmide de Complexidade (Slide 27)

**Tipo**: Pirâmide
**Descrição**: 5 níveis de complexidade, do mais simples (base) ao mais complexo (topo)
**Mermaid**:
```mermaid
flowchart TB
    L4["Nível 4: Multi-Agente"] --> L3["Nível 3: Agente Autônomo"]
    L3 --> L2["Nível 2: Workflow Complexo"]
    L2 --> L1["Nível 1: Workflow Simples"]
    L1 --> L0["Nível 0: Single LLM Call + RAG"]
    
    L0 -. "90% dos casos" .-> P0([Start here])
    L4 -. "raro" .-> P4([Último recurso])
```

---

### D11 — Comparação 3 Implementações (Slide 30)

**Tipo**: 3 colunas comparativas
**Descrição**: Python puro (50 linhas), LangGraph (20 linhas), OpenAI SDK (15 linhas)
**Mermaid**:
```mermaid
flowchart LR
    subgraph P["Python Puro (~50 linhas)"]
        direction TB
        P1["Controle: ✅ Total"]
        P2["Transparência: ✅ Total"]
        P3["Esforço: ⚠️ Alto"]
        P4["Produção: ⚠️ Manual"]
    end
    subgraph L["LangGraph (~20 linhas)"]
        direction TB
        L1["Controle: ⚠️ Parcial"]
        L2["Transparência: ✅ Alto"]
        L3["Esforço: ✅ Médio"]
        L4["Produção: ✅ Ready"]
    end
    subgraph O["OpenAI SDK (~15 linhas)"]
        direction TB
        O1["Controle: ❌ Mínimo"]
        O2["Transparência: ❌ Baixo"]
        O3["Esforço: ✅ Baixo"]
        O4["Produção: ✅ Ready"]
    end
```

---

### D13 — Trace Tree / Spans (Slide 40)

**Tipo**: Árvore de spans com timeline
**Descrição**: Root span (Agent Run) com child spans (LLM calls, tool calls) em timeline
**Mermaid**:
```mermaid
flowchart TB
    Root["Agent Run (root span)"]
    Root --> S1["LLM Call #1 (step 0)"]
    S1 --> T1["Tool: calculator(123, 456, *)"]
    Root --> S2["LLM Call #2 (step 1)"]
    S2 --> T2["Tool: calculator(56088, 789, +)"]
    Root --> S3["LLM Call #3 (step 2 — answer)"]
    
    T1 -. 2.1s .- Timeline
    T2 -. 1.8s .- Timeline
    S3 -. 0.9s .- Timeline
```

---

### D14 — Arquitetura Coding Agent SWE-bench (Slide 45)

**Tipo**: Flowchart
**Descrição**: issue → Augmented LLM (Claude + tools + memory) → Agent Loop → patch
**Mermaid**:
```mermaid
flowchart TB
    Issue([issue text]) --> AL
    subgraph AL["Augmented LLM (Claude)"]
        direction TB
        Tools["Tools: view_file, edit_file, run_tests"]
        Mem["Memory: repo state"]
    end
    AL --> Loop
    subgraph Loop["Agent Loop (max_steps)"]
        T1["Thought: entender issue"]
        T1 --> A1["Action: view_file(path)"]
        A1 --> O1["Observation: conteúdo"]
        O1 --> T2["Thought: localizar bug"]
        T2 --> A2["Action: edit_file(...)"]
        A2 --> O2["Observation: diff aplicado"]
        O2 --> T3["Action: run_tests()"]
        T3 --> O3["Observation: testes passaram"]
        O3 --> T4["Thought: pronto"]
    end
    Loop --> Patch([patch / diff])
```

---

### D15 — Mapa da Especialização (Slide 56)

**Tipo**: Mind map radial
**Descrição**: ETHAGT01 no centro com conexões para módulos futuros
**Mermaid**:
```mermaid
mindmap
  root((ETHAGT01))
    ETHAGT02
      Tool Calling
      ACI
    ETHAGT03
      5 Workflows
      Composição
    ETHAGT04
      Reasoning
      Reflexion, ToT
    ETHAGT05
      Memory
      Checkpointer
    ETHAGT06
      RAG Agêntico
    ETHAGT08
      MCP
    ETHAGT09
      Multi-Agent
    ETHAGT12
      AgentOps
      Traces
    ETHAGT13
      Security
    ETHAGT16
      Sociedades
```

---

## Resumo de Produção

| # | Nome | Tipo | Status | Slide |
|---|---|---|---|---|
| D1 | Taxonomia unificada | Mind map | 🆕 Novo | 9 |
| D2 | Augmented LLM | Flowchart | ✅ Existe | 12 |
| D3 | RAG fixo vs agêntico | Comparação | 🆕 Novo | 13 |
| D4 | Tool calling sequence | Sequência | 🆕 Novo | 14 |
| D5 | Working vs persistent memory | Comparação | 🆕 Novo | 15 |
| D6 | Agent loop (ReAct) | Flowchart | ✅ Existe | 18 |
| D7 | Workflow vs agente | Fluxograma | ✅ Existe | 24 |
| D8 | 5 workflows canônicos | Grid | 🆕 Novo | 25 |
| D9 | Árvore de decisão | Fluxograma | ✅ = D7 | 26 |
| D10 | Pirâmide de complexidade | Pirâmide | 🆕 Novo | 27 |
| D11 | Comparação 3 implementações | Colunas | 🆕 Novo | 30 |
| D12 | Framework comparison | Flowchart | ✅ Existe | 31/32 |
| D13 | Trace tree (spans) | Árvore | 🆕 Novo | 40 |
| D14 | Coding agent SWE-bench | Flowchart | 🆕 Novo | 45 |
| D15 | Mapa da especialização | Mind map | 🆕 Novo | 56 |

**Total**: 4 existentes + 1 reutilizado + 8 novos = 13 diagramas únicos a produzir/manter.
