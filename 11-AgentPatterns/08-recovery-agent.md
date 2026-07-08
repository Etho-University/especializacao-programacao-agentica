# Recovery Agent

> Padrão 8/23 · Categoria B — Planejamento e Execução

## Intenção
Recuperar de falhas durante execução (timeouts, erros, loops).

## Estrutura
Detecta anomalia → aplica estratégia (retry, fallback, re-planejamento).

## Quando usar
Produção; agentes de longa duração; ambientes instáveis.

## Anti-patterns
- Retry cego infinito
- Sem classificação de erro

## Custo
Variável; deve ter orçamento próprio.

## Referências
- Padrões de resiliência (circuit breaker, saga)
- ETHAGT14 — Escalabilidade & Produção
