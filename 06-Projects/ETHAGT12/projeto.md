# ETHAGT12 — Projeto do Módulo: Eval Report de Agente em τ-bench/GAIA

> Curso: AgentOps, Observabilidade & Avaliação (LLMOps para agentes) · Pilar: Técnico 40% + Prático 10% · Equipe: individual ou dupla

## Contexto / Cenário

O time de ML/AI de uma empresa de assistentes virtuais precisa apresentar para a diretoria um relatório rigoroso que responda: "Nosso agente de suporte está pronto para produção?" A diretoria exige evidências, não anedotas — e cobra comparabilidade com benchmarks canônicos. O agente (construído em módulos anteriores) deve ser avaliado em um subconjunto de τ-bench (tool use em domínios como airline/retail) ou GAIA (raciocínio geral multi-step). O desafio é montar um pipeline de avaliação reproduzível, com observabilidade (traces), LLM-as-judge calibrado, golden cases, e um relatório que categorize falhas honestamente — incluindo o que ainda *não* funciona.

## Objetivo

Avaliar um agente (construído em módulos anteriores, ou fornecido) em um subconjunto de τ-bench ou GAIA; produzir um eval report completo e reproduzível com pipeline de re-execução, dataset versionado, análise de falhas categorizada e correções propostas.

## Requisitos

### Funcionais

1. Agente avaliado em ≥30 casos de τ-bench (airline ou retail) ou GAIA (Level 1-2).
2. Observabilidade end-to-end: traces (spans) via LangSmith, Phoenix ou Langfuse para cada run.
3. Avaliação automatizada: success rate, partial credit, custo/latência por caso, métricas de processo (steps, loops, tool misuse).
4. LLM-as-judge com rubrica explícita, vieses mitigados (position bias, verbosity bias) e ≥5 golden cases para calibração.
5. Pipeline de re-execução: script único regenera o eval report a partir do dataset versionado.
6. Detecção de regressão: alteração de prompt/modelo deve ser detectável pelo pipeline.

### Não-funcionais

- Eval reproduzível: re-execução produz resultados dentro de ±5% (com modelo e seed fixos).
- Custo total da avaliação documentado.
- Dataset versionado (git ou DVC) com ground truth.
- Traces exportáveis e navegáveis (URL ou arquivo).
- Latência da suíte de eval completa ≤ 15 minutos.

## Entregáveis

- Eval report (template `24-Templates/template-eval-report.md`): métricas, análise de falhas, comparações honestas.
- Dataset versionado (≥30 casos com ground truth e critério de sucesso).
- Código de re-execução (pipeline reproduzível, script único).
- Análise de falhas (≥3 categorias com exemplos, causa raiz e correção proposta).

## Critérios de sucesso (mensuráveis)

- Eval é reproduzível: re-execução gera resultados dentro de ±5% com modelo e seed fixos.
- ≥3 categorias de falha documentadas com correção proposta (ex.: tool misuse, loop, contexto insuficiente).
- Success rate reportado com intervalo de confiança (não apenas ponto).
- LLM-as-judge calibrado: concordância com humano (≥5 golden cases) ≥70%.
- Pipeline detecta regressão: mudança intencional de prompt que degrada performance é sinalizada automaticamente.

## Competências avaliadas

- C1 Programação Agêntica — nível **A** (integração de observabilidade e eval em sistema agêntico).
- C2 Multi-Agent Systems — nível **B** (traces em sistemas com múltiplos componentes).
- C4 Agent Memory — nível **B** (observabilidade de contexto e estado).
- C5 AgentOps & Avaliação — nível **A** (pipeline de eval, LLM-as-judge, benchmarks, eval report).

## Referências

- Apostila: `04-Apostilas/ETHAGT12/apostila.md`
- Rubrica técnica: `08-Assignments/ETHAGT12/assignment-01.md`
