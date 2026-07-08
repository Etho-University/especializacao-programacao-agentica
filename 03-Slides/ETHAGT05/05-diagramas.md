# ETHAGT05 — Sugestões de Diagramas

> 16 diagramas necessários para a apresentação.
> 3 já existem em `12-Diagrams/ETHAGT05/`. 13 novos a produzir.

---

## Diagramas Existentes (3)

| # | Slide | Arquivo | Descrição |
|---|---|---|---|
| D3 | 14 | `memory-layers.mmd` | 4 camadas integradas (working, episódica, semântica, procedural) + checkpointer |
| D6 | 24 | `checkpointer-resume.mmd` | Fluxo pause/resume com thread_id e HITL |
| D9 | 36 | `eviction-flow.mmd` | Política de eviction: relevância × idade × entidade crítica |

> **Nota**: Os 3 diagramas existentes cobrem os fluxos centrais do módulo. Os demais (D1, D2, D4, D5, D7, D8, D10, D11, D12, D13, D14, D15, D16) são novos.

---

## Diagramas Novos (13)

### D1 — Recall Accuracy vs Posição no Contexto (Slide 9)

**Tipo**: Gráfico de linha (curva U)
**Descrição**: Acurácia de recall em função da posição do token no contexto. Curva em U: alta no início, baixa no meio, alta no fim.
**Mermaid**:
```mermaid
flowchart LR
    subgraph G["Recall Accuracy vs Position"]
        direction LR
        P1["Início: ✅ Alto"]
        P2["Meio: ❌ Baixo<br/>(Lost in the Middle)"]
        P3["Fim: ✅ Alto"]
    end
    P1 --> P2 --> P3
```
**Estilo**: Curva em U, início e fim em `etho-success`, meio em `etho-danger`.
**Fonte**: Liu et al. *Lost in the Middle* (arXiv:2307.03172).

---

### D2 — Comparação 4 Camadas de Memória (Slide 13)

**Tipo**: Tabela 4×4
**Descrição**: Grid comparativo das 4 camadas de memória (Working, Episódica, Semântica, Procedural) com eixos: o que armazena, onde, como recupera, quando usar.
**Mermaid**:
```mermaid
flowchart LR
    subgraph T["4 Camadas de Memória"]
        direction TB
        W["Working | context window | no prompt | sempre"]
        E["Episódica | vector DB | similaridade+metadata | recall de contexto"]
        S["Semântica | KB/KG | query estruturada | verdade estável"]
        P["Procedural | playbook | match de objetivo | tarefas repetidas"]
    end
```
**Estilo**: Cada coluna em cor distinta (`etho-info`, `etho-accent`, `etho-success`, `etho-warning`).

---

### D4 — MemGPT: Analogia SO (Slide 16)

**Tipo**: Analogia visual
**Descrição**: Comparação lado a lado: Sistema Operacional (RAM + Disco + Gerenciamento de Memória) vs LLM (Context Window + Memória Persistente + Self-editing).
**Mermaid**:
```mermaid
flowchart LR
    subgraph OS["Sistema Operacional"]
        RAM["RAM (limitada, rápida)"]
        DISK["Disco (ilimitado, lento)"]
        MMU["MMU: page-in / page-out"]
        RAM <-->|"swap"| DISK
        MMU -.controla.-> RAM
        MMU -.controla.-> DISK
    end
    subgraph LLM["LLM como SO (MemGPT)"]
        CW["Context Window (limitada)"]
        MEM["Memória Persistente (ilimitada)"]
        SELF["Self-editing: page-in / page-out"]
        CW <-->|"recall / evict"| MEM
        SELF -.gerencia.-> CW
        SELF -.gerencia.-> MEM
    end
```
**Fonte**: Packer et al. *MemGPT* (arXiv:2310.08560).

---

### D5 — Comparação de Backends (Slide 22)

**Tipo**: Tabela comparativa 3 colunas
**Descrição**: Postgres vs SQLite vs Redis em 7 eixos: durabilidade, latência, multi-tenant, custo, operação, TTL, ACID.
**Mermaid**:
```mermaid
flowchart LR
    subgraph PG["Postgres"]
        direction TB
        PG1["Durabilidade: ✅ Alta"]
        PG2["Latência: ⚠️ Média"]
        PG3["Multi-tenant: ✅ Sim"]
        PG4["ACID: ✅ Sim"]
        PG5["Uso: Produção"]
    end
    subgraph SQ["SQLite"]
        direction TB
        SQ1["Durabilidade: ✅ Alta (local)"]
        SQ2["Latência: ✅ Baixa"]
        SQ3["Multi-tenant: ❌ Não"]
        SQ4["ACID: ✅ Sim"]
        SQ5["Uso: Desenvolvimento"]
    end
    subgraph RD["Redis"]
        direction TB
        RD1["Durabilidade: ⚠️ Média"]
        RD2["Latência: ✅ Baixíssima"]
        RD3["Multi-tenant: ✅ Sim"]
        RD4["TTL: ✅ Nativo"]
        RD5["Uso: Cache de sessão"]
    end
```

