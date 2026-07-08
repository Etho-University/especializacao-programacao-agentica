# ETHAGT16 — Sugestões de Diagramas

> 19 diagramas referenciados pela apresentação.
> 3 já existem em `12-Diagrams/ETHAGT16/`. 16 novos a produzir.

---

## Diagramas Existentes (3)

| # | Slide | Arquivo | Descrição |
|---|---|---|---|
| D6 | 13 | `society.mmd` | Sociedade: papéis + normas + emergência |
| D10 | 25 | `research-pipeline.mmd` | Pipeline de pesquisa autônoma com HITL |
| D15 | 36 | `emergence.mmd` | Comportamento emergente: agentes → interações → padrões |

> **Nota**: Os 3 diagramas existentes cobrem 3 dos 19 necessários. Os demais (D1-D5, D7-D9, D11-D14, D16-D19) são novos.

---

## Diagramas Novos (16)

### D1 — Escala: 1 Agente → Sociedade → Emergência (Slide 5)

**Tipo**: Crescimento visual
**Descrição**: Sequência 1 ponto → 5 pontos (grupo) → 25 pontos (sociedade) → 100 pontos (emergência)
**Mermaid**:
```mermaid
flowchart LR
    A["1 agente<br/>(ponto)"]
    B["5 agentes<br/>(grupo)"]
    C["25 agentes<br/>(sociedade)"]
    D["100+ agentes<br/>(emergência)"]
    A --> B --> C --> D
```
**Estilo**: Pontos surgem e formam rede. Cores `etho-primary` → `etho-accent`.

---

### D2 — Timeline de Marcos 2022-2024 (Slide 6)

**Tipo**: Timeline horizontal
**Descrição**: ReAct (2022) → tool calling + multi-agent frameworks (2023) → Generative Agents / Smallville (abr/2023) → AI Scientist + AlphaEvolve (2024)
**Mermaid**:
```mermaid
timeline
    title Marcos de sociedades de agentes
    2022 : ReAct (Yao et al.)
    2023 : Tool calling nativo
         : Multi-agent frameworks
         : Generative Agents (Smallville, abr/2023)
    2024 : AI Scientist (Sakana, ago/2024)
         : AlphaEvolve (DeepMind)
    2025+ : Sociedades autônomas
```

---

### D3 — Escada de 4 Níveis: Agente → Sociedade (Slide 8)

**Tipo**: Escada
**Descrição**: Nível 0 (agente individual) → Nível 1 (grupo) → Nível 2 (instituição) → Nível 3 (sociedade)
**Mermaid**:
```mermaid
flowchart TB
    L3["Nível 3: Sociedade (25+ agentes, emergência)"]
    L2["Nível 2: Instituição (papéis, normas, hierarquia)"]
    L1["Nível 1: Pequeno grupo (2-5 agentes)"]
    L0["Nível 0: Agente individual (LLM + tools + memory)"]
    L3 --> L2 --> L1 --> L0
```

---

### D4 — 5 Papéis em Círculo (Slide 9)

**Tipo**: Mind map radial
**Descrição**: Pesquisador, Crítico, Sintetizador, Revisor, Editor em círculo
**Mermaid**:
```mermaid
mindmap
  root((Sociedade))
    Pesquisador
      explora
      levanta informação
    Crítico
      identifica falhas
      questiona premissas
    Sintetizador
      integra divergentes
    Revisor
      valida qualidade
      coherence
    Editor
      finaliza
      publica
```

---

### D5 — Grafo de Confiança / Reputação (Slide 11)

**Tipo**: Grafo com pesos
**Descrição**: Agentes como nós, arestas com peso de confiança
**Mermaid**:
```mermaid
flowchart LR
    A((A))
    B((B))
    C((C))
    D((D))
    A == "0.9" ==> B
    B == "0.7" ==> C
    C == "0.4" ==> D
    A == "0.2" ==> D
    A == "0.8" ==> C
```
**Estilo**: Arestas grossas = alta confiança; finas/vermelhas = baixa confiança.

---

### D7 — Grupo vs Instituição vs Sociedade (Slide 14)

