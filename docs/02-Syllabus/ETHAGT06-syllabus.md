---
tags:
  - ETHAGT06
  - syllabus
  - rag
  - retrieval
---

# `ETHAGT06` — RAG Agêntico

> Fase B · Carga 30 h · Versão 1.0 · Julho 2026

## 1. Identificação

| Campo | Valor |
|---|---|
| Código | `ETHAGT06` |
| Título | RAG Agêntico (Adaptive · Corrective · Self-RAG · Agentic) |
| Fase interna | B |
| Carga horária | 30 h |
| Pré-requisitos | `ETHAGT04` (RAG Systems do Framework Etho recomendado) |
| Módulos que dependem deste | `ETHAGT07`, `ETHAGT90` |

## 2. Objetivos

**Objetivo geral**: Evoluir além do RAG "ingênuo" para **RAG agêntico**, onde o agente decide *quando*, *o quê* e *como* recuperar, com correção iterativa e auto-avaliação.

**Objetivos específicos**:
1. Diagnosticar limites do RAG ingênuo em produção.
2. Implementar Adaptive RAG, Corrective RAG (CRAG), Self-RAG e Agentic RAG.
3. Aplicar técnicas de qualidade: chunking inteligente, re-ranking, query rewriting, hybrid search.
4. Construir pipeline de avaliação de RAG (faithfulness, relevance, context recall/precision).
5. Produzir um sistema RAG multi-tenant com segurança.

## 3. Competências desenvolvidas

| Competência | Nível ao final |
|---|---|
| C1 Programação Agêntica | **A** |
| C3 MCP & Tool Use | B |
| C4 Agent Memory | **I** |
| C5 AgentOps & Avaliação | **I** |

## 4. Conteúdo programático

### Unidade 1 — Por que o RAG ingênuo falha (3 h)
- Tipos de falha: chunking ruim, embedding errado, sem re-rank, sem eval
- Casos: dados tabulares, multilingual, multi-modal
- O custo de "vector DB resolve tudo"

### Unidade 2 — Adaptive RAG (4 h)
- Decidir quando recuperar (ou responder direto)
- Decidir quanto recuperar
- Estratégias: routing por complexidade/pergunta

### Unidade 3 — Corrective RAG (CRAG) (5 h)
- Avaliar relevância dos docs recuperados
- Três caminhos: usar / corrigir / buscar na web
- Trigger de fallback

### Unidade 4 — Self-RAG (4 h)
- Modelo treinado para refletir sobre recuperação
- Tokens de reflexão
- Adaptação para modelos não-treinados: prompting

### Unidade 5 — Agentic RAG (5 h)
- Agente dirige todo o processo: planeja busca, refina queries, decide parar
- Multi-hop: cadeias de recuperação
- Tools de busca (web, interno, KG) como ferramentas do agente

### Unidade 6 — Engenharia de qualidade (5 h)
- Chunking: semântico, hierárquico, late-chunking
- Re-ranking (Cohere, bge, Jina)
- Query rewriting / HyDE
- Hybrid search (BM25 + densa)
- Multi-vector (ColBERT, estilo)

### Unidade 7 — Avaliação de RAG (4 h)
- Métricas: faithfulness, answer relevance, context precision/recall
- Ragas, TruLens, DeepEval
- LLM-as-judge com vieses mitigados
- Dataset deHoldout

## 5. Bibliografia

### Fundamental
- Lewis, P. et al. *Retrieval-Augmented Generation* (arXiv:2005.11401).
- Asai, A. *Self-RAG* (arXiv:2310.11511).
- Yan, S. *Corrective RAG (CRAG)* (arXiv:2401.15884).

### Complementar
- LangGraph examples: `adaptive_rag`, `crag`, `self_rag`, `agentic_rag`.
- Edge, D. *GraphRAG: From Local to Global* (Microsoft).

## 6. Papers canônicos

- `arXiv:2005.11401` — RAG original
- `arXiv:2310.11511` — Self-RAG
- `arXiv:2401.15884` — Corrective RAG
- `arXiv:2404.16130` — GraphRAG

## 7. Laboratórios

- **Lab 1** (4 h): "Diagnosticando falhas". Rodar RAG ingênuo em um corpus problemático; identificar 3 classes de falha.
- **Lab 2** (5 h): "Agentic RAG multi-hop". Implementar agente que refina queries e combina fontes.

## 8. Projeto do módulo

**Descrição**: construir um sistema RAG de produção sobre um corpus técnico (ex.: documentação Etho), com pipeline agêntico, eval automatizado (Ragas) e relatório de qualidade.
**Entrega**: sistema + eval report (template `24-Templates/template-eval-report.md`) + ADR.
**Critério de sucesso**: faithfulness ≥ 0.85 e context recall ≥ 0.80 no dataset de teste.

## 9. Exercícios

1. Diferencie Adaptive RAG de Self-RAG.
2. Quando CRAG decide buscar na web?
3. Liste 3 estratégias de chunking e quando cada brilha.
4. Escreva um prompt de re-ranking por relevância.
5. Verdadeiro/falso: "Sempre adicionar mais docs recuperados melhora a resposta."

## 10. Avaliação

| Pilar | Peso | Instrumento |
|---|---|---|
| Técnico | 40% | Projeto + eval report |
| Consultivo | 30% | Apresentação dos resultados para "cliente" |
| Comportamental | 20% | Code review |
| Prático | 10% | Demo: agente respondendo com fontes |

**Nota mínima**: 3,0.

## 11. Slides

- Slides: `03-Slides/ETHAGT06-slides.md` (~85 slides).

## 12. Leitura complementar

- Anthropic *Contextual Retrieval*; Cohere rerank docs.

## 13. Ferramentas

- LangGraph, Qdrant/Milvus, Cohere/bge, Ragas, TruLens.

## 14. Diagramas

- Diagramas: `12-Diagrams/ETHAGT06/` — adaptive-rag.mmd, crag-flow.mmd, eval-pipeline.mmd.

## 15. Estudo de caso

- RAG em produção em assistentes enterprise.

## 16. Ficha de pesquisa

- Ficha: `20-Research/ETHAGT06-pesquisa.md`.

---

*Mantido por: Universidade Etho · Versão 1.0 · Julho 2026*
