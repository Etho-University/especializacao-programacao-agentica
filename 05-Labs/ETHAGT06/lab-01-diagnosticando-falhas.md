# ETHAGT06 — Lab 1: Diagnosticando falhas de RAG

> Curso: RAG Agêntico · Carga: 30h · Pré-req: ETHAGT04

## Objetivo
Rodar um pipeline de RAG "ingênuo" (naive RAG) sobre um corpus intencionalmente problemático, identificar e categorizar pelo menos 3 classes de falha, e documentar as causas raiz.

## Preparação
- Ambiente: Python 3.11+, `pip install openai chromadb ragas`, `.env` com API key
- Dados/recursos: corpus problemático (fornecido em `corpus/`): documentos com chunks mal-delimitados, tabelas em texto, conteúdo multilingual, PDFs mal-parsed
- Leitura prévia: Apostila ETHAGT06, Unidade 1 (Por que o RAG ingênuo falha)

## Roteiro
### Passo 1 — Inspecionar o corpus problemático
Examine os documentos em `corpus/` e identifique problemas potenciais:

```
corpus/
  doc1.md    → texto com tabelas mal-formatadas
  doc2.pdf   → PDF com múltiplas colunas (parse quebrado)
  doc3.txt   → mixing PT/EN sem separação
  doc4.md    → uma única linha de 5000 tokens (sem chunking natural)
  doc5.json  → dados estruturados achatados em texto
```

**Checkpoint:** lista de problemas potenciais documentada em `corpus_audit.md`.

### Passo 2 — Implementar o naive RAG
Construa o pipeline mais simples possível (sem otimizações):

```python
def naive_rag(question):
    # 1. Embed a pergunta
    q_vec = embed(question)
    # 2. Buscar top-5 chunks (sem re-rank, sem query rewriting)
    chunks = vector_db.search(q_vec, limit=5)
    # 3. Stuffing: juntar tudo no prompt
    context = "\n".join(c.text for c in chunks)
    # 4. LLM gera resposta
    return call_llm(f"Context: {context}\nQuestion: {question}\nAnswer:")
```

**Checkpoint:** pipeline ingênuo roda e produz respostas (boas ou ruins).

### Passo 3 — Chunking intencionalmente ruim
Use chunking fixo de 1000 caracteres sem sobreposição para maximizar falhas:

```python
def naive_chunk(text, size=1000, overlap=0):
    return [text[i:i+size] for i in range(0, len(text), size - overlap)]
```

**Checkpoint:** um parágrafo cortado no meio aparece em 2 chunks diferentes.

### Passo 4 — Conjunto de perguntas de teste
Crie 15 perguntas cujas respostas estão no corpus, cobrindo diferentes tipos de dificuldade:

```json
[
  {"id": "Q1", "question": "Qual o valor na célula B3 da tabela?", "type": "tabular", "expected": "..."},
  {"id": "Q2", "question": "What is the main conclusion?", "type": "multilingual", "expected": "..."},
  {"id": "Q3", "question": "Resuma os 3 pontos principais", "type": "multi_chunk", "expected": "..."}
]
```

**Checkpoint:** 15 perguntas rotuladas por tipo de dificuldade.

### Passo 5 — Executar e coletar falhas
Rode o naive RAG nas 15 perguntas e classifique cada resposta como correta/incorreta/parcial:

```python
results = []
for q in questions:
    answer = naive_rag(q["question"])
    verdict = judge_answer(answer, q["expected"])
    results.append({**q, "answer": answer, "verdict": verdict})
```

**Checkpoint:** 15 resultados coletados com veredito em `raw_results.json`.

### Passo 6 — Categorizar classes de falha
Analise os resultados e identifique pelo menos 3 classes de falha:

| Classe de falha | Descrição | Perguntas afetadas |
|---|---|---|
| **F1: Chunk boundary** | Resposta cortada entre 2 chunks | Q5, Q8 |
| **F2: Tabela perdida** | Dado tabular não recuperado | Q1, Q11 |
| **F3: Multilingual mismatch** | Embedding PT não recuperou EN | Q2, Q14 |
| **F4: Over-retrieval** | Contexto irrelevante ofuscou resposta | Q3, Q7 |

**Checkpoint:** ≥3 classes de falha identificadas com perguntas afetadas.

### Passo 7 — Diagnóstico de causa raiz
Para cada classe de falha, identifique a causa raiz e proponha correção:

```markdown
## F1: Chunk boundary
- **Causa raiz**: chunking fixo corta sentenças no meio
- **Correção proposta**: chunking semântico por parágrafo + overlap de 200 tokens
```

**Checkpoint:** cada classe tem causa raiz e correção proposta.

### Passo 8 — Métricas com Ragas
Use Ragas para quantificar as falhas automaticamente:

```python
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy, context_precision, context_recall

scores = evaluate(dataset, metrics=[faithfulness, answer_relevancy,
                                     context_precision, context_recall])
```

| Métrica | Score |
|---|---|
| Faithfulness | ? |
| Answer Relevancy | ? |
| Context Precision | ? |
| Context Recall | ? |

**Checkpoint:** scores do Ragas calculados e baixos (esperado, dado o corpus problemático).

## Desafios extras
- Aplique UMA correção simples (ex.: re-ranking) e meça melhoria em uma classe de falha
- Tente hybrid search (BM25 + densa) e veja se resolve F2 (tabelas)
- Adicione query rewriting e meça se resolve F3 (multilingual)

## Entrega
- Repositório com `naive_rag.py`, `raw_results.json`, `failure_analysis.md`, `ragas_scores.json`
- Commit no padrão `ETHAGT06: lab-1 diagnosticar falhas de rag`

## Rubrica
Avaliado pela rubrica em `08-Assignments/ETHAGT06/assignment-01.md` (Pilar Comportamental 20%: colaboração em labs).
