# ETHAGT01 — Projeto do Módulo: Research Assistant Agêntico

> Curso: Arquitetura Cognitiva de Agentes LLM · Pilar: Técnico 40% + Prático 10% · Equipe: individual ou dupla

## Contexto / Cenário

Você foi contratado por uma *fintech* de investimentos emergentes que mantém uma base interna de relatórios de análise, atas de earnings calls e glossário de termos financeiros. O time de analistas perde tempo respondendo perguntas factuais que já têm resposta em documentos internos. A diretoria quer um *research assistant* que, dada uma pergunta factual (ex.: "Qual o EBITDA ajustado da Petrobras no 3T25?"), decida autonomamente entre: (a) responder direto a partir do conhecimento paramétrico do modelo, (b) recuperar de um corpus local via RAG, ou (c) acionar uma tool de busca na web. O sistema deve ser transparente, observável e justificável — a área de compliance exige rastreabilidade das decisões do agente.

## Objetivo

Implementar um agente *research assistant* no padrão ReAct (Augmented LLM) que decide entre três caminhos de ação (resposta direta, retrieval local ou busca web) em cada turno. O mesmo agente deve ser entregue em três versões — Python puro, LangGraph e um terceiro framework à escolha (CrewAI, PydanticAI ou Agno) — com um README comparativo que justifique a escolha de stack para produção.

## Requisitos

### Funcionais

1. O agente recebe uma pergunta factual em linguagem natural e retorna uma resposta com citação de fonte.
2. Decisão de rota (direto / local / web) é tomada pelo próprio agente em cada iteração do loop ReAct.
3. Base local: vetor store simples (ChromaDB ou Qdrant) com ≥30 documentos de domínio financeiro.
4. Tool de busca web: integração com uma API pública (DuckDuckGo, Tavily ou SerpAPI).
5. Loop ReAct com no máximo 5 iterações e condição de parada clara.
6. Três implementações equivalentes em comportamento: Python puro, LangGraph, framework à escolha.

### Não-funcionais

- Logging estruturado (JSON) com timestamps para cada etapa Thought → Action → Observation.
- Traces de execução exportáveis (arquivo `.json` ou `.html` por run).
- Custo e latência registrados por chamada de LLM.
- Custo total por pergunta ≤ US$ 0,10 (usando modelo Haiku ou equivalente).
- Latência mediana por pergunta ≤ 8 segundos.
- Container Docker para execução reproduzível.

## Entregáveis

- Código (repositório Git com README detalhado e instruções de execução).
- README comparativo (3 versões × ≥3 critérios: controle, transparência, esforço de implementação).
- Traces de exemplo (≥6 runs, cobrindo os 3 caminhos de decisão).
- Relatório de custo/latência por versão.

## Critérios de sucesso (mensuráveis)

- Agente funcional e coerente nas 3 versões, respondendo corretamente a ≥80% das 10 perguntas do conjunto de teste.
- Comparação justifica a escolha de stack com base em ≥3 critérios explícitos (controle fino, transparência, esforço de desenvolvimento).
- Os três caminhos de decisão (direto / local / web) são exercitados ao menos uma vez nos traces entregues.
- Trace de cada run demonstra o raciocínio (Thought) antes de cada Action.
- Nenhuma das 3 versões entra em loop infinito (limite de iterações respeitado em 100% das execuções).

## Competências avaliadas

- C1 Programação Agêntica — nível **I** (implementação do agent loop ReAct do zero).
- C3 MCP & Tool Use — nível **B** (tools bem documentadas, schema claro).
- C4 Agent Memory — nível **B** (working memory gerenciada na context window).
- C5 AgentOps & Avaliação — nível **B** (logs estruturados, traces, custo/latência desde o dia 1).

## Referências

- Apostila: `04-Apostilas/ETHAGT01/apostila.md`
- Rubrica técnica: `08-Assignments/ETHAGT01/assignment-01.md`
