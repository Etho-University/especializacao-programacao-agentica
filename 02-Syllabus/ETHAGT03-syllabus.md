# `ETHAGT03` — Padrões de Workflow Agêntico

> Especialização em Programação Agêntica · Universidade Etho
> Fase A · Carga 30 h · Versão 1.0 · Última atualização: Julho 2026

## 1. Identificação

| Campo | Valor |
|---|---|
| Código | `ETHAGT03` |
| Título | Padrões de Workflow Agêntico (os 5 da Anthropic + composições) |
| Fase interna | A — Fundamentos Agênticos |
| Fase Etho | Especialização (Fase 4) |
| Carga horária | 30 h |
| Pré-requisitos | `ETHAGT01` (recomendado `ETHAGT02`) |
| Módulos que dependem deste | `ETHAGT04`, `ETHAGT09`, `ETHAGT10`, `ETHAGT90` |

## 2. Objetivos

**Objetivo geral**: Dominar os **5 padrões canônicos de workflow** de Anthropic e suas composições, sabendo escolher e combinar para obter previsibilidade sem sacrificar qualidade.

**Objetivos específicos**:
1. Implementar os 5 workflows: prompt chaining, routing, parallelization (sectioning + voting), orchestrator-workers, evaluator-optimizer.
2. Identificar gates programáticos e onde inseri-los.
3. Combinar workflows em pipelines mais complexos.
4. Justificar a escolha de workflow vs agente autônomo em um cenário real.
5. Medir trade-offs de custo/latência/qualidade entre abordagens.

## 3. Competências desenvolvidas

| Competência | Nível ao final |
|---|---|
| C1 Programação Agêntica | **I** |
| C2 Multi-Agent Systems | B |
| C3 MCP & Tool Use | B |
| C5 AgentOps & Avaliação | B |

## 4. Conteúdo programático

### Unidade 1 — Por que workflows antes de agentes (3 h)
- O princípio de Anthropic: comece simples
- Workflows = previsibilidade; agentes = flexibilidade
- Custo de complexidade prematura
- Mapa dos 5 padrões e quando cada brilha

### Unidade 2 — Prompt Chaining (4 h)
- Estrutura: LLM → gate → LLM → …
- Onde adicionar gates (validação, classificação)
- Quando trade-off de latência por accuracy vale
- Exemplo: gerar rascunho → revisar critérios → reescrever

### Unidade 3 — Routing (4 h)
- Classificação como etapa separada
- Routing por modelo (Haiku para fácil, Sonnet para difícil)
- Routing por prompt/tools especializados
- Avaliando a qualidade do classificador

### Unidade 4 — Parallelization (5 h)
- **Sectioning**: subtarefas independentes em paralelo
- **Voting**: mesma tarefa N vezes, agregação
- Guardrails em paralelo (modelo responde + modelo filtra)
- Avaliação LLM-as-judge em paralelo
- Erros comuns: dependências ocultas, custo explodindo

### Unidade 5 — Orchestrator-Workers (5 h)
- Distinção chave vs parallelization: subtarefas são **dinâmicas**
- Orquestrador como LLM que planeja + sintetiza
- Implementação: task-decomposition + workers + reducer
- Casos: coding em múltiplos arquivos, search em múltiplas fontes

### Unidade 6 — Evaluator-Optimizer (5 h)
- Loop gerar → avaliar → refinar até critério
- Quando.tem valor: feedback humano articulável; LLM consegue avaliar
- Critérios claros e mensuráveis
- Convergência: parar por score, max iters, ou delta estagnado

### Unidade 7 — Composições e limites (4 h)
- Composições típicas: routing → parallelization → evaluator-optimizer
- Quando combinar vira agente (e como saber)
- Sinais de que você está forçando workflow em problema que pede agente

## 5. Bibliografia

### Fundamental
- Anthropic. *Building Effective Agents*. 2024. (Seção principal)
- arXiv:2601.12560. *Agentic AI: Architectures, Taxonomies, and Evaluation*. 2026.

### Complementar
- Towards AI. *Agent Workflow Patterns — Beyond Anthropic's Playbook*. 2025.
- LangGraph *Examples/* (plan-and-execute, llm-compiler, multi-agent).

## 6. Papers canônicos

- `arXiv:2305.04091` — Plan-and-Solve (decorrelação de planejamento e execução)
- `arXiv:2305.18323` — ReWOO (plan "cego" + paralelismo de evidências)
- `arXiv:2312.04511` — LLMCompiler (paralelização estruturada)

## 7. Laboratórios

- **Lab 1** (5 h): "Os 5 em 1 dia". Implementar versões mínimas dos 5 workflows em um domínio comum (ex.: responder a ticket de suporte).
- **Lab 2** (5 h): "Composição". Construir pipeline routing → parallelization (3 workers) → evaluator-optimizer. Medir custo/latência.

## 8. Projeto do módulo

**Descrição**: dada uma tarefa de síntese de relatório a partir de múltiplas fontes, projetar e implementar o workflow composto mais adequado. Comparar 2 abordagens (ex.: prompt chaining vs orchestrator-workers) em qualidade, custo e latência.
**Entrega**: código + benchmark + ADR justificando a escolha.
**Critério de sucesso**: ADR coerente; medições reais em ≥20 casos.

## 9. Exercícios

1. Para 5 cenários, indique o workflow mais adequado e por quê.
2. Quando voting é preferível a sectioning?
3. Descreva um gate programático útil em prompt chaining de tradução.
4. Verdadeiro/falso: "Orchestrator-workers é sempre melhor que parallelization."
5. Escreva a condição de parada de um evaluator-optimizer para tradução literária.

## 10. Avaliação

| Pilar | Peso | Instrumento |
|---|---|---|
| Técnico | 40% | Projeto + prova de trade-offs |
| Consultivo | 30% | Defesa do ADR para "cliente" |
| Comportamental | 20% | Code review em duplas |
| Prático | 10% | Demo: workflow escolhido rodando |

**Nota mínima**: 3,0.

## 11. Slides

`03-Slides/ETHAGT03-slides.md` — ~90 slides, um conjunto de diagramas por workflow.

## 12. Leitura complementar

- Schluntz, E. & Albert, A. *Building more effective AI agents* (YouTube).
- Pat McGuinness Substack (série sobre workflows).
- Coinbase, Thomson Reuters, Intercom case studies (Anthropic).

## 13. Ferramentas

Python · LangGraph (estado + edges) · OpenAI Agents SDK · Docker · um profiler de custo/latência próprio.

## 14. Diagramas

`12-Diagrams/ETHAGT03/` — um `.mmd` por workflow (prompt-chaining, routing, parallelization-sectioning, parallelization-voting, orchestrator-workers, evaluator-optimizer) + composições.

## 15. Estudo de caso

Coinbase / Intercom — como workflows agênticos foram usados em produção para suporte ao cliente. `09-CaseStudies/`.

## 16. Ficha de pesquisa

`20-Research/ETHAGT03-pesquisa.md` — Anthropic (5 padrões); LangGraph examples/ (plan-and-execute, llm-compiler); arXiv:2305.04091, 2305.18323. Consulta: Julho 2026.

---

*Mantido por: Universidade Etho · Versão 1.0 · Julho 2026*
