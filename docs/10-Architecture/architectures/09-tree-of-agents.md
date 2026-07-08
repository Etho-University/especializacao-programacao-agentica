# Tree of Agents

> Topologia 9/12 · ETHAGT04

## Descrição
Árvore de exploração com backtracking — uma implementação do algoritmo LATS (Language Agent Tree Search) onde múltiplos caminhos de raciocínio são explorados em paralelo, com poda e seleção.

## Estrutura
```
              [Raiz]
          /     |     \
      [Filho1] [Filho2] [Filho3]
       /   \        |        /   \
    [..]  [..]   [..]    [..]  [..]
```
- **Seleção**: escolher nós promissores (UCT)
- **Expansão**: gerar N continuations
- **Simulação**: avaliar caminhos
- **Backpropagation**: atualizar valores

## Quando usar
- Problemas difíceis com múltiplos caminhos viáveis
- Vale a pena explorar antes de executar
- Tempo e custo são secundários

## Quando evitar
- Problemas simples (overkill)
- Custo sensível (N× chamadas)
- Latência crítica

## Trade-offs
| Prós | Contras |
|------|---------|
| Poderoso para problemas complexos | Caro (N× chamadas) |
| Exploração sistemática | Complexo de implementar |
| Resultados superiores em benchmark | Latência alta |

## Referências
- ETHAGT04 — Reasoning & Planning
- LATS: Zhou et al. (arXiv:2310.01757)
- Tree of Thoughts: Yao et al. (arXiv:2305.10601)

## Diagramas relacionados
- `12-Diagrams/ETHAGT04/01-tree-of-thoughts.mmd`
