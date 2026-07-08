# Critic

> Padrão 9/23 · Categoria C — Avaliação e Melhoria

## Intenção
Avaliar saída de outro agente em loop; núcleo do evaluator-optimizer.

## Estrutura
Gerador → `critic` → feedback → gerador refina.

## Quando usar
Feedback humano articulável; LLM consegue avaliar.

## Anti-patterns
- Critic genérico
- Sem critério de parada

## Custo
2× chamadas por iteração.

## Referências
- Anthropic *Evaluator-Optimizer* workflow
- Reflexion: Shinn et al. (arXiv:2303.11366)
- ETHAGT03 — Workflows & Planejamento
