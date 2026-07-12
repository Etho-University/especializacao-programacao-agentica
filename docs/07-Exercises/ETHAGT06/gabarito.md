# ETHAGT06 — Gabarito

> Restrito a mentores. Cada resposta justificada com referência à apostila.

## Múltipla escolha

1. **b)** — CRAG avalia a relevância dos documentos recuperados e escolhe entre: usar diretamente, corrigir (extração de trechos relevantes), ou buscar na web como fallback quando a recuperação local é insuficiente (Capítulo 3 — Corrective RAG).

2. **a)** — HyDE gera um documento/resposta hipotético para a pergunta e usa seu embedding como query, aproximando o estilo da pergunta ao dos documentos indexados (Capítulo 6.3 — Query rewriting / HyDE).

3. **b)** — Adaptive RAG decide quando recuperar (ou responder direto) e quanto recuperar, roteando por complexidade/pergunta (Capítulo 2 — Adaptive RAG).

4. **b)** — Faithfulness mede se a resposta é fiel aos documentos recuperados, sem alucinação — ou seja, se toda afirmação da resposta é suportada pelo contexto recuperado (Capítulo 7 — Avaliação de RAG).

## Verdadeiro ou Falso (justificado)

1. **Falso.** Adicionar mais documentos pode diluir a relevância (mais ruído no contexto), aumentar custo de tokens e confundir o modelo. A qualidade importa mais que a quantidade; re-ranking é essencial (Capítulo 6 e Seção de exercícios do syllabus).

2. **Verdadeiro.** Self-RAG usa tokens de reflexão para decidir se a recuperação é necessária, se os docs são relevantes, e se a resposta é suportada. Em modelos não-treinados, isso é adaptado via prompting (Capítulo 4 — Self-RAG).

3. **Verdadeiro.** HyDE é útil quando a pergunta (curta, interrogativa) tem baixa similaridade semântica com os documentos (descritivos, longos). O documento hipotético aproxima os embeddings (Capítulo 6.3).

4. **Verdadeiro.** Agentic RAG multi-hop encadeia recuperações: o agente recupera, identifica informações parciais, reformula a query e recupera novamente até ter informação suficiente (Capítulo 5 — Agentic RAG).

## Código curto

1. **Corrective RAG:**
```python
def crag(query):
    docs = retrieve(query)
    relevance = assess_relevance(query, docs)
    if relevance == "high":
        return generate(query, docs)
    elif relevance == "low":
        web_docs = web_search(query)
        return generate(query, web_docs)
    else:  # medium
        extracted = extract_relevant(docs)  # corrigir
        return generate(query, extracted)
```
Referência: Capítulo 3 (Corrective RAG).

2. **Prompt de re-ranking:**
```
Você é um avaliador de relevância. Dada a pergunta e 5 documentos,
classifique os 3 mais relevantes.

Pergunta: {query}
Documentos: {docs}

Para cada documento selecionado, justifique em uma frase por que é relevante.
Retorne JSON: [{"doc_id": 1, "reason": "..."}]
```
Referência: Capítulo 6.2 (Re-ranking).

3. **Agentic RAG multi-hop:**
```python
def agentic_rag(query, max_hops=3):
    context = ""
    for hop in range(max_hops):
        docs = retrieve(query, context)
        answer = llm(query, context + docs)
        if llm_is_sufficient(answer, query):
            return answer
        query = llm_reformulate(query, docs)  # nova query
    return answer
```
Referência: Capítulo 5 (Agentic RAG multi-hop).

## Análise de trade-off

1. **Adaptive RAG vs. Self-RAG:** Adaptive RAG usa um roteador/classificador externo para decidir quando e quanto recuperar (abordagem agêntica via prompting). Self-RAG é um modelo treinado com tokens de reflexão que internaliza essa decisão. Self-RAG é mais integrado mas requer treinamento; Adaptive RAG é mais flexível e funciona com qualquer modelo (Capítulos 2 e 4).

2. **Chunking semântico vs. fixo:** Semântico preserva a coerência semântica (divide por tópicos/parágrafos), melhor para recuperação precisa. Fixo é mais simples e rápido mas pode cortar informações no meio. Semântico brilha em documentos heterogêneos; fixo basta em textos uniformes (Capítulo 6.1).

3. **Hybrid search vs. densa pura:** Hybrid (BM25 + densa) captura tanto match exato de termos (nomes, IDs, jargão) quanto similaridade semântica. Vale o custo extra quando o corpus tem vocabulário técnico, nomes próprios, ou códigos — onde busca densa pura falha (Capítulo 6.4).

## Debug / diagnóstico

1. **Diagnóstico:** O RAG recupera um único chunk por query; perguntas multi-hop precisam de informações em múltiplos chunks que não estão no mesmo resultado. **Correções:** (1) Implementar Agentic RAG multi-hop com query reformulation; (2) Aumentar o top-k com re-ranking para capturar chunks complementares (Capítulo 5).

2. **Causas de baixo faithfulness:**
   - **Chunking ruim:** chunks grandes incluem ruído. Correção: chunking semântico menor.
   - **Sem re-ranking:** docs irrelevantes no contexto. Correção: adicionar re-ranking.
   - **Prompt fraco:** não instrui o modelo a usar só o contexto. Correção: prompt com restrição "responda apenas com base no contexto".
   Referência: Capítulo 6 e 7.
