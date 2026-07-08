# ETHAGT06 — Projeto do Módulo: Sistema RAG Agêntico de Produção

> Curso: RAG Agêntico (Adaptive · Corrective · Self-RAG · Agentic) · Pilar: Técnico 40% + Prático 10% · Equipe: individual ou dupla

## Contexto / Cenário

A Universidade Etho precisa de um assistente que responda perguntas de alunos e professores com base na documentação oficial da especialização (ementas, regulamentos, calendário acadêmico, FAQs, apostilas). Um RAG ingênuo já foi tentado e falhou: chunking inadequado quebra tabelas de ementa, não há re-ranking, perguntas multi-hop (ex.: "Quais são os pré-requisitos do curso ETHAGT10 e qual a carga horária total da fase C?") retornam respostas parciais ou alucinadas, e não há pipeline de avaliação automatizada para detectar regressões. A coordenação quer um sistema RAG *agêntico* que decida quando recuperar, corrija recuperações ruins, e seja avaliado continuamente com métricas canônicas (faithfulness, context recall/precision).

## Objetivo

Construir um sistema RAG de produção sobre o corpus da documentação Etho, com pipeline agêntico (Adaptive + Corrective RAG), engenharia de qualidade (chunking semântico, re-ranking, hybrid search) e avaliação automatizada com Ragas. Entregar um eval report completo que demonstre que o sistema atinge os critérios de qualidade e um ADR justificando as escolhas de arquitetura.

## Requisitos

### Funcionais

1. Corpus: ≥100 documentos da documentação Etho (ementas, regulamentos, FAQs, calendário).
2. Pipeline agêntico: Adaptive RAG (decide recuperar ou responder direto) + Corrective RAG (avalia relevância dos docs, fallback para web search se necessário).
3. Engenharia de qualidade: chunking semântico/hierárquico, hybrid search (BM25 + densa), re-ranking (bge ou Cohere), query rewriting/HyDE.
4. Multi-hop: agente refina queries e encadeia recuperações para perguntas que exigem múltiplas fontes.
5. Avaliação automatizada com Ragas: faithfulness, answer relevance, context precision, context recall.
6. Dataset de teste (holdout) com ≥40 perguntas e referências (ground truth).

### Não-funcionais

- Latência mediana por pergunta ≤ 5 segundos.
- Custo por pergunta ≤ US$ 0,05.
- Multi-tenant seguro: isolamento de corpus por papel (aluno vs professor).
- Pipeline de eval reproduzível (script único regenera o eval report).
- Observabilidade: traces de cada etapa de recuperação (query gerada, docs recuperados, score de relevância).

## Entregáveis

- Código (repositório com pipeline RAG agêntico + dataset de teste).
- Eval report (template `24-Templates/template-eval-report.md`): métricas Ragas, análise de falhas, comparação com RAG ingênuo.
- ADR justificando escolhas (chunking, hybrid search, CRAG vs Self-RAG, modelo de re-ranking).
- Demo com 5 perguntas representativas respondendo com fontes citadas.

## Critérios de sucesso (mensuráveis)

- Faithfulness ≥ 0,85 no dataset de teste (≥40 perguntas).
- Context recall ≥ 0,80 no dataset de teste.
- Pipeline agêntico supera RAG ingênuo em ≥15% em pelo menos 2 métricas Ragas.
- Eval report é reproduzível: re-execução gera os mesmos resultados (±5%).
- ≥3 categorias de falha do RAG ingênuo são documentadas com correção aplicada.

## Competências avaliadas

- C1 Programação Agêntica — nível **A** (agente que dirige a recuperação).
- C3 MCP & Tool Use — nível **B** (tools de busca como ferramentas do agente).
- C4 Agent Memory — nível **I** (gestão de contexto recuperado na context window).
- C5 AgentOps & Avaliação — nível **I** (pipeline de eval Ragas, métricas, regressão).

## Referências

- Apostila: `04-Apostilas/ETHAGT06/apostila.md`
- Rubrica técnica: `08-Assignments/ETHAGT06/assignment-01.md`
