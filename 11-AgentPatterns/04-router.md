# Router

> Padrão 4/23 · Categoria A — Orquestração

## Intenção
Classificar input e direcionar para handler especializado.

## Estrutura
`classifier` → ramo A/B/C.

## Quando usar
Categorias distintas com tratamentos próprios.

## Anti-patterns
- Categorias ambíguas
- Sem fallback

## Custo
1 classificação + 1 handler.

## Referências
- Anthropic *Routing* workflow
- ETHAGT03 — Workflows & Planejamento
