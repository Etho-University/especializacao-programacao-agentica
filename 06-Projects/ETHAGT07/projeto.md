# ETHAGT07 — Projeto do Módulo: Pipeline Híbrido Vector + Knowledge Graph

> Curso: Knowledge Graphs & Vector Databases para Agentes · Pilar: Técnico 40% + Prático 10% · Equipe: individual ou dupla

## Contexto / Cenário

Um escritório jurídico que atende clientes em propriedade intelectual mantém um acervo de ~5.000 documentos: patentes, decisões judiciais, contratos de licenciamento e pareceres técnicos. As perguntas dos advogados são frequentemente *multi-hop* e relacional: "Quais patentes co-citadas com a BR-102020-XYZ foram posteriormente invalidadas em decisões do TRF-2?" ou "Liste todos os licenciados do portfólio da empresa A que também são co-autores em patentes da empresa B." RAG vetorial puro falha nessas consultas porque não captura relações estruturais. A direção quer avaliar se um pipeline híbrido (vector DB para recall semântico + knowledge graph para raciocínio relacional, via GraphRAG) resolve o problema sem explodir custo de construção e manutenção.

## Objetivo

Construir um pipeline híbrido (vector + knowledge graph) sobre um corpus técnico (documentos jurídicos ou equivalente do domínio do aluno), com um agente de retrieval que escolhe entre vector search, graph query (Cypher) ou ambos, e justifica a escolha. Entregar um benchmark comparando vector-only, graph-only e híbrido em casos mono-hop e multi-hop, com ADR justificando a estratégia recomendada.

## Requisitos

### Funcionais

1. Vector DB (Qdrant ou pgvector) indexando o corpus com embeddings e metadata filtering.
2. Knowledge graph em Neo4j (ou memgraph) modelando entidades e relações relevantes (ex.: patente, inventor, empresa, decisão, tribunal) extraídas do corpus via LLM.
3. GraphRAG: comunidades detectadas e sumarizadas, suportando local e global search.
4. Agente de retrieval que, dada uma pergunta, decide estratégia (vector / graph / híbrido) e justifica a decisão.
5. Benchmark com ≥15 perguntas mono-hop e ≥15 multi-hop, com ground truth.
6. Comparação de 3 estratégias: vector-only, graph-only, híbrido.

### Não-funcionais

- Latência de query vector ≤ 500 ms; query graph ≤ 1 s; híbrido ≤ 2 s.
- Custo de construção do KG (LLM para extração de entidades/relações) documentado.
- Observabilidade: traces de cada estratégia de retrieval com score de confiança.
- Reindexação incremental documentada (como adicionar novos documentos).
- Corpus de ≥500 documentos (pode ser sintético ou subset de domínio real).

## Entregáveis

- Código (repositório com vector DB, KG, agente de retrieval híbrido).
- Benchmark (3 estratégias × ≥30 perguntas: success rate, latência, custo).
- ADR justificando a estratégia recomendada (quando vector, quando graph, quando híbrido).
- Modelagem do KG (esquema de entidades/relações) documentada em diagrama.

## Critérios de sucesso (mensuráveis)

- Híbrido melhora success rate em casos multi-hop em ≥20% vs vector-only, sem explodir custo (custo híbrido ≤ 2× vector-only).
- Agente de retrieval escolhe a estratégia correta em ≥75% dos casos (validado contra ground truth de estratégia ideal).
- GraphRAG responde corretamente a ≥60% das perguntas multi-hop.
- Benchmark cobre ≥15 perguntas mono-hop e ≥15 multi-hop com medições reais.
- Custo de construção e manutenção do KG é quantificado e justificado no ADR.

## Competências avaliadas

- C1 Programação Agêntica — nível **A** (agente de retrieval que decide estratégia).
- C3 MCP & Tool Use — nível **B** (tools de query vector e Cypher integradas).
- C4 Agent Memory — nível **A** (KG como memória estruturada).
- C5 AgentOps & Avaliação — nível **I** (benchmark comparativo, custo de construção/manutenção).

## Referências

- Apostila: `04-Apostilas/ETHAGT07/apostila.md`
- Rubrica técnica: `08-Assignments/ETHAGT07/assignment-01.md`
