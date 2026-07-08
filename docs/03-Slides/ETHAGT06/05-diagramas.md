# ETHAGT06 — Sugestões de Diagramas

> 17 diagramas necessários para a apresentação.
> 3 já existem em `12-Diagrams/ETHAGT06/`. 14 novos a produzir.

---

## Diagramas Existentes (3)

| # | Slide | Arquivo | Descrição |
|---|---|---|---|
| D5 | 19 | `adaptive-rag.mmd` | Adaptive RAG: classificador → 3 caminhos |
| D7 | 28 | `crag-flow.mmd` | CRAG: avaliador → usar/corrigir/web |
| D16 | 72 | `eval-pipeline.mmd` | Pipeline de avaliação com métricas Ragas |

---

## Diagramas Novos (14)

### D1 — Evolução RAG Fixo → RAG Agêntico (Slide 7)

**Tipo**: Timeline horizontal
**Descrição**: Marcos históricos de 2020 a 2025 com 4 arquiteturas
**Mermaid**:
```mermaid
flowchart LR
    A["2020<br/>RAG original<br/>(Lewis et al.)"] --> B["2023<br/>Self-RAG<br/>(Asai)"]
    B --> C["2024<br/>CRAG<br/>(Yan)"]
    C --> D["2024<br/>GraphRAG<br/>(Edge)"]
    D --> E["2025<br/>Agentic RAG"]
    E --> F["Agente decide<br/>quando/o quê/como"]
```
**Estilo**: Marcos em `etho-primary`, setas em `etho-accent`.

---

### D2 — Pipeline do RAG Ingênuo com Pontos de Falha (Slide 9)

**Tipo**: Flowchart com marcações
**Descrição**: Pipeline canônico com 4 pontos de falha destacados em vermelho
**Mermaid**:
```mermaid
flowchart LR
    Q[query] --> E[embed] --> V[vector search<br/>top-k] --> S[stuff into prompt] --> G[generate]
    E -. "Falha 1:<br/>sinônimos não capturados" .-> X1[⚠️]
    V -. "Falha 2:<br/>top-k traz irrelevante" .-> X2[⚠️]
    S -. "Falha 3:<br/>contexto quebrado" .-> X3[⚠️]
    G -. "Falha 4:<br/>alucinação sobre docs ruins" .-> X4[⚠️]
```

---

### D3 — 4 Tipos de Falha do RAG (Slides 10-13)

**Tipo**: Grid 2x2
**Descrição**: Chunking, embedding, re-rank, avaliação
**Mermaid**:
```mermaid
flowchart TB
    subgraph F1["Falha 1: Chunking"]
        direction TB
        A1["Corta contexto"]
        A2["512 tokens fixo"]
    end
    subgraph F2["Falha 2: Embedding"]
        direction TB
        B1["Similaridade lexical"]
        B2["Não captura semântica"]
    end
    subgraph F3["Falha 3: Sem Re-Rank"]
        direction TB
        C1["Top-k = top-lixo"]
        C2["1 bom + 4 irrelevantes"]
    end
    subgraph F4["Falha 4: Sem Avaliação"]
        direction TB
        D1["Cego em produção"]
        D2["Funciona na demo"]
    end
```

---

### D4 — Casos Problemáticos (Slide 14)

**Tipo**: Grid 3 colunas
**Descrição**: Dados tabulares, multilingual, multimodal
**Mermaid**:
```mermaid
flowchart TB
    subgraph T["Tabular"]
        direction TB
        T1["Embeddings não capturam<br/>estrutura de tabela"]
        T2["Solução: SQL + texto"]
    end
    subgraph M["Multilingual"]
        direction TB
        M1["Mesma ideia em PT vs EN<br/>→ distância alta"]
        M2["Solução: multilingual embeddings"]
    end
    subgraph MM["Multimodal"]
        direction TB
        MM1["Texto + imagem + tabela<br/>exigem estratégias"]
        MM2["Solução: CLIP / GPT-4V"]
    end
```

---

### D6 — Implementação Adaptive RAG em LangGraph (Slide 21)

