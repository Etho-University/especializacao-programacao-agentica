# Recursive

> Topologia 10/12 · ETHAGT15

## Descrição
Meta-agentes que criam sub-agentes recursivamente para lidar com subtarefas emergentes. A estrutura não é pré-definida — emerge da execução.

## Estrutura
```
[Agente Pai]
    │
    ├──► cria [Sub-Agente A] para subtarefa X
    │       │
    │       └──► cria [Sub-Agente A.1] para sub-subtarefa
    │
    └──► cria [Sub-Agente B] para subtarefa Y
```

## Quando usar
- Problemas muito abertos onde estrutura emerge
- Meta-programming (agentes que escrevem agentes)
- Sistemas auto-evolutivos

## Quando evitar
- Sem orçamento claro (explosão)
- Sem validação de sub-agentes
- Problemas com estrutura conhecida (faça pipeline)

## Trade-offs
| Prós | Contras |
|------|---------|
| Adaptativo ao problema | Risco de explosão combinatoria |
| Potencial ilimitado | Difícil de governar |
| Útil para fronteira (pesquisa) | Custo imprevisível |

## Referências
- ETHAGT15 — Meta-Agentes
- Voyager: Wang et al. (arXiv:2305.16291)
- AI Scientist: Lu et al. (arXiv:2408.06292)
