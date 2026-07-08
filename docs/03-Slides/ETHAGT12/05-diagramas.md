# ETHAGT12 — Sugestões de Diagramas

> 22 diagramas necessários para a apresentação.
> 3 já existem em `12-Diagrams/ETHAGT12/`. 19 novos a produzir.

---

## Diagramas Existentes (3)

| # | Slide | Arquivo | Descrição |
|---|---|---|---|
| D5 | 17 | `trace-anatomy.mmd` | Trace com spans e atributos |
| D14 | 39 | `eval-pipeline.mmd` | Pipeline de eval com CI (gate) |
| D15 | 46 | `benchmark-landscape.mmd` | Landscape dos benchmarks canônicos |

---

## Diagramas Novos (19)

### D1 — Teste Manual vs Produção (Slide 5)

**Tipo**: Gráfico de barras
**Descrição**: Duas barras lado a lado — "Teste manual: 100%" (verde) vs "Produção: 30%" (vermelho)
**Mermaid**:
```mermaid
xychart-beta
    title "Success Rate: Teste vs Produção"
    x-axis ["Teste manual (5 casos)", "Produção (1000 casos)"]
    y-axis "Success Rate (%)" 0 --> 100
    bar [100, 30]
```
**Estilo**: Barra teste em `etho-success`, produção em `etho-danger`.

---

### D2 — Árvore de Possibilidades (Slide 8)

**Tipo**: Árvore
**Descrição**: 1 prompt → múltiplos caminhos (não-determinismo)
**Mermaid**:
```mermaid
flowchart TB
    P(["prompt: 'reserve voo'"])
    P --> A1["Thought: buscar voos"]
    P --> A2["Thought: perguntar datas"]
    P --> A3["Thought: verificar login"]
    A1 --> B1["Tool: search_flights"]
    A2 --> B2["Response: quais datas?"]
    A3 --> B3["Tool: check_auth"]
    B1 --> C1["..."]
    B2 --> C2["..."]
    B3 --> C3["..."]
```

---

### D3 — Agente Cercado por Fontes Mutáveis (Slide 9)

**Tipo**: Flowchart
**Descrição**: Agente no centro, cercado por API, DB, Web, FS
**Mermaid**:
```mermaid
flowchart TB
    API["API externa<br/>(muda versão)"]
    DB["Database / RAG<br/>(cresce)"]
    Web["Web<br/>(conteúdo muda)"]
    FS["Filesystem<br/>(estado varia)"]
    AGT(["Agente"]) <--> API
    AGT <--> DB
    AGT <--> Web
    AGT <--> FS
```

---

### D4 — Árvore de Spans Conceitual (Slide 16)

**Tipo**: Árvore
**Descrição**: Root span → children → leaves, com timing
**Mermaid**:
```mermaid
flowchart TB
    Root["ROOT SPAN<br/>t=0 ... t=8s"]
    Root --> S1["LLM Call #1<br/>t=0-1.2s"]
    Root --> S2["Tool Call A<br/>t=1.2-3.5s"]
    Root --> S3["LLM Call #2<br/>t=3.5-5s"]
    Root --> S4["Tool Call B<br/>t=5-7.8s"]
    Root --> S5["LLM Call #3<br/>t=7.8-8s"]
```

---

### D6 — Span com Atributos GenAI (Slide 18)

**Tipo**: Bloco de código anotado
**Descrição**: Span OTel com atributos GenAI semantic conventions
**Mermaid**:
```mermaid
flowchart LR
    subgraph Span["span: chat.completion"]
        A1["gen_ai.system = openai"]
        A2["gen_ai.request.model = gpt-4o"]
        A3["gen_ai.usage.prompt_tokens = 1250"]
        A4["gen_ai.usage.completion_tokens = 380"]
        A5["latency_ms = 1850"]
    end
```

---

### D7 — Comparação LangSmith vs Phoenix vs Langfuse vs OpenLLMetry (Slide 19)

**Tipo**: Tabela 4 colunas
**Descrição**: Tabela comparativa de ferramentas
**Mermaid**:
```mermaid
flowchart LR
    subgraph T["Comparação de Tooling"]
        direction TB
        L["LangSmith — LangChain, SaaS"]
        P["Phoenix — agnóstico, OSS"]
        F["Langfuse — agnóstico, self-host"]
        O["OpenLLMetry — instrumentação auto"]
    end
```

