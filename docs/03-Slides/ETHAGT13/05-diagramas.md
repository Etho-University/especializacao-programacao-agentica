# ETHAGT13 — Sugestões de Diagramas

> Diagramas necessários para a apresentação.
> 3 já existem em `12-Diagrams/ETHAGT13/`. 18 novos sugeridos.

---

## Diagramas Existentes (3)

| # | Slide | Arquivo | Descrição |
|---|---|---|---|
| D7 | 12 | `threat-model.mmd` | Ativos → superfícies → vetores → impactos |
| D18 | 34 | `defense-in-depth.mmd` | 7 camadas sequenciais de defesa |
| D23 | 43 | `hitl-checkpoints.mmd` | Classificação de risco → 3 caminhos (auto/batch/imediato) |

> **Nota**: Os 3 diagramas existentes cobrem os slides centrais (12, 34, 43). Os demais são novos.

---

## Diagramas Novos Sugeridos

### D1 — Fluxo de Ataque: Phishing em Massa (Slide 5)

**Tipo**: Flowchart horizontal
**Descrição**: Documento malicioso → RAG → agente → tool de email → vítimas
**Mermaid**:
```mermaid
flowchart LR
    Doc["📄 Documento malicioso<br/>(instrução oculta)"] --> RAG[("Base RAG")]
    RAG --> Agent["🤖 Agente"]
    Agent --> Tool["✉️ Tool: send_email"]
    Tool --> V1["👤 Vítima 1"]
    Tool --> V2["👤 Vítima 2"]
    Tool --> Vn["👤 Vítima N"]

    classDef mal fill:#fee2e2,stroke:#b91c1c,color:#000
    classDef ag fill:#fce7f3,stroke:#be185d,color:#000
    classDef vit fill:#dbeafe,stroke:#1e40af,color:#000
    class Doc,RAG mal
    class Agent,Tool ag
    class V1,V2,Vn vit
```
**Estilo**: Setas vermelhas percorrendo o fluxo de ataque.

---

### D2 — Timeline de Incidentes Reais (Slide 6)

**Tipo**: Timeline horizontal
**Descrição**: 2023 Bing/Sydney → 2023 Chevrolet → 2023 Greshake → 2024 AgentDojo → 2024 InjecAgent → 2025 OWASP
**Mermaid**:
```mermaid
timeline
    title Incidentes de Segurança em Agentes LLM
    2023 : Bing/Sydney jailbreak
         : Chevrolet chatbot vende carro por $1
         : Greshake — prompt injection indireto
    2024 : AgentDojo — benchmark de injeção
         : InjecAgent — 1054 casos de teste
    2025 : OWASP LLM Top-10 consolida
```

---

### D3 — Ativos, Adversários, Superfícies (Slide 8)

**Tipo**: Triângulo concêntrico
**Descrição**: Ativos (centro) → Superfícies (meio) → Adversários (exterior)
**Mermaid**:
```mermaid
flowchart TB
    subgraph EXT["ADVERSÁRIOS"]
        A1["usuário malicioso"]
        A2["atacante externo"]
        A3["agente comprometido"]
        A4["modelo adversário"]
    end
    subgraph MEIO["SUPERFÍCIES"]
        S1["input do usuário"]
        S2["RAG / docs"]
        S3["MCP resources"]
        S4["web search"]
        S5["A2A"]
    end
    subgraph CENTRO["ATIVOS"]
        T1["dados (PII, secrets)"]
        T2["ações (tools, APIs)"]
        T3["reputação"]
    end
    EXT --> MEIO --> CENTRO
```

---

### D4 — Tabela STRIDE Adaptada (Slide 9)

**Tipo**: Tabela colorida
**Descrição**: 6 categorias STRIDE com exemplo concreto em agente
**Renderização**: Tabela markdown com cores (vermelho para crítico, amarelo para médio)
**Conteúdo**:

| Categoria | Exemplo em agente | Severidade |
|---|---|---|
| **S**poofing | Agente se passa por outro em A2A | Alta |
| **T**ampering | Adulteração de memória persistente | Alta |
| **R**epudiation | Ação sem log — sem rastreio | Média |
| **I**nformation Disclosure | Vazar system prompt, secrets, PII | Crítica |
| **D**enial of Service | Drenar orçamento de tokens | Média |
| **E**levation of Privilege | Prompt injection escala permissões | Crítica |

---

