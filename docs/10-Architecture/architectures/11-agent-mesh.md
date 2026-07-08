# Agent Mesh

> Topologia 11/12 · ETHAGT10

## Descrição
Topologia peer-to-peer flat onde todos os agentes podem se comunicar diretamente. Não há hierarquia nem coordenação central — cada agente decide com quem falar.

## Estrutura
```
    [A] ─── [B]
    / \     / \
  [C] [D]─[E] [F]
```
Cada agente: roteia, processa, e mantém estado local.

## Quando usar
- Poucos agentes altamente colaborativos
- Exploração e prototipação
- Quando a estrutura de coordenação é desconhecida

## Quando evitar
- Muitos agentes (N² conexões)
- Previsibilidade necessária
- Requisitos de auditoria/rastreabilidade

## Trade-offs
| Prós | Contras |
|------|---------|
| Flexibilidade máxima | N² conexões |
| Sem SPOF | Custo e complexidade altos |
| Colaboração direta | Debug muito difícil |

## Referências
- ETHAGT10 — Topologias Multi-Agente
- Comum em sistemas distribuídos clássicos; raro em LLM
