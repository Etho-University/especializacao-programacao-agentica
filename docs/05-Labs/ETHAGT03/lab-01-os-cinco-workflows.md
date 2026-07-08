# ETHAGT03 — Lab 1: Os 5 workflows em um dia

> Curso: Padrões de Workflow Agêntico · Carga: 30h · Pré-req: ETHAGT01

## Objetivo
Implementar versões mínimas (mas funcionais) dos 5 padrões de workflow canônicos da Anthropic — prompt chaining, routing, parallelization, orchestrator-workers e evaluator-optimizer — em um domínio comum: responder a tickets de suporte ao cliente.

## Preparação
- Ambiente: Python 3.11+, `pip install openai`, `.env` com API key
- Dados/recursos: `tickets.json` com 10 tickets de suporte pré-rotulados
- Leitura prévia: Apostila ETHAGT03, Unidades 2-6 (um workflow por unidade)

## Roteiro
### Passo 1 — Setup do domínio comum
Crie o arquivo `tickets.json` com 10 tickets de suporte variados (técnico, billing, feature request, bug):

```json
[
  {"id": "T1", "category": "technical", "text": "App crasha ao fazer login com Google"},
  {"id": "T2", "category": "billing", "text": "Fui cobrado duas vezes este mês"},
  {"id": "T3", "category": "feature", "text": "Gostaria de exportar relatórios em PDF"}
]
```

**Checkpoint:** arquivo com 10 tickets cobrindo pelo menos 4 categorias.

### Passo 2 — Workflow 1: Prompt Chaining
Implemente um pipeline de 3 etapas: (1) classificar ticket → (2) gerar rascunho de resposta → (3) revisar e polir:

```python
def prompt_chaining(ticket):
    category = call_llm(f"Classify this ticket into technical/billing/feature/bug:\n{ticket}")
    draft = call_llm(f"Write a support response for a {category} ticket:\n{ticket}")
    final = call_llm(f"Review and polish this support response for tone and clarity:\n{draft}")
    return final
```

Adicione um **gate programático**: se a categoria for "bug", redirecione para um template especial.

**Checkpoint:** pipeline de 3 etapas roda e produz resposta polida; gate de "bug" funciona.

### Passo 3 — Workflow 2: Routing
Implemente um classificador que roteia por **modelo** (fácil → mini, difícil → full) e por **prompt especializado**:

```python
def routing(ticket):
    difficulty = call_llm(f"Rate difficulty 1-5: {ticket}", model="gpt-4o-mini")
    level = int(difficulty.strip())
    model = "gpt-4o" if level >= 4 else "gpt-4o-mini"
    template = PROMPTS.get(category_from(ticket), DEFAULT_TEMPLATE)
    return call_llm(template.format(ticket=ticket), model=model)
```

**Checkpoint:** tickets simples usam modelo menor; tickets complexos usam modelo maior.

### Passo 4 — Workflow 3: Parallelization (sectioning)
Divida a resposta em 3 subtarefas independentes executadas em paralelo: diagnóstico, solução, FAQ relacionado:

```python
import asyncio
async def parallelization_sectioning(ticket):
    tasks = [
        call_llm_async(f"Diagnose this issue: {ticket}"),
        call_llm_async(f"Propose a solution: {ticket}"),
        call_llm_async(f"List 2 related FAQ items: {ticket}")
    ]
    diagnosis, solution, faq = await asyncio.gather(*tasks)
    return f"{diagnosis}\n\n{solution}\n\nRelated: {faq}"
```

**Checkpoint:** as 3 chamadas executam em paralelo e o resultado é combinado.

### Passo 5 — Workflow 3b: Parallelization (voting)
Implemente voting: gere 3 respostas independentes e use um modelo para escolher a melhor:

```python
async def parallelization_voting(ticket):
    candidates = await asyncio.gather(*[
        call_llm_async(f"Respond to: {ticket}", temperature=0.7) for _ in range(3)
    ])
    best = call_llm(f"Pick the best response. Options:\n{candidates}")
    return best
```

**Checkpoint:** 3 candidatos são gerados e um é selecionado pelo juiz.

### Passo 6 — Workflow 4: Orchestrator-Workers
Implemente um orquestrador que **decompõe dinamicamente** o ticket em subtarefas e as atribui a workers:

```python
def orchestrator_workers(ticket):
    plan = call_llm(f"Break this support ticket into subtasks as JSON list:\n{ticket}")
    subtasks = json.loads(plan)
    results = [worker(subtask) for subtask in subtasks]
    final = call_llm(f"Synthesize these worker outputs into one response:\n{results}")
    return final
```

**Checkpoint:** orquestrador gera plano dinâmico (número de subtasks varia por ticket).

### Passo 7 — Workflow 5: Evaluator-Optimizer
Implemente o loop gerar → avaliar → refinar com critério de parada:

```python
def evaluator_optimizer(ticket, max_iters=3):
    response = call_llm(f"Respond to: {ticket}")
    for i in range(max_iters):
        score = call_llm(f"Rate this response 1-10 on helpfulness, accuracy, tone:\n{response}")
        if int(score) >= 8:
            return response
        feedback = call_llm(f"What needs improvement?\n{response}")
        response = call_llm(f"Improve based on feedback: {feedback}\nOriginal: {response}")
    return response
```

**Checkpoint:** loop para quando score ≥ 8 ou max_iters atingido.

### Passo 8 — Comparação dos 5 workflows
Rode os 5 workflows nos mesmos 10 tickets e meça custo (tokens), latência e qualidade percebida (1-5):

| Workflow | Tokens médios | Latência média | Qualidade média |
|---|---|---|---|
| Prompt Chaining | | | |
| Routing | | | |
| Parallelization (sec) | | | |
| Parallelization (vote) | | | |
| Orchestrator-Workers | | | |
| Evaluator-Optimizer | | | |

**Checkpoint:** tabela preenchida e salva em `comparison.md`.

## Desafios extras
- Componha routing + evaluator-optimizer e compare com cada um isoladamente
- Adicione um gate programático que detecta tickets de churn e roteia para humano
- Meça o tempo de desenvolvimento de cada workflow (qual é mais rápido de implementar?)

## Entrega
- Repositório com `workflows.py`, `tickets.json`, `comparison.md`, traces em `traces/`
- Commit no padrão `ETHAGT03: lab-1 implementar cinco workflows`

## Rubrica
Avaliado pela rubrica em `08-Assignments/ETHAGT03/assignment-01.md` (Pilar Comportamental 20%: colaboração em labs).