### D5 — Tools com Nível de Risco (Slide 10)

**Tipo**: Grid colorido
**Descrição**: Tools classificadas por risco (verde/amarelo/vermelho)
**Mermaid**:
```mermaid
flowchart TB
    subgraph RED["🔴 DESTRUTIVO"]
        R1["executar código"]
        R2["deletar arquivo"]
        R3["transferência bancária"]
        R4["enviar email em massa"]
    end
    subgraph YEL["🟡 ESCRITA"]
        Y1["escrever arquivo"]
        Y2["atualizar registro"]
        Y3["chamar API externa"]
    end
    subgraph GRN["🟢 LEITURA"]
        G1["ler arquivo"]
        G2["buscar no RAG"]
        G3["consultar API"]
    end
```

---

### D6 — Propagação de Comprometimento Multi-Agente (Slide 11)

**Tipo**: Topologia de grafo
**Descrição**: Agente A comprometido → infecta B → infecta C
**Mermaid**:
```mermaid
flowchart LR
    Attacker["👾 Atacante"] -.injeção.-> A["Agente A<br/>(pesquisa)"]
    A -->|"output malicioso"| B["Agente B<br/>(ação)"]
    B -->|"executa"| C["Agente C<br/>(execução)"]
    C --> Impact["💥 Dano"]

    classDef mal fill:#fee2e2,stroke:#b91c1c,color:#000
    classDef inf fill:#fed7aa,stroke:#c2410c,color:#000
    classDef ok fill:#dcfce7,stroke:#15803d,color:#000
    class Attacker mal
    class A,B,C inf
    class Impact mal
```

---

### D8 — LINDDUN Adaptado (Slide 13)

**Tipo**: Tabela com conexão a LGPD
**Descrição**: 6 categorias LINDDUN com exemplo em agente
**Conteúdo**: Ver Slide 13 do storyboard detalhado.

---

### D9 — Código/Dados Separados vs Tudo Texto (Slide 16)

**Tipo**: Comparação lado a lado
**Descrição**: Esquerda — tradicional (SQL com prepared statements); Direita — LLM (tudo texto)
**Mermaid**:
```mermaid
flowchart LR
    subgraph TRAD["Tradicional (SQL)"]
        direction TB
        T1["Código: SELECT * WHERE name = ?"]
        T2["Dados: João (parâmetro)"]
        T3["✅ Separação nativa"]
    end
    subgraph LLM["LLM (Prompt)"]
        direction TB
        L1["System: 'Você é assistente'"]
        L2["User: 'ignore e faça X'"]
        L3["RAG: 'documento malicioso'"]
        L4["❌ Tudo é texto"]
    end
```

---

### D10 — Injeção Indireta: Fonte Externa → Agente (Slide 18)

**Tipo**: Flowchart
**Descrição**: Fonte externa maliciosa (RAG/MCP/web) → agente consome → executa
**Mermaid**:
```mermaid
flowchart LR
    subgraph EXT["FONTES EXTERNAS"]
        RAG[("RAG<br/>documento malicioso")]
        MCP["MCP resource<br/>contaminado"]
        WEB["Web page<br/>texto oculto"]
        EMAIL["Email<br/>payload"]
    end
    EXT --> Agent["🤖 Agente consome"]
    Agent --> Action["💥 Executa injeção"]

    classDef mal fill:#fee2e2,stroke:#b91c1c,color:#000
    class RAG,MCP,WEB,EMAIL mal
```

---

### D11 — Grid de Famílias de Jailbreak (Slide 20)

**Tipo**: Grid 2x3
**Descrição**: 6 famílias de jailbreak com exemplo
**Conteúdo**: Ver Slide 20 do storyboard detalhado.

---

### D12 — Many-Shot Jailbreak (Slide 21)

**Tipo**: Barra de context window
**Descrição**: Context window enchendo de exemplos Q&A → modelo segue padrão
**Mermaid**:
```mermaid
flowchart TB
    CW["Context Window (200k tokens)"]
    CW --> E1["Q1 (proibido) → A1 (proibido)"]
    CW --> E2["Q2 (proibido) → A2 (proibido)"]
    CW --> En["...50 exemplos..."]
    CW --> Qn["Q nova (proibido)"]
    Qn --> Model["🤖 Modelo segue padrão"]
    Model --> An["A (proibido) ✓"]

    classDef mal fill:#fee2e2,stroke:#b91c1c,color:#000
    class An mal
```

