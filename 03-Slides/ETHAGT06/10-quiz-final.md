# ETHAGT06 — Quiz Final

> Quiz individual, sem consulta, 3 perguntas de múltipla escolha (slides) + 2 bônus.
> Tempo estimado: 3 min
> **Critério**: ≥2 acertos = compreensão básica atingida.

---

## Pergunta 1

Qual é a diferença fundamental entre Adaptive RAG e Self-RAG?

- A) Adaptive usa vector DB, Self-RAG usa grafo de conhecimento
- B) Adaptive decide quando recuperar, Self-RAG também avalia a própria resposta (hallucination check)
- C) Adaptive é mais caro que Self-RAG porque faz mais chamadas de LLM
- D) Não há diferença significativa — são nomes diferentes para a mesma técnica

<details>
<summary>Resposta</summary>

**B) Adaptive decide quando recuperar, Self-RAG também avalia a própria resposta**

Adaptive RAG adiciona um classificador que decide SE recuperar (e quanto). Self-RAG vai além: o modelo reflete sobre os docs recuperados E sobre a própria resposta, emitindo tokens como `[Fully supported]` para verificar se a resposta é suportada pelos docs (hallucination check). Adaptive não avalia a resposta; Self-RAG sim.
</details>

---

## Pergunta 2

Em CRAG (Corrective RAG), quando o sistema decide buscar na web como fallback?

- A) Sempre, como primeiro passo antes de consultar a base local
- B) Quando o avaliador de relevância classifica os documentos locais como irrelevantes
- C) Quando a resposta gerada é muito curta ou genérica
- D) Quando o usuário pede explicitamente uma busca na web

<details>
<summary>Resposta</summary>

**B) Quando o avaliador classifica os documentos locais como irrelevantes**

CRAG recupera da base local e um avaliador classifica cada doc em `correto` / `ambíguo` / `incorreto`. Se a maioria é `incorreto`, o sistema faz web search como fallback (caminho 3). Se `correto`, usa direto (caminho 1). Se `ambíguo`, refina via knowledge refinement (caminho 2). Web search só é acionado quando a base local não tem a resposta.
</details>

---

## Pergunta 3

Qual métrica mede se a resposta gerada é fiel aos documentos recuperados (sem alucinação)?

- A) Context precision
- B) Answer relevance
- C) Faithfulness
- D) Context recall

<details>
<summary>Resposta</summary>

**C) Faithfulness**

Faithfulness decompõe a resposta em claims e verifica cada claim contra os documentos recuperados. Score = claims suportadas / total de claims. Mede alucinação: se a resposta diz algo que não está nos docs, faithfulness cai. Context precision/recall são métricas de retrieval (qualidade dos docs). Answer relevance mede se a resposta responde à pergunta (mas não se é fiel).
</details>

---

## Pergunta Bônus 1 (não conta para nota)

Qual das 4 arquiteturas de RAG agêntico você deveria implementar PRIMEIRO?

- A) Agentic RAG — é a mais poderosa
- B) Self-RAG — garante grounding máximo
- C) Adaptive RAG — é a mais simples e resolve muitos casos
- D) CRAG — tem fallback web

<details>
<summary>Resposta</summary>

**C) Adaptive RAG**

Regra: comece simples, suba de nível com evidência de insuficiência. Adaptive RAG resolve muitos casos (perguntas triviais → direto, perguntas específicas → recuperar) com baixo custo e complexidade. Só adicione CRAG (avaliador), Self-RAG (hallucination check) ou Agentic (multi-hop) quando houver evidência de que Adaptive é insuficiente. Pular direto para Agentic sem entender as anteriores é anti-pattern.
</details>

---

## Pergunta Bônus 2 (não conta para nota)

Qual técnica reduz falhas de recuperação ao processar o documento inteiro ANTES de chunkar?

- A) Chunking fixo com overlap
- B) Hybrid search (BM25 + densa)
- C) Late chunking (Contextual Retrieval)
- D) Re-ranking com cross-encoder

<details>
<summary>Resposta</summary>

**C) Late chunking (Contextual Retrieval)**

Late chunking (Anthropic Contextual Retrieval, 2024) processa o documento completo no modelo ANTES de dividir em chunks. Cada chunk recebe o contexto do documento, então o embedding captura a semântica do todo, não só do fragmento. Reduz falhas de recuperação em 30-50% segundo a Anthropic.
</details>

---

## Resultado

| Acertos | Avaliação |
|---|---|
| 3/3 | Excelente — compreensão completa das 4 arquiteturas e avaliação |
| 2/3 | Bom — compreensão sólida, revisar 1 ponto |
| 1/3 | Suficiente — revisar diferenças entre arquiteturas |
| 0/3 | Insuficiente — reler papers Self-RAG (2310.11511) e CRAG (2401.15884) |