**Tipo**: 3 colunas comparativas
**Descrição**: Eixos controle / adaptabilidade / previsibilidade / risco
**Mermaid**:
```mermaid
flowchart LR
    subgraph G["Grupo"]
        G1["Controle: alto"]
        G2["Adaptabilidade: baixa"]
        G3["Previsibilidade: alta"]
        G4["Risco: baixo"]
    end
    subgraph I["Instituição"]
        I1["Controle: médio"]
        I2["Adaptabilidade: médio"]
        I3["Previsibilidade: média"]
        I4["Risco: médio"]
    end
    subgraph S["Sociedade"]
        S1["Controle: baixo"]
        S2["Adaptabilidade: alta"]
        S3["Previsibilidade: baixa"]
        S4["Risco: alto"]
    end
```

---

### D8 — Mapa de Smallville (Slide 17)

**Tipo**: Mapa estilizado
**Descrição**: Mapa de Smallville (parque, café, casas, escola) com agentes distribuídos
**Estilo**: Imagem ilustrativa baseada em Park et al. (arXiv:2304.03442).

---

### D9 — Pipeline Smallville: Memory → Reflection → Action (Slide 18)

**Tipo**: Flowchart
**Descrição**: Memory stream → Retrieval (recência + relevância + importância) → Reflection → Planning → Action
**Mermaid**:
```mermaid
flowchart LR
    M["Memory stream<br/>(log cronológico)"]
    R["Retrieval<br/>(recência + relevância + importância)"]
    Ref["Reflection<br/>(síntese de alto nível)"]
    P["Planning<br/>(rotina + objetivos)"]
    A["Action"]
    M --> R --> Ref --> P --> A
```

---

### D11 — Fluxo AI Scientist em 5 Etapas (Slide 26)

**Tipo**: Flowchart
**Descrição**: Ideação → Literatura → Código → Experimento → Paper
**Mermaid**:
```mermaid
flowchart LR
    I["1. Ideação"] --> L["2. Literatura"]
    L --> C["3. Código"]
    C --> E["4. Experimento"]
    E --> P["5. Paper"]
    P -. "~$15/paper" .- Cost([custo])
```

---

### D12 — AI Scientist 4 Stages com Feedback (Slide 27)

**Tipo**: Pipeline com loop
**Descrição**: Ideation → Experimentation → Paper writing → Review com loop de revisão
**Mermaid**:
```mermaid
flowchart LR
    S1["Stage 1<br/>Ideation"]
    S2["Stage 2<br/>Experimentação<br/>(escreve + roda código)"]
    S3["Stage 3<br/>Paper writing<br/>(LaTeX)"]
    S4["Stage 4<br/>Review<br/>(LLM como reviewer)"]
    Dec{"Continuar,<br/>refinar,<br/>abandonar?"}
    S1 --> S2 --> S3 --> S4 --> Dec
    Dec -- "refinar" --> S2
    Dec -- "continuar" --> Out([paper])
    Dec -- "abandonar" --> Drop([descartar])
```

---

### D13 — Loop Evolutivo AlphaEvolve (Slide 28)

**Tipo**: Loop
**Descrição**: LLM propõe mutações → avaliador testa → mantém melhores → LLM
**Mermaid**:
```mermaid
flowchart LR
    L["LLM<br/>propõe mutação"]
    M["Mutação no código"]
    E["Avaliador automático<br/>(executa e mede)"]
    Sel["Seleção<br/>(mantém melhores)"]
    L --> M --> E --> Sel
    Sel -. "feedback" .-> L
```

---

### D14 — Time de 4 Agentes com Canal de Comunicação (Slide 29)

**Tipo**: Diagrama de equipe
**Descrição**: Pesquisador, Programador, Revisor, Escritor com canal compartilhado
**Mermaid**:
```mermaid
flowchart TB
    Bus["Canal de comunicação compartilhado"]
    P["Pesquisador"]
    Pr["Programador"]
    Re["Revisor"]
    Es["Escritor"]
    Bus <--> P
    Bus <--> Pr
    Bus <--> Re
    Bus <--> Es
```

---

### D16 — Emergência Desejada vs Indesejada (Slide 37)

