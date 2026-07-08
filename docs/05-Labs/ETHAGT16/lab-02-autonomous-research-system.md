# ETHAGT16 — Lab 2: Autonomous research system

> Curso: Sociedades de Agentes & Autonomous Research Systems · Carga: 15h · Pré-req: ETHAGT16 Lab 1

## Objetivo
Construir um protótipo de sistema de pesquisa autônoma que, dada uma pergunta técnica, executa o pipeline completo — revisão de literatura, formulação de hipótese, experimento simulado e relatório — inspirado no AI Scientist da Sakana.

## Preparação
- Ambiente: Python 3.11+, `pip install openai`, `.env` com API key
- Dados/recursos: 3 perguntas de pesquisa em `research_questions.json`
- Leitura prévia: Apostila ETHAGT16, Unidade 3 (Autonomous Research Systems) e Unidade 4 (Emergência)

## Roteiro
### Passo 1 — Modelar o pipeline de pesquisa
Defina as etapas do sistema autônomo:

```python
@dataclass
class ResearchPipeline:
    question: str
    literature: list[dict] = field(default_factory=list)
    hypothesis: str = ""
    experiment_design: str = ""
    results: dict = field(default_factory=dict)
    analysis: str = ""
    report: str = ""
    citations: list[str] = field(default_factory=list)
    stage: str = "init"
```

**Checkpoint:** pipeline modela as 6 etapas da pesquisa científica.

### Passo 2 — Etapa 1: Revisão de literatura
O agente busca e sintetiza literatura existente:

```python
def literature_review(pipeline: ResearchPipeline):
    # Buscar papers relevantes (simulado ou via arXiv API)
    papers = search_arxiv(pipeline.question, max_results=10)

    # Sintetizar estado da arte
    synthesis = call_llm(f"""You are a research assistant conducting a literature review.
    Question: {pipeline.question}
    Papers found: {[{"title": p.title, "abstract": p.abstract[:200]} for p in papers]}

    Summarize:
    1. What is known about this topic?
    2. What are the main approaches?
    3. What gaps exist?""")

    pipeline.literature = [{"title": p.title, "id": p.id} for p in papers]
    pipeline.citations = [p.id for p in papers]
    pipeline.stage = "literature_done"
    return synthesis
```

**Checkpoint:** etapa produz síntese da literatura com citações.

### Passo 3 — Etapa 2: Formulação de hipótese
Com base na literatura, o agente propõe uma hipótese:

```python
def formulate_hypothesis(pipeline: ResearchPipeline):
    prompt = f"""Based on this literature review:
    {pipeline.literature[-1] if pipeline.literature else 'No literature yet'}

    And the research question: {pipeline.question}

    Formulate a testable hypothesis. Be specific and falsifiable.
    Format: 'We hypothesize that...'
    """
    hypothesis = call_llm(prompt)
    pipeline.hypothesis = hypothesis
    pipeline.stage = "hypothesis_done"
    return hypothesis
```

**Checkpoint:** hipótese é específica, testável e baseada na literatura.

### Passo 4 — Etapa 3: Design experimental
O agente desenha como testar a hipótese:

```python
def design_experiment(pipeline: ResearchPipeline):
    prompt = f"""Design a computational experiment to test this hypothesis:
    {pipeline.hypothesis}

    Specify:
    1. What to measure (variables, metrics)
    2. What conditions to compare (baseline vs treatment)
    3. What data/datasets to use
    4. How to evaluate results
    5. Expected outcome if hypothesis is true

    Be concrete and implementable."""
    design = call_llm(prompt)
    pipeline.experiment_design = design
    pipeline.stage = "experiment_designed"
    return design
```

**Checkpoint:** design experimental é concreto com variáveis e métricas.

### Passo 5 — Etapa 4: Execução do experimento (simulada)
Como não temos laboratório real, simule o experimento com LLM:

```python
def run_experiment(pipeline: ResearchPipeline):
    # Simular dados experimentais
    prompt = f"""Simulate the results of this experiment:
    Design: {pipeline.experiment_design}
    Hypothesis: {pipeline.hypothesis}

    Generate plausible results as JSON:
    {{
      "baseline": {{"metric1": ..., "metric2": ...}},
      "treatment": {{"metric1": ..., "metric2": ...}},
      "statistical_test": {{"p_value": ..., "effect_size": ...}},
      "n_samples": ...
    }}
    Make numbers realistic, not too perfect."""
    results = json.loads(call_llm(prompt, temperature=0.7))
    pipeline.results = results
    pipeline.stage = "experiment_done"
    return results
```

**Checkpoint:** experimento simulado produz dados plausíveis com testes estatísticos.

### Passo 6 — Etapa 5: Análise
O agente interpreta os resultados:

