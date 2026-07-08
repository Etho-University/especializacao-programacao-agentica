# ETHAGT12 — Lab 1: Traces everywhere

> Curso: AgentOps, Observabilidade & Avaliação · Carga: 30h · Pré-req: ETHAGT11

## Objetivo
Adicionar observabilidade end-to-end a um agente existente usando LangSmith ou Arize Phoenix, criar traces estruturados de todas as chamadas (LLM, tools, retrieval) e construir um dashboard de monitoramento.

## Preparação
- Ambiente: Python 3.11+, `pip install langsmith openai` ou `pip install arize-phoenix openinference-instrumentation-openai`, `.env` com `LANGSMITH_API_KEY`
- Dados/recursos: agente ReAct do ETHAGT01 Lab 1 (ou qualquer agente existente)
- Leitura prévia: Apostila ETHAGT12, Unidade 2 (Observabilidade)

## Roteiro
### Passo 1 — Escolher a ferramenta de tracing
Escolha LangSmith (cloud) ou Phoenix (self-hosted). Para Phoenix local:

```python
import phoenix as px
px.launch_app()  # abre UI em localhost:6006
```

Para LangSmith:

```python
import os
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_PROJECT"] = "ethagt12-lab"
```

**Checkpoint:** tooling configurado e UI acessível.

### Passo 2 — Instrumentar o agente
Adicione tracing automático via OpenTelemetry (Phoenix) ou LangSmith decorator:

```python
# Phoenix: auto-instrumentação
from openinference.instrumentation.openai import OpenAIInstrumentor
OpenAIInstrumentor().instrument()

# LangSmith: wrap com @traceable
from langsmith import traceable

@traceable(name="agent_step")
def agent_step(messages):
    response = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
    return response
```

**Checkpoint:** chamadas ao LLM aparecem automaticamente nos traces.

### Passo 3 — Adicionar spans customizados
Crie spans para tool calls e retrieval com metadados:

```python
from langsmith import traceable

@traceable(name="tool_call", metadata={"type": "tool"})
def execute_tool(tool_name, args):
    result = TOOLS[tool_name](args)
    return result

@traceable(name="retrieval", metadata={"type": "retrieval"})
def retrieve(query):
    docs = vector_db.search(query, limit=5)
    return docs
```

**Checkpoint:** cada tool e retrieval aparece como span filho no trace.

### Passo 4 — Adicionar métricas customizadas
Capture métricas de negócio em cada step:

```python
@traceable(name="agent_run")
def run_agent(question):
    start = time.time()
    # ... execução do agente ...
    latency = time.time() - start
    # Adicionar métricas ao trace
    return {
        "answer": answer,
        "metrics": {
            "latency_s": latency,
            "tokens_used": token_count,
            "tools_called": tools_count,
            "steps": step_count,
            "cost_usd": calculate_cost(tokens)
        }
    }
```

**Checkpoint:** métricas aparecem nos metadados de cada trace.

### Passo 5 — Executar bateria de testes
Rode 10 perguntas e observe os traces:

```python
questions = load_questions("test_questions.json")
for q in questions:
    result = run_agent(q)
    print(f"Q: {q} → A: {result['answer'][:80]}...")
```

**Checkpoint:** 10 traces visíveis na UI com spans hierárquicos.

### Passo 6 — Analisar traces
Use a UI para analisar:
1. Qual step é mais lento? (LLM call vs tool vs retrieval)
2. Quantos tokens cada step consome?
3. Onde ocorrem falhas?
4. Qual o custo total por execução?

**Checkpoint:** análise documentada em `trace_analysis.md`.

### Passo 7 — Criar um dashboard
Crie um dashboard customizado (ou use o LangSmith Dashboard) com:
- Latência média por step
- Distribuição de tokens
- Taxa de sucesso vs falha
- Custo acumulado por dia

```python
# LangSmith: criar dataset de avaliação
from langsmith import Client
client = Client()
dataset = client.create_dataset("ethagt12-eval")
for q in questions:
    client.create_example(inputs={"question": q}, dataset_id=dataset.id)
```

**Checkpoint:** dashboard mostra 4+ métricas em tempo real.

### Passo 8 — Detectar anomalias
Configure alertas ou detecção manual de execuções anômalas:
- Execução com latência > p95
- Execução com custo > média + 2σ
- Execução com loop de tools (mesma tool chamada 3+x)

```python
def detect_anomalies(traces):
    anomalies = []
    for trace in traces:
        if trace.latency > p95_threshold:
            anomalies.append({"trace": trace.id, "type": "high_latency"})
        if trace.cost > avg_cost * 2:
            anomalies.append({"trace": trace.id, "type": "high_cost"})
    return anomalies
```

**Checkpoint:** pelo menos 1 anomalia detectada e documentada.

## Desafios extras
- Adicione distributed tracing se o agente chamar serviços externos (MCP servers)
- Implemente sampling: trace 100% em dev, 10% em produção
- Compare LangSmith vs Phoenix vs Langfuse (mesmo agente, 3 ferramentas)
- Adicione OpenTelemetry GenAI semantic conventions padronizadas

## Entrega
- Repositório com agente instrumentado, `trace_analysis.md`, screenshots do dashboard
- Commit no padrão `ETHAGT12: lab-1 adicionar observabilidade traces`

## Rubrica
Avaliado pela rubrica em `08-Assignments/ETHAGT12/assignment-01.md` (Pilar Comportamental 20%: colaboração em labs).
