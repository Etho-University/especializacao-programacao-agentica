# Workflow: Orchestrator-Workers

## Intenção
Um LLM central (orchestrator) **dinamicamente** decompõe a tarefa em subtarefas, delega a workers LLM, e sintetiza os resultados.

## Estrutura
```
[Orchestrator] ─► [worker A] ─┐
              ├─► [worker B] ─┼─► [Synthesizer]
              └─► [worker C] ─┘
```

## Distinção crucial vs parallelization
Em parallelization, subtarefas são **predefinidas**. Em orchestrator-workers, são **dinâmicas** — o orchestrator decide quais existem com base no input.

## Quando usar
- Subtarefas **não são previsíveis** a partir do input.
- Precisa decompor dinamicamente.
- Síntese agrega valor (não só concatena).

## Exemplos
- Coding agent: edita múltiplos arquivos — quais depende da tarefa.
- Search: múltiplas fontes — quais consultar depende da pergunta.

## Implementação
Orchestrator = LLM que recebe tarefa e gera plano de subtarefas. Cada subtarefa vira chamada worker. Resultados voltam para síntese.

Fronteira fluida com **Plan-and-Execute** (agente). Depende de quanto controle você retém no código.

## Anti-patterns
- Subtarefas com sobreposição (workers duplicam).
- Synthesis fraca (só concatena).
- Orchestrator sem critério de parada.

## Custo
1 chamada orchestrator + N chamadas workers + 1 chamada synthesis = N+2. Mais caro que parallelization fixo.

## Referências
- Anthropic *Building Effective Agents* (2024).
- Wang et al. *Plan-and-Solve* (arXiv:2305.04091).
