# ETHAGT04 — Reasoning & Planning
## Storyboard da Apresentação

> **Universidade Etho · Especialização em Programação Agêntica**
> Fase B — Razão, Memória e Conhecimento · 30 h
> Storyboard v1.0 · Julho 2026

---

## Metadados da Apresentação

| Campo | Valor |
|---|---|
| Código | ETHAGT04 |
| Título | Reasoning & Planning (do CoT ao inference-time reasoning) |
| Duração estimada | 120 min (2 blocos de 60 min) |
| Total de slides | 90 |
| Público | Arquitetos, Engenheiros de Software, Engenheiros de IA, Cientistas de Dados, Tech Leads |
| Pré-requisitos | ETHAGT01, ETHAGT02, ETHAGT03 |
| Competências | C1 (I), C2 (B), C4 (B), C5 (B) |

---

## Mapa Visual da Apresentação

```
BLOCO 1 (60 min)                              BLOCO 2 (60 min)
┌──────────────────────────────┐              ┌──────────────────────────────┐
│ SEÇÃO A — Abertura (8 min)   │              │ SEÇÃO E — Reflexion (12 min) │
│  Capa · Objetivos · Agenda   │              │  Auto-crítica · Memória de   │
│  Motivação · Espectro        │              │  erros · Convergência        │
├──────────────────────────────┤              ├──────────────────────────────┤
│ SEÇÃO B — Tipologia (14 min) │              │ SEÇÃO F — Self-Discover (8m) │
│  CoT · Self-Consistency      │              │  Composição de estratégia    │
│  Linear vs Árvore vs Grafo   │              │  Primitivas como blocos      │
├──────────────────────────────┤              ├──────────────────────────────┤
│ SEÇÃO C — Plan-and-Execute   │              │ SEÇÃO G — Reasoning Nativo   │
│  (16 min)                    │              │  (14 min)                    │
│  Planner/Executor · ReWOO    │              │  o1/o3 · Claude thinking     │
│  Trade-offs · Re-planejar    │              │  Reasoning model vs prompting│
├──────────────────────────────┤              ├──────────────────────────────┤
│ SEÇÃO D — ToT e LATS (18 min)│              │ SEÇÃO H — Falhas e Orçamento│
│  Busca em árvore · MCTS+LLM  │              │  (12 min)                    │
│  Backtracking · Custo        │              │  Loops · Budget · Benchmarks │
│  Intervalo (5 min)           │              ├──────────────────────────────┤
└──────────────────────────────┘              │ SEÇÃO I — Fechamento (8 min) │
                                               │  Comparação · Quiz · Q&A     │
                                               └──────────────────────────────┘
```

---

## Storyboard Detalhado

### SEÇÃO A — Abertura (Slides 1-7 · 8 min)

---

#### Slide 1 — Capa
- **Tipo**: Capa
- **Objetivo**: Identificar a aula, professor e contexto
- **Conteúdo**:
  - ETHAGT04 — Reasoning & Planning
  - Universidade Etho · Especialização em Programação Agêntica
  - Fase B — Razão, Memória e Conhecimento · 30 h
  - Professor · Data
- **Diagrama**: Logo Etho + imagem de fundo (rede neural com nós em árvore)
- **Tempo**: 1 min

---

#### Slide 2 — Objetivos do Módulo
- **Tipo**: Conteúdo
- **Objetivo**: Deixar claro o que o aluno deve conseguir fazer ao final
- **Conteúdo**:
  - Objetivo geral: Dominar o espectro de estratégias de raciocínio e planejamento
  - 5 objetivos específicos: tipologia, implementar 7 padrões, reasoning nativo, trade-offs, falhas
- **Tempo**: 2 min

---

#### Slide 3 — Competências Desenvolvidas
- **Tipo**: Conteúdo
- **Conteúdo**: C1 (I), C2 (B), C4 (B), C5 (B)
- **Tempo**: 1 min

---

#### Slide 4 — Agenda
- **Tipo**: Conteúdo
- **Conteúdo**: 9 seções com tempos estimados
- **Tempo**: 1 min

