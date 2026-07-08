# ETHAGT16 — Lab 1: Mini sociedade de agentes

> Curso: Sociedades de Agentes & Autonomous Research Systems · Carga: 15h · Pré-req: ETHAGT15

## Objetivo
Simular uma mini sociedade de 5 agentes com papéis distintos (pesquisador, crítico, sintetizador, revisor, editor) que colaboram para produzir um relatório de pesquisa, e analisar a dinâmica emergente da interação.

## Preparação
- Ambiente: Python 3.11+, `pip install openai`, `.env` com API key
- Dados/recursos: 3 tópicos de pesquisa em `topics.json`
- Leitura prévia: Apostila ETHAGT16, Unidade 1 (Sociedades de agentes) e Unidade 2 (Simulações sociais)

## Roteiro
### Passo 1 — Definir os papéis sociais
Modele 5 papéis com responsabilidades claras:

```python
ROLES = {
    "researcher": {
        "instructions": "You are a researcher. Find and present key information on the topic. Be thorough and factual.",
        "personality": "curious, methodical",
        "tools": ["search_web", "search_papers"]
    },
    "critic": {
        "instructions": "You are a critic. Challenge claims, find weaknesses, demand evidence.",
        "personality": "skeptical, rigorous",
        "tools": ["fact_check"]
    },
    "synthesizer": {
        "instructions": "You synthesize inputs from others into coherent narratives. Find connections.",
        "personality": "integrative, holistic",
        "tools": []
    },
    "reviewer": {
        "instructions": "You review for clarity, accuracy, and completeness. Suggest improvements.",
        "personality": "detail-oriented, fair",
        "tools": []
    },
    "editor": {
        "instructions": "You are the final editor. Polish language, ensure structure, make decisions.",
        "personality": "decisive, quality-focused",
        "tools": []
    }
}
```

**Checkpoint:** 5 papéis definidos com instruções, personalidade e tools.

### Passo 2 — Modelar o espaço compartilhado (blackboard social)
A sociedade compartilha um workspace:

```python
@dataclass
class SocietyWorkspace:
    topic: str
    findings: list[dict] = field(default_factory=list)
    critiques: list[dict] = field(default_factory=list)
    synthesis: str = ""
    review_notes: list[str] = field(default_factory=list)
    final_report: str = ""
    turn: int = 0
    history: list[dict] = field(default_factory=list)

    def add_contribution(self, role, content, contribution_type):
        entry = {"role": role, "content": content, "type": contribution_type,
                 "turn": self.turn}
        self.history.append(entry)
        if contribution_type == "finding":
            self.findings.append(entry)
        elif contribution_type == "critique":
            self.critiques.append(entry)
```

**Checkpoint:** workspace acumula contribuições tipadas de cada agente.

### Passo 3 — Implementar os turnos de fala
Cada agente age em sequência, lendo o workspace:

```python
def researcher_turn(workspace: SocietyWorkspace):
    prompt = f"""{ROLES["researcher"]["instructions"]}
    Topic: {workspace.topic}
    Previous findings: {[f["content"][:100] for f in workspace.findings[-3:]]}
    Find NEW information not yet covered. Output 3 key findings."""
    findings = call_llm(prompt)
    workspace.add_contribution("researcher", findings, "finding")
    return findings

def critic_turn(workspace: SocietyWorkspace):
    prompt = f"""{ROLES["critic"]["instructions"]}
    Topic: {workspace.topic}
    Findings to critique: {[f["content"] for f in workspace.findings]}
    Challenge weak claims. Identify gaps. Output your critiques."""
    critique = call_llm(prompt)
    workspace.add_contribution("critic", critique, "critique")
    return critique
```

**Checkpoint:** pesquisador e crítico produzem contribuições distintas.

### Passo 4 — O ciclo de colaboração
Execute o ciclo completo: pesquisa → crítica → síntese → revisão → edição:

