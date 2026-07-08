# Workflow: Parallelization

## Intenção
Múltiplos LLMs rodam **simultaneamente**; resultados agregados programaticamente. Duas variantes: **sectioning** e **voting**.

## Estrutura

### Sectioning (subtarefas independentes)
```
input ─► particionar ─┬─► [LLM A: parte A]
                      ├─► [LLM B: parte B]
                      └─► [LLM C: parte C]
                              │
                              ▼
                         aggregator
```

### Voting (mesma tarefa N vezes)
```
input ─► replicar ─┬─► [LLM (tentativa 1, prompt/temp diferente)]
                   ├─► [LLM (tentativa 2)]
                   └─► [LLM (tentativa 3)]
                              │
                              ▼
                         aggregator (maioria / união / melhor)
```

## Quando usar sectioning
- Partes independentes do problema.
- Velocidade importa (paralelismo).
- Cada parte beneficia de atenção focada.
- Exemplo: **guardrails em paralelo** (responder + filtrar separados).

## Quando usar voting
- Quer **confiança** via diversidade.
- Risco de alucinação; múltiplas tentativas reduzem erro.
- Pode avaliar qual é melhor (evaluator).

## Agregação (código)
- Maioria (voting).
- União (qualquer flag = alerta).
- Interseção (todos concordam).
- Melhor de N via evaluator.
- Combinação (sintetizar).

## Anti-patterns
- Dependências ocultas entre "independentes".
- Voting sem agregação clara.
- Custo explodindo (N× trabalho sem justificativa).
- Prompts idênticos em voting (precisa diversidade).

## Custo
N× chamadas LLM (paralelas em wall-clock). Justificar com ganho de qualidade/confiança.

## Referências
- Anthropic *Building Effective Agents* (2024).
- Wang et al. *Self-Consistency* (arXiv:2203.11171).