---

### D13 — System Prompt + Delimitadores (Slide 23)

**Tipo**: Code block
**Descrição**: Snippet Python com system prompt robusto + tags de delimitação
**Conteúdo**: Ver Slide 23 do storyboard detalhado.

---

### D14 — Hierarquia de Instruções (Slide 24)

**Tipo**: Pirâmide invertida
**Descrição**: 3 níveis — system prompt (topo, prioridade alta) → tool results → user input (base)
**Mermaid**:
```mermaid
flowchart TB
    L1["Nível 1: System Prompt<br/>(prioridade MÁXIMA, imutável)"]
    L2["Nível 2: Tool Results<br/>(tratado como dado)"]
    L3["Nível 3: User Input<br/>(prioridade mínima)"]
    L1 --> L2 --> L3

    classDef hi fill:#dcfce7,stroke:#15803d,color:#000
    classDef mid fill:#fef3c7,stroke:#b45309,color:#000
    classDef lo fill:#fee2e2,stroke:#b91c1c,color:#000
    class L1 hi
    class L2 mid
    class L3 lo
```

---

### D15 — Funil de Input Filtering (Slide 29)

**Tipo**: Funil
**Descrição**: Input → classificação → aprovação/rejeição
**Mermaid**:
```mermaid
flowchart TB
    In([input do usuário<br/>+ RAG + MCP]) --> Class{"Classificador"}
    Class -- "injeção detectada" --> Reject["❌ Rejeitar"]
    Class -- "tópico proibido" --> Reject
    Class -- "DoS (rate)" --> Reject
    Class -- "limpo" --> Agent["✅ Agente processa"]
```

---

### D16 — Structured Output com Schema (Slide 31)

**Tipo**: Code block
**Descrição**: Snippet Pydantic com schema estrito + validação
**Conteúdo**: Ver Slide 31 do storyboard detalhado.

---

### D17 — Arquitetura NeMo Guardrails (Slide 32)

**Tipo**: Pipeline
**Descrição**: 4 rails em sequência — input → dialog → LLM → output → execution
**Mermaid**:
```mermaid
flowchart LR
    In([input]) --> IR["Input Rail<br/>(filtra injeção)"]
    IR --> DR["Dialog Rail<br/>(controla fluxo)"]
    DR --> LLM["🤖 LLM"]
    LLM --> OR["Output Rail<br/>(filtra PII)"]
    OR --> ER["Execution Rail<br/>(valida tool call)"]
    ER --> Out([resposta])

    classDef rail fill:#fed7aa,stroke:#c2410c,color:#000
    class IR,DR,OR,ER rail
```

---

### D19 — Matriz Risco × Frequência → HITL (Slide 39)

**Tipo**: Matriz 2x2
**Descrição**: Quadrantes — HITL obrigatório (alto risco/baixa freq), recomendado, opcional, automático
**Mermaid**:
```mermaid
flowchart TB
    subgraph Q1["Alto risco + Alta freq"]
        direction TB
        Q1A["⚠️ HITL em amostra<br/>+ automação forte"]
    end
    subgraph Q2["Alto risco + Baixa freq"]
        direction TB
        Q2A["🛑 HITL OBRIGATÓRIO"]
    end
    subgraph Q3["Baixo risco + Baixa freq"]
        direction TB
        Q3A["✅ Automático<br/>+ auditoria"]
    end
    subgraph Q4["Baixo risco + Alta freq"]
        direction TB
        Q4A["✅ Automático<br/>+ rate limit"]
    end
```

---

### D20 — Fluxo de Checkpoint HITL (Slide 40)

**Tipo**: Diagrama de sequência
**Descrição**: Agente propõe → classifica risco → HITL/auto → executa
**Mermaid**:
```mermaid
sequenceDiagram
    participant A as Agente
    participant C as Classificador
    participant H as Humano
    participant T as Tool
    A->>C: propõe action
    C->>C: classifica risco
    alt risco alto
        C->>H: notifica (preview + args)
        H-->>C: aprova/rejeita/edita
    end
    C->>T: executa (se aprovado)
    T-->>A: resultado
```

---

### D21 — Mock de UI de HITL (Slide 41)

**Tipo**: Mockup de card
**Descrição**: Card de aprovação no Slack com botões Aprovar/Rejeitar/Editar
**Renderização**: Screenshot/mockup de card de mensagem com:
- Header: "🤖 Agente quer executar ação"
- Body: nome da tool, args, contexto
- Botões: [Aprovar] [Rejeitar] [Editar]