---

### D8 — Logs Estruturados vs Traces (Slide 20)

**Tipo**: Comparação
**Descrição**: Logs (JSON sequencial) vs Traces (árvore hierárquica)
**Mermaid**:
```mermaid
flowchart LR
    subgraph Logs["Logs estruturados"]
        L1["{ts, step, thought, action}"]
        L2["{ts, step, observation}"]
        L3["{ts, step, response}"]
    end
    subgraph Traces["Traces"]
        direction TB
        T0["root"]
        T0 --> T1["LLM"]
        T0 --> T2["Tool"]
        T2 --> T3["sub-span"]
    end
```

---

### D9 — Funil de Amostragem (Slide 21)

**Tipo**: Funil
**Descrição**: 100% traces → amostragem → 10% armazenados (com erros sempre capturados)
**Mermaid**:
```mermaid
flowchart TB
    All["100% traces gerados"]
    Error["erros: 100% capturados"]
    Success["sucesso: 10% amostrados"]
    All --> Head{"head ou tail?"}
    Head --> Error
    Head --> Success
    Error --> Stored[(storage)]
    Success --> Stored
```

---

### D10 — Dashboard Mínimo de Observabilidade (Slide 22)

**Tipo**: Mock dashboard com 6 painéis (grid 2x3)
**Descrição**: 6 painéis: success rate, latência P50/P95/P99, custo, tool usage, erros, distribuição de steps
**Mermaid**:
```mermaid
flowchart TB
    subgraph Dash["Dashboard de Observabilidade"]
        direction TB
        P1["1. Success rate 24h"]
        P2["2. Latência P50/P95/P99"]
        P3["3. Custo por execução"]
        P4["4. Tool usage"]
        P5["5. Erros por tipo"]
        P6["6. Distribuição de steps"]
    end
```

---

### D11 — Latência P50/P95/P99 (Slide 23)

**Tipo**: Gráfico de linha
**Descrição**: Distribuição de latência com marcadores P50, P95, P99
**Mermaid**:
```mermaid
xychart-beta
    title "Latência por execução"
    x-axis "percentil" [P50, P75, P90, P95, P99]
    y-axis "latência (s)" 0 --> 30
    line [3, 5, 9, 14, 28]
```

---

### D12 — Fluxo LLM-as-Judge (Slide 30)

**Tipo**: Flowchart
**Descrição**: agent output → judge prompt (com rubrica) → judge LLM → score + justificativa
**Mermaid**:
```mermaid
flowchart LR
    In["input"] --> Agent["agent LLM"]
    Agent --> Out["output"]
    Out --> Judge["judge LLM + rubrica"]
    In --> Judge
    Judge --> Score["score + justificativa"]
```

---

### D13 — Exemplo de Golden Case em Código (Slide 34)

**Tipo**: Bloco de código
**Descrição**: Estrutura de golden case em Python
**Mermaid**:
```mermaid
flowchart TB
    GC["Golden Case"]
    GC --> ID["id: GC-042"]
    GC --> In["input: 'Qual a capital da França?'"]
    GC --> Ev["eval_fn: assert 'Paris' in response"]
    GC --> Cat["category: factual"]
```

---

### D16 — Fluxo SWE-bench (Slide 47)

**Tipo**: Flowchart
**Descrição**: issue → agente → patch → testes → pass/fail
**Mermaid**:
```mermaid
flowchart LR
    Issue([issue GitHub]) --> Agent["Agente"]
    Agent --> Patch([patch])
    Patch --> Tests{"testes passam?"}
    Tests -- sim --> Resolved([resolved])
    Tests -- não --> Failed([failed])
```

---

### D17 — Arquitetura τ-bench (Slide 49)

**Tipo**: Flowchart
**Descrição**: user simulator ↔ agent ↔ tools
**Mermaid**:
```mermaid
flowchart LR
    User["User Simulator"] <-->|chat| Agent["Agent"]
    Agent <-->|tool calls| Tools["Tools (APIs)"]
    Tools --> Policy["Policy DB"]
    Tools --> Booking["Booking DB"]
```

---

### D18 — Grid de Ambientes AgentBench (Slide 50)