**Tipo**: Flowchart
**Descrição**: StateGraph com nós e conditional edges
**Mermaid**:
```mermaid
flowchart TB
    Start([state]) --> Route["route_query<br/>(classificador)"]
    Route -- "no retrieval" --> Gen
    Route -- "simple" --> Ret["retrieve top-3"]
    Route -- "complex" --> RW["query_rewrite"]
    RW --> Ret2["retrieve"]
    Ret --> Gen["generate"]
    Ret2 --> Gen
    Gen --> End([resposta])
```
> **Nota**: Espelha o exemplo `adaptive_rag` do LangGraph.

---

### D8 — Self-RAG Flow com Tokens de Reflexão (Slide 38)

**Tipo**: Flowchart com tokens nos edges
**Descrição**: Fluxo controlado por tokens `[Retrieve]`, `[Relevant]`, `[Fully supported]`
**Mermaid**:
```mermaid
flowchart TB
    Q([pergunta]) --> R{"[Retrieve?]<br/>precisa recuperar?"}
    R -- "sim" --> Ret[retrieve]
    R -- "não" --> G[generate]
    Ret --> Rel{"[Relevant?]<br/>doc relevante?"}
    Rel -- "sim" --> G
    Rel -- "não" --> Ret
    G --> Sup{"[Fully supported?]<br/>resposta suportada?"}
    Sup -- "sim" --> Out([resposta])
    Sup -- "não" --> G
```

---

### D9 — Comparação Adaptive vs CRAG vs Self-RAG (Slide 42)

**Tipo**: Tabela 3 colunas
**Descrição**: Checkpoints destacados por arquitetura
**Mermaid**:
```mermaid
flowchart LR
    subgraph A["Adaptive RAG"]
        direction TB
        A1["Decide SE recuperar ✅"]
        A2["Avalia docs ❌"]
        A3["Avalia resposta ❌"]
    end
    subgraph C["CRAG"]
        direction TB
        C1["Decide SE recuperar ❌"]
        C2["Avalia docs ✅"]
        C3["Avalia resposta ❌"]
    end
    subgraph S["Self-RAG"]
        direction TB
        S1["Decide SE recuperar ✅"]
        S2["Avalia docs ✅"]
        S3["Avalia resposta ✅"]
    end
```

---

### D10 — Multi-Hop Retrieval (Slide 48)

**Tipo**: Sequência encadeada
**Descrição**: Cadeia de buscas dependentes
**Mermaid**:
```mermaid
flowchart LR
    Q["Quem fundou a empresa<br/>que criou o ChatGPT?"]
    Q --> H1["Hop 1:<br/>quem criou o ChatGPT?<br/>→ OpenAI"]
    H1 --> H2["Hop 2:<br/>quem fundou a OpenAI?<br/>→ Sam Altman et al."]
    H2 --> A["Síntese:<br/>Sam Altman, Elon Musk, ..."]
```

---

### D11 — GraphRAG: Do Local ao Global (Slide 52)

**Tipo**: Flowchart
**Descrição**: Pipeline de extração → comunidades → sumarização
**Mermaid**:
```mermaid
flowchart LR
    Corpus[Corpus] --> Ext["Extrair entidades<br/>e relações"]
    Ext --> Comm["Agrupar em<br/>comunidades"]
    Comm --> Sum["Sumarizar<br/>comunidades"]
    Sum --> Q[/"Pergunta global?<br/>recuperar subgrafo"/]
```

---

### D12 — Escalada Adaptive → CRAG → Self-RAG → Agentic (Slide 55)

**Tipo**: Escada/pirâmide
**Descrição**: 4 níveis crescentes em complexidade e controle
**Mermaid**:
```mermaid
flowchart TB
    L4["Agentic: agente dirige tudo<br/>(planeja, busca, refina, para)"]
    L4 --> L3["Self-RAG: avalia docs + resposta"]
    L3 --> L2["CRAG: avalia docs, fallback web"]
    L2 --> L1["Adaptive: decide SE recuperar"]
    L1 --> Base([Comece aqui])
    L1 -. "custo baixo" .-> C1[baixo]
    L4 -. "custo alto" .-> C4[alto]
```

---

### D13 — Estratégias de Chunking (Slides 57-59)

