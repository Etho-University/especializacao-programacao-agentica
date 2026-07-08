# Workflow: Routing

## Intenção
Classificar o input e direcioná-lo para um **ramo especializado** com prompt/tools/modelo próprios.

## Estrutura
```
input ─► [Classifier] ─┬─► [LLM A]
                       ├─► [LLM B]
                       └─► [LLM C]
```

## Quando usar
- Categorias distintas melhor tratadas separadamente.
- Classificação confiável.
- Quer otimizar custo (casos fáceis → modelo menor).

## Quando evitar
- Categorias sobrepostas.
- Sem fallback.
- Volume baixo que não justifica.

## Variações
- **Por tipo de input** (geral/reembolso/técnico).
- **Por modelo** (fácil → Haiku; difícil → Sonnet).
- **Por prompt/tools** (cada ramo especializado).

## Classificador
Pode ser LLM (pouco-shot) ou modelo tradicional (logistic regression sobre embeddings). Avalie accuracy em dataset rotulado.

## Anti-patterns
- Categorias ambíguas.
- Sem fallback para input não-classificável.
- Re-roteamento em loop (A→B→A).

## Custo
1 chamada de classificação + 1 chamada no ramo escolhido. Geralmente barato.

## Referências
- Anthropic *Building Effective Agents* (2024).
