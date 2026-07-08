# Swarm

> Topologia 8/12 · ETHAGT09

## Descrição
Agentes leves que se passam handoffs (transferência de controle) sem autoridade central. O agente ativo decide para qual especialista delegar — não há supervisor.

## Estrutura
```
[Agente A] ─handoff► [Agente B] ─handoff► [Agente C]
    ▲                                            │
    └──────────────── handoff ───────────────────┘
```

## Quando usar
- Fluxo conversacional com múltiplas especialidades
- Especialistas claramente definidos
- Baixa latência (handoff é rápido)
- Experiência do usuário fluida

## Quando evitar
- Workflow rígido pré-definido
- Muitos agentes sobrepostos (handoff ambíguo)
- Necessita rastreabilidade total (handoffs são implícitos)

## Trade-offs
| Prós | Contras |
|------|---------|
| Leve e flexível | Coordenação difícil |
| Experiência fluida | Rastreabilidade limitada |
| Boa para chatbots | Escala limitada |

## Referências
- ETHAGT09 — Comunicação Multi-Agente
- OpenAI Swarm (experimental)
- LangGraph handoffs

## Diagramas relacionados
- `12-Diagrams/ETHAGT09/01-swarm.mmd`
