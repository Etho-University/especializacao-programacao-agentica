# ETHAGT01 — Lab 1: ReAct em 50 linhas

> Curso: Arquitetura Cognitiva de Agentes LLM · Carga: 25h · Pré-req: nenhum

## Objetivo
Implementar um agent loop ReAct (Thought → Action → Observation) em Python puro, sem nenhum framework, chamando uma LLM API e usando uma tool de cálculo.

## Preparação
- Ambiente: Python 3.11+, `pip install openai` (ou `anthropic`), `.env` com `OPENAI_API_KEY`
- Dados/recursos: não há
- Leitura prévia: Apostila ETHAGT01, Unidade 3 (Agent Loop: ReAct) e Unidade 6 (Observabilidade)

## Roteiro
### Passo 1 — Estrutura do loop
Crie `agent.py` com a função principal `run(query, max_iters=10)` que itera até obter uma resposta final ou atingir o limite de iterações. Cada iteração produz: `Thought`, `Action`, `Observation`.

```python
import re, json
from openai import OpenAI

client = OpenAI()
SYSTEM = """You are a ReAct agent. Use this format strictly:
Thought: <reasoning>
Action: <tool_name>[<args>]
OR
Thought: <reasoning>
Answer: <final answer>"""
```

**Checkpoint:** o arquivo executa sem erro e a string `SYSTEM` está definida.

### Passo 2 — Definir a tool de cálculo
Implemente uma tool `calculate` que recebe uma expressão matemática e retorna o resultado:

```python
def calculate(expression: str) -> str:
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception as e:
        return f"Error: {e}"

TOOLS = {"calculate": calculate}
```

**Checkpoint:** `calculate("2 + 3 * 4")` retorna `"14"`.

### Passo 3 — Parser de Action
Escreva uma função `parse_action(text)` que extrai o nome da tool e os argumentos da resposta do LLM usando regex:

```python
def parse_action(text):
    m = re.search(r"Action:\s*(\w+)\[(.*?)\]", text, re.DOTALL)
    if m:
        return m.group(1), m.group(2).strip()
    return None, None
```

**Checkpoint:** `parse_action("Action: calculate[2+2]")` retorna `("calculate", "2+2")`.

### Passo 4 — O agent loop
Implemente o loop principal que chama o LLM, faz parse da action, executa a tool e alimenta a observation de volta:

```python
def run(query, max_iters=10):
    messages = [{"role": "system", "content": SYSTEM},
                {"role": "user", "content": query}]
    for i in range(max_iters):
        resp = client.chat.completions.create(
            model="gpt-4o-mini", messages=messages, temperature=0)
        text = resp.choices[0].message.content
        print(f"--- Iter {i+1} ---\n{text}\n")
        if "Answer:" in text:
            return re.search(r"Answer:\s*(.*)", text, re.DOTALL).group(1)
        tool_name, args = parse_action(text)
        if tool_name in TOOLS:
            obs = TOOLS[tool_name](args)
        else:
            obs = f"Unknown tool: {tool_name}"
        messages.append({"role": "assistant", "content": text})
        messages.append({"role": "user", "content": f"Observation: {obs}"})
    return "Max iterations reached"
```

**Checkpoint:** `run("Quanto é 17 * 23 + 100?")` retorna `"491"`.

### Passo 5 — Logging estruturado
Adicione logging estruturado (JSON por iteração) com timestamp, iteração, thought, action, observation, tokens consumidos e latência:

```python
import time, json, datetime
def log_step(iteration, thought, action, observation, tokens, latency):
    entry = {"ts": datetime.datetime.now().isoformat(),
             "iter": iteration, "thought": thought,
             "action": action, "observation": observation,
             "tokens": tokens, "latency_ms": latency}
    print(json.dumps(entry, ensure_ascii=False))
```

**Checkpoint:** cada iteração produz uma linha JSON válida com todos os campos.

### Passo 6 — Salvando o trace
Ao final de cada execução, grave o log completo em `trace.jsonl` para inspeção posterior:

```python
with open("trace.jsonl", "a", encoding="utf-8") as f:
    for entry in trace_log:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
```

**Checkpoint:** `trace.jsonl` contém uma linha por iteração, legível por `jq`.

### Passo 7 — Teste de caso extremo
Teste com uma pergunta que **não** precisa de tool (ex.: "Qual a capital do Brasil?") e verifique se o agente responde direto sem chamar `calculate`.

**Checkpoint:** agente produz `Answer:` sem nenhuma `Action:` neste caso.

## Desafios extras
- Adicione uma segunda tool `search_wikipedia(query)` usando `wikipedia` package
- Implemente um limite de tokens por execução (orçamento) que interrompe o loop
- Adicione detecção de loop infinito (mesma action repetida 2x consecutivas)

## Entrega
- Repositório Git com `agent.py`, `README.md` e `trace.jsonl`
- Trace de exemplo com pelo menos 2 perguntas diferentes
- Commit no padrão `ETHAGT01: lab-1 implementar react-loop`

## Rubrica
Avaliado pela rubrica em `08-Assignments/ETHAGT01/assignment-01.md` (Pilar Comportamental 20%: colaboração em labs).
