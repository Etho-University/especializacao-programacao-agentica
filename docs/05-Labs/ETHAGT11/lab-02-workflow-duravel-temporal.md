# ETHAGT11 — Lab 2: Workflow durável em Temporal

> Curso: Event-Driven Agents & Workflow Orchestration · Carga: 25h · Pré-req: ETHAGT11 Lab 1

## Objetivo
Implementar um workflow de longa duração (agente de processamento de documentos) usando Temporal para durable execution, e demonstrar que o workflow sobrevive a crashes do processo sem perder estado.

## Preparação
- Ambiente: Python 3.11+, `pip install temporalio`, Docker
- Dados/recursos: Temporal server local via Docker
- Leitura prévia: Apostila ETHAGT11, Unidade 3 (Orquestração de workflows) e Unidade 4 (Durable execution)

## Roteiro
### Passo 1 — Subir o Temporal server
```bash
curl -sSf https://raw.githubusercontent.com/temporalio/cli/main/install.sh | sh
temporal server start-dev --log-level error
```

**Checkpoint:** Temporal UI acessível em `http://localhost:8233`.

### Passo 2 — Definir as activities
Activities são unidades de trabalho executáveis e re-executáveis (com retry):

```python
from temporalio import activity

@activity.defn
async def extract_text(document_path: str) -> str:
    """Extract text from a document."""
    # Simular trabalho demorado
    await asyncio.sleep(5)
    return f"Extracted text from {document_path}"

@activity.defn
async def analyze_with_llm(text: str) -> dict:
    """Analyze extracted text with an LLM agent."""
    await asyncio.sleep(10)  # simular chamada LLM lenta
    return {"summary": f"Analysis of: {text[:50]}...", "sentiment": "positive"}

@activity.defn
async def generate_report(analysis: dict) -> str:
    """Generate final report from analysis."""
    await asyncio.sleep(3)
    return f"REPORT\n======\n{analysis['summary']}\nSentiment: {analysis['sentiment']}"
```

**Checkpoint:** 3 activities definidas com tipos de retorno claros.

### Passo 3 — Definir o workflow
O workflow orquestra as activities com durable execution:

```python
from temporalio import workflow
from datetime import timedelta

@workflow.defn
class DocumentProcessingWorkflow:
    @workflow.run
    async def run(self, document_path: str) -> str:
        # Cada activity é automaticamente persistida
        text = await workflow.execute_activity(
            extract_text, document_path,
            start_to_close_timeout=timedelta(seconds=30))

        analysis = await workflow.execute_activity(
            analyze_with_llm, text,
            start_to_close_timeout=timedelta(seconds=60))

        report = await workflow.execute_activity(
            generate_report, analysis,
            start_to_close_timeout=timedelta(seconds=30))

        return report
```

**Checkpoint:** workflow define a sequência de activities com timeouts.

### Passo 4 — Implementar o worker
O worker executa workflows e activities:

```python
from temporalio.worker import Worker

async def run_worker():
    client = await Client.connect("localhost:7233")
    worker = Worker(
        client,
        task_queue="document-processing",
        workflows=[DocumentProcessingWorkflow],
        activities=[extract_text, analyze_with_llm, generate_report]
    )
    await worker.run()
```

**Checkpoint:** worker conecta ao Temporal e fica pronto para processar.

### Passo 5 — Iniciar o workflow
Inicie o workflow a partir de um cliente:

```python
from temporalio.client import Client

async def start_workflow():
    client = await Client.connect("localhost:7233")
    result = await client.start_workflow(
        DocumentProcessingWorkflow.run,
        "/data/document.pdf",
        id="doc-processing-001",
        task_queue="document-processing"
    )
    return result
```

**Checkpoint:** workflow iniciado e visível no Temporal UI.

### Passo 6 — Teste de crash recovery
O teste crítico: **mate o worker no meio da execução e veja o workflow retomar**:

1. Inicie o workflow
2. Aguarde a primeira activity completar (visível no UI)
3. `Ctrl+C` no worker (matar o processo)
4. Reinicie o worker
5. O workflow **continua de onde parou** — não recomeça do zero

```python
# O workflow retoma da SEGUNDA activity, pois a primeira já completou
# Temporal sabe exatamente qual activity já executou
```

**Checkpoint:** após reiniciar o worker, o workflow completa sem recomeçar do zero.

### Passo 7 — Adicionar retries e compensação
Adicione retry policy nas activities:

```python
from temporalio.common import RetryPolicy

analysis = await workflow.execute_activity(
    analyze_with_llm, text,
    start_to_close_timeout=timedelta(seconds=60),
    retry_policy=RetryPolicy(
        initial_interval=timedelta(seconds=1),
        maximum_interval=timedelta(seconds=10),
        maximum_attempts=3
    ))
```

E compensação em caso de falha:

```python
@activity.defn
async def cleanup_partial_results(workflow_id: str) -> str:
    """Compensating activity: clean up if workflow fails."""
    ...
```

**Checkpoint:** activity com retry policy falha 3x e então dispara compensação.

### Passo 8 — HITL via signal
Adicione um signal para HITL — pausar o workflow e esperar aprovação humana:

```python
@workflow.defn
class DocumentProcessingWorkflow:
    def __init__(self):
        self.approved = False

    @workflow.signal
    def approve(self):
        self.approved = True

    @workflow.run
    async def run(self, document_path: str) -> str:
        text = await workflow.execute_activity(
            extract_text, document_path, start_to_close_timeout=timedelta(seconds=30))
        analysis = await workflow.execute_activity(
            analyze_with_llm, text, start_to_close_timeout=timedelta(seconds=60))

        # Esperar aprovação humana
        await workflow.wait_condition(lambda: self.approved)

        report = await workflow.execute_activity(
            generate_report, analysis, start_to_close_timeout=timedelta(seconds=30))
        return report
```

**Checkpoint:** workflow pausa em `wait_condition` até receber signal `approve`.

## Desafios extras
- Adicione um timer: se a aprovação não vier em 1 hora, auto-rejeitar
- Implemente child workflows para processar múltiplos documentos em paralelo
- Adicione query: permitir consultar o estado do workflow sem afetá-lo
- Use Temporal para orquestrar 3 agentes (do Lab 1 de Kafka) em vez de Kafka

## Entrega
- Repositório com `workflow.py`, `worker.py`, `client.py`, `crash_demo.md` (passo a passo)
- Evidência do crash recovery (screenshot do Temporal UI mostrando retomada)
- Commit no padrão `ETHAGT11: lab-2 implementar workflow durável temporal`

## Rubrica
Avaliado pela rubrica em `08-Assignments/ETHAGT11/assignment-01.md` (Pilar Comportamental 20%: colaboração em labs).
