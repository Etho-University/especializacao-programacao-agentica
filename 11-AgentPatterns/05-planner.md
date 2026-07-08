# Planner

> Padrão 5/23 · Categoria B — Planejamento e Execução

## Intenção
Decompor objetivo em sequência de passos executáveis.

## Estrutura
`planner(goal) → [step1, step2, ...]`. Pode ser replanner se necessário.

## Quando usar
Problema decompõe-se naturalmente; vale planejar antes.

## Anti-patterns
- Plano rígido sem re-planejamento
- Plano muito granular

## Custo
1 chamada (barato).

## Referências
- Plan-and-Solve (arXiv:2305.04091)
- LangGraph `plan-and-execute`
- ETHAGT04 — Reasoning & Planning
