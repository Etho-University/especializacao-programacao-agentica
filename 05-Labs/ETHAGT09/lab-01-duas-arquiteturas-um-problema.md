# ETHAGT09 — Lab 1: Duas arquiteturas, um problema

> Curso: Comunicação e Coordenação Multi-Agente · Carga: 25h · Pré-req: ETHAGT04

## Objetivo
Resolver a mesma tarefa (análise de um PR de código) usando duas arquiteturas de comunicação distintas — Group Chat (estilo AutoGen) e Blackboard — e comparar as duas em qualidade, custo, latência e complexidade de implementação.

## Preparação
- Ambiente: Python 3.11+, `pip install openai langgraph`, `.env` com API key
- Dados/recursos: 3 diffs de PR em [`prs/`](https://github.com/Etho-University/especializacao-programacao-agentica/tree/main/05-Labs/ETHAGT09/prs) (fornecidos), com questões conhecidas
- Leitura prévia: Apostila ETHAGT09, Unidade 2 (Padrões de conversação) e Unidade 3 (Blackboard)

## Roteiro
### Passo 1 — Definir os agentes especialistas
Crie 3 especialistas com prompts distintos:

```python
AGENTS = {
    "security": {"role": "Security Reviewer",
                 "system": "You are a security expert. Review code for vulnerabilities."},
    "style": {"role": "Style Reviewer",
              "system": "You are a code style expert. Check naming, formatting, best practices."},
    "logic": {"role": "Logic Reviewer",
              "system": "You are a logic expert. Check correctness, edge cases, error handling."}
}
```

**Checkpoint:** 3 agentes definidos com system prompts distintos.

### Passo 2 — Arquitetura 1: Group Chat
Implemente um group chat onde um seletor escolhe quem fala a seguir:

```python
def group_chat_review(pr_diff):
    messages = [{"role": "user", "content": f"Review this PR diff:\n{pr_diff}"}]
    transcript = []
    for round in range(6):  # máximo 6 turnos
        # Seletor decide quem fala
        speaker = selector_agent(messages, list(AGENTS.keys()))
        response = call_agent(speaker, messages)
        messages.append({"role": "assistant", "name": speaker, "content": response})
        transcript.append({"speaker": speaker, "content": response})
    return transcript
```

**Checkpoint:** group chat produz uma sequência de reviews dos 3 especialistas.

### Passo 3 — Implementar o seletor
O seletor decide qual agente fala a seguir com base no estado:

```python
def selector_agent(messages, available_agents):
    prompt = f"""Given the conversation so far, which agent should speak next?
    Available: {available_agents}
    If review is complete, reply: DONE
    Conversation: {messages[-3:]}"""
    choice = call_llm(prompt).strip()
    return choice if choice in available_agents else "DONE"
```

**Checkpoint:** seletor rotaciona entre os 3 agentes e eventualmente diz "DONE".

### Passo 4 — Arquitetura 2: Blackboard
Implemente um espaço compartilhado onde cada especialista lê e escreve:

```python
from dataclasses import dataclass, field

@dataclass
class Blackboard:
    findings: dict = field(default_factory=lambda: {
        "security": [], "style": [], "logic": [], "synthesis": []
    })
    status: str = "open"

def blackboard_review(pr_diff):
    bb = Blackboard()
    bb.findings["input"] = [pr_diff]
    for round in range(3):
        for agent_name in ["security", "style", "logic"]:
            # Agente lê o blackboard inteiro e contribui
            contribution = call_agent(agent_name, f"""Blackboard state:
            {bb.findings}
            Add your findings (or 'nothing to add').""")
            if "nothing to add" not in contribution.lower():
                bb.findings[agent_name].append(contribution)
    # Sintetizador lê tudo e produz review final
    bb.findings["synthesis"].append(
        call_llm(f"Synthesize a final review:\n{bb.findings}"))
    return bb
```

**Checkpoint:** blackboard acumula contribuições e o sintetizador produz review final.

### Passo 5 — Comparação lado a lado
Rode ambas as arquiteturas nos mesmos 3 PRs:

```python
for pr_file in glob("prs/*.diff"):
    diff = open(pr_file).read()
    gc_result = group_chat_review(diff)
    bb_result = blackboard_review(diff)
    # Salvar resultados
```

**Checkpoint:** ambos os sistemas produzem reviews para os 3 PRs.

### Passo 6 — Medir métricas
Compare as duas arquiteturas:

| Métrica | Group Chat | Blackboard |
|---|---|---|
| Qualidade da review (1-5, julgado por humano) | | |
| Tokens consumidos | | |
| Latência total | | |
| Número de turnos/mensagens | | |
| Convergência (chegou a conclusão?) | | |

**Checkpoint:** tabela preenchida em `comparison.md`.

### Passo 7 — Análise de comunicação
Analise como a informação flui em cada arquitetura:

```markdown
## Group Chat
- Comunicação: sequencial, cada agente vê tudo que foi dito
- Vantagem: contexto rico, agentes reagem uns aos outros
- Desvantagem: ruído, agentes podem concordar prematuramente

## Blackboard
- Comunicação: indireta via espaço compartilhado
- Vantagem: isolamento, cada especialista foca no seu
- Desvantagem: menos sinergia, síntese depende de um agente final
```

**Checkpoint:** análise documenta prós/contras de cada padrão de comunicação.

### Passo 8 — Conclusão e recomendação
Escreva uma recomendação: para quais cenários cada arquitetura é melhor?

**Checkpoint:** recomendação clara em `recommendation.md`.

## Desafios extras
- Adicione um 4º agente "devil's advocate" que discorda e veja como cada arquitetura lida
- Implemente o group chat com handoff (estilo Swarm) em vez de seletor central
- Meça o "overhead de comunicação": quantos tokens são gastos em coordenação vs análise?

## Entrega
- Repositório com `group_chat.py`, `blackboard.py`, `comparison.md`, `recommendation.md`
- Commit no padrão `ETHAGT09: lab-1 comparar group chat vs blackboard`

## Rubrica
Avaliado pela rubrica em `08-Assignments/ETHAGT09/assignment-01.md` (Pilar Comportamental 20%: colaboração em labs).
