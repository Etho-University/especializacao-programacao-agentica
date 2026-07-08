# Hybrid

> Topologia 12/12 · ETHAGT10, ETHAGT90

## Descrição
Composição realista de múltiplas topologias — ex.: supervisor (coordenação) + event-driven (comunicação assíncrona) + pipeline (etapas fixas). É a topologia mais comum em produção.

## Estrutura
```
[Supervisor Global]
    │
    ▼
[Event Bus: Kafka] ───► Agent Pool (workers)
    │                          │
    ▼                          ▼
[Pipeline: review → publish]  [RAG Pipeline]
```
Cada subsistema usa a topologia mais adequada.

## Quando usar
- Produção real (quase sempre híbrido)
- Sistemas com requisitos variados (partes síncronas e assíncronas)
- Quando uma topologia pura não atende a todos os requisitos

## Quando evitar
- Protótipos (comece simples)
- Sistemas pequenos (complexidade desnecessária)
- Equipe sem experiência em sistemas distribuídos

## Trade-offs
| Prós | Contras |
|------|---------|
| Otimizado para o caso | Complexidade máxima |
| Melhor relação custo/benefício | ADR necessário para cada decisão |
| Padrão real de produção | Debug multi-topologia |

## Referências
- ETHAGT10 — Topologias Multi-Agente
- ETHAGT90 — Capstone
- Casos de produção: Anthropic, Block, Notion