**Tipo**: 2 colunas
**Descrição**: Esquerda (verde) desejada; direita (vermelho) indesejada
**Mermaid**:
```mermaid
flowchart LR
    subgraph Des["Desejada (verde)"]
        D1["Cooperação espontânea"]
        D2["Divisão de trabalho"]
        D3["Inovação"]
        D4["Formação de normas"]
    end
    subgraph Ind["Indesejada (vermelho)"]
        I1["Conluio"]
        I2["Discriminação"]
        I3["Echo chamber"]
        I4["Corrida armamentista"]
    end
```

---

### D17 — Pirâmide de Alinhamento (Slide 38)

**Tipo**: Pirâmide (camadas)
**Descrição**: Base = valores individuais; meio = normas sociais; topo = constitution
**Mermaid**:
```mermaid
flowchart TB
    Top["Constitution (regras globais)"]
    Mid["Normas sociais (votação, reputação)"]
    Bas["Valores individuais (alinhamento por agente)"]
    Top --> Mid --> Bas
```

---

### D18 — Mapa da Fronteira de Pesquisa (Slide 43)

**Tipo**: Mind map
**Descrição**: Fronteira no centro com AI Scientist, AlphaEvolve, AutoGen research, Swarm research
**Mermaid**:
```mermaid
mindmap
  root((Fronteira 2024+))
    AI Scientist
      Sakana
      ML end-to-end
    AlphaEvolve
      DeepMind
      evolução de algoritmos
    AutoGen research
      multi-agent framework
    Swarm research
      grandes populações
    Constitutional AI
      sociedades
```

---

### D19 — Mapa da Especialização ETHAGT01 → ETHAGT90 (Slide 49)

**Tipo**: Timeline / mapa
**Descrição**: Augmented LLM (ETHAGT01) → ... → Sociedades (ETHAGT16) → Capstone (ETHAGT90)
**Mermaid**:
```mermaid
flowchart LR
    A["ETHAGT01<br/>Augmented LLM"]
    B["ETHAGT04-10<br/>Reasoning, Memory, RAG, Multi-Agent"]
    C["ETHAGT12-15<br/>AgentOps, Security, Eval"]
    D["ETHAGT16<br/>Sociedades + Research"]
    E["ETHAGT90<br/>Capstone"]
    A --> B --> C --> D --> E
```

---

## Resumo de Produção

| # | Nome | Tipo | Status | Slide |
|---|---|---|---|---|
| D1 | Escala agente → sociedade | Crescimento | 🆕 Novo | 5 |
| D2 | Timeline de marcos | Timeline | 🆕 Novo | 6 |
| D3 | Escada de 4 níveis | Escada | 🆕 Novo | 8 |
| D4 | 5 papéis em círculo | Mind map | 🆕 Novo | 9 |
| D5 | Grafo de confiança | Grafo | 🆕 Novo | 11 |
| D6 | Sociedade de agentes | Flowchart | ✅ Existe | 13 |
| D7 | Grupo vs Instituição vs Sociedade | Colunas | 🆕 Novo | 14 |
| D8 | Mapa de Smallville | Mapa | 🆕 Novo | 17 |
| D9 | Pipeline Smallville | Flowchart | 🆕 Novo | 18 |
| D10 | Research pipeline | Flowchart | ✅ Existe | 25 |
| D11 | Fluxo AI Scientist 5 etapas | Flowchart | 🆕 Novo | 26 |
| D12 | AI Scientist 4 stages + feedback | Pipeline | 🆕 Novo | 27 |
| D13 | Loop AlphaEvolve | Loop | 🆕 Novo | 28 |
| D14 | Time de 4 agentes | Diagrama | 🆕 Novo | 29 |
| D15 | Emergência | Flowchart | ✅ Existe | 36 |
| D16 | Desejada vs indesejada | 2 colunas | 🆕 Novo | 37 |
| D17 | Pirâmide de alinhamento | Pirâmide | 🆕 Novo | 38 |
| D18 | Mapa da fronteira | Mind map | 🆕 Novo | 43 |
| D19 | Mapa da especialização | Timeline | 🆕 Novo | 49 |

**Total**: 3 existentes + 16 novos = 19 diagramas a produzir/manter.
