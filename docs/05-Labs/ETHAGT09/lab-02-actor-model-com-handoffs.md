# ETHAGT09 — Lab 2: Actor model com handoffs

> Curso: Comunicação e Coordenação Multi-Agente · Carga: 25h · Pré-req: ETHAGT09 Lab 1

## Objetivo
Implementar um sistema multi-agente usando o actor model com handoffs (estilo OpenAI Swarm), onde cada agente encapsula seu estado e transfere controle para outro agente quando necessário.

## Preparação
- Ambiente: Python 3.11+, `pip install openai`, `.env` com API key
- Dados/recursos: nenhum
- Leitura prévia: Apostila ETHAGT09, Unidade 4 (Actor Model) e Unidade 2 (Handoffs)

## Roteiro
### Passo 1 — Definir a estrutura do Actor-Agent
Modele cada agente como um actor com estado encapsulado:

```python
from dataclasses import dataclass, field
from typing import Callable

@dataclass
class Agent:
    name: str
    instructions: str
    tools: dict[str, Callable] = field(default_factory=dict)
    handoff_targets: list[str] = field(default_factory=list)
    state: dict = field(default_factory=dict)
```

**Checkpoint:** `Agent` encapsula instruções, tools, handoffs e estado privado.

### Passo 2 — Criar agentes especializados
Defina 3 agentes para um sistema de suporte técnico:

```python
triage = Agent(
    name="Triage",
    instructions="You triage user issues. Route to technical or billing.",
    handoff_targets=["technical", "billing"]
)
technical = Agent(
    name="Technical",
    instructions="You solve technical issues. If billing-related, handoff to billing.",
    tools={"search_kb": search_kb, "run_diagnostic": run_diagnostic},
    handoff_targets=["triage", "billing"]
)
billing = Agent(
    name="Billing",
    instructions="You handle billing issues. If technical, handoff to technical.",
    tools={"check_invoices": check_invoices, "process_refund": process_refund},
    handoff_targets=["triage", "technical"]
)
AGENTS = {"triage": triage, "technical": technical, "billing": billing}
```

**Checkpoint:** 3 agentes definidos com tools e handoffs distintos.

### Passo 3 — Implementar o handoff
O handoff transfere controle de um agente para outro:

```python
@dataclass
class Handoff:
    to_agent: str
    reason: str
    context: str  # informação passada adiante

def detect_handoff(response, current_agent):
    if "TRANSFER TO" in response:
        target = response.split("TRANSFER TO")[1].strip().lower()
        if target in current_agent.handoff_targets:
            return Handoff(to_agent=target, reason="requested by agent",
                          context=response)
    return None
```

**Checkpoint:** handoff detecta pedido de transferência e valida o target.

### Passo 4 — O actor loop
Implemente o loop de cada actor — processa mensagem, decide action ou handoff:

```python
async def actor_loop(agent_name, message, context=""):
    agent = AGENTS[agent_name]
    prompt = f"""{agent.instructions}
    Available tools: {list(agent.tools.keys())}
    Available handoffs: {agent.handoff_targets}
    To use a tool: CALL tool_name[args]
    To handoff: TRANSFER TO agent_name
    To respond: REPLY: <message>
    Context: {context}
    User: {message}"""
    response = call_llm(prompt)

    handoff = detect_handoff(response, agent)
    if handoff:
        return await actor_loop(handoff.to_agent, message,
                               context=handoff.context)

    if "CALL" in response:
        tool_name, args = parse_call(response)
        result = agent.tools[tool_name](args)
        return await actor_loop(agent_name, f"Tool result: {result}",
                               context=context)

    if "REPLY:" in response:
        return response.split("REPLY:")[1].strip()

    return response
```

**Checkpoint:** loop processa tools e handoffs recursivamente até produzir uma resposta.

### Passo 5 — Testar o handoff
Teste cenários que exigem transferência entre agentes:

```python
# Cenário 1: questão técnica simples
result = await actor_loop("triage", "Não consigo fazer login")
# Esperado: triage → technical → resolve

# Cenário 2: questão de billing
result = await actor_loop("triage", "Fui cobrado duas vezes")
# Esperado: triage → billing → resolve

# Cenário 3: questão mista
result = await actor_loop("triage", "Comprei plano premium mas não funciona")
# Esperado: triage → billing → technical (ou vice-versa)
```

**Checkpoint:** handoffs funcionam corretamente nos 3 cenários.

### Passo 6 — Rastrear a cadeia de handoffs
Registre o caminho percorrido para análise:

```python
async def actor_loop_tracked(agent_name, message, path=None, context=""):
    if path is None:
        path = []
    path.append(agent_name)
    # ... resto do loop
    return result, path

result, path = await actor_loop_tracked("triage", "Comprei premium mas não funciona")
print(f"Path: {' → '.join(path)}")
# Output: Path: triage → billing → technical
```

**Checkpoint:** cada execução produz o caminho de agentes percorrido.

### Passo 7 — Prevenir loops de handoff
Detecte ciclos: se um agente aparece 2x no path, aborte:

```python
def check_loop(path, max_visits=2):
    from collections import Counter
    counts = Counter(path)
    if any(v >= max_visits for v in counts.values()):
        raise RuntimeError(f"Handoff loop detected: {' → '.join(path)}")
```

**Checkpoint:** loop circular (A → B → A) é detectado e interrompido.

### Passo 8 — Comparar handoff vs seletor central
Compare o sistema de handoffs (Lab 2) com o group chat com seletor (Lab 1):

| Métrica | Handoff (Swarm) | Group Chat (Seletor) |
|---|---|---|
| Latência média | | |
| Tokens por resolução | | |
| Caminho médio (agentes envolvidos) | | |
| Complexidade de implementação | | |

**Checkpoint:** comparação documentada em `comparison.md`.

## Desafios extras
- Implemente handoff bidirecional com contexto acumulado (não resetar entre transfers)
- Adicione um agente "supervisor" que pode forçar handoff se um agente ficar preso
- Implemente o actor model com `asyncio` real (atores concorrentes, não sequenciais)
- Adicione estado persistente por agente (memory entre handoffs)

## Entrega
- Repositório com `actor_agents.py`, `traces/`, `comparison.md`
- Commit no padrão `ETHAGT09: lab-2 implementar actor model com handoffs`

## Rubrica
Avaliado pela rubrica em `08-Assignments/ETHAGT09/assignment-01.md` (Pilar Comportamental 20%: colaboração em labs).
