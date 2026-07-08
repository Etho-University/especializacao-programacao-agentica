# Executor

> Padrão 6/23 · Categoria B — Planejamento e Execução

## Intenção
Operar passos do plano, chamando tools conforme necessário.

## Estrutura
Loop sobre passos; cada passo vira chamada LLM/tool.

## Quando usar
Sempre (parceiro do Planner).

## Anti-patterns
Executor que re-planeja implicitamente (vira agente).

## Custo
N chamadas (uma por passo).

## Referências
- Plan-and-Solve (arXiv:2305.04091)
- LangGraph `plan-and-execute`
- ETHAGT04 — Reasoning & Planning
