# Scheduler

> Padrão 7/23 · Categoria B — Planejamento e Execução

## Intenção
Agendar e priorizar tarefas em sistemas com múltiplas demandas.

## Estrutura
Fila de tarefas com prioridade; scheduler decide ordem.

## Quando usar
Muitos pedidos concorrentes; ordem importa.

## Anti-patterns
- FIFO cego (sem prioridade)
- Starvation (tarefas de baixa prioridade nunca executam)

## Custo
Baixo (decisão, não execução).

## Referências
- Sistemas operacionais (escalonamento)
- Filas de produção
- ETHAGT11 — Event-Driven & Orquestração
