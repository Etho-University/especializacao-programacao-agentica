# ETHAGT05 — Lab 1: Checkpointer em Postgres

> Curso: Memória de Agentes · Carga: 25h · Pré-req: ETHAGT04

## Objetivo
Implementar um agente com checkpointing em Postgres que pode ser interrompido a qualquer momento e retomado dias depois, preservando todo o estado da conversa e do raciocínio.

## Preparação
- Ambiente: Python 3.11+, `pip install langgraph langgraph-checkpoint-postgres psycopg psycopg-pool`, Docker (para Postgres)
- Dados/recursos: container Postgres local
- Leitura prévia: Apostila ETHAGT05, Unidade 2 (Checkpointer e estado persistente)

## Roteiro
### Passo 1 — Subir o Postgres
Inicie um container Postgres local:

```bash
docker run --name agent-pg -e POSTGRES_PASSWORD=agent123 -e POSTGRES_DB=agents -p 5432:5432 -d postgres:16
```

**Checkpoint:** `docker ps` mostra o container rodando; `psql` conecta com sucesso.

### Passo 2 — Configurar o checkpointer
Crie a conexão e o `PostgresSaver`:

```python
from langgraph.checkpoint.postgres import PostgresSaver
from psycopg import Connection

DB_URI = "postgresql://postgres:agent123@localhost:5432/agents"
conn = Connection.connect(DB_URI)
checkpointer = PostgresSaver(conn)
checkpointer.setup()  # cria tabelas
```

**Checkpoint:** tabelas de checkpoint criadas no Postgres (`\dt` mostra `checkpoints`).

### Passo 3 — Definir o estado do agente
Modele o estado serializável do agente:

```python
from typing import TypedDict, Annotated
from langgraph.graph import MessagesState

class AgentState(TypedDict):
    messages: list
    user_id: str
    session_id: str
    step_count: int
```

**Checkpoint:** `AgentState` é um TypedDict com campos serializáveis.

### Passo 4 — Construir o grafo do agente
Crie um agente simples (com tools) usando LangGraph:

```python
from langgraph.graph import StateGraph, START, END

def agent_node(state: AgentState):
    response = call_llm(state["messages"])
    return {"messages": state["messages"] + [response],
            "step_count": state["step_count"] + 1}

graph = StateGraph(AgentState)
graph.add_node("agent", agent_node)
graph.add_edge(START, "agent")
graph.add_edge("agent", END)
app = graph.compile(checkpointer=checkpointer)
```

**Checkpoint:** grafo compila sem erro com checkpointer conectado.

### Passo 5 — Configurar thread_id
Cada sessão usa um `thread_id` único que permite resumir:

```python
config = {"configurable": {"thread_id": "session-001"}}
result = app.invoke(
    {"messages": [{"role": "user", "content": "Oi, meu nome é João"}],
     "user_id": "user-1", "session_id": "session-001", "step_count": 0},
    config=config
)
```

**Checkpoint:** primeira mensagem processada e salva no Postgres.

### Passo 6 — Simular interrupção
Pare o processo Python. Inspecione o estado salvo no Postgres:

```sql
SELECT thread_id, checkpoint_id, created_at
FROM checkpoints WHERE thread_id = 'session-001';
```

**Checkpoint:** estado da sessão está persistido no banco após o kill do processo.

### Passo 7 — Retomar a sessão
Crie um novo processo Python, reconecte ao mesmo `thread_id` e continue a conversa:

```python
# NOVO PROCESSO — horas ou dias depois
config = {"configurable": {"thread_id": "session-001"}}
result = app.invoke(
    {"messages": [{"role": "user", "content": "Qual o meu nome?"}]},
    config=config
)
# O agente deve lembrar: "João"
```

**Checkpoint:** agente responde "João" corretamente, provando que o estado foi recuperado.

### Passo 8 — Time travel (branching)
Use o checkpointing para voltar a um estado anterior e bifurcar:

```python
# Listar todos os checkpoints da thread
states = list(app.get_state_history(config))
# Voltar ao segundo checkpoint
old_config = states[2].config
# Continuar a partir dali (nova branch)
result = app.invoke(
    {"messages": [{"role": "user", "content": "E se eu fosse Maria?"}]},
    config=old_config
)
```

**Checkpoint:** nova branch criada a partir de um estado anterior; ambas as versões coexistem.

## Desafios extras
- Implemente expiry automático: sessões não acessadas há 30 dias são removidas
- Use SQLite em vez de Postgres e compare a experiência
- Adicione encriptação de PII no estado antes de salvar no checkpointer
- Implemente versionamento de schema: o que acontece se o `AgentState` mudar entre versões?

## Entrega
- Repositório com `agent.py`, `docker-compose.yml`, `demo.md` (passo a passo da demo)
- Evidência de interrupção + retomada (screenshot ou log)
- Commit no padrão `ETHAGT05: lab-1 implementar checkpointer postgres`

## Rubrica
Avaliado pela rubrica em `08-Assignments/ETHAGT05/assignment-01.md` (Pilar Comportamental 20%: colaboração em labs).