**Tipo**: Grid
**Descrição**: 8 ambientes do AgentBench
**Mermaid**:
```mermaid
flowchart TB
    subgraph AB["AgentBench — 8 ambientes"]
        OS["OS"]
        DB["DB"]
        KG["Knowledge Graph"]
        Web["Web"]
        Card["Card Game"]
        HH["Household"]
        AL["Alfworld"]
        Mind["Mind2Web"]
    end
```

---

### D19 — Shadow Runs e Canary (Slide 58)

**Tipo**: Flowchart
**Descrição**: Shadow (paralelo) → canary (5%) → full (100%)
**Mermaid**:
```mermaid
flowchart LR
    Shadow["Shadow run<br/>(paralelo, sem usuário)"] --> Canary["Canary<br/>5% tráfego"]
    Canary --> C25["Canary 25%"]
    C25 --> C50["Canary 50%"]
    C50 --> Full["Full deploy<br/>100%"]
    Full -. rollback .-> Canary
```

---

### D20 — Gráfico de Pizza de Categorias de Falha (Slide 62)

**Tipo**: Pizza chart
**Descrição**: Distribuição de categorias de falha
**Mermaid**:
```mermaid
pie title Categorias de falha
    "Tool errada" : 35
    "Alucinação" : 25
    "Incompleto" : 20
    "Não entendeu tarefa" : 10
    "Loop" : 5
    "Erro de tool" : 5
```

---

### D21 — Ciclo de Melhoria Anthropic (Slide 68)

**Tipo**: Ciclo
**Descrição**: eval → trace → categorizar falhas → corrigir → re-eval
**Mermaid**:
```mermaid
flowchart LR
    Eval["Rodar SWE-bench"] --> Trace["Analisar traces"]
    Trace --> Cat["Categorizar falhas"]
    Cat --> Fix["Corrigir (prompt/tool/arch)"]
    Fix --> Eval
```

---

### D22 — Mapa da Especialização com ETHAGT12 (Slide 76)

**Tipo**: Mind map radial
**Descrição**: ETHAGT12 no centro com conexões para módulos
**Mermaid**:
```mermaid
mindmap
  root((ETHAGT12))
    ETHAGT11
      LLMOps básico
    ETHAGT13
      Segurança
      Observabilidade como defesa
    ETHAGT90
      Capstone
      Eval report
    Labs
      Traces Everywhere
      Eval automatizado
```

---

## Resumo de Produção

| # | Nome | Tipo | Status | Slide |
|---|---|---|---|---|
| D1 | Teste vs produção | Gráfico barras | 🆕 Novo | 5 |
| D2 | Árvore de possibilidades | Árvore | 🆕 Novo | 8 |
| D3 | Agente + fontes mutáveis | Flowchart | 🆕 Novo | 9 |
| D4 | Árvore de spans conceitual | Árvore | 🆕 Novo | 16 |
| D5 | Anatomia de trace | Flowchart | ✅ Existe | 17 |
| D6 | Span GenAI attributes | Código | 🆕 Novo | 18 |
| D7 | Comparação tooling | Tabela | 🆕 Novo | 19 |
| D8 | Logs vs traces | Comparação | 🆕 Novo | 20 |
| D9 | Funil de amostragem | Funil | 🆕 Novo | 21 |
| D10 | Dashboard 6 painéis | Mock | 🆕 Novo | 22 |
| D11 | Latência P50/P95/P99 | Gráfico | 🆕 Novo | 23 |
| D12 | Fluxo LLM-as-judge | Flowchart | 🆕 Novo | 30 |
| D13 | Golden case em código | Código | 🆕 Novo | 34 |
| D14 | Pipeline eval com CI | Flowchart | ✅ Existe | 39 |
| D15 | Landscape benchmarks | Mind map | ✅ Existe | 46 |
| D16 | Fluxo SWE-bench | Flowchart | 🆕 Novo | 47 |
| D17 | Arquitetura τ-bench | Flowchart | 🆕 Novo | 49 |
| D18 | Grid AgentBench | Grid | 🆕 Novo | 50 |
| D19 | Shadow/canary | Flowchart | 🆕 Novo | 58 |
| D20 | Pizza categorias falha | Pizza | 🆕 Novo | 62 |
| D21 | Ciclo Anthropic | Ciclo | 🆕 Novo | 68 |
| D22 | Mapa especialização | Mind map | 🆕 Novo | 76 |

**Total**: 3 existentes + 19 novos = 22 diagramas a produzir/manter.
