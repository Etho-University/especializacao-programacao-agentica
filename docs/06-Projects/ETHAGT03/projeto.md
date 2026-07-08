# ETHAGT03 — Projeto do Módulo: Workflow de Síntese de Relatório Multi-fonte

> Curso: Padrões de Workflow Agêntico · Pilar: Técnico 40% + Prático 10% · Equipe: individual ou dupla

## Contexto / Cenário

Um escritório de consultoria estratégica precisa gerar relatórios executivos semanais que sintetizam informações de múltiplas fontes heterogêneas: relatórios de mercado (PDFs), transcripts de entrevistas com clientes, dados de benchmarking em planilhas, e notícias recentes de webscraping. Hoje, analistas seniores gastam ~6 horas por relatório colando, filtrando e redigindo. A diretoria quer automatizar o pipeline de síntese escolhendo o *workflow composto* mais adequado — mas sem delegar ao agente decisões que devem ser determinísticas (gates de qualidade). O desafio é escolher e justificar a composição de padrões (prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer) que maximize qualidade previsível sem custos explosivos.

## Objetivo

Dada uma tarefa de síntese de relatório a partir de múltiplas fontes, projetar e implementar o workflow composto mais adequado. Comparar empiricamente 2 abordagens (ex.: prompt chaining vs orchestrator-workers) em qualidade, custo e latência, justificando a escolha em um ADR (Architecture Decision Record) apoiado por medições reais em um conjunto de ≥20 casos.

## Requisitos

### Funcionais

1. Pipeline que consome ≥3 tipos de fonte (documentos, transcripts, dados estruturados) e produz um relatório executivo estruturado (≥800 palavras, com seções definidas).
2. Pelo menos 2 workflows implementados e comparados lado a lado.
3. Gates programáticos explícitos (ex.: validação de cobertura de fontes, checagem de seções obrigatórias) entre etapas.
4. Se usado orchestrator-workers, o decomposer divide a tarefa em subtarefas dinâmicas; se usado evaluator-optimizer, há critério de parada mensurável (score, max iters, ou delta estagnado).
5. Saída estruturada com seções, referências e nota de confiança por seção.

### Não-funcionais

- Custo total por relatório documentado e ≤ US$ 0,50.
- Latência total por relatório ≤ 90 segundos.
- Benchmark reproduzível: ≥20 relatórios gerados com mesmas fontes para comparação estatística.
- Avaliação de qualidade via LLM-as-judge com rubrica explícita (coesão, cobertura, acurácia) + ≥3 casos avaliados por humano.
- Implementação via LangGraph (estado + edges condicionais).

## Entregáveis

- Código (repositório com README documentando a composição escolhida).
- Benchmark comparativo (2 abordagens × ≥20 casos × métricas: qualidade, custo, latência).
- ADR justificando a escolha de workflow (contexto, opções, decisão, consequências).
- Logs de execução de cada etapa do pipeline.

## Critérios de sucesso (mensuráveis)

- ADR coerente que referencia medições reais e segue template ADR do repositório.
- ≥20 casos executados com medições reais de custo e latência para ambas as abordagens.
- Workflow escolhido apresenta qualidade (LLM-as-judge) ≥15% superior ao baseline mais simples (resposta direta sem pipeline).
- Diferença de custo entre as 2 abordagens é quantificada e discutida no ADR.
- Gates programáticos bloqueiam saídas inválidas em 100% dos casos de teste de regressão.

## Competências avaliadas

- C1 Programação Agêntica — nível **I** (implementação dos 5 workflows + composição).
- C2 Multi-Agent Systems — nível **B** (orchestrator-workers com múltiplos workers).
- C3 MCP & Tool Use — nível **B** (tools de leitura de fontes integradas ao workflow).
- C5 AgentOps & Avaliação — nível **B** (benchmark, LLM-as-judge, medições de custo/latência).

## Referências

- Apostila: `04-Apostilas/ETHAGT03/apostila.md`
- Rubrica técnica: `08-Assignments/ETHAGT03/assignment-01.md`
