# Workflow: Evaluator-Optimizer

## Intenção
Um LLM gera saída; outro avalia contra critérios e dá feedback; gerador refina. Loop até satisfazer critério.

## Estrutura
```
[Generator] ─► [Evaluator] ─► satisfaz? ─não─► [Generator] (com feedback)
                  │
                  sim
                  ▼
              [saída final]
```

## Quando usar (sinais de bom fit)
1. **Feedback humano articulável melhora a saída** — se você consegue descrever como melhorar, o evaluator também consegue.
2. **O LLM consegue avaliar** — a tarefa tem critérios objetivos suficientes.

## Exemplos
- Tradução literária (tradutor + crítico de nuances).
- Busca complexa (search + evaluator decide se precisa de mais).
- Geração de código (gera + evaluator roda testes).

## Critérios de parada
- Score atingiu limite (evaluator numérico ≥ X).
- Delta estagnado (melhora < ε).
- Max iterations (teto).
- Tempo/custo orçado.

## Anti-patterns
- Sem critério de parada (loop infinito).
- Evaluator genérico ("está bom?").
- Evaluator muito leniente (sempre aprova) ou muito rígido.
- Generator não usa o feedback (ignora crítica).

## Custo
2 chamadas por iteração × N iterações. Calibre N (max 3-5 tipicamente).

## Referências
- Anthropic *Building Effective Agents* (2024).
- Shinn et al. *Reflexion* (arXiv:2303.11366) — variação com memória cross-tentativa.
