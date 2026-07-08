# `ETHAGT04` — Reasoning & Planning

> Fase B · Carga 30 h · Versão 1.0 · Julho 2026

## 1. Identificação

| Campo | Valor |
|---|---|
| Código | `ETHAGT04` |
| Título | Reasoning & Planning (do CoT ao inference-time reasoning) |
| Fase interna | B — Razão, Memória e Conhecimento |
| Carga horária | 30 h |
| Pré-requisitos | `ETHAGT03` |
| Módulos que dependem deste | `ETHAGT05`, `ETHAGT06`, `ETHAGT09` |

## 2. Objetivos

**Objetivo geral**: Dominar o espectro de estratégias de **raciocínio e planejamento** para agentes — desde CoT simples até Tree of Thoughts, LATS, Reflexion e Self-Discover — incluindo a transição para *inference-time reasoning* nativo (modelos o1/o3/Claude reasoning).

**Objetivos específicos**:
1. Caracterizar planejamento *antes* vs *durante* a ação; *linear* vs *em árvore*.
2. Implementar: ReAct (revisão), Plan-and-Execute, ReWOO, Tree of Thoughts, LATS, Reflexion, Self-Discover.
3. Compreender quando usar reasoning model nativo vs padrão promptado.
4. Avaliar trade-offs: qualidade × custo × latência × robustez.
5. Lidar com falhas clássicas: plano rígido, re-planejamento ausente, loops.

## 3. Competências desenvolvidas

| Competência | Nível ao final |
|---|---|
| C1 Programação Agêntica | **I** |
| C2 Multi-Agent Systems | B |
| C4 Agent Memory | B |
| C5 AgentOps & Avaliação | B |

## 4. Conteúdo programático

### Unidade 1 — Tipologia do raciocínio (3 h)
- CoT (zero-shot, few-shot, self-consistency)
- Raciocínio antes vs durante a ação
- Linear vs árvore vs grafo
- O casamento reasoning + tools

### Unidade 2 — Plan-and-Execute e ReWOO (5 h)
- Planner gera plano; executor opera
- ReWOO: plano "cego" + evidências paralelas; redução de tokens
- Vantagens: eficiência; desvantagens: rigidez
- Quando re-planejar

### Unidade 3 — Tree of Thoughts e LATS (5 h)
- Exploração em árvore com avaliação de estados
- LATS: MCTS + LLM; Backtracking
- Custo vs qualidade; quando vale
- Casos: raciocínio matemático, planejamento de código

### Unidade 4 — Reflexion (4 h)
- Auto-crítica após falha; memória de erros anteriores
- Reflexion vs Reflection pattern simples
- Convergência e limite de tentativas

### Unidade 5 — Self-Discover (3 h)
- O agente compõe sua própria estratégia de raciocínio
- Primitivas (REACT, CoT, etc.) como building blocks
- Quando o problema é tão novo que não há padrão pronto

### Unidade 6 — Inference-Time Reasoning nativo (5 h)
- Modelos treinados para pensar: o1, o3, Claude com extended thinking
- O que muda no design do agente (sem CoT promptado, mais tools, orçamento de tokens)
- Quando escolher reasoning model vs prompting
- Custo e latência: estratégias de mitigação

### Unidade 7 — Falhas, loops e orçamento (5 h)
- Detecção e quebra de loops
- Orçamento de tokens/passos
- Re-planejamento supervisionado
- Avaliação comparativa (lab de benchmarks)

## 5. Bibliografia

### Fundamental
- Yao, S. *Tree of Thoughts* (arXiv:2305.10601).
- Shinn, N. *Reflexion* (arXiv:2303.11366).
- Wang, X. *Self-Consistency* (arXiv:2203.11171).
- OpenAI. *Learning to Reason with LLMs* (o1 launch paper).

### Complementar
- Xu, B. et al. *ReWOO* (arXiv:2305.18323).
- *LLMCompiler* (arXiv:2312.04511).
- *Self-Discover* (arXiv:2402.03620).

## 6. Papers canônicos

- `arXiv:2305.10601` — Tree of Thoughts
- `arXiv:2303.11366` — Reflexion
- `arXiv:2402.03620` — Self-Discover
- `arXiv:2310.01757` — LATS (Language Agent Tree Search, Zhou et al.)

## 7. Laboratórios

- **Lab 1** (5 h): "Plan-and-Execute vs ReAct". Mesma tarefa complexa (ex.: planejar e resolver um problema multi-step) com os dois padrões; comparar custo e qualidade.
- **Lab 2** (5 h): "Reflexion com memória". Agente que aprende com 3 tentativas anteriores em um benchmark de raciocínio.

## 8. Projeto do módulo

**Descrição**: implementar um agente que resolve um subconjunto de GAIA (general assistant) usando pelo menos 3 padrões de raciocínio à escolha. Comparar resultados e justificar.
**Entrega**: código + benchmark + ADR de estratégia.
**Critério de sucesso**: diferença de success rate entre padrões mensurada e discutida.

## 9. Exercícios

1. Para 5 classes de problema, indique a estratégia de raciocínio mais adequada.
2. Quando reasoning model nativo *substitui* Tree of Thoughts?
3. Escreva a estrutura de memória de um agente Reflexion.
4. Por que ReWOO reduz custo vs ReAct?
5. Verdadeiro/falso: "Self-Discover é sempre superior a CoT."

## 10. Avaliação

| Pilar | Peso | Instrumento |
|---|---|---|
| Técnico | 40% | Projeto + prova de padrões |
| Consultivo | 30% | Apresentação comparativa para especialista |
| Comportamental | 20% | Code review |
| Prático | 10% | Demo: padrão escolhido resolvendo caso |

**Nota mínima**: 3,0.

## 11. Slides

- Slides: `03-Slides/ETHAGT04-slides.md` (~90 slides).

## 12. Leitura complementar

- Karpathy "Thinking clearly"; Anthropic *Interpretability of Reasoning*.

## 13. Ferramentas

- Python, LangGraph, OpenAI o-series (opcional), `gsm8k`, `GAIA` subsets.

## 14. Diagramas

- Diagramas: `12-Diagrams/ETHAGT04/` — tot-search-tree.mmd, reflexion-loop.mmd, plan-execute.mmd.

## 15. Estudo de caso

- agentes resolvendo SWE-bench com LATS/Reflexion.

## 16. Ficha de pesquisa

- Ficha: `20-Research/ETHAGT04-pesquisa.md` (arXiv listados acima).

---

*Mantido por: Universidade Etho · Versão 1.0 · Julho 2026*
