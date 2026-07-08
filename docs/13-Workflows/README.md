# Workflows Agênticos — Catálogo

Biblioteca dos **workflows** (sistemas onde LLMs e tools são orquestrados por caminhos de código predefinidos). Distinção canônica de Anthropic (*Building Effective Agents*, dez/2024). Aprofundamento do curso `ETHAGT03`.

## Os 5 padrões canônicos

| # | Workflow | Arquivo | Quando usar |
|---|---|---|---|
| 1 | **Prompt Chaining** | [`prompt-chaining.md`](prompt-chaining.md) | subtarefas fixas em sequência, com gates |
| 2 | **Routing** | [`routing.md`](routing.md) | categorias distintas com tratamentos próprios |
| 3 | **Parallelization** | [`parallelization.md`](parallelization.md) | subtarefas independentes (sectioning) ou voting |
| 4 | **Orchestrator-Workers** | [`orchestrator-workers.md`](orchestrator-workers.md) | subtarefas dinâmicas decididas pelo LLM |
| 5 | **Evaluator-Optimizer** | [`evaluator-optimizer.md`](evaluator-optimizer.md) | loop gerar/avaliar/refinar com critério claro |

## Variações e composições

| Nome | Arquivo | Composição |
|---|---|---|
| **Routing + Parallelization + Evaluator-Optimizer** | [`composition-routing-parallel-evaluator.md`](composition-routing-parallel-evaluator.md) | padrão típico de suporte |
| **Self-Consistency** | [`self-consistency.md`](self-consistency.md) | voting com amostragem diversa |
| **Mixture-of-Experts (routing por especialista)** | [`moe-routing.md`](moe-routing.md) | routing para "especialistas" por domínio |

## Quando NÃO usar workflow

- Tarefa aberta, passos imprevisíveis → **agente autônomo** (ver `11-AgentPatterns/`).
- 1 chamada bem feita basta → não adicione complexidade.

## Princípio

> Comece com a **solução mais simples possível**. Só aumente complexidade quando demonstradamente melhorar o resultado. (Anthropic)