```python
def run_society(topic, rounds=2):
    ws = SocietyWorkspace(topic=topic)

    for round_num in range(rounds):
        ws.turn = round_num + 1

        # Turno 1: Pesquisador coleta informações
        researcher_turn(ws)

        # Turno 2: Crítico desafia
        critic_turn(ws)

        # Turno 3: Sintetizador integra
        ws.synthesis = synthesizer_turn(ws)

        # Turno 4: Revisor verifica
        review = reviewer_turn(ws)
        ws.review_notes.append(review)

        # Se revisor aprovar e não for a última rodada, fazer mais uma
        if "APPROVED" in review and round_num == rounds - 1:
            break

    # Turno final: Editor aperfeiçoa
    ws.final_report = editor_turn(ws)
    return ws
```

**Checkpoint:** ciclo completo executa e produz um relatório final.

### Passo 5 — Sintetizador e editor
Implemente os papéis integradores:

```python
def synthesizer_turn(ws):
    prompt = f"""{ROLES["synthesizer"]["instructions"]}
    Topic: {ws.topic}
    Findings: {[f["content"] for f in ws.findings]}
    Critiques: {[c["content"] for c in ws.critiques]}
    Synthesize into a coherent narrative. Address critiques."""
    return call_llm(prompt)

def editor_turn(ws):
    prompt = f"""{ROLES["editor"]["instructions"]}
    Topic: {ws.topic}
    Synthesis: {ws.synthesis}
    Review notes: {ws.review_notes}
    Produce the FINAL polished report with clear structure:
    1. Executive Summary
    2. Key Findings
    3. Analysis
    4. Conclusion"""
    return call_llm(prompt)
```

**Checkpoint:** síntese endereça críticas; editor produz relatório estruturado.

### Passo 6 — Executar para 3 tópicos
Rode a sociedade para 3 tópicos diferentes:

```python
for topic in TOPICS:
    print(f"\n=== Society working on: {topic} ===")
    workspace = run_society(topic, rounds=2)
    save_report(workspace, f"reports/{topic['id']}.md")
    print(f"Report saved. History: {len(workspace.history)} contributions.")
```

**Checkpoint:** 3 relatórios produzidos e salvos.

### Passo 7 — Analisar a dinâmica emergente
Examine o histórico de interações:

```python
def analyze_dynamics(workspace):
    contributions_by_role = Counter(c["role"] for c in workspace.history)
    total_tokens = sum(len(c["content"].split()) for c in workspace.history)
    # Quem contribuiu mais? O crítico mudou a direção?
    return {
        "contributions": dict(contributions_by_role),
        "total_words": total_tokens,
        "rounds": workspace.turn,
        "critic_impact": did_critic_change_direction(workspace)
    }
```

| Tópico | Rounds | Contribuições | Palavras totais | Crítico impactou? |
|---|---|---|---|---|
| Tópico 1 | | | | |
| Tópico 2 | | | | |
| Tópico 3 | | | | |

**Checkpoint:** análise de dinâmica social documentada em `dynamics.md`.

### Passo 8 — Avaliar qualidade do relatório
Use LLM-as-judge para avaliar os relatórios:

```python
def evaluate_report(report, topic):
    prompt = f"""Rate this research report on:
    - Accuracy (1-5)
    - Completeness (1-5)
    - Structure (1-5)
    - Addressed counterarguments (1-5)
    Report: {report}
    Topic: {topic}"""
    return call_llm(prompt)
```

**Checkpoint:** relatórios avaliados com scores em 4 dimensões.

## Desafios extras
- Adicione um 6º agente "devil's advocate" que sempre discorda e veja o impacto
- Permita que agentes se comuniquem diretamente (não só via workspace)
- Implemente votação: se 3+ agentes discordam da síntese, refazer
- Meça convergência: quantas rodadas até o grupo chegar a consenso?

## Entrega
- Repositório com `society.py`, `reports/`, `dynamics.md`, `quality_eval.md`
- Commit no padrão `ETHAGT16: lab-1 simular mini sociedade de agentes`

## Rubrica
Avaliado pela rubrica em `08-Assignments/ETHAGT16/assignment-01.md` (Pilar Comportamental 20%: colaboração em labs).
