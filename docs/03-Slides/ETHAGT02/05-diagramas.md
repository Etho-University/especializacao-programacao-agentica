# ETHAGT02 — Sugestões de Diagramas

> 11 diagramas necessários para a apresentação.
> 3 já existem em `12-Diagrams/ETHAGT02/`. 8 novos a produzir.

---

## Diagramas Existentes (3)

| # | Slide | Arquivo | Descrição |
|---|---|---|---|
| D8 | 35 | `risk-matrix.mmd` | Matriz de risco 2×2 (reversibilidade × impacto) |
| D9 | 36 | `hitl-flow.mmd` | Fluxo HITL para tool destrutiva (agente → runtime → humano → tool real) |
| D10 | 42 | `aci-iteration-loop.mmd` | Loop de iteração ACI (design → workbench → medir → diagnosticar) |

> **Nota**: Os 3 diagramas existentes cobrem as seções E e F. Os demais são novos.

---

## Diagramas Novos (8)

### D1 — Fluxo de Function Calling (Slide 8)

**Tipo**: Diagrama de sequência
**Descrição**: Usuário → LLM → tool_call (JSON) → execução → observation → LLM → resposta
**Mermaid**:
```mermaid
sequenceDiagram
    participant U as Usuário
    participant L as LLM
    participant T as Tool
    U->>L: "Busque preço do iPhone 15"
    L->>L: Thought: preciso pesquisar
    L->>T: tool_call: search_product("iPhone 15")
    T->>T: consulta catálogo
    T-->>L: Observation: {"price": 7999, "stock": 12}
    L->>L: Thought: tenho a informação
    L-->>U: "O iPhone 15 custa R$ 7.999 com 12 em estoque."
```

---

### D2 — Structured Outputs / Constrained Decoding (Slide 10)

**Tipo**: Comparação
**Descrição**: Esquerda: geração livre (pode produzir JSON inválido). Direita: constrained decoding (token a token forçado ao schema)
**Mermaid**:
```mermaid
flowchart LR
    subgraph Free["Geração Livre"]
        direction TB
        F1["Prompt + schema"]
        F2["LLM gera texto livre"]
        F3["Parser tenta extrair JSON"]
        F4["⚠️ Pode falhar"]
    end
    subgraph Constrained["Constrained Decoding"]
        direction TB
        C1["Prompt + schema"]
        C2["LLM gera token a token"]
        C3["Cada token validado vs schema"]
        C4["✅ JSON válido garantido"]
    end
```

---

### D3 — Multi-tool Calls em Paralelo (Slide 11)

**Tipo**: Fluxograma
**Descrição**: Uma resposta do LLM com 2 tool_calls executadas em paralelo
**Mermaid**:
```mermaid
flowchart TB
    L["LLM retorna 2 tool_calls"] --> T1["search_product(iPhone)"]
    L --> T2["search_product(Samsung)"]
    T1 --> O1["Observation: R$ 7999"]
    T2 --> O2["Observation: R$ 5499"]
    O1 --> L2["LLM combina → resposta final"]
    O2 --> L2
    L2 --> R["'iPhone: R$ 7999, Samsung: R$ 5499'"]
```

---

### D4 — Poka-yoke: Path Relativo → Absoluto (Slide 21)

**Tipo**: Antes/Depois
**Descrição**: Tool `view_file` antes aceitava paths relativos (erro possível). Depois exige path absoluto (erro impossível).
**Mermaid**:
```mermaid
flowchart LR
    subgraph Antes["❌ Antes (path relativo)"]
        direction TB
        A1["view_file('src/main.py')"]
        A2["Modelo pode estar em qualquer dir"]
        A3["Resultado: erro ou arquivo errado"]
    end
    subgraph Depois["✅ Depois (path absoluto + regex)"]
        direction TB
        D1["view_file('/repo/src/main.py')"]
        D2["pattern: ^/.+$"]
        D3["Erro impossível pelo design"]
    end
    Antes -- "poka-yoke" --> Depois
```

---

### D5 — Arquitetura Coding Agent SWE-bench (Slide 25)

