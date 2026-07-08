# ETHAGT06 — Lab 2: Agentic RAG multi-hop

> Curso: RAG Agêntico · Carga: 30h · Pré-req: ETHAGT06 Lab 1

## Objetivo
Implementar um agente que dirige o processo de retrieval: planeja buscas, refina queries iterativamente, combina múltiplas fontes e decide quando parar — resolvendo perguntas multi-hop que o RAG ingênuo não consegue.

## Preparação
- Ambiente: Python 3.11+, `pip install openai qdrant-client langgraph`, `.env` com API key
- Dados/recursos: corpus com informações relacionadas em múltiplos documentos (ex.: biografias + cronologias + eventos)
- Leitura prévia: Apostila ETHAGT06, Unidade 5 (Agentic RAG) e Unidade 3 (CRAG)

## Roteiro
### Passo 1 — Definir perguntas multi-hop
Crie 5 perguntas que exigem encadear 2-3 recuperações:

```json
[
  {"id": "MH1", "question": "Quem dirigiu o filme que ganhou o Oscar de melhor filme em 2020, e qual outra filme desse diretor ganhou um prêmio importante?",
   "hops": ["search Oscar 2020 winner", "search director", "search other films"]}
]
```

**Checkpoint:** 5 perguntas com hops documentados.

### Passo 2 — Indexar o corpus
Prepare o vector store com chunking semântico:

```python
from qdrant_client import QdrantClient
client = QdrantClient("localhost", port=6333)
client.create_collection("docs", vectors_config={"size": 1536, "distance": "Cosine"})
for doc in semantic_chunks(corpus):
    client.upsert("docs", points=[{"id": doc.id, "vector": embed(doc.text), "payload": {"text": doc.text}}])
```

**Checkpoint:** corpus indexado com chunks semânticos.

### Passo 3 — Implementar o retrieval tool
A tool que o agente usa para buscar:

```python
def retrieve(query: str, limit: int = 5) -> list[str]:
    results = client.search("docs", query_vec=embed(query), limit=limit)
    return [r.payload["text"] for r in results[0].points]
```

**Checkpoint:** tool retorna documentos relevantes para uma query de teste.

### Passo 4 — Implementar CRAG (Corrective RAG)
Adicione avaliação de relevância dos docs recuperados:

```python
def assess_relevance(question, docs):
    prompt = f"""Rate relevance of these docs to the question (relevant/irrelevant/ambiguous).
    Question: {question}
    Docs: {docs}
    Reply: relevant | irrelevant | ambiguous"""
    return call_llm(prompt).strip().lower()

def crag_retrieve(question):
    docs = retrieve(question)
    relevance = assess_relevance(question, docs)
    if relevance == "relevant":
        return docs, "use"
    elif relevance == "irrelevant":
        return web_search(question), "web_fallback"
    else:
        return refine_and_re_search(question, docs), "corrected"
```

**Checkpoint:** CRAG roteia para 3 caminhos: usar, web, ou corrigir.

### Passo 5 — Query rewriting
Implemente reescrita de query quando a primeira busca não retorna resultados úteis:

```python
def rewrite_query(original, docs):
    prompt = f"""The query '{original}' returned these docs: {docs[:200]}
    Rewrite the query to find better results. Output only the new query."""
    return call_llm(prompt).strip()
```

**Checkpoint:** query reescrita é diferente da original e mais específica.

### Passo 6 — O agent loop multi-hop
Implemente o agente que itera — recuperando, avaliando, refinando até ter informação suficiente:

```python
def agentic_rag(question, max_hops=4):
    gathered = []
    queries_tried = []
    for hop in range(max_hops):
        # Agente decide próxima query
        plan = call_llm(f"""Given question: {question}
        Info gathered so far: {gathered}
        Queries tried: {queries_tried}
        What should I search next? Or do I have enough to answer?
        Reply: SEARCH[query] or ANSWER[result]""")
        if plan.startswith("ANSWER"):
            return plan[len("ANSWER"):]
        query = extract_query(plan)
        queries_tried.append(query)
        docs, action = crag_retrieve(query)
        gathered.append({"query": query, "docs": docs, "action": action})
    return "Max hops reached"
```

**Checkpoint:** agente faz múltiplos hops e para quando tem informação suficiente.

### Passo 7 — Executar e comparar
Rode o agentic RAG nas 5 perguntas multi-hop e compare com naive RAG (Lab 1):

| Pergunta | Naive RAG | Agentic RAG | Hops usados |
|---|---|---|---|
| MH1 | Incorreto | Correto | 3 |
| MH2 | Parcial | Correto | 2 |

**Checkpoint:** agentic RAG resolve pelo menos 4 das 5 perguntas multi-hop.

### Passo 8 — Avaliação de qualidade
Use LLM-as-judge para avaliar faithfulness e answer relevancy:

```python
def evaluate_agentic(questions, results):
    for q, r in zip(questions, results):
        faithfulness = llm_judge(f"Is this answer faithful to the sources?\n{r}")
        completeness = llm_judge(f"Does it answer all parts of: {q}?\n{r}")
```

**Checkpoint:** scores de qualidade calculados e documentados.

## Desafios extras
- Adicione uma fonte de knowledge graph como tool alternativa ao vector search
- Implemente self-RAG: agente decide se precisa recuperar ou pode responder direto
- Meça custo por hop e encontre o sweet spot (quantos hops valem o custo?)

## Entrega
- Repositório com `agentic_rag.py`, `crag.py`, `comparison.md`, traces
- Commit no padrão `ETHAGT06: lab-2 implementar agentic rag multihop`

## Rubrica
Avaliado pela rubrica em `08-Assignments/ETHAGT06/assignment-01.md` (Pilar Comportamental 20%: colaboração em labs).