---

### D7 — Branching: Árvore de Checkpoints (Slide 26)

**Tipo**: Git graph
**Descrição**: Árvore de checkpoints estilo `git log --graph`, mostrando branch a partir de checkpoint anterior.
**Mermaid**:
```mermaid
gitGraph
    commit id: "cp_001"
    commit id: "cp_002"
    commit id: "cp_003"
    branch alt-path
    checkout alt-path
    commit id: "cp_003a (fork)"
    commit id: "cp_004a"
    checkout main
    commit id: "cp_004"
    commit id: "cp_005"
```

---

### D8 — Sumarização em Cascata (Slide 34)

**Tipo**: Pirâmide invertida
**Descrição**: Mensagens brutas → Sumário L1 → Sumário L2 → Sumário L3, cada nível com menos detalhe e mais abstração.
**Mermaid**:
```mermaid
flowchart BT
    L0["Mensagens brutas (10k tokens)"]
    L1["Sumário L1 (2k tokens)"]
    L2["Sumário L2 (500 tokens)"]
    L3["Sumário L3 (100 tokens)"]
    L0 -->|"comprimir"| L1
    L1 -->|"comprimir"| L2
    L2 -->|"comprimir"| L3
```
**Estilo**: Largura decrescente de baixo para cima (pirâmide invertida).

---

### D10 — Entity-Centric Memory (Slide 37)

**Tipo**: Diagrama de entidades com page-in/page-out
**Descrição**: Agente no centro, entidades como "pastas" de memória. Apenas a entidade ativa está page-in (na context window); as demais estão page-out.
**Mermaid**:
```mermaid
flowchart TB
    Agent["Agente"]
    subgraph Context["Context Window (RAM)"]
        Active["Entidade ativa: 'Projeto X'"]
    end
    subgraph Disk["Memória Persistente (Disco)"]
        E1["Entidade: 'Usuário'"]
        E2["Entidade: 'Projeto Y'"]
        E3["Entidade: 'Tarefa Z'"]
    end
    Agent <-->|"page-in"| Active
    Active <-->|"page-out"| Disk
    Agent -.acessa.-> E1
    Agent -.acessa.-> E2
    Agent -.acessa.-> E3
```
**Fonte**: MemGPT (Packer et al.); Zep.

---

### D11 — Pipeline Completo de Recall Vetorial (Slide 46)

**Tipo**: Pipeline horizontal
**Descrição**: 6 etapas do recall episódico: query → embedding → metadata filter → vector search → re-ranking → inserção no contexto.
**Mermaid**:
```mermaid
flowchart LR
    Q["1. Query atual"] --> E["2. Embedding"]
    E --> MF["3. Metadata filter<br/>(user, session, time)"]
    MF --> VS["4. Vector search<br/>(top-K candidatos)"]
    VS --> RR["5. Re-ranking<br/>(top-N final)"]
    RR --> CT["6. Inserir no contexto"]
    CT --> A["Agente responde<br/>com memória"]
```

---

### D12 — Consolidação: Episódica → Semântica (Slide 52)

**Tipo**: Transformação
**Descrição**: Múltiplos eventos episódicos convergem, passam por processo de consolidação, e resultam em fatos semânticos.
**Mermaid**:
```mermaid
flowchart LR
    subgraph EP["Episódica (vector DB)"]
        direction TB
        V1["'João perguntou sobre decorators' (12/jan)"]
        V2["'João pediu ajuda com asyncio' (25/jan)"]
        V3["'João compartilhou repo de FastAPI' (03/fev)"]
    end
    CONS["Consolidação<br/>(offline / batch)"]
    subgraph SE["Semântica (KB)"]
        direction TB
        F1["'João é dev Python (interm-avanç)'"]
        F2["Interesses: decorators, asyncio, FastAPI"]
    end
    V1 --> CONS
    V2 --> CONS
    V3 --> CONS
    CONS --> F1
    CONS --> F2
```

---

### D13 — Knowledge Graph como Memória (Slide 54)

**Tipo**: Grafo de entidades
**Descrição**: Mini KG com 5 nós (João, Projeto X, Python, Sprint 20, Backend) e relações (trabalha_em, usa, livre_em, é_tipo_de).
**Mermaid**:
```mermaid
flowchart TB
    Jo["João"]
    PX["Projeto X"]
    Py["Python"]
    S20["Sprint 20"]
    BE["Backend"]
    Jo -- "trabalha_em" --> PX
    PX -- "usa" --> Py
    PX -- "é_tipo_de" --> BE
    Jo -- "livre_em" --> S20
```

