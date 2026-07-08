# ETHAGT01 — Lab 2: Augmented LLM

> Curso: Arquitetura Cognitiva de Agentes LLM · Carga: 25h · Pré-req: ETHAGT01 Lab 1

## Objetivo
Transformar o agente ReAct do Lab 1 em um *Augmented LLM* completo, adicionando retrieval (vector store simples), duas tools adicionais e um mecanismo de decisão entre responder direto, recuperar conhecimento ou usar uma tool.

## Preparação
- Ambiente: Python 3.11+, `pip install openai chromadb numpy`, `.env` com API key
- Dados/recursos: corpus de 10-20 documentos curtos (ex.: trechos de Wikipedia sobre ciência)
- Leitura prévia: Apostila ETHAGT01, Unidade 2 (Augmented LLM)

## Roteiro
### Passo 1 — Construir o vector store
Crie uma base de conhecimento com `chromadb` contendo 10-20 documentos curtos:

```python
import chromadb
client = chromadb.Client()
collection = client.create_collection("knowledge")

docs = [
    {"id": "d1", "text": "A fotossíntese converte CO2 e água em glicose e oxigênio."},
    {"id": "d2", "text": "Python foi criado por Guido van Rossum em 1991."},
    # ... 18 documentos a mais
]
for d in docs:
    collection.add(ids=[d["id"]], documents=[d["text"]])
```

**Checkpoint:** `collection.count()` retorna 20 (ou o número de docs inseridos).

### Passo 2 — Tool de retrieval
Implemente a tool `retrieve` que busca documentos relevantes:

```python
def retrieve(query: str) -> str:
    results = collection.query(query_texts=[query], n_results=3)
    docs = results["documents"][0]
    return "\n".join(docs) if docs else "No relevant documents found."

TOOLS["retrieve"] = retrieve
```

**Checkpoint:** `retrieve("fotossíntese")` retorna o documento `d1`.

### Passo 3 — Segunda tool útil
Adicione uma tool `get_current_date()` que retorna a data/hora atual — útil para perguntas temporais:

```python
from datetime import datetime
def get_current_date(dummy="") -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M")
TOOLS["get_current_date"] = get_current_date
```

**Checkpoint:** agente consegue responder "Que dia é hoje?" usando a tool.

### Passo 4 — Atualizar o prompt do sistema
Modifique o `SYSTEM` prompt para instruir o agente sobre **quando** usar cada recurso:

```
You have access to:
- calculate[expression]: for math
- retrieve[query]: to search your knowledge base for facts
- get_current_date[]: to get today's date
Use retrieve ONLY when the question requires factual knowledge you're unsure about.
For simple questions you know, answer directly.
```

**Checkpoint:** prompt descreve claramente os 3 recursos e quando usar cada um.

### Passo 5 — Atualizar o parser e o loop
O parser de `parse_action` já funciona para múltiplas tools. Garanta que o loop lida com tools sem argumentos (como `get_current_date`):

```python
if tool_name in TOOLS:
    obs = TOOLS[tool_name](args) if args else TOOLS[tool_name]()
```

**Checkpoint:** todas as 3 tools funcionam sem erro de aridade.

### Passo 6 — Bateria de testes de decisão
Execute 6 perguntas e documente o comportamento do agente:

| # | Pergunta | Comportamento esperado |
|---|---|---|
| 1 | "Quanto é 50 * 12?" | `calculate` |
| 2 | "O que é fotossíntese?" | `retrieve` |
| 3 | "Que dia é hoje?" | `get_current_date` |
| 4 | "Qual a capital da França?" | `Answer:` direto |
| 5 | "Quantos dias desde 2025-01-01 até hoje?" | `get_current_date` + `calculate` |
| 6 | "Quem criou Python e em que ano?" | `retrieve` |

**Checkpoint:** o agente acerta a estratégia em pelo menos 5 das 6 perguntas.

### Passo 7 — Análise do trace
Analise os traces e responda: em quantas iterações o agente usou retrieval desnecessariamente? Em quantas deixou de usar quando deveria?

**Checkpoint:** análise documentada em `analysis.md` com contagem e observações.

### Passo 8 — Documentação ACI das tools
Escreva descrições ricas (estilo docstring) para cada tool, como se fossem para um desenvolvedor júnior — incluindo exemplos de uso e edge cases.

**Checkpoint:** cada tool tem descrição de 3+ linhas com exemplo.

## Desafios extras
- Adicione uma quarta tool `web_search` (mock ou real com `duckduckgo-search`)
- Implemente um mecanismo que conta tokens de cada retrieval e poda se exceder um budget
- Compare o agente com retrieval vs sem retrieval em 10 perguntas factuais

## Entrega
- Repositório com `agent.py`, `knowledge_base.py`, `trace.jsonl`, `analysis.md`
- Trace demonstrando decisão correta entre retrieve / calculate / answer
- Commit no padrão `ETHAGT01: lab-2 adicionar augmented-llm`

## Rubrica
Avaliado pela rubrica em `08-Assignments/ETHAGT01/assignment-01.md` (Pilar Comportamental 20%: colaboração em labs).