```python
def analyze_results(pipeline: ResearchPipeline):
    prompt = f"""Analyze these experimental results:
    Hypothesis: {pipeline.hypothesis}
    Results: {json.dumps(pipeline.results, indent=2)}

    Provide:
    1. What do the results show?
    2. Is the hypothesis supported or rejected?
    3. Statistical significance interpretation
    4. Limitations of the experiment
    5. Implications"""
    analysis = call_llm(prompt)
    pipeline.analysis = analysis
    pipeline.stage = "analysis_done"
    return analysis
```

**Checkpoint:** análise interpreta resultados com significância estatística e limitações.

### Passo 7 — Etapa 6: Geração do relatório
Produza o relatório final no formato de paper:

```python
def generate_report(pipeline: ResearchPipeline):
    prompt = f"""Write a research report in academic style:

    # {pipeline.question}

    ## Abstract
    [200-word summary]

    ## 1. Introduction
    [Context from literature]

    ## 2. Hypothesis
    {pipeline.hypothesis}

    ## 3. Methodology
    {pipeline.experiment_design}

    ## 4. Results
    {json.dumps(pipeline.results)}

    ## 5. Analysis
    {pipeline.analysis}

    ## 6. Conclusion
    [Summary and future work]

    ## References
    {pipeline.citations}

    Use the information above. Make it coherent and well-structured."""
    report = call_llm(prompt)
    pipeline.report = report
    pipeline.stage = "complete"
    return report
```

**Checkpoint:** relatório tem estrutura acadêmica completa com todas as seções.

### Passo 8 — Orquestrar o pipeline completo
Execute todas as etapas em sequência:

```python
async def autonomous_research(question):
    pipeline = ResearchPipeline(question=question)

    stages = [
        ("Literature Review", literature_review),
        ("Hypothesis Formulation", formulate_hypothesis),
        ("Experiment Design", design_experiment),
        ("Experiment Execution", run_experiment),
        ("Analysis", analyze_results),
        ("Report Generation", generate_report),
    ]

    for name, stage_fn in stages:
        print(f"  → {name}...")
        stage_fn(pipeline)
        print(f"    Done. Stage: {pipeline.stage}")

    return pipeline

# Executar para 3 perguntas
async def main():
    for q in RESEARCH_QUESTIONS:
        print(f"\n=== Research: {q} ===")
        result = await autonomous_research(q)
        save_report(result, f"research_output/{slugify(q)}.md")

asyncio.run(main())
```

**Checkpoint:** pipeline completo executa para 3 perguntas e produz 3 relatórios.

### Passo 9 — Avaliação crítica
Avalie a qualidade da pesquisa autônoma:

```python
def evaluate_research(pipeline):
    criteria = {
        "literature_coverage": "Did the review cite relevant papers?",
        "hypothesis_quality": "Is it specific and testable?",
        "experiment_rigor": "Is the design sound?",
        "analysis_depth": "Does analysis address limitations?",
        "report_coherence": "Is the report well-structured?"
    }
    scores = {}
    for criterion, question in criteria.items():
        raw = llm_judge(f"Rate 1-5: {question}\nReport: {pipeline.report[:500]}")
        m = re.search(r"[1-5]", str(raw))
        scores[criterion] = int(m.group()) if m else 3   # default neutro se parsing falhar
    return scores
```

| Critério | Pesquisa 1 | Pesquisa 2 | Pesquisa 3 |
|---|---|---|---|
| Literature coverage | /5 | /5 | /5 |
| Hypothesis quality | /5 | /5 | /5 |
| Experiment rigor | /5 | /5 | /5 |
| Analysis depth | /5 | /5 | /5 |
| Report coherence | /5 | /5 | /5 |

**Checkpoint:** 3 pesquisas avaliadas em 5 critérios.

### Passo 10 — Reflexão crítica
Documente honestamente o que funcionou e o que falhou:

```markdown
## Reflexão Crítica

### O que funcionou
- [listar aspectos positivos]

### O que falhou
- [listar limitações]

### Limitações fundamentais
- Experimentos são SIMULADOS, não reais
- Literatura é limitada ao que o LLM conhece/arXiv
- Não há verificação de validade científica real

### Questões éticas
- Automação de pesquisa: quem é o autor?
- Resultados simulados podem ser apresentados como reais?
- Responsabilidade por conclusões erradas?
```

**Checkpoint:** reflexão crítica honesta em `critical_reflection.md`.

## Desafios extras
- Adicione um agente "peer reviewer" que critica o paper gerado como revisor real
- Conecte a fontes reais (arXiv API, Semantic Scholar) para literatura
- Permita múltiplas hipóteses concorrentes e seleção da melhor
- Implemente iteração: se o peer reviewer rejeita, refazer etapas

## Entrega
- Repositório com `research_system.py`, `research_output/`, `quality_eval.md`, `critical_reflection.md`
- Commit no padrão `ETHAGT16: lab-2 construir autonomous research system`

## Rubrica
Avaliado pela rubrica em `08-Assignments/ETHAGT16/assignment-01.md` (Pilar Comportamental 20%: colaboração em labs).
