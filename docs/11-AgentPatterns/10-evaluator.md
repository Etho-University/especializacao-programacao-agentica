# Evaluator

> Padrão 10/23 · Categoria C — Avaliação e Melhoria

## Intenção
Medir qualidade contra critérios objetivos (não necessariamente em loop).

## Estrutura
`evaluator(output, criteria) → score + breakdown`.

## Quando usar
Eval automatizado; CI para agentes.

## Anti-patterns
- Evaluator subjetivo
- Sem calibração

## Custo
1 chamada por avaliação.

## Referências
- LLM-as-judge
- Ragas
- ETHAGT12 — AgentOps & Avaliação
