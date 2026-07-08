# ADR-001: Escolha de Topologia Hierarchical para Sistema de Pesquisa

> **Status**: Proposto · **Data**: Julho 2026 · **Autor**: [Nome]

## Contexto
Sistema multi-agente com 15+ workers em 3 domínios (pesquisa web, análise código, síntese). Requer isolamento de contexto e escalabilidade.

## Decisão
Adotar topologia **Hierarchical** com 3 níveis: Supervisor Global → Sub-Supervisores de Domínio → Workers Especializados.

## Alternativas consideradas
- **Supervisor único**: rejeitado porque 15+ workers criam gargalo de decisão e contexto único excessivo.
- **Swarm**: rejeitado porque handoffs implícitos dificultam rastreabilidade exigida.
- **Event-Driven puro**: rejeitado porque a sequência planejar→executar→sintetizar exige coordenação explícita.

## Consequências
- **Positivas**: isolamento de contexto por domínio; escala horizontal em cada sub-árvore.
- **Negativas**: latência adicional (3 hops); complexidade de debug entre níveis.
- **Risco**: sub-supervisor pode se tornar gargalo local → mitigação com timeout + fallback.

## Referências
- Catálogo de Arquiteturas: `10-Architecture/architectures/03-hierarchical.md`
- ETHAGT10 — Topologias Multi-Agente
