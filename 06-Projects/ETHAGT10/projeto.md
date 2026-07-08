# ETHAGT10 — Projeto do Módulo: Revisão de PR Multi-Agente

> Curso: Padrões de Arquitetura Multi-Agente (topologias) · Pilar: Técnico 40% + Prático 10% · Equipe: individual ou dupla

## Contexto / Cenário

Uma empresa de infraestrutura de devops recebe dezenas de pull requests por dia em um monorepo crítico. A revisão manual é gargalo: senior engineers gastam ~40% do tempo em review. O time de Platform Engineering quer um sistema multi-agente de revisão automatizada onde especialistas virtuais (segurança, performance, estilo/arquitetura, testes) analisam cada PR em paralelo e um supervisor consolida o veredito. O desafio arquitetural é escolher a topologia certa: Supervisor com workers especializados? Hierarchical com sub-equipes? Swarm com handoffs? A escolha deve ser justificada com medições reais, não intuição.

## Objetivo

Dada a tarefa de revisão de pull requests com especialistas virtuais, projetar e implementar a topologia multi-agente mais adequada (justificada em ADR). Comparar a topologia escolhida com pelo menos 1 alternativa em um benchmark de PRs reais, medindo qualidade de review, custo, latência e consistência.

## Requisitos

### Funcionais

1. Sistema que recebe um PR (diff + contexto) e produz um relatório de revisão estruturado (issues por categoria, severidade, sugestões).
2. ≥4 agentes especialistas (segurança, performance, arquitetura/estilo, testes/cobertura).
3. Topologia principal implementada (Supervisor, Hierarchical, Swarm, ou outra) + ≥1 alternativa para comparação.
4. Supervisor/agente consolidador agrega as contribuições e resolve conflitos (ex.: especialista de segurança pede refactor, especialista de performance pede early return).
5. Saída compatível com formato de review do GitHub (comentários por arquivo/linha).

### Não-funcionais

- Benchmark em ≥15 PRs reais (open-source ou sintéticos com issues injetados).
- Latência por PR ≤ 60 segundos para topologia escolhida.
- Custo por PR documentado por topologia.
- ADR segue template do repositório (contexto, opções, decisão, consequências).
- Avaliação de qualidade: LLM-as-judge + ≥5 PRs revisados por humano (ground truth).

## Entregáveis

- Código (repositório com as topologias implementadas).
- ADR de topologia (justificativa baseada em medições, não opinião).
- Benchmark comparativo (topologia escolhida vs alternativa: qualidade, custo, latência).
- Demo: sistema revisando um PR ao vivo com output formatado.

## Critérios de sucesso (mensuráveis)

- ADR coerente com medições reais justificando a topologia escolhida.
- ≥15 PRs avaliados com medições reais de qualidade, custo e latência para ambas as topologias.
- Topologia escolhida atinge precision ≥0,7 e recall ≥0,6 na detecção de issues (vs ground truth humano em ≥5 PRs).
- Diferença de custo e latência entre topologias é quantificada e discutida no ADR.
- Supervisor resolve conflitos entre especialistas sem contradita em ≥85% dos PRs.

## Competências avaliadas

- C1 Programação Agêntica — nível **A** (sistema multi-agente de produção).
- C2 Multi-Agent Systems — nível **A** (escolha e justificação de topologia, supervisor, workers).
- C3 MCP & Tool Use — nível **B** (tools de leitura de diff, query de código).
- C4 Agent Memory — nível **B** (estado compartilhado entre agentes).
- C6 Agent Security — nível **B** (especialista de segurança, não-execução de código não-confiado).

## Referências

- Apostila: `04-Apostilas/ETHAGT10/apostila.md`
- Rubrica técnica: `08-Assignments/ETHAGT10/assignment-01.md`
