# Hierarchical

> Topologia 3/12 · ETHAGT10

## Descrição
Árvore de supervisores em níveis: supervisor de topo delega a sub-supervisores, que coordenam workers. Hierarquia real com isolamento de domínio.

## Estrutura
```
         [Supervisor Global]
            /           \
    [Sup. Pesquisa]  [Sup. Escrita]
        /      \          /     \
    W1      W2        W3     W4
```

## Quando usar
- Muitos workers (>10)
- Sub-domínios naturalmente separáveis (ex.: pesquisa, escrita, revisão, publicação)
- Isolamento de contexto e ferramentas por domínio

## Quando evitar
- Sistemas pequenos (a complexidade não se justifica)
- Baixa latência crítica (cada nível adiciona hop)

## Trade-offs
| Prós | Contras |
|------|---------|
| Escala bem (O(log N) profundidade) | Latência média-alta |
| Isolamento de contexto por nível | Complexidade de debug |
| Reaproveitamento de sub-árvores | Coordenação entre ramos é difícil |

## Referências
- ETHAGT10 — Topologias Multi-Agente
- MetaGPT
- LangGraph `hierarchical_agent_teams`

## Diagramas relacionados
- `12-Diagrams/ETHAGT10/02-hierarchical.mmd`
