# Blackboard

> Topologia 4/12 · ETHAGT09

## Descrição
Espaço compartilhado (blackboard) onde múltiplos agentes especialistas leem e escrevem incrementalmente, sem comunicação direta entre si.

## Estrutura
```
                   [Blackboard]
                  /      |      \
        Espec. A    Espec. B   Espec. C
```
- **Blackboard**: estrutura de dados compartilhada (banco, cache, doc)
- **Especialistas**: agentes que contribuem quando identificam oportunidade

## Quando usar
- Problema dinâmico onde especialistas contribuem incrementalmente
- Baixo acoplamento desejado entre agentes
- Conhecimento é aditivo (cada agente acrescenta)

## Quando evitar
- Poucos agentes com papéis claros (mensagens diretas são mais simples)
- Ordem de execução importa (pipeline é melhor)
- Custo sensível (todos veem todo o blackboard)

## Trade-offs
| Prós | Contras |
|------|---------|
| Flexibilidade máxima | Custo de tokens alto |
| Baixo acoplamento | Sem garantia de conclusão |
| Paralelismo natural | Conteúdo pode crescer sem limite |

## Referências
- ETHAGT09 — Comunicação Multi-Agente
- Clássico de IA (Newell, 1962)

## Diagramas relacionados
- `12-Diagrams/ETHAGT09/03-blackboard.mmd`
