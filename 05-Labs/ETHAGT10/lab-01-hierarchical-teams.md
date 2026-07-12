# ETHAGT10 — Lab 1: Hierarchical teams

> Curso: Padrões de Arquitetura Multi-Agente · Carga: 30h · Pré-req: ETHAGT09

## Objetivo
Implementar uma topologia hierarchical com um supervisor no topo, 2 workers especializados e 1 sub-worker — usando LangGraph — e demonstrar delegação, síntese e retorno de resultados.

## Preparação
- Ambiente: Python 3.11+, `pip install langgraph openai`, `.env` com API key
- Dados/recursos: tarefas de análise de código (3 snippets em [`tasks/`](https://github.com/Etho-University/especializacao-programacao-agentica/tree/main/05-Labs/ETHAGT10/tasks))
- Leitura prévia: Apostila ETHAGT10, Unidade 2 (Supervisor e Hierarchical)

## Roteiro
### Passo 1 — Modelar a hierarquia
Defina a estrutura: Supervisor → [Frontend Worker, Backend Worker] → [DB Sub-worker]

```
            Supervisor
           /          \
    Frontend         Backend
                       |
                     DB Sub
```

**Checkpoint:** diagrama da hierarquia desenhado em `hierarchy.md`.

### Passo 2 — Definir os workers
Crie os workers especializados com suas tools e system prompts:

```python
frontend_worker = create_agent(
    name="frontend",
    instructions="You are a frontend specialist. Review React/Vue/HTML code.",
    tools={"lint_js": lint_js, "check_accessibility": check_accessibility}
)
backend_worker = create_agent(
    name="backend",
    instructions="You are a backend specialist. Review API/server code.",
    tools={"lint_python": lint_python, "check_security": check_security}
)
db_subworker = create_agent(
    name="db",
    instructions="You are a database specialist. Review SQL/migrations.",
    tools={"validate_sql": validate_sql, "check_indexes": check_indexes}
)
```

**Checkpoint:** 3 agentes especializados com tools distintas.

### Passo 3 — Implementar o supervisor
O supervisor decompõe a tarefa, delega e sintetiza:

```python
def supervisor_node(state):
    task = state["task"]
    plan = call_llm(f"""Break this task into subtasks for workers:
    Available workers: frontend, backend
    Task: {task}
    Output JSON: [{{"worker": "frontend", "subtask": "..."}}, ...]""")
    subtasks = json.loads(plan)
    return {"subtasks": subtasks, "messages": state["messages"]}
```

**Checkpoint:** supervisor gera plano de delegação em JSON.

### Passo 4 — Implementar a execução de workers
Cada worker processa sua subtarefa:

```python
def worker_node(state, worker_name):
    worker_subtasks = [s for s in state["subtasks"] if s["worker"] == worker_name]
    results = []
    for st in worker_subtasks:
        # Se a subtarefa envolve DB, delegar ao sub-worker
        if "database" in st["subtask"].lower() or "sql" in st["subtask"].lower():
            sub_result = db_subworker.run(st["subtask"])
            results.append({"worker": worker_name, "subtask": st["subtask"],
                          "result": sub_result, "delegated_to": "db"})
        else:
            result = AGENTS[worker_name].run(st["subtask"])
            results.append({"worker": worker_name, "subtask": st["subtask"],
                          "result": result})
    return {"worker_results": results}
```

**Checkpoint:** backend worker delega tarefas de DB ao sub-worker quando apropriado.

### Passo 5 — Síntese do supervisor
O supervisor coleta resultados e produz resposta final:

```python
def synthesis_node(state):
    results = state["worker_results"]
    final = call_llm(f"""Synthesize the worker results into a cohesive review:
    Results: {results}
    Produce a structured report with sections per concern.""")
    return {"final_report": final}
```

**Checkpoint:** supervisor sintetiza resultados em relatório estruturado.

### Passo 6 — Montar o grafo em LangGraph
Conecte os nós em um grafo hierarchical:

```python
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
import operator

class TeamState(TypedDict):
    task: str
    subtasks: list
    worker_results: Annotated[list, operator.add]   # reducer: acumula (barreira)
    final_report: str

graph = StateGraph(TeamState)
graph.add_node("supervisor_plan", supervisor_node)
graph.add_node("frontend", lambda s: worker_node(s, "frontend"))
graph.add_node("backend", lambda s: worker_node(s, "backend"))
graph.add_node("synthesis", synthesis_node)

graph.add_edge(START, "supervisor_plan")
# Fan-out para os workers em paralelo; o reducer (operator.add) em
# worker_results funciona como barreira: synthesis só roda após ambos.
graph.add_edge("supervisor_plan", "frontend")
graph.add_edge("supervisor_plan", "backend")
graph.add_edge("frontend", "synthesis")
graph.add_edge("backend", "synthesis")
graph.add_edge("synthesis", END)

app = graph.compile()
```

**Checkpoint:** grafo compila e executa uma tarefa de teste end-to-end.

### Passo 7 — Testar com tarefa real
Execute o sistema hierarchical em uma tarefa de review de código completo (frontend + backend + DB):

```python
result = app.invoke({"task": "Revise este PR: [frontend em React + API em Flask + migration SQL]",
                     "messages": []})
print(result["final_report"])
```

**Checkpoint:** supervisor delega corretamente e o sub-worker de DB é acionado.

### Passo 8 — Análise da topologia
Documente prós e contras da topologia hierarchical:

```markdown
## Vantagens
- Especialização clara (cada worker foca no seu domínio)
- Sub-delegação resolve problemas complexos
- Supervisor mantém visão global

## Desvantagens
- Supervisor é gargalo (single point)
- Latência maior (múltiplos níveis)
- Debug mais complexo
```

**Checkpoint:** análise em `topology_analysis.md`.

## Desafios extras
- Adicione um 3º worker (DevOps) e um 2º sub-worker (Security sob Backend)
- Compare com uma topologia flat (sem sub-worker)
- Implemente re-planejamento: se um worker falha, supervisor ajusta o plano
- Meça a latência por nível da hierarquia

## Entrega
- Repositório com `hierarchical.py`, `hierarchy.md`, `topology_analysis.md`
- Commit no padrão `ETHAGT10: lab-1 implementar hierarchical teams`

## Rubrica
Avaliado pela rubrica em `08-Assignments/ETHAGT10/assignment-01.md` (Pilar Comportamental 20%: colaboração em labs).
