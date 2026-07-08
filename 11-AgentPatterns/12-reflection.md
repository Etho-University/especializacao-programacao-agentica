# Reflection Agent

> Padrão 12/23 · Categoria C — Avaliação e Melhoria

## Intenção
Auto-crítica: o agente avalia sua própria saída e aprende.

## Estrutura
Agente → `reflection` (auto-avaliação) → memória → próxima tentativa.

## Quando usar
Sinal de falha; múltiplas tentativas; aprender com erros.

## Anti-patterns
- Reflexão genérica
- Sem uso efetivo da memória

## Custo
1 chamada extra por tentativa.

## Referências
- Reflexion: Shinn et al. (arXiv:2303.11366)
- ETHAGT05 — Memória de Agentes
