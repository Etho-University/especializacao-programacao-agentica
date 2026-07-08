# ETHAGT05 — Lab 2: Memória episódica

> Curso: Memória de Agentes · Carga: 25h · Pré-req: ETHAGT05 Lab 1

## Objetivo
Construir um agente com memória episódica vetorial que recorda interações anteriores relevantes via recall semântico, e comparar o desempenho do agente com e sem memória em sessões espaçadas.

## Preparação
- Ambiente: Python 3.11+, `pip install openai qdrant-client langgraph`, `.env` com API key
- Dados/recursos: Qdrant local (Docker)
- Leitura prévia: Apostila ETHAGT05, Unidade 4 (Memória vetorial para recall) e Unidade 1 (tipos)

## Roteiro
### Passo 1 — Subir o Qdrant
```bash
docker run --name qdrant -p 6333:6333 -d qdrant/qdrant
```

**Checkpoint:** Qdrant acessível em `http://localhost:6333/dashboard`.

### Passo 2 — Modelar memória episódica
Defina a estrutura de um episódio (evento memorizado):

```python
from datetime import datetime
from pydantic import BaseModel

class Episode(BaseModel):
    id: str
    user_id: str
    timestamp: datetime
    event_type: str  # question, answer, feedback, action
    content: str
    metadata: dict = {}
```

**Checkpoint:** `Episode` cobre os campos essenciais de um evento memorável.

### Passo 3 — Implementar o EpisodicMemoryStore
Crie a camada de memória que armazena e recupera episódios:

```python
from qdrant_client import QdrantClient
from openai import OpenAI

class EpisodicMemoryStore:
    def __init__(self):
        self.qdrant = QdrantClient("localhost", port=6333)
        self.llm_client = OpenAI()
        self.qdrant.create_collection("episodes", vectors_config={"size": 1536, "distance": "Cosine"})

    def store(self, episode: Episode):
        embedding = self._embed(episode.content)
        self.qdrant.upsert("episodes", points=[{
            "id": episode.id,
            "vector": embedding,
            "payload": episode.model_dump()
        }])

    def recall(self, query: str, user_id: str, limit: int = 5) -> list[Episode]:
        query_vec = self._embed(query)
        results = self.qdrant.search("episodes", query_vec=query_vec,
            query_filter={"must": [{"key": "user_id", "match": {"value": user_id}}]},
            limit=limit)
        return [Episode(**r.payload) for r in results]

    def _embed(self, text: str) -> list[float]:
        return self.llm_client.embeddings.create(
            input=text, model="text-embedding-3-small").data[0].embedding
```

**Checkpoint:** `store()` e `recall()` funcionam; episódio é armazenado e recuperado.

### Passo 4 — Integrar memória ao agente
O agente consulta a memória antes de responder:

```python
def agent_with_memory(question, user_id, memory: EpisodicMemoryStore):
    relevant = memory.recall(question, user_id, limit=3)
    context = "\n".join(f"[{e.timestamp}] {e.content}" for e in relevant)
    prompt = f"""Previous relevant interactions:
    {context or 'No prior memory.'}
    User question: {question}"""
    response = call_llm(prompt)
    # Armazenar esta interação como novo episódio
    memory.store(Episode(id=uuid4(), user_id=user_id,
        timestamp=datetime.now(), event_type="qa",
        content=f"Q: {question}\nA: {response}"))
    return response
```

**Checkpoint:** agente recupera memórias, usa no contexto e armazena nova interação.

### Passo 5 — Cenário de teste: 3 sessões espaçadas
Simule 3 sessões para o mesmo usuário, com perguntas que se referenciam:

```python
# Sessão 1
agent_with_memory("Meu projeto usa Python 3.12 e FastAPI", "user-1", memory)
# Sessão 2 (simular depois)
agent_with_memory("Qual versão do Python eu uso?", "user-1", memory)
# Sessão 3
agent_with_memory("Adicionei pytest ao projeto. O que mais uso?", "user-1", memory)
```

**Checkpoint:** Sessão 2 recupera a memória da Sessão 1 e responde "Python 3.12".

### Passo 6 — Metadata filtering
Adicione filtro por período temporal: só recupera episódios dos últimos 7 dias:

```python
def recall_recent(self, query, user_id, days=7, limit=5):
    cutoff = datetime.now() - timedelta(days=days)
    # Adicionar filtro de timestamp no Qdrant
    ...
```

**Checkpoint:** episódios antigos (>7 dias) não são recuperados com `recall_recent`.

### Passo 7 — Experimento comparativo
Conduza o experimento: 10 perguntas, executadas com e sem memória, medindo accuracy:

```python
for q in test_questions:
    # Sem memória
    answer_no_mem = agent_without_memory(q)
    # Com memória (após "treinar" com contexto prévio)
    answer_with_mem = agent_with_memory(q, "user-1", memory)
```

| Configuração | Accuracy (10) | Tokens médios | Referencia contexto anterior? |
|---|---|---|---|
| Sem memória | /10 | | Não |
| Com memória | /10 | | Sim |

**Checkpoint:** tabela preenchida mostrando diferença de qualidade.

### Passo 8 — Análise de trade-offs
Discuta em `analysis.md`:
1. Quando a memória episódica **ajuda** vs quando é **ruído**?
2. Qual o custo de embedding + storage vs benefício?
3. Quais tipos de pergunta se beneficiam mais?

**Checkpoint:** análise documenta pelo menos 2 cenários onde memória ajudou e 1 onde atrapalhou.

## Desafios extras
- Implemente re-ranking dos episódios recuperados (ex.: por relevância temporal + semântica)
- Adicione consolidação: episódios muito similares são fundidos (episódica → semântica)
- Implemente redação de PII antes de armazenar episódios (LGPD/GDPR)
- Compare recall por similaridade semântica vs recall por keyword (BM25)

## Entrega
- Repositório com `memory_store.py`, `agent.py`, `comparison.md`, `analysis.md`
- Traces mostrando recall funcionando em sessões espaçadas
- Commit no padrão `ETHAGT05: lab-2 implementar memória episódica`

## Rubrica
Avaliado pela rubrica em `08-Assignments/ETHAGT05/assignment-01.md` (Pilar Comportamental 20%: colaboração em labs).