---

### D14 — Memory Stream de Generative Agents (Slide 56)

**Tipo**: Timeline
**Descrição**: Memory stream de um agente de Smallville com observações, timestamps, e scores de recência/importância/relevância.
**Mermaid**:
```mermaid
flowchart TB
    subgraph MS["Memory Stream (Generative Agents)"]
        direction TB
        M1["'Klaus me convidou para planejar um jantar' (recency=0.95, importance=8, relevance=0.9)"]
        M2["'Estou cansado de planejar eventos' (recency=0.80, importance=5, relevance=0.6)"]
        M3["'Vi Maria na cafeteria' (recency=0.60, importance=2, relevance=0.3)"]
        M4["'Terminei meu artigo' (recency=0.30, importance=9, relevance=0.7)"]
    end
    Score["Score = α·recency + β·importance + γ·relevance"]
    MS --> Score
    Score --> Recall["Top-K recall"]
```
**Fonte**: Park et al. *Generative Agents* (arXiv:2304.03442).

---

### D15 — Consistência em Multi-Agente (Slide 59)

**Tipo**: Diagrama de concorrência
**Descrição**: 3 agentes compartilham memória. Race condition: agente A lê fato, B atualiza, A usa fato desatualizado.
**Mermaid**:
```mermaid
sequenceDiagram
    participant A as Agente A
    participant M as Memória Compartilhada
    participant B as Agente B
    A->>M: READ fato "saldo = 100"
    Note over A: A tem saldo = 100
    B->>M: WRITE "saldo = 50"
    A->>M: usa saldo = 100 (desatualizado!)
    Note over A,M: Race condition!
```

---

### D16 — Direito ao Esquecimento: 3 Estratégias (Slide 61)

**Tipo**: Comparação 3 colunas
**Descrição**: Três estratégias para implementar "esquecer usuário X" em memória vetorial: delete por metadata, re-embed, cryptographic erasure.
**Mermaid**:
```mermaid
flowchart LR
    subgraph S1["1. Delete por metadata"]
        direction TB
        D1["WHERE user_id = X"]
        D2["Requer metadata no insert"]
        D3["Rápido, mas não cobre sumários"]
    end
    subgraph S2["2. Re-embed"]
        direction TB
        R1["Remover eventos"]
        R2["Re-gerar sumários consolidados"]
        R3["Custo alto, mas consistente"]
    end
    subgraph S3["3. Cryptographic erasure"]
        direction TB
        C1["Encriptar por usuário"]
        C2["Destruir chave"]
        C3["Instantâneo, criptograficamente seguro"]
    end
```

---

## Resumo de Produção

| # | Nome | Tipo | Status | Slide |
|---|---|---|---|---|
| D1 | Recall accuracy (curva U) | Gráfico | 🆕 Novo | 9 |
| D2 | Comparação 4 camadas | Tabela | 🆕 Novo | 13 |
| D3 | 4 camadas integradas | Flowchart | ✅ Existe | 14 |
| D4 | MemGPT analogia SO | Analogia | 🆕 Novo | 16 |
| D5 | Comparação backends | Tabela | 🆕 Novo | 22 |
| D6 | Checkpointer resume | Flowchart | ✅ Existe | 24 |
| D7 | Branching (git graph) | Git graph | 🆕 Novo | 26 |
| D8 | Sumarização em cascata | Pirâmide | 🆕 Novo | 34 |
| D9 | Eviction flow | Flowchart | ✅ Existe | 36 |
| D10 | Entity-centric memory | Entidades | 🆕 Novo | 37 |
| D11 | Pipeline recall vetorial | Pipeline | 🆕 Novo | 46 |
| D12 | Consolidação episódica→semântica | Transformação | 🆕 Novo | 52 |
| D13 | Knowledge graph como memória | Grafo | 🆕 Novo | 54 |
| D14 | Memory stream (Generative Agents) | Timeline | 🆕 Novo | 56 |
| D15 | Consistência multi-agente | Sequência | 🆕 Novo | 59 |
| D16 | Direito ao esquecimento | Comparação | 🆕 Novo | 61 |

**Total**: 3 existentes + 13 novos = 16 diagramas únicos a produzir/manter.

---

## Pendências de Produção

- [ ] Produzir 13 diagramas novos (D1, D2, D4, D5, D7, D8, D10, D11, D12, D13, D14, D15, D16)
- [ ] Validar 3 diagramas existentes (D3, D6, D9) com a versão final dos slides
- [ ] Screenshot do demo de checkpointer em Postgres (Slide 28)
- [ ] Gráfico "Lost in the Middle" — curva U original (Slide 9)
- [ ] Dashboard de observabilidade de memória (Slide 63)