**Tipo**: Flowchart
**Descrição**: issue → agente com tools (view_file, edit_file, run_tests) em loop → patch
**Mermaid**:
```mermaid
flowchart TB
    Issue([issue text]) --> AL
    subgraph AL["Coding Agent"]
        direction TB
        Tools["Tools: view_file, edit_file, run_tests"]
        Sandbox["Sandbox: container isolado"]
    end
    AL --> Loop
    subgraph Loop["Agent Loop"]
        T1["Thought: entender issue"]
        T1 --> A1["Action: view_file(abs_path)"]
        A1 --> O1["Observation: código"]
        O1 --> T2["Thought: localizar bug"]
        T2 --> A2["Action: edit_file(abs_path, old, new)"]
        A2 --> O2["Observation: diff aplicado"]
        O2 --> A3["Action: run_tests()"]
        A3 --> O3["Observation: testes passaram"]
    end
    Loop --> Patch([patch / diff])
```

---

### D6 — Idempotência com request_id (Slide 29)

**Tipo**: Fluxo de sequência
**Descrição**: Retry com mesma request_id → servidor detecta duplicata → retorna cache
**Mermaid**:
```mermaid
sequenceDiagram
    participant A as Agente
    participant T as Tool (send_email)
    participant S as Servidor
    A->>T: request_id="abc123", email={...}
    T->>S: processar com request_id="abc123"
    S-->>T: ✅ enviado (200)
    T-->>A: Observation: enviado
    Note over A: Timeout — achar que falhou
    A->>T: request_id="abc123" (retry)
    T->>S: request_id="abc123" (já existe)
    S-->>T: ⏭️ deduplicado (idempotente)
    T-->>A: Observation: já enviado (não duplicou)
```

---

### D7 — Tipologia de Tools: 4 Tipos (Slide 31)

**Tipo**: Tabela visual
**Descrição**: 4 quadrantes com tipo de tool, exemplo, nível de proteção
**Mermaid**:
```mermaid
flowchart TB
    subgraph Read["📖 Leitura (segura)"]
        R1["search, get_order, view_file"]
        R2["Sem proteção especial"]
    end
    subgraph Write["✏️ Escrita (reversível)"]
        W1["update_profile, create_cart"]
        W2["Log + validação"]
    end
    subgraph Destructive["💣 Destrutiva (irreversível)"]
        D1["delete_account, drop_table"]
        D2["HITL OBRIGATÓRIO"]
    end
    subgraph External["🌐 External Side-Effect"]
        E1["send_email, deploy, transfer"]
        E2["HITL + dry-run + auditoria"]
    end
```

---

### D11 — Dashboard de Métricas (Slide 43)

**Tipo**: Mockup de dashboard
**Descrição**: 4 cards de métricas: taxa de uso correto, custo por chamada, latência, taxa de erro
**Mermaid**:
```mermaid
flowchart LR
    subgraph Dashboard["Workbench Dashboard"]
        direction TB
        M1["✅ Taxa de uso correto: 87%<br/>Meta: ≥85%"]
        M2["💰 Custo/chamada: $0.004<br/>Meta: <$0.01"]
        M3["⏱️ Latência p50: 1.8s<br/>Meta: <3s"]
        M4["❌ Taxa de erro: 8%<br/>Meta: <10%"]
    end
```

---

## Resumo de Produção

| # | Nome | Tipo | Status | Slide |
|---|---|---|---|---|
| D1 | Fluxo de function calling | Sequência | 🆕 Novo | 8 |
| D2 | Structured outputs | Comparação | 🆕 Novo | 10 |
| D3 | Multi-tool em paralelo | Fluxograma | 🆕 Novo | 11 |
| D4 | Poka-yoke path relativo→absoluto | Antes/Depois | 🆕 Novo | 21 |
| D5 | Coding agent SWE-bench | Flowchart | 🆕 Novo | 25 |
| D6 | Idempotência com request_id | Sequência | 🆕 Novo | 29 |
| D7 | Tipologia de 4 tipos de tools | Tabela visual | 🆕 Novo | 31 |
| D8 | Matriz de risco 2×2 | Matriz | ✅ Existe | 35 |
| D9 | HITL flow | Flowchart | ✅ Existe | 36 |
| D10 | Workbench iteration loop | Loop | ✅ Existe | 42 |
| D11 | Dashboard de métricas | Mockup | 🆕 Novo | 43 |

**Total**: 3 existentes + 8 novos = 11 diagramas a produzir/manter.
