# ETHAGT03 — Lab 2: Composição de workflows

> Curso: Padrões de Workflow Agêntico · Carga: 30h · Pré-req: ETHAGT03 Lab 1

## Objetivo
Construir um pipeline composto que combina 3 padrões de workflow (routing → parallelization → evaluator-optimizer) para resolver uma tarefa de síntese de relatório a partir de múltiplas fontes, medindo custo e latência em cada estágio.

## Preparação
- Ambiente: Python 3.11+, `pip install openai`, `.env` com API key
- Dados/recursos: `sources/` com 5-10 documentos sobre um tema (ex.: sustentabilidade, IA)
- Leitura prévia: Apostila ETHAGT03, Unidade 7 (Composições e limites)

## Roteiro
### Passo 1 — Definir a tarefa composta
A tarefa: dado um conjunto de fontes e uma pergunta, produzir um relatório estruturado. O pipeline deve: (1) classificar a pergunta, (2) buscar em paralelo em múltiplas fontes, (3) avaliar e refinar o relatório.

```python
TASK = """
Given sources in /sources/ and a user question, produce a structured report
with: Executive Summary, Key Findings, Recommendations.
"""
```

**Checkpoint:** tarefa e fontes definidas; pelo menos 5 documentos em `sources/`.

### Passo 2 — Estágio 1: Routing
Implemente o classificador inicial que roteia por **tipo de pergunta** e seleciona o prompt apropriado:

```python
def route_question(question, sources):
    prompt = f"""Classify this question into one of:
    - factual (needs precise data)
    - analytical (needs reasoning over data)
    - creative (needs synthesis/suggestions)
    Question: {question}
    Reply with one word."""
    qtype = call_llm(prompt).strip()
    template = TEMPLATES[qtype]
    return qtype, template
```

**Checkpoint:** routing classifica corretamente 3 tipos de pergunta de teste.

### Passo 3 — Estágio 2: Parallelization com 3 workers
Implemente 3 workers paralelos que extraem informação de ângulos diferentes:

```python
async def parallel_extraction(question, template, sources):
    workers = [
        ("key_facts", extract_key_facts(question, sources)),
        ("trends", extract_trends(question, sources)),
        ("counterpoints", extract_counterpoints(question, sources))
    ]
    names = [n for n, _ in workers]
    tasks = [t for _, t in workers]
    # asyncio.gather executa as corrotinas concorrentemente (em paralelo)
    outcomes = await asyncio.gather(*tasks)
    return dict(zip(names, outcomes))
```

**Checkpoint:** 3 workers executam em paralelo via `asyncio.gather`.

### Passo 4 — Gate programático entre estágios
Adicione um gate que verifica se os 3 workers produziram conteúdo suficiente (mínimo de palavras):

```python
def gate_extraction(results):
    for name, content in results.items():
        if len(content.split()) < 20:
            return False, f"Worker '{name}' produced insufficient content"
    return True, "passed"
```

**Checkpoint:** gate bloqueia passagem se algum worker retornar conteúdo vazio/curto.

### Passo 5 — Estágio 3: Evaluator-Optimizer
Combine os resultados dos workers e refine iterativamente:

```python
def synthesize_and_optimize(question, results, max_iters=3):
    draft = call_llm(f"Synthesize into a report:\nQuestion: {question}\nData: {results}")
    for i in range(max_iters):
        eval_result = call_llm(f"""Evaluate this report on completeness,
        accuracy, structure (1-10 each):\n{draft}""")
        scores = parse_scores(eval_result)
        if all(v >= 8 for v in scores.values()):
            return draft
        draft = call_llm(f"Improve based on: {eval_result}\nCurrent:\n{draft}")
    return draft
```

**Checkpoint:** loop para quando todos os critérios ≥ 8 ou max_iters atingido.

### Passo 6 — Instrumentação de custo/latência
Adicione medição granular por estágio:

```python
@dataclass
class StageMetrics:
    stage: str
    tokens_in: int
    tokens_out: int
    latency_ms: float
    cost_usd: float

metrics = []
# Instrumentar cada call_llm com timing e token counting
```

**Checkpoint:** cada estágio produz um objeto `StageMetrics` e é coletado.

### Passo 7 — Execução e relatório de medições
Rode o pipeline composto em 5 perguntas diferentes e produza uma tabela:

| Pergunta | Routing (tokens/ms) | Parallel (tokens/ms) | Eval-Opt (tokens/ms) | Total |
|---|---|---|---|---|

**Checkpoint:** tabela salva em `metrics.md` com dados de 5 execuções.

### Passo 8 — Análise de trade-offs
Escreva uma análise (1 página) respondendo:
1. Onde está o gargalo de custo? De latência?
2. O evaluator-optimizer vale o custo extra?
3. Em que cenário você simplificaria este pipeline (removeria um estágio)?

**Checkpoint:** análise documentada em `tradeoff_analysis.md`.

## Desafios extras
- Substitua o evaluator-optimizer por voting (3 versões paralelas + juiz) e compare custo/qualidade
- Adicione um fallback: se o parallelization falhar, usar prompt chaining simples
- Meça o pipeline com modelo mini vs full e veja onde a diferença é maior

## Entrega
- Repositório com `pipeline.py`, `metrics.md`, `tradeoff_analysis.md`, traces
- Commit no padrão `ETHAGT03: lab-2 compor workflows com medição`

## Rubrica
Avaliado pela rubrica em `08-Assignments/ETHAGT03/assignment-01.md` (Pilar Comportamental 20%: colaboração em labs).
