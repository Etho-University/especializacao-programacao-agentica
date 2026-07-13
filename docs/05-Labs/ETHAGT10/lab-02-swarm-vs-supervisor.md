# ETHAGT10 — Lab 2: Swarm vs Supervisor

> Curso: Padrões de Arquitetura Multi-Agente · Carga: 30h · Pré-req: ETHAGT10 Lab 1

## Objetivo
Implementar a mesma tarefa em duas topologias (Swarm com handoffs e Supervisor centralizado), medir custo, latência, qualidade e robustez, e produzir um ADR justificando quando usar cada uma.

## Preparação
- Ambiente: Python 3.11+, `pip install langgraph openai`, `.env` com API key
- Dados/recursos: 5 tarefas de suporte técnico variadas em [`tasks.json`](https://raw.githubusercontent.com/Etho-University/especializacao-programacao-agentica/main/05-Labs/ETHAGT10/tasks.json)
- Leitura prévia: Apostila ETHAGT10, Unidade 3 (Swarm) e Unidade 2 (Supervisor)

## Roteiro
### Passo 1 — Definir agentes compartilhados
Crie 4 agentes que serão usados em ambas as topologias:

```python
SHARED_AGENTS = {
    "triage": Agent("Triage", "Route issues to the right specialist."),
    "tech": Agent("Tech", "Solve technical problems.", tools={"search_kb": search_kb}),
    "billing": Agent("Billing", "Handle billing.", tools={"check_invoices": check_invoices}),
    "escalation": Agent("Escalation", "Handle complex/rare cases.")
}
```

**Checkpoint:** 4 agentes definidos para ambas as topologias.

### Passo 2 — Topologia 1: Supervisor
Implemente um supervisor centralizado que roteia todas as mensagens:

```python
def supervisor_topology(task):
    messages = [{"role": "user", "content": task}]
    for _ in range(8):  # max turnos
        # Supervisor decide quem age
        decision = call_llm(f"""As supervisor, decide which agent acts next.
        Agents: {list(SHARED_AGENTS.keys())}
        Conversation: {messages}
        Reply: DELEGATE[agent_name] or FINALIZE[answer]""")
        if "FINALIZE" in decision:
            return extract_answer(decision)
        agent_name = extract_delegate(decision)
        response = call_agent(agent_name, messages)
        messages.append({"role": "assistant", "name": agent_name, "content": response})
    return "Max turns reached"
```

**Checkpoint:** supervisor delega e finaliza corretamente.

### Passo 3 — Topologia 2: Swarm
Implemente swarm com handoffs (sem coordenador central):

```python
def swarm_topology(task, entry_agent="triage"):
    current = entry_agent
    context = task
    path = [current]
    for _ in range(8):
        agent = SHARED_AGENTS[current]
        response = call_agent_with_handoff(agent, context)
        handoff = detect_handoff(response, agent)
        if handoff:
            current = handoff.to_agent
            context = handoff.context
            path.append(current)
        elif "REPLY:" in response:
            return response.split("REPLY:")[1].strip(), path
    return "Max turns", path
```

**Checkpoint:** swarm transfere entre agentes sem coordenador central.

### Passo 4 — Executar benchmark
Rode ambas as topologias nas 5 tarefas:

```python
results = []
for task in tasks:
    sv_result = supervisor_topology(task["question"])
    sw_result, sw_path = swarm_topology(task["question"])
    results.append({
        "task_id": task["id"],
        "supervisor": {"answer": sv_result, "correct": check(sv_result, task["expected"])},
        "swarm": {"answer": sw_result, "correct": check(sw_result, task["expected"]),
                  "path": sw_path}
    })
```

**Checkpoint:** 10 execuções (5 × 2 topologias) registradas em `benchmark.json`.

### Passo 5 — Medir custo e latência
Instrumente cada topologia:

```python
@dataclass
class TopologyMetrics:
    topology: str
    task_id: str
    correct: bool
    tokens: int
    latency_s: float
    agents_involved: int
    turns: int
```

**Checkpoint:** métricas coletadas para as 10 execuções.

### Passo 6 — Análise comparativa
Produza tabela comparativa:

| Métrica | Supervisor | Swarm |
|---|---|---|
| Accuracy (5) | /5 | /5 |
| Tokens médios | | |
| Latência média | | |
| Agentes envolvidos (média) | | |
| Robustez (trata edge case?) | | |

**Checkpoint:** tabela preenchida em `comparison.md`.

### Passo 7 — Análise de robustez
Teste um cenário adverso: tarefa que nenhum agente sabe resolver bem.

- **Supervisor**: pode escalar para `escalation` agent explicitamente
- **Swarm**: pode ficar em loop de handoffs até atingir max turns

**Checkpoint:** comportamento sob falha documentado para ambas.

### Passo 8 — Escrever o ADR
Escreva um Architecture Decision Record justificando a escolha:

```markdown
# ADR: Swarm vs Supervisor para Suporte Técnico

## Contexto
Sistema de suporte com 4 agentes especializados.

## Decisão
[Swarm | Supervisor] — justifique baseado nos dados.

## Comparação
[Inserir tabela do Passo 6]

## Consequências
- Vantagem escolhida: ...
- Trade-off aceito: ...
```

**Checkpoint:** ADR completo em `adr-topology.md` com dados empíricos.

## Desafios extras
- Adicione uma 3ª topologia (blackboard) e compare as três
- Implemente um híbrido: supervisor com handoff para sub-protocolos
- Meça "overhead de coordenação": % de tokens gastos em roteamento vs resolução
- Teste com 10+ agentes e veja onde cada topologia quebra

## Entrega
- Repositório com `swarm.py`, `supervisor.py`, `benchmark.json`, `comparison.md`, `adr-topology.md`
- Commit no padrão `ETHAGT10: lab-2 comparar swarm vs supervisor`

## Rubrica
Avaliado pela rubrica em `08-Assignments/ETHAGT10/assignment-01.md` (Pilar Comportamental 20%: colaboração em labs).