---

#### Slide 5 — Motivação: Quando ReAct Não Basta
- **Tipo**: Conteúdo
- **Objetivo**: Criar tensão — ReAct linear falha em problemas que exigem exploração
- **Conteúdo**:
  - Exemplo: "Planeje viagem de 7 dias com orçamento R$5000"
  - ReAct entra em loop ou faz plano ruim (sem backtracking)
  - Um passo errado no meio inviabiliza todo o plano
- **Tempo**: 2 min

---

#### Slide 6 — Contexto: O Espectro do Raciocínio
- **Tipo**: Diagrama
- **Objetivo**: Mostrar o panorama de estratégias
- **Conteúdo**: Linha do tempo CoT (2022) → ReAct (2023) → ToT (2023) → Reflexion (2023) → LATS (2024) → Self-Discover (2024) → o1 (2024)
- **Diagrama**: `12-Diagrams/ETHAGT04/reasoning-spectrum.mmd`
- **Tempo**: 1 min

---

### SEÇÃO B — Tipologia do Raciocínio (Slides 8-18 · 14 min)

---

#### Slide 7 — [SEÇÃO] Tipologia do Raciocínio
- **Tipo**: Seção
- **Tempo**: 0.5 min

---

#### Slide 8 — Chain-of-Thought: A Fundação
- **Tipo**: Conteúdo
- **Conteúdo**: CoT zero-shot, few-shot; "Let's think step by step"
- **Tempo**: 2 min

---

#### Slide 9 — Self-Consistency
- **Tipo**: Conteúdo
- **Conteúdo**: Múltiplas amostras + votação majoritária
- **Tempo**: 2 min

---

#### Slide 10 — Antes vs Durante a Ação
- **Tipo**: Comparação
- **Conteúdo**: Plan-and-Execute (antes) vs ReAct (durante)
- **Tempo**: 2 min

---

#### Slide 11 — Linear vs Árvore vs Grafo
- **Tipo**: Diagrama
- **Conteúdo**: ReAct (linear) → ToT (árvore) → LATS (grafo/MCTS)
- **Tempo**: 2 min

---

#### Slide 12 — Reasoning + Tools
- **Tipo**: Conteúdo
- **Conteúdo**: O casamento entre raciocínio e tool calling
- **Tempo**: 2 min

---

### SEÇÃO C — Plan-and-Execute e ReWOO (Slides 19-30 · 16 min)

---

#### Slide 13 — [SEÇÃO] Plan-and-Execute e ReWOO
- **Tipo**: Seção
- **Tempo**: 0.5 min

---

#### Slide 14 — Plan-and-Execute: Arquitetura
- **Tipo**: Diagrama
- **Conteúdo**: Planner gera plano → Executor opera sequencialmente → Replanner (opcional)
- **Diagrama**: `12-Diagrams/ETHAGT04/plan-execute.mmd`
- **Tempo**: 3 min

---

#### Slide 15 — ReWOO: Reasoning WithOut Observation
- **Tipo**: Conteúdo
- **Conteúdo**: Plano "cego" + evidências paralelas; redução de tokens
- **Tempo**: 3 min

---

#### Slide 16 — Trade-offs: Eficiência vs Flexibilidade
- **Tipo**: Comparação
- **Conteúdo**: Plan-and-Execute vs ReAct vs ReWOO
- **Tempo**: 3 min

---

#### Slide 17 — Quando Re-planejar
- **Tipo**: Conteúdo
- **Conteúdo**: Sinais de que o plano falhou; re-planejamento dinâmico
- **Tempo**: 2 min

---

### SEÇÃO D — Tree of Thoughts e LATS (Slides 31-45 · 18 min)

---

#### Slide 18 — [SEÇÃO] Tree of Thoughts e LATS
- **Tipo**: Seção
- **Tempo**: 0.5 min

---

#### Slide 19 — Tree of Thoughts: Busca em Árvore
- **Tipo**: Diagrama
- **Conteúdo**: Decompor → Gerar candidatos → Avaliar → Buscar (BFS/DFS)
- **Diagrama**: `12-Diagrams/ETHAGT04/tot-search-tree.mmd`
- **Tempo**: 4 min

