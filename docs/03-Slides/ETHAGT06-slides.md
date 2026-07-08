# ETHAGT06 — RAG Agêntico — Slides

> Apresentação para aula síncrona · ~50 min · 14 slides

## Estrutura da aula
- Abertura (5 min): gancho/motivação
- Teoria (25 min): conceitos principais com diagramas de referência
- Demonstração (10 min): código ao vivo ou walkthrough de lab
- Exercício (5 min): questão rápida ou discussão
- Fechamento (5 min): conexão com próximo módulo, leitura recomendada

## Slides

### Slide 1 — Título
- ETHAGT06 — RAG Agêntico (Adaptive · Corrective · Self-RAG · Agentic)
- Professor, data, Universität Etho
- Pré-requisito: ETHAGT04 (RAG Systems do Framework Etho recomendado)
- ~1 min

### Slide 2 — Agenda
1. Por que o RAG ingênuo falha
2. Adaptive RAG
3. Corrective RAG (CRAG)
4. Self-RAG
5. Agentic RAG
6. Engenharia de qualidade (chunking, re-rank, hybrid)
7. Avaliação de RAG
- ~1 min

### Slide 3 — Gancho / Motivação
- Problema: RAG ingênuo "embed + top-k" falha em produção silenciosamente
- Exemplo: pergunta "qual a política de férias para estagiários?" — recupera chunks errados, responde com info genérica
- A solução: agente que decide quando, o quê e como recuperar
- Pergunta: *Quantos de vocês já usaram RAG e obtiveram resposta errada com alta confiança?*
- ~3 min

### Slide 4 — Por que o RAG Ingênuo Falha
- Tipos de falha: chunking ruim, embedding inadequado, sem re-rank, sem eval
- Casos problemáticos: dados tabulares, multilingual, multi-modal
- O custo de "vector DB resolve tudo"
- Pergunta: *Qual o pior tipo de falha — não responder ou responder errado com confiança?*
- ~3 min

### Slide 5 — Adaptive RAG
- Decidir **quando** recuperar (ou responder direto da base do modelo)
- Decidir **quanto** recuperar (quantidade dinâmica de chunks)
- Estratégias: routing por complexidade/pergunta
- Exemplo: "Quem é o presidente do Brasil?" → responde direto; "Qual a política de férias para estagiários?" → recupera
- Diagrama: `12-Diagrams/ETHAGT06/adaptive-rag.mmd`
- ~4 min

### Slide 6 — Corrective RAG (CRAG)
- Avaliar relevância dos docs recuperados (grau de relevância)
- Três caminhos: usar (se relevante) / corrigir (se parcial) / buscar na web (se irrelevante)
- Trigger de fallback: quando a base local não tem a resposta
- Diagrama: `12-Diagrams/ETHAGT06/crag-flow.mmd`
- ~4 min

### Slide 7 — Self-RAG
- Modelo treinado para refletir sobre recuperação
- Tokens de reflexão: `[Retrieve]`, `[Relevant]`, `[Irrelevant]`, `[Support]`, `[No Support]`
- Adaptação para modelos não-treinados: prompting com reflexão
- Caso: perguntas que exigem julgar se o documento recuperado realmente suporta a resposta
- ~3 min

### Slide 8 — Agentic RAG
- Agente dirige todo o processo: planeja busca, refina queries, decide parar
- Multi-hop: cadeias de recuperação ("quem fundou a empresa que criou o ChatGPT?")
- Tools de busca (web, interno, KG) como ferramentas do agente
- Agente decide entre multiple sources e sintetiza
- Referência: `05-Labs/ETHAGT06/Lab2-Agentic-RAG-Multi-Hop`
- ~4 min

### Slide 9 — DEMO: Diagnosticando Falhas de RAG
- Código ao vivo: rodar RAG ingênuo em corpus problemático (docs da Etho)
- Identificar 3 classes de falha ao vivo:
  1. Chunking quebra contexto no meio
  2. Embedding não captura sinônimos
  3. Sem re-rank, top-k traz lixo
- Mostrar antes/depois das correções
- Referência: `05-Labs/ETHAGT06/Lab1-Diagnosticando-Falhas`
- ~5 min

### Slide 10 — Engenharia de Qualidade
- Chunking: semântico, hierárquico, late-chunking
- Re-ranking (Cohere, bge, Jina)
- Query rewriting / HyDE (gera resposta hipotética para buscar)
- Hybrid search (BM25 + densa)
- Multi-vector (ColBERT)
- Pergunta: *Query rewriting: o agente deve reescrever a pergunta do usuário? Quando?*
- ~4 min

### Slide 11 — Avaliação de RAG
- Métricas: faithfulness, answer relevance, context precision/recall
- Frameworks: Ragas, TruLens, DeepEval
- LLM-as-judge com vieses mitigados
- Dataset de holdout para regressão
- Diagrama: `12-Diagrams/ETHAGT06/eval-pipeline.mmd`
- ~3 min

### Slide 12 — Exercício: Adaptive vs Self-RAG
- Cenário: sistema de FAQ jurídico com 10.000 documentos
- Em duplas: quando usar Adaptive RAG vs Self-RAG?
- Critérios: tipo de pergunta, custo, qualidade esperada
- 3 min discussão, 2 min compartilhar
- ~5 min

### Slide 13 — Conexão com Próximo Módulo
- ETHAGT07 — Knowledge Graphs & Vector DBs: além do RAG plano
- Leitura: Asai et al. *Self-RAG* (arXiv:2310.11511)
- Yan et al. *Corrective RAG* (arXiv:2401.15884)
- Edge et al. *GraphRAG* (Microsoft, arXiv:2404.16130)
- ~2 min

### Slide 14 — Referências
- Lewis, P. et al. *Retrieval-Augmented Generation* (arXiv:2005.11401)
- Asai, A. *Self-RAG* (arXiv:2310.11511)
- Yan, S. *Corrective RAG (CRAG)* (arXiv:2401.15884)
- LangGraph examples: adaptive_rag, crag, self_rag, agentic_rag
- Anthropic *Contextual Retrieval* blog
- ~1 min
