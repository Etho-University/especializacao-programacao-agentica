# ETHAGT02 — Lab 1: Refatorando tools

> Curso: Tool Calling e Agent-Computer Interface (ACI) · Carga: 25h · Pré-req: ETHAGT01

## Objetivo
Receber 5 tools mal-desenhadas, aplicar os princípios de ACI da Anthropic (poka-yoke, descrições ricas, paths absolutos, schemas estritos) e medir a melhoria na taxa de uso correto em 20 casos.

## Preparação
- Ambiente: Python 3.11+, `pip install openai pydantic instructor`, `.env` com API key
- Dados/recursos: arquivo `tools_v0.py` (fornecido com 5 tools ruins) e `test_cases.json` (20 casos)
- Leitura prévia: Apostila ETHAGT02, Unidade 2 (ACI como disciplina) e Unidade 5 (Erros comuns)

## Roteiro
### Passo 1 — Inspecionar as tools originais
Examine as 5 tools em `tools_v0.py`. Cada uma tem pelo menos um anti-pattern:

| Tool | Problema |
|---|---|
| `search(q)` | Nome e parâmetro ambíguos; sem descrição |
| `get_data(type, id, fmt, opt)` | 4 parâmetros sem tipo, sem default, sem enum |
| `update_record(rec)` | Aceita JSON genérico; path relativo |
| `calc(e)` | `eval()` perigoso; aceita qualquer string |
| `send(msg, to, subj, cc, bcc, att)` | 6 parâmetros; sem validação de email; destrutiva sem HITL |

**Checkpoint:** você identificou pelo menos 1 anti-pattern por tool e documentou em `audit.md`.

### Passo 2 — Refatorar `search` → `search_knowledge_base`
Aplique: nome descritivo, descrição rica, schema Pydantic, path absoluto do índice:

```python
from pydantic import BaseModel, Field

class SearchInput(BaseModel):
    query: str = Field(..., min_length=3, max_length=200,
        description="Natural-language search query, e.g. 'how to reset password'")
    limit: int = Field(default=5, ge=1, le=20,
        description="Max number of results to return (1-20)")

async def search_knowledge_base(query: str, limit: int = 5) -> list[dict]:
    """Search the internal knowledge base (path: /data/kb/index).
    Returns up to `limit` articles matching the query.
    Example: search_knowledge_base(query='password reset', limit=3)
    """
    ...
```

**Checkpoint:** tool tem nome, descrição, schema Pydantic e exemplo de uso.

### Passo 3 — Refatorar `get_data` com enums e defaults
Use `enum` para `type` e `fmt`, adicione defaults, torne `opt` explícito:

```python
from enum import Enum
class DataType(str, Enum):
    USER = "user"
    ORDER = "order"
    TICKET = "ticket"
class OutputFormat(str, Enum):
    SUMMARY = "summary"
    FULL = "full"
```

**Checkpoint:** parâmetros ambíguos agora têm tipos restritos e defaults.

### Passo 4 — Refatorar `update_record` com idempotência
Adicione `request_id` para idempotência, path absoluto, e trate erro com mensagem útil ao modelo:

```python
def update_record(record_id: str, fields: dict, request_id: str) -> str:
    """Update a record by absolute ID. Idempotent via request_id.
    Returns confirmation or error message helpful to the LLM."""
    ...
```

**Checkpoint:** a tool aceita `request_id` e retorna mensagem útil em caso de erro.

### Passo 5 — Refatorar `calc` com sandbox seguro
Substitua `eval()` por `ast.literal_eval` ou `numexpr.evaluate`, restrinja operadores:

```python
import numexpr
def calculate(expression: str) -> str:
    """Evaluate a mathematical expression. Only +, -, *, /, **, () allowed.
    Example: calculate('3.14 * 2**2')"""
    if not re.match(r'^[\d\.\+\-\*\/\(\) ]+$', expression):
        return "Error: only numeric expressions with +, -, *, /, **, () are allowed"
    return str(numexpr.evaluate(expression))
```

**Checkpoint:** `calculate("__import__('os')")` retorna erro, não executa.

### Passo 6 — Refatorar `send` → `send_email` com HITL
Marque como destrutiva, adicione validação de email e HITL:

```python
async def send_email(to: str, subject: str, body: str,
                     require_confirmation: bool = True) -> str:
    """Send an email. DESTRUCTIVE — requires human confirmation by default.
    Set require_confirmation=False only for test/sandbox mode."""
    if not re.match(r'^[\w.+-]+@[\w-]+\.[\w.-]+$', to):
        return f"Error: invalid email address '{to}'"
    if require_confirmation:
        return f"DRY-RUN: would send to {to}. Set require_confirmation=False to execute."
    ...
```

**Checkpoint:** por padrão a tool faz dry-run; email inválido retorna erro tratado.

### Passo 7 — Construir o workbench
Crie um script `workbench.py` que roda 20 casos de teste (`test_cases.json`) contra o agente com as tools e mede: taxa de uso correto, custo, latência:

```python
def run_workbench(tools, cases):
    results = []
    for case in cases:
        start = time.time()
        response = agent.run(case["query"], tools=tools)
        elapsed = time.time() - start
        correct = judge(response, case["expected"])
        results.append({"case": case["id"], "correct": correct, "latency": elapsed})
    accuracy = sum(r["correct"] for r in results) / len(results)
    return accuracy, results
```

**Checkpoint:** workbench roda os 20 casos e produz `results.json` com accuracy.

### Passo 8 — Comparar antes vs depois
Rode o workbench com `tools_v0.py` e depois com `tools_v1.py` (refatoradas). Compare:

| Métrica | v0 (original) | v1 (refatorada) | Delta |
|---|---|---|---|
| Taxa de uso correto | ? | ? | ? |
| Custo médio (tokens) | ? | ? | ? |
| Latência média (s) | ? | ? | ? |

**Checkpoint:** tabela preenchida com números reais em `comparison.md`.

## Desafios extras
- Adicione um 6º caso de edge case ao workbench (ex.: query ambígua) e veja como as tools refatoradas se saem
- Escreva um conjunto de testes de regressão automatizados para as tools (pytest)
- Tente consolidar 2 tools similares em 1 e meça o impacto

## Entrega
- Repositório com `tools_v0.py`, `tools_v1.py`, `workbench.py`, `comparison.md`, `results.json`
- Relatório curto (1 página) documentando os anti-patterns encontrados e correções
- Commit no padrão `ETHAGT02: lab-1 refatorar tools com ACI`

## Rubrica
Avaliado pela rubrica em `08-Assignments/ETHAGT02/assignment-01.md` (Pilar Comportamental 20%: colaboração em labs).