---

#### Slide 20 — LATS: Language Agent Tree Search
- **Tipo**: Conteúdo
- **Conteúdo**: MCTS + LLM; backtracking; UCT para seleção
- **Tempo**: 4 min

---

#### Slide 21 — Custo vs Qualidade
- **Tipo**: Conteúdo
- **Conteúdo**: N+ chamadas de LLM; quando vale o custo
- **Tempo**: 3 min

---

#### Slide 22 — DEMO: ToT em Ação
- **Tipo**: Código
- **Conteúdo**: Resolvendo problema de raciocínio com ToT
- **Tempo**: 5 min

---

### SEÇÃO E — Reflexion (Slides 46-55 · 12 min)

---

#### Slide 23 — [SEÇÃO] Reflexion
- **Tipo**: Seção
- **Tempo**: 0.5 min

---

#### Slide 24 — Reflexion: Auto-Crítica após Falha
- **Tipo**: Diagrama
- **Conteúdo**: Agente tenta → Falha → Reflete → Memória de erros → Tenta novamente
- **Diagrama**: `12-Diagrams/ETHAGT04/reflexion-loop.mmd`
- **Tempo**: 4 min

---

#### Slide 25 — Reflexion vs Reflection Pattern
- **Tipo**: Comparação
- **Conteúdo**: Reflexion (memória persistente de erros) vs Reflection simples (auto-crítica em uma passada)
- **Tempo**: 3 min

---

#### Slide 26 — Convergência e Limites
- **Tipo**: Conteúdo
- **Conteúdo**: Limite de tentativas; quando Reflexion converge vs diverge
- **Tempo**: 3 min

---

### SEÇÃO F — Self-Discover (Slides 56-63 · 8 min)

---

#### Slide 27 — [SEÇÃO] Self-Discover
- **Tipo**: Seção
- **Tempo**: 0.5 min

---

#### Slide 28 — Self-Discover: Composição de Estratégia
- **Tipo**: Conteúdo
- **Conteúdo**: O agente compõe sua própria estratégia a partir de primitivas
- **Tempo**: 3 min

---

#### Slide 29 — Primitivas como Building Blocks
- **Tipo**: Conteúdo
- **Conteúdo**: REACT, CoT, ToT como blocos selecionáveis
- **Tempo**: 2 min

---

### SEÇÃO G — Inference-Time Reasoning Nativo (Slides 64-75 · 14 min)

---

#### Slide 30 — [SEÇÃO] Inference-Time Reasoning Nativo
- **Tipo**: Seção
- **Tempo**: 0.5 min

---

#### Slide 31 — Modelos Treinados para Pensar
- **Tipo**: Conteúdo
- **Conteúdo**: o1, o3, Claude com extended thinking; RL para raciocínio
- **Tempo**: 3 min

---

#### Slide 32 — O Que Muda no Design do Agente
- **Tipo**: Conteúdo
- **Conteúdo**: Sem CoT promptado; mais tools; orçamento de reasoning tokens
- **Tempo**: 4 min

---

#### Slide 33 — Reasoning Model vs Prompting
- **Tipo**: Comparação
- **Conteúdo**: Quando escolher cada abordagem
- **Tempo**: 3 min

---

#### Slide 34 — Custo e Latência
- **Tipo**: Conteúdo
- **Conteúdo**: Estratégias de mitigação; caching de reasoning
- **Tempo**: 3 min

---

### SEÇÃO H — Falhas, Loops e Orçamento (Slides 76-84 · 12 min)

---

#### Slide 35 — [SEÇÃO] Falhas, Loops e Orçamento
- **Tipo**: Seção
- **Tempo**: 0.5 min

---

#### Slide 36 — Detecção e Quebra de Loops
- **Tipo**: Conteúdo
- **Conteúdo**: Monitorar repetição; heurísticas de detecção
- **Tempo**: 3 min

---

