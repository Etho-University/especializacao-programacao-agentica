# Strategy Evolver

> Padrão 19/23 · Categoria F — Meta-Agência e Evolução

## Intenção
Evoluir estratégias/prompts/topologias ao longo do tempo com base em performance.

## Estrutura
Loop: medir performance → gerar variação → avaliar → promover/rejeitar.

## Quando usar
Sistemas de longa duração; otimização contínua.

## Anti-patterns
- Evoluir sem eval rigoroso
- Deriva de objetivos

## Custo
Alto (muitas execuções para avaliar).

## Referências
- DSPy
- Promptbreeder (arXiv:2309.16797)
- Voyager (arXiv:2305.16291)
- ETHAGT15 — Meta-Agentes
