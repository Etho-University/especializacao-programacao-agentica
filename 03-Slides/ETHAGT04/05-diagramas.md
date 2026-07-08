# ETHAGT04 — Sugestões de Diagramas

> 16 diagramas necessários para a apresentação.
> 4 já existem em `12-Diagrams/ETHAGT04/`. 12 novos a produzir.

---

## Diagramas Existentes (4)

| # | Slide | Arquivo | Descrição |
|---|---|---|---|
| D3 | 9 | `reasoning-spectrum.mmd` | Espectro do raciocínio: CoT → ReAct → ToT/LATS → reasoning nativo |
| D6 | 21 | `plan-execute.mmd` | Planner → plano → Executor → Replanner (loop) |
| D8 | 33 | `tot-search-tree.mmd` | Árvore de busca ToT com avaliação de estados e poda |
| D10 | 48 | `reflexion-loop.mmd` | Tentativa → Evaluator → Reflector → memória → nova tentativa |

> **Nota**: Os 4 diagramas existentes cobrem os fluxos centrais. Os demais aprofundam cada técnica.

---

## Diagramas Novos (12)

### D1 — Taxonomia Linear vs Árvore vs Grafo (Slide 11)

**Tipo**: Comparação lado a lado
**Descrição**: Três estruturas de raciocínio: linear (cadeia), árvore (ramificações com poda), grafo (nós interconectados com revisit)
**Mermaid**:
```mermaid
flowchart LR
    subgraph Linear["Linear (CoT)"]
        L1[passo 1] --> L2 --> L3 --> L4[resposta]
    end
    subgraph Arvore["Árvore (ToT)"]
        T1[root] --> T2[ramo A]
        T1 --> T3[ramo B]
        T2 --> T4[solução]
        T3 -.podar.-> TX[❌]
    end
    subgraph Grafo["Grafo (ReWOO/Reflexion)"]
        G1[plano] --> G2[worker 1]
        G1 --> G3[worker 2]
        G2 --> G4[solver]
        G3 --> G4
        G4 --> G5{revisar}
        G5 --> G1
    end
```

---

### D2 — Chain-of-Thought: Zero-shot vs Few-shot (Slide 13)

**Tipo**: Comparação
**Descrição**: Esquerda: prompt direto sem exemplo de raciocínio. Direita: prompt com exemplo "pensando passo a passo"
**Mermaid**:
```mermaid
flowchart TB
    subgraph Zero["Zero-shot CoT"]
        Z1["Prompt: 'Resolva: ...<br/>Pense passo a passo'"] --> Z2["LLM gera<br/>chain of thought"] --> Z3[resposta]
    end
    subgraph Few["Few-shot CoT"]
        F1["Prompt: 2-3 exemplos<br/>com raciocínio visível"] --> F2["LLM imita<br/>o padrão"] --> F3[resposta]
    end
```

---

### D4 — Self-Consistency (Slide 15)

**Tipo**: Diagrama de fluxo
**Descrição**: Mesmo prompt → N amostras (temperatura alta) → N cadeias de pensamento → votação da maioria
**Mermaid**:
```mermaid
flowchart TB
    P[prompt + CoT] --> S1[Amostra 1]
    P --> S2[Amostra 2]
    P --> SN[Amostra N]
    S1 --> V{Votação da<br/>maioria}
    S2 --> V
    SN --> V
    V --> Out[resposta consensual]
```

---

### D5 — Raciocínio Antes vs Durante a Ação (Slide 16)

**Tipo**: Comparação lado a lado
**Descrição**: Esquerda: planeja tudo antes (Plan-and-Execute). Direita: raciocina a cada step (ReAct)
**Mermaid**:
```mermaid
flowchart LR
    subgraph Antes["Planejar ANTES"]
        A1[problema] --> A2[plano completo] --> A3[executar] --> A4[resposta]
    end
    subgraph Durante["Raciocinar DURANTE"]
        D1[problema] --> D2[thought] --> D3[action] --> D4[observation]
        D4 --> D2
    end
```

---

### D7 — ReWOO: Plano Cego + Evidências Paralelas (Slide 24)