#### Slide 37 — Orçamento de Tokens e Passos
- **Tipo**: Conteúdo
- **Conteúdo**: max_steps, max_tokens, max_cost
- **Tempo**: 3 min

---

#### Slide 38 — Re-planejamento Supervisionado
- **Tipo**: Conteúdo
- **Conteúdo**: HITL no plano; checkpoints de validação
- **Tempo**: 3 min

---

### SEÇÃO I — Fechamento (Slides 85-90 · 8 min)

---

#### Slide 39 — Comparação Geral das Estratégias
- **Tipo**: Comparação
- **Conteúdo**: Tabela: ReAct vs Plan-Execute vs ToT vs LATS vs Reflexion vs Self-Discover
- **Tempo**: 2 min

---

#### Slide 40 — Anti-Patterns
- **Tipo**: Conteúdo
- **Conteúdo**: Plano rígido, re-planejamento ausente, loops, ToT para problema simples
- **Tempo**: 2 min

---

#### Slide 41 — Quiz Final
- **Tipo**: Exercício
- **Conteúdo**: 5 perguntas de múltipla escolha
- **Tempo**: 2 min

---

#### Slide 42 — Conexão com Próximos Módulos
- **Tipo**: Conteúdo
- **Conteúdo**: ETHAGT05 (memória), ETHAGT06 (RAG), ETHAGT09 (multi-agente)
- **Tempo**: 1 min

---

#### Slide 43 — Leitura Recomendada
- **Tipo**: Referências
- **Conteúdo**: ToT, Reflexion, LATS, Self-Discover, o1 paper
- **Tempo**: 0.5 min

---

#### Slide 44 — Q&A / Encerramento
- **Tipo**: Capa
- **Tempo**: 1 min

---

## Resumo do Storyboard

| Seção | Slides | Tempo | Conteúdo |
|---|---|---|---|
| A — Abertura | 1-7 | 8 min | Capa, objetivos, competências, agenda, motivação, espectro |
| B — Tipologia | 8-18 | 14 min | CoT, Self-Consistency, antes/durante, linear/árvore/grao |
| C — Plan-and-Execute | 19-30 | 16 min | Planner/Executor, ReWOO, trade-offs, re-planejar |
| D — ToT e LATS | 31-45 | 18 min | Busca em árvore, MCTS+LLM, custo vs qualidade, DEMO |
| E — Reflexion | 46-55 | 12 min | Auto-crítica, memória de erros, convergência |
| F — Self-Discover | 56-63 | 8 min | Composição de estratégia, primitivas |
| G — Reasoning Nativo | 64-75 | 14 min | o1/o3/Claude, design, reasoning vs prompting, custo |
| H — Falhas e Orçamento | 76-84 | 12 min | Loops, budget, benchmarks |
| I — Fechamento | 85-90 | 8 min | Comparação, anti-patterns, quiz, Q&A |
| **Total** | **90** | **120 min** | |

---

## Diagramas Necessários

| # | Slide | Diagrama | Tipo | Fonte |
|---|---|---|---|---|
| D1 | 6 | Espectro de raciocínio | Timeline | `12-Diagrams/ETHAGT04/reasoning-spectrum.mmd` |
| D2 | 11 | Linear vs Árvore vs Grafo | Comparação | Novo |
| D3 | 14 | Plan-and-Execute | Flowchart | `12-Diagrams/ETHAGT04/plan-execute.mmd` |
| D4 | 15 | ReWOO | Flowchart | Novo |
| D5 | 19 | ToT search tree | Árvore | `12-Diagrams/ETHAGT04/tot-search-tree.mmd` |
| D6 | 20 | LATS/MCTS | Grafo | Novo |
| D7 | 24 | Reflexion loop | Loop | `12-Diagrams/ETHAGT04/reflexion-loop.mmd` |
| D8 | 28 | Self-Discover | Composição | Novo |
| D9 | 32 | Reasoning nativo vs prompting | Comparação | Novo |
| D10 | 39 | Comparação geral | Tabela | Novo |

---

> **Aguardando aprovação deste storyboard para gerar os slides detalhados com notas do professor.**
