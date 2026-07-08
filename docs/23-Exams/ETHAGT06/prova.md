# ETHAGT06 — Prova do Módulo: RAG Agêntico

> Universidade Etho · Versão 1.0 · Julho 2026
> Duração: ~60 min · 10 questões · closed book · Pilar Técnico (40%)

Esta prova avalia a evolução do RAG ingênuo para RAG agêntico: Adaptive RAG, Corrective RAG, Self-RAG, Agentic RAG, engenharia de qualidade e avaliação sistemática.

---

## Parte 1 — Conceitos (Q1-4)

**1. (Múltipla escolha)** Qual é a principal diferença entre Adaptive RAG e Self-RAG?
- (a) Adaptive RAG usa modelos menores
- (b) Adaptive RAG roteia por complexidade via classificador externo; Self-RAG usa tokens de reflexão internos ao modelo
- (c) Self-RAG não recupera documentos
- (d) Adaptive RAG é sempre mais barato

**2. (V/F justificado)** "Sempre adicionar mais documentos recuperados melhora a resposta do RAG."

**3. (Múltipla escolha)** No Corrective RAG (CRAG), o que acontece quando os documentos recuperados são classificados como **incorretos** (irrelevantes)?
- (a) O sistema retorna erro
- (b) O sistema descarta os documentos e busca na web como fallback
- (c) O sistema usa os documentos mesmo assim
- (d) O sistema reinicia a query

**4. (V/F justificado)** "O anti-pattern 'vector DB resolve tudo' é a crença de que jogar tudo num vector database é um sistema completo de RAG."

---

## Parte 2 — Aplicação e trade-off (Q5-8)

**5. (Trade-off)** Liste 3 classes de falha do RAG ingênuo e uma correção para cada.

**6. (Análise de qualidade)** Explique a diferença entre busca densa (vetorial) e esparsa (BM25). Quando o hybrid search é preferível?

**7. (Debug de RAG)** Um sistema RAG tem faithfulness baixa (0.45) mas context recall alto (0.92). O que isso indica? Qual técnica de engenharia de qualidade poderia ajudar?

**8. (V/F justificado)** "O HyDE gera um documento hipotético que seria a resposta ideal e busca por documentos similares a esse, casando por semântica da resposta."

---

## Parte 3 — Projeto curto (Q9-10)

**9. (Projeto curto)** Escreva o esqueleto de um Agentic RAG multi-hop onde o agente tem acesso a 3 tools (`search_internal`, `search_web`, `search_kg`) e decide quantos hops executar.

**10. (Projeto curto)** Defina as 4 métricas canônicas de avaliação de RAG (estilo Ragas) e diga o que cada uma mede.

---

## Critérios de correção (resumo)

| Conceito | Questões | Peso |
|---|---|---|
| Padrões agênticos (Adaptive/CRAG/Self-RAG) | 1, 3 | 20% |
| Falhas do RAG ingênuo | 4, 5 | 20% |
| Engenharia de qualidade | 6, 8 | 20% |
| Avaliação & métricas | 2, 7, 10 | 25% |
| Agentic RAG | 9 | 15% |

**Conversão**: cada questão vale 10 pts; total 100 pts. Nota 1-5.
- 90+ pts: 5,0
- 75-89: 4,0
- 60-74: 3,0 (mínimo aprovação)
- <60: reprovação.

Gabarito comentado em [`gabarito.md`](gabarito.md).
