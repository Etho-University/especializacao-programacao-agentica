# ETHAGT04 — Projeto do Módulo: Agente Raciocinador para o Benchmark GAIA

> Curso: Reasoning & Planning (do CoT ao inference-time reasoning) · Pilar: Técnico 40% + Prático 10% · Equipe: individual ou dupla

## Contexto / Cenário

Um laboratório de pesquisa aplicada em IA quer avaliar qual estratégia de raciocínio maximiza o desempenho de um assistente geral em tarefas multi-step do mundo real — não em benchmarks triviais como GSM8K, mas no GAIA, que exige navegação de arquivos, raciocínio multi-hop, uso de tools e combinação de evidências. Há debate interno: parte do time defende Plan-and-Execute (estrutura, custo previsível), outra parte defende Tree of Thoughts/LATS (exploração, qualidade), e há quem aposte em reasoning models nativos (o1/o3, Claude com extended thinking). Você recebe um subconjunto de 20 questões do GAIA (Level 1-2) e deve implementar o agente com pelo menos 3 estratégias distintas, medir e recomendar.

## Objetivo

Implementar um agente que resolve um subconjunto do benchmark GAIA usando pelo menos 3 padrões de raciocínio à escolha (ex.: ReAct, Plan-and-Execute/ReWOO, Tree of Thoughts/LATS, Reflexion, Self-Discover, ou reasoning model nativo). Comparar os resultados (success rate, custo, latência, robustez) e justificar a estratégia recomendada em um ADR.

## Requisitos

### Funcionais

1. Agente que resolve questões do GAIA (subconjunto de ≥20 questões Level 1-2) com tools de acesso a arquivos, web search e cálculo.
2. Pelo menos 3 padrões de raciocínio implementados e intercambiáveis (mesma interface, mesma base de tools).
3. Cada padrão registra: plano/árvore de pensamentos, ações executadas, observações, e resposta final.
4. Reflexion (se usado) mantém memória de falhas entre tentativas no mesmo problema.
5. Mecanismo de orçamento: limite de tokens/passos por questão, com quebra de loops.

### Não-funcionais

- Cada run é traceável (logging de cada reasoning step com timestamps).
- Custo por questão documentado por padrão.
- Reprodutível: seed de execução + versão de modelo fixados no relatório.
- Latência mediana por questão ≤ 60 segundos (para padrões não-tree).
- Suíte de testes de regressão para evitar loop infinito em qualquer padrão.

## Entregáveis

- Código (repositório com as 3+ estratégias e executor de benchmark).
- Benchmark (≥20 questões × 3 padrões, com success rate, custo e latência).
- ADR de estratégia de raciocínio (contexto, opções avaliadas, decisão, trade-offs).
- Traces representativos de cada padrão resolvendo a mesma questão.

## Critérios de sucesso (mensuráveis)

- Diferença de success rate entre os padrões é mensurada e discutida com justificativa técnica.
- Pelo menos um padrão atinge success rate ≥ 30% nas questões Level 1 do GAIA.
- Custo total do benchmark é reportado por padrão e comparado.
- ADR justifica a escolha do padrão recomendado com base em dados, não opinião.
- Nenhum padrão entra em loop infinito (orçamento de passos respeitado em 100% das execuções).

## Competências avaliadas

- C1 Programação Agêntica — nível **I** (implementação de padrões de raciocínio avançados).
- C2 Multi-Agent Systems — nível **B** (plan-and-execute com decomposição).
- C4 Agent Memory — nível **B** (memória de falhas no Reflexion, working memory).
- C5 AgentOps & Avaliação — nível **B** (benchmark, success rate, custo/latência, ADR).

## Referências

- Apostila: `04-Apostilas/ETHAGT04/apostila.md`
- Rubrica técnica: `08-Assignments/ETHAGT04/assignment-01.md`
