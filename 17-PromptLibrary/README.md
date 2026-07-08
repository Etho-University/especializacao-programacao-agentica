# 17 — Prompt Library

Biblioteca de **prompts** organizados por padrão e por domínio. Versão inicial foca em prompts reutilizáveis; prompts sensíveis não entram aqui.

## Convenção

Cada prompt: `NN-contexto.md` com seções: **objetivo** · **variáveis** · **template** · **exemplo de uso** · **trade-offs** · **variações**.

## Categorias planejadas

- `system/` — system prompts base
- `planning/` — prompts de planejamento (CoT, decomposição)
- `reflection/` — prompts de auto-crítica
- `routing/` — prompts de classificação
- `extraction/` — extração estruturada
- `summarization/` — sumarização
- `tools/` — descrições de tools (ACI)

## Princípios

- Prompts são **dados**, não código
- Versionados
- Testados (golden cases)
- Sem segredos