---

### D22 — Estrutura de Log de Auditoria (Slide 42)

**Tipo**: Tabela de log
**Descrição**: Campos do log de HITL — timestamp, humano, ação, decisão, justificativa
**Conteúdo**:

| timestamp | humano | tool | args | decisão | justificativa |
|---|---|---|---|---|---|
| 2026-07-07T14:32 | ana@etho | send_email | {to, subject} | aprovado | "confirmação de pedido" |
| 2026-07-07T14:35 | bob@etho | delete_file | {path: "/"} | rejeitado | "path suspeito" |

---

### D24 — Grid de Categorias de Red Team (Slide 46)

**Tipo**: Grid 2x3
**Descrição**: 6 categorias de teste com exemplo
**Conteúdo**: Ver Slide 46 do storyboard detalhado.

---

### D25 — Fluxo de Exfiltração (Slide 47)

**Tipo**: Flowchart
**Descrição**: Agente → tool/output → atacante; filtro intercepta
**Mermaid**:
```mermaid
flowchart LR
    Agent["🤖 Agente"] --> Filter{"Output Filter<br/>(PII, secrets)"}
    Filter -- "detecta PII" --> Block["❌ Bloquear/Mascarar"]
    Filter -- "limpo" --> Out([usuário])
    Agent -.->|"via tool"| ToolCheck{"Tool Allowlist"}
    ToolCheck -- "endpoint externo" --> Block2["❌ Bloquear"]

    classDef bl fill:#fee2e2,stroke:#b91c1c,color:#000
    class Block,Block2 bl
```

---

### D26 — Pipeline Garak/PyRIT (Slide 51)

**Tipo**: Pipeline CI
**Descrição**: PR → Garak/PyRIT roda probes → resultados → gate (pass/fail)
**Mermaid**:
```mermaid
flowchart LR
    PR["🔀 PR merge"] --> Garak["Garak<br/>(probes)"]
    PR --> PyRIT["PyRIT<br/>(multi-turn)"]
    Garak --> Report["📊 Relatório ASR"]
    PyRIT --> Report
    Report --> Gate{"ASR < threshold?"}
    Gate -- "sim" --> Merge["✅ Merge"]
    Gate -- "não" --> Block["❌ Bloquear"]

    classDef ok fill:#dcfce7,stroke:#15803d,color:#000
    classDef no fill:#fee2e2,stroke:#b91c1c,color:#000
    class Merge ok
    class Block no
```

---

### D27 — Métricas de Segurança Dashboard (Slide 53)

**Tipo**: Dashboard com gauges e charts
**Descrição**: ASR por categoria (gauge), tendência ao longo do tempo (line chart), coverage (bar)
**Renderização**: Mockup de dashboard estilo Grafana com 4 painéis.

---

### D28 — EU AI Act Risk Classification (Slide 60)

**Tipo**: Pirâmide de risco
**Descrição**: 4 níveis — inaceitável / alto risco / risco limitado / risco mínimo
**Mermaid**:
```mermaid
flowchart TB
    L4["Inaceitável<br/>(proibido)"]
    L3["Alto Risco<br/>(obrigações rigorosas)"]
    L2["Risco Limitado<br/>(transparência)"]
    L1["Risco Mínimo<br/>(livre)"]
    L4 --> L3 --> L2 --> L1

    Agent["🤖 Agente autônomo + tools"] -.->|"provável"| L3

    classDef un fill:#7f1d1d,stroke:#000,color:#fff
    classDef hi fill:#fee2e2,stroke:#b91c1c,color:#000
    classDef lim fill:#fed7aa,stroke:#c2410c,color:#000
    classDef min fill:#dcfce7,stroke:#15803d,color:#000
    class L4 un
    class L3 hi
    class L2 lim
    class L1 min
```

---

### D29 — Cadeia de Responsabilidade (Slide 61)

**Tipo**: Cadeia horizontal
**Descrição**: Dev → Operador → Agente → Ação, com responsabilidades
**Mermaid**:
```mermaid
flowchart LR
    Dev["👨‍💻 Desenvolvedor<br/>(constrói com defesa)"]
    Ops["⚙️ Operador<br/>(deploya com config)"]
    Agent["🤖 Agente<br/>(executa)"]
    Action["💥 Ação<br/>(impacto)"]
    Dev --> Ops --> Agent --> Action

    classDef res fill:#dbeafe,stroke:#1e40af,color:#000
    class Dev,Ops res
```

