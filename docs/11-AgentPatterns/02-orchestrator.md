# Orchestrator

> Padrão 2/23 · Categoria A — Orquestração

## Intenção
Decompor dinamicamente a tarefa em subtarefas e delegar a workers, sintetizando resultados.

## Estrutura
`orchestrator` gera plano → `workers` executam → `synthesizer` integra.

## Quando usar
Subtarefas **não são previsíveis**; problema aberto.

## Anti-patterns
- Workers duplicando trabalho
- Synthesis só concatenando

## Custo
N+2 chamadas (orchestrator + N workers + synth).

## Referências
- Anthropic *Orchestrator-Workers* workflow
- ETHAGT03 — Workflows & Planejamento