**Tipo**: Comparação 4 colunas
**Descrição**: Fixo, semântico, hierárquico, late-chunking
**Mermaid**:
```mermaid
flowchart LR
    subgraph CF["Fixo"]
        direction TB
        CF1["512 tokens"]
        CF2["Corta contexto"]
    end
    subgraph CS["Semântico"]
        direction TB
        CS1["Agrupa por tópicos"]
        CS2["Preserva semântica"]
    end
    subgraph CH["Hierárquico"]
        direction TB
        CH1["Seção → parágrafo"]
        CH2["Parent-child"]
    end
    subgraph CL["Late Chunking"]
        direction TB
        CL1["Contexto do doc"]
        CL2["Embeddings ricos"]
    end
```

---

### D14 — HyDE Flow (Slide 62)

**Tipo**: Sequência
**Descrição**: pergunta → resposta hipotética → embed → search
**Mermaid**:
```mermaid
flowchart LR
    Q[pergunta] --> H["Gerar resposta<br/>HIPOTÉTICA"]
    H --> E["Embed da<br/>resposta hipotética"]
    E --> S["Vector search"]
    S --> D[docs relevantes]
```

---

### D15 — Hybrid Search: BM25 + Densa (Slide 63)

**Tipo**: Flowchart com fusão
**Descrição**: Dois ramos (BM25 + densa) → reciprocal rank fusion
**Mermaid**:
```mermaid
flowchart TB
    Q[query] --> B["BM25<br/>(lexical)"]
    Q --> D["Densa<br/>(embedding)"]
    B --> RRF["Reciprocal Rank Fusion<br/>(RRF)"]
    D --> RRF
    RRF --> Top["top-k final"]
```

---

### D17 — Matriz Precision × Recall (Slide 73)

**Tipo**: Matriz 2x2
**Descrição**: Quadrantes de qualidade de retrieval com re-ranking
**Mermaid**:
```mermaid
flowchart TB
    subgraph Q1["Alta precision, Baixa recall"]
        direction TB
        Q1A["Poucos docs, todos bons<br/>Faltam alguns"]
    end
    subgraph Q2["Alta precision, Alta recall"]
        direction TB
        Q2A["✅ Ideal<br/>re-rank ajuda aqui"]
    end
    subgraph Q3["Baixa precision, Baixa recall"]
        direction TB
        Q3A["❌ Catastrófico"]
    end
    subgraph Q4["Baixa precision, Alta recall"]
        direction TB
        Q4A["Muitos docs, muito ruído<br/>Top-k puro"]
    end
```

---

## Resumo de Produção

| # | Nome | Tipo | Status | Slide |
|---|---|---|---|---|
| D1 | Evolução RAG fixo → agêntico | Timeline | 🆕 Novo | 7 |
| D2 | Pipeline ingênuo com falhas | Flowchart | 🆕 Novo | 9 |
| D3 | 4 tipos de falha (grid) | Grid 2x2 | 🆕 Novo | 10-13 |
| D4 | Casos problemáticos | Grid 3 col | 🆕 Novo | 14 |
| D5 | Adaptive RAG | Flowchart | ✅ Existe | 19 |
| D6 | Adaptive RAG em LangGraph | Flowchart | 🆕 Novo | 21 |
| D7 | CRAG Flow | Flowchart | ✅ Existe | 28 |
| D8 | Self-RAG (tokens de reflexão) | Flowchart | 🆕 Novo | 38 |
| D9 | Comparação Adaptive/CRAG/Self-RAG | Tabela | 🆕 Novo | 42 |
| D10 | Multi-hop retrieval | Sequência | 🆕 Novo | 48 |
| D11 | GraphRAG (local → global) | Flowchart | 🆕 Novo | 52 |
| D12 | Escalada Adaptive→Agentic | Escada | 🆕 Novo | 55 |
| D13 | Estratégias de chunking | Comparação | 🆕 Novo | 57-59 |
| D14 | HyDE flow | Sequência | 🆕 Novo | 62 |
| D15 | Hybrid search (BM25 + densa) | Flowchart | 🆕 Novo | 63 |
| D16 | Eval pipeline | Flowchart | ✅ Existe | 72 |
| D17 | Matriz precision × recall | Matriz | 🆕 Novo | 73 |

**Total**: 3 existentes + 14 novos = 17 diagramas a produzir/manter.