---

### D30 — Template de ADR (Slide 62)

**Tipo**: Documento template
**Descrição**: Campos do ADR de risco
**Conteúdo**:
```
ADR-XXX: [Título da decisão]
Data: YYYY-MM-DD
Status: Aceito

# Contexto
[Por que decidimos]

# Decisão
[O que decidimos]

# Alternativas consideradas
[O que mais poderia ser feito]

# Consequências
[O que acontece com esta decisão]

# Risco residual
[O que ainda pode dar errado]

# Assinaturas
Tech Lead: ___  Security: ___  Stakeholder: ___
```

---

## Resumo de Produção

| # | Nome | Tipo | Status | Slide |
|---|---|---|---|---|
| D1 | Fluxo de ataque phishing | Flowchart | 🆕 Novo | 5 |
| D2 | Timeline de incidentes | Timeline | 🆕 Novo | 6 |
| D3 | Ativos/adversários/superfícies | Triângulo | 🆕 Novo | 8 |
| D4 | Tabela STRIDE adaptada | Tabela | 🆕 Novo | 9 |
| D5 | Tools com nível de risco | Grid | 🆕 Novo | 10 |
| D6 | Propagação multi-agente | Topologia | 🆕 Novo | 11 |
| D7 | Threat model | Flowchart | ✅ Existe | 12 |
| D8 | Tabela LINDDUN | Tabela | 🆕 Novo | 13 |
| D9 | Código/dados vs texto | Comparação | 🆕 Novo | 16 |
| D10 | Injeção indireta (fonte externa) | Flowchart | 🆕 Novo | 18 |
| D11 | Grid famílias de jailbreak | Grid | 🆕 Novo | 20 |
| D12 | Many-shot jailbreak | Diagrama | 🆕 Novo | 21 |
| D13 | System prompt + delimitadores | Código | 🆕 Novo | 23 |
| D14 | Hierarquia de instruções | Pirâmide | 🆕 Novo | 24 |
| D15 | Funil de input filtering | Funil | 🆕 Novo | 29 |
| D16 | Structured output schema | Código | 🆕 Novo | 31 |
| D17 | NeMo Guardrails pipeline | Pipeline | 🆕 Novo | 32 |
| D18 | Defense in depth (7 camadas) | Flowchart | ✅ Existe | 34 |
| D19 | Matriz risco × frequência | Matriz | 🆕 Novo | 39 |
| D20 | Fluxo de checkpoint HITL | Sequência | 🆕 Novo | 40 |
| D21 | Mock UI de HITL | Mockup | 🆕 Novo | 41 |
| D22 | Estrutura de log auditoria | Tabela | 🆕 Novo | 42 |
| D23 | HITL checkpoints (3 caminhos) | Flowchart | ✅ Existe | 43 |
| D24 | Grid categorias de red team | Grid | 🆕 Novo | 46 |
| D25 | Fluxo de exfiltração | Flowchart | 🆕 Novo | 47 |
| D26 | Pipeline Garak/PyRIT | Pipeline | 🆕 Novo | 51 |
| D27 | Dashboard de métricas | Dashboard | 🆕 Novo | 53 |
| D28 | EU AI Act risk classification | Pirâmide | 🆕 Novo | 60 |
| D29 | Cadeia de responsabilidade | Cadeia | 🆕 Novo | 61 |
| D30 | Template de ADR | Documento | 🆕 Novo | 62 |

**Total**: 3 existentes + 27 novos sugeridos = 30 diagramas para produção/manutenção.

---

## Prioridade de Produção

| Prioridade | Diagramas | Justificativa |
|---|---|---|
| **P0 (essenciais)** | D7, D18, D23 (existentes), D1, D10, D12, D14 | Conceitos centrais — defense in depth, injeção indireta, many-shot |
| **P1 (importantes)** | D3, D4, D5, D6, D9, D15, D17, D19, D20, D26, D28 | Apoio visual a conceitos chave |
| **P2 (desejáveis)** | D2, D8, D11, D13, D16, D21, D22, D24, D25, D27, D29, D30 | Enriquecimento visual |

**Recomendação**: Produzir P0 e P1 primeiro (18 diagramas); P2 conforme tempo.