**Tipo**: Flowchart
**Descrição**: Planner gera plano com variáveis (#E1, #E2...) → Workers executam em paralelo → Solver substitui variáveis com evidências
**Mermaid**:
```mermaid
flowchart TB
    P([problema]) --> Planner["Planner<br/>gera plano com #E1, #E2, #E3"]
    Planner --> W1["Worker 1: #E1"]
    Planner --> W2["Worker 2: #E2"]
    Planner --> W3["Worker 3: #E3"]
    W1 --> Solver["Solver<br/>substitui variáveis"]
    W2 --> Solver
    W3 --> Solver
    Solver --> Out([resposta])

    classDef pl fill:#fce7f3,stroke:#be185d,color:#000
    classDef wk fill:#dbeafe,stroke:#1e40af,color:#000
    classDef sv fill:#dcfce7,stroke:#15803d,color:#000
    class Planner pl
    class W1,W2,W3 wk
    class Solver sv
```

---

### D9 — LATS: MCTS + LLM (Slide 37)

**Tipo**: Flowchart
**Descrição**: Seleção → Expansão → Avaliação (LLM) → Simulação → Backpropagation, com memória externa
**Mermaid**:
```mermaid
flowchart TB
    Root[raiz] --> Sel{Seleção<br/>UCB-1}
    Sel --> Exp[Expansão<br/>gerar N actions]
    Exp --> Eva[Avaliação<br/>LLM pontua estado]
    Eva --> Sim[Simulação<br/>rollout]
    Sim --> Back[Backpropagation<br/>atualizar valores]
    Back --> Ext{Solução<br/>encontrada?}
    Ext -- não --> Root
    Ext -- sim --> Out([resposta])
    Mem[("memória externa<br/>Reflexion")] -.-> Exp
```

---

### D11 — Reflexion: Estrutura de Memória (Slide 49)

**Tipo**: Diagrama de dados
**Descrição**: Estrutura da memória episódica de reflexões — cada tentativa gera uma reflexão verbal armazenada
**Mermaid**:
```mermaid
flowchart TB
    subgraph Mem["Memória de Reflexões (episódica)"]
        R1["Tentativa 1: 'Esqueci de verificar<br/>o formato da data'"]
        R2["Tentativa 2: 'A API retorna<br/>ISO 8601, não DD/MM'"]
        R3["Tentativa 3: 'Preciso checar<br/>timezone antes de comparar'"]
    end
    Mem --> Prompt["System Prompt + reflexões"]
    Prompt --> Agent["Agente ReAct<br/>(tentativa N+1)"]
    Agent --> Result{sucesso?}
    Result -- não --> Eval[Evaluator]
    Eval --> Refl[Self-Reflection]
    Refl --> Mem
```

---

### D12 — Reflexion vs Reflection Pattern Simples (Slide 52)

**Tipo**: Comparação
**Descrição**: Esquerda: reflection simples (critica e reescreve na mesma sessão). Direita: Reflexion (memória persiste entre tentativas, aprende com falhas anteriores)
**Mermaid**:
```mermaid
flowchart LR
    subgraph Simples["Reflection Pattern (simples)"]
        S1[gerar] --> S2[criticar] --> S3[reescrever]
        S3 --> S4[resposta]
    end
    subgraph Full["Reflexion (memória episódica)"]
        F1[tentativa 1] --> F2[falha]
        F2 --> F3[reflexão 1]
        F3 --> Mem[("memória")]
        Mem --> F4[tentativa 2<br/>+ reflexão 1]
        F4 --> F5[sucesso]
    end
```

---

### D13 — Self-Discover: Composição de Primitivas (Slide 58)

**Tipo**: Flowchart
**Descrição**: Fase 1 (Select) escolhe primitivas → Fase 2 (Adapt) adapta ao problema → Fase 3 (Implement) compõe reasoning module
**Mermaid**:
```mermaid
flowchart LR
    Prob[problema] --> Sel["Select<br/>escolher primitivas<br/>de um catálogo"]
    Sel --> Adapt["Adapt<br/>ajustar ao problema"]
    Adapt --> Impl["Implement<br/>compor reasoning<br/>module final"]
    Impl --> Exec["Executar<br/>raciocínio composto"]
    Exec --> Out([resposta])

    subgraph Catalog["Catálogo de primitivas"]
        P1[CoT]
        P2[Decomposição]
        P3[Pensamento crítico]
        P4[Analogia]
    end
    Catalog -.-> Sel
```

---

### D14 — Inference-Time Reasoning: Promptado vs Nativo (Slide 66)

**Tipo**: Comparação
**Descrição**: Esquerda: CoT promptado (você escreve "pense passo a passo"). Direita: reasoning model nativo (modelo pensa internamente, hidden chain)
**Mermaid**:
```mermaid
flowchart LR
    subgraph Prompt["Reasoning Promptado"]
        PR1["Prompt: 'Pense passo a passo'"] --> PR2[LLM] --> PR3["CoT visível<br/>no output"]
    end
    subgraph Native["Reasoning Nativo (o1/o3)"]
        NA1[Prompt] --> NA2["Reasoning interno<br/>(hidden tokens)"]
        NA2 --> NA3[Resposta final]
        NA2 -.conta tokens<br/>de reasoning.-> Budget["Orçamento<br/>de reasoning"]
    end
```

---

### D15 — Detecção de Loops (Slide 77)

**Tipo**: Diagrama de estado
**Descrição: Como detectar e quebrar loops: janela deslizante, hash de actions, contador de repetição
**Mermaid**:
```mermaid
flowchart TD
    Action[action atual] --> Hash{hash(action)<br/>em janela<br/>das últimas K?}
    Hash -- sim, ≥3x --> Alert[⚠️ LOOP detectado]
    Alert --> Break["Quebrar:<br/>1. Injetar reflexão<br/>2. Forçar replanejamento<br/>3. Escalar para HITL"]
    Hash -- não --> Continue[continuar execução]
    Break --> Result[nova action]
```

---

### D16 — Mapa de Decisão: Qual Técnica Usar? (Slide 85)

**Tipo**: Fluxograma de decisão
**Descrição**: Árvore de decisão para escolher a técnica de raciocínio
**Mermaid**:
```mermaid
flowchart TD
    Q([Problema]) --> S1{Consegue resolver<br/>em 1 chamada?}
    S1 -- sim --> CoT["CoT simples<br/>(+ Self-Consistency)"]
    S1 -- não --> S2{Precisa de tools<br/>durante o raciocínio?}
    S2 -- não --> S3{Cada passo é<br/>independente?}
    S2 -- sim --> S4{Custo é prioridade<br/>absoluta?}
    S3 -- sim --> PE["Plan-and-Execute<br/>ou ReWOO"]
    S3 -- não --> ToT["Tree of Thoughts<br/>ou LATS"]
    S4 -- sim --> ReWOO["ReWOO"]
    S4 -- não --> S5{Pode falhar e<br/>tentar de novo?}
    S5 -- sim --> Refl["Reflexion"]
    S5 -- não --> React["ReAct"]
    Q --> S6{Problema totalmente<br/>novo/inédito?}
    S6 -- sim --> SD["Self-Discover"]
    S6 -- não --> S1
```

---

## Resumo de Produção

| # | Nome | Tipo | Status | Slide |
|---|---|---|---|---|
| D1 | Linear vs árvore vs grafo | Comparação | 🆕 Novo | 11 |
| D2 | CoT zero-shot vs few-shot | Comparação | 🆕 Novo | 13 |
| D3 | Espectro do raciocínio | Flowchart | ✅ Existe | 9 |
| D4 | Self-Consistency | Fluxo | 🆕 Novo | 15 |
| D5 | Antes vs durante a ação | Comparação | 🆕 Novo | 16 |
| D6 | Plan-and-Execute | Flowchart | ✅ Existe | 21 |
| D7 | ReWOO (plano cego) | Flowchart | 🆕 Novo | 24 |
| D8 | ToT search tree | Árvore | ✅ Existe | 33 |
| D9 | LATS (MCTS + LLM) | Flowchart | 🆕 Novo | 37 |
| D10 | Reflexion loop | Flowchart | ✅ Existe | 48 |
| D11 | Memória de Reflexion | Dados | 🆕 Novo | 49 |
| D12 | Reflexion vs Reflection simples | Comparação | 🆕 Novo | 52 |
| D13 | Self-Discover composição | Flowchart | 🆕 Novo | 58 |
| D14 | Promptado vs nativo | Comparação | 🆕 Novo | 66 |
| D15 | Detecção de loops | Estado | 🆕 Novo | 77 |
| D16 | Árvore de decisão de técnica | Decisão | 🆕 Novo | 85 |

**Total**: 4 existentes + 12 novos = 16 diagramas.
