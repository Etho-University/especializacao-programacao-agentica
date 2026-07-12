# Template — Relatório de Avaliação de Agente (Eval Report)

> Preenchido ao avaliar um agente/sistema (lab, projeto, capstone). Artefato central do módulo `ETHAGT12` e exigência do Capstone. Estende boas práticas de LangSmith/Phoenix/Langfuse.

---

# Eval Report — `[Nome do Sistema]`

- **Data**: `[DD/MM/AAAA]`
- **Avaliador**: `[nome]`
- **Versão do sistema**: `[sha / tag]`
- **Cenário**: `[descrição curta]`

## 1. Objetivos e hipóteses

O que o sistema deveria fazer e quais métricas atestar.

## 2. Configuração experimental

| Item | Valor |
|---|---|
| Modelos | `[ex.: Claude Sonnet 4.5 (planner), Haiku 4.5 (workers)]` |
| Framework | `[ex.: LangGraph]` |
| Dataset | `[ex.: GAIA dev, 100 amostras]` |
| Benchmarks | `[SWE-bench / τ-bench / custom]` |
| Run count | `[N runs por caso]` |
| Temperatura | `[...]` |

## 3. Métricas

### 3.1 Qualidade da tarefa
- **Success rate**: `[X%]` (definição: `[...]`)
- **Partial credit**: `[X%]`
- **LLM-as-judge score** (média ± desvio): `[X.X ± Y.Y]`

### 3.2 Eficiência
- **Steps médios por tarefa**: `[N]`
- **Latência p50/p95**: `[Xs / Ys]`
- **Tokens in/out médios**: `[N / M]`
- **Custo por tarefa**: `[$X.XX]`

### 3.3 Robustez
- ** taxa de loops infinitos**: `[X%]`
- **Taxa de erro recuperável**: `[X%]`
- **Taxa de erro fatal**: `[X%]`

### 3.4 Segurança (se aplicável)
- **Prompt injection**: passou em `[X/Y]` testes red team
- **Tool misuse**: `[X%]`

## 4. Resultados detalhados

Tabela por caso/dimensão. Anexar traces (link para LangSmith/Phoenix).

## 5. Análise de falhas

Top 3 categorias de falha + exemplo + causa raiz + correção proposta.

| # | Categoria | Exemplo | Causa raiz | Correção |
|---|---|---|---|---|
| 1 | `[...]` | `[...]` | `[...]` | `[...]` |

## 6. Comparações

Vs baseline (versão anterior, ou framework alternativo, ou humano).

## 7. Conclusões e próximos passos

- **Pronto para produção?** `[Sim / Com ressalvas / Não]`
- **Riscos remanescentes**: `[...]`
- **Próximos experimentos**: `[...]`

## 8. Reprodutibilidade

- Código: `[link/SHA]`
- Datasets: `[link/version]`
- Configs: `[link]`
- Traces: `[link]`
- Comando de rerun: `[cmd]`

---

*Sempre que possível, anexar: gráfico de distribuição de scores, trace exemplar de sucesso, trace exemplar de falha.*
