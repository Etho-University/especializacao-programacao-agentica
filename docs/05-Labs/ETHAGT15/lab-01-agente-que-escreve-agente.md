# ETHAGT15 — Lab 1: Agente que escreve agente

> Curso: Meta-Agentes & Sistemas Autoaprendentes · Carga: 15h · Pré-req: ETHAGT10

## Objetivo
Construir um meta-agente que, dada uma descrição de tarefa, gera automaticamente um agente especializado (prompt + tools + configuração) e o avalia em um benchmark antes de "deployar".

## Preparação
- Ambiente: Python 3.11+, `pip install openai pydantic`, `.env` com API key
- Dados/recursos: 3 descrições de tarefas em `task_specs.json`
- Leitura prévia: Apostila ETHAGT15, Unidade 1 (Meta-agência) e Unidade 2 (Geração de agentes)

## Roteiro
### Passo 1 — Definir a especificação de tarefa
Modele a entrada do meta-agente — uma descrição da tarefa desejada:

```python
class TaskSpec(BaseModel):
    name: str
    description: str
    domain: str  # ex: "customer_support", "code_review", "data_analysis"
    example_inputs: list[str]
    success_criteria: str
    available_tools_description: str  # descrição das tools que o agente pode usar

TASK_SPECS = [
    TaskSpec(name="ticket-classifier", description="Classify support tickets by urgency",
             domain="customer_support",
             example_inputs=["App crashed during checkout", "How do I change my password?"],
             success_criteria="Correct urgency label (low/medium/high/critical)",
             available_tools_description="search_kb(query): search knowledge base"),
    # ... 2 specs a mais
]
```

**Checkpoint:** 3 specs de tarefa definidas com exemplos e critérios.

### Passo 2 — O meta-agente (gerador)
O meta-agente recebe uma spec e produz a configuração de um agente:

```python
class GeneratedAgent(BaseModel):
    name: str
    system_prompt: str
    tools_config: dict  # nome → descrição + quando usar
    reasoning_strategy: str  # "react", "plan_execute", "direct"
    max_steps: int

def meta_agent_generate(spec: TaskSpec) -> GeneratedAgent:
    prompt = f"""You are a meta-agent. Design an AI agent for this task.

    Task: {spec.description}
    Domain: {spec.domain}
    Available tools: {spec.available_tools_description}
    Success criteria: {spec.success_criteria}
    Example inputs: {spec.example_inputs}

    Produce a JSON with:
    - name: short name for the agent
    - system_prompt: complete system prompt with instructions
    - tools_config: which tools to enable and when to use them
    - reasoning_strategy: react | plan_execute | direct
    - max_steps: max agent loop iterations

    Output ONLY valid JSON."""
    response = call_llm(prompt, model="gpt-4o", temperature=0.3)
    return GeneratedAgent(**json.loads(response))
```

**Checkpoint:** meta-agente produz `GeneratedAgent` válido para cada spec.

### Passo 3 — Instanciar o agente gerado
Construa um agente funcional a partir da configuração gerada:

```python
def instantiate_agent(config: GeneratedAgent):
    """Cria um agente executável a partir da configuração gerada."""
    def run(input_text):
        messages = [
            {"role": "system", "content": config.system_prompt},
            {"role": "user", "content": input_text}
        ]
        for step in range(config.max_steps):
            response = call_llm_with_tools(messages, tools_config=config.tools_config)
            messages.append(response)
            if response.is_final:
                return response.content
        return "Max steps reached"
    return run
```

**Checkpoint:** agente gerado executa e produz respostas para os inputs de exemplo.

### Passo 4 — Avaliar o agente gerado
Crie um eval rápido para validar o agente antes do "deploy":

```python
def evaluate_generated_agent(agent_fn, spec: TaskSpec, n_tests=5):
    results = []
    for i in range(n_tests):
        test_input = spec.example_inputs[i % len(spec.example_inputs)]
        output = agent_fn(test_input)
        # LLM-as-judge baseado no success_criteria
        score = llm_judge(output, spec.success_criteria)
        results.append({"input": test_input, "output": output, "passed": score})
    accuracy = sum(r["passed"] for r in results) / len(results)
    return accuracy, results
```

**Checkpoint:** agente gerado é avaliado com accuracy mensurável.

### Passo 5 — Loop de geração + avaliação
Gere, avalie e itere se a qualidade não for suficiente:

```python
def generate_and_evaluate(spec: TaskSpec, min_accuracy=0.7, max_attempts=3):
    for attempt in range(max_attempts):
        print(f"Generation attempt {attempt+1}")
        config = meta_agent_generate(spec)
        agent_fn = instantiate_agent(config)
        accuracy, results = evaluate_generated_agent(agent_fn, spec)

        print(f"  Accuracy: {accuracy:.0%}")
        if accuracy >= min_accuracy:
            print("  ✓ Agent approved!")
            return config, accuracy, results
        else:
            print("  ✗ Below threshold, regenerating...")

    return config, accuracy, results  # retorna melhor esforço
```

**Checkpoint:** loop gera, avalia e itera até atingir threshold ou max_attempts.

### Passo 6 — Executar para 3 tarefas
Rode o meta-agente para as 3 specs:

```python
for spec in TASK_SPECS:
    config, accuracy, results = generate_and_evaluate(spec)
    print(f"{spec.name}: accuracy={accuracy:.0%}")
    save_agent_config(config, f"generated_agents/{spec.name}.json")
```

| Tarefa | Tentativas | Accuracy final | Strategy |
|---|---|---|---|
| ticket-classifier | | | |
| code-reviewer | | | |
| data-analyst | | | |

**Checkpoint:** 3 agentes gerados, avaliados e salvos.

### Passo 7 — Sandbox de segurança
Antes de usar um agente gerado, valide-o em sandbox:

```python
def sandbox_validate(config: GeneratedAgent):
    """Verifica que o agente gerado não é perigoso."""
    # 1. Não deve ter tools não permitidas
    for tool_name in config.tools_config:
        if tool_name not in ALLOWED_TOOLS:
            return False, f"Disallowed tool: {tool_name}"
    # 2. System prompt não deve conter instruções perigosas
    dangerous_patterns = ["ignore all", "delete", "rm -rf", "exfiltrate"]
    for pattern in dangerous_patterns:
        if pattern in config.system_prompt.lower():
            return False, f"Dangerous pattern in prompt: {pattern}"
    return True, "passed"
```

**Checkpoint:** sandbox valida agentes gerados antes do uso.

### Passo 8 — Análise crítica
Documente reflexões sobre o processo:

```markdown
## Análise
1. Quais tarefas o meta-agente gerou bons agentes? Quais não?
2. A qualidade do system prompt gerado é comparável a um humano?
3. O loop de iteração melhora significativamente?
4. Quais os riscos de "deployar" agentes gerados automaticamente?
```

**Checkpoint:** análise crítica em `meta_agent_analysis.md`.

## Desafios extras
- Adicione meta-otimização: usar o feedback do eval para melhorar o prompt do meta-agente
- Permita que o meta-agente gere tools customizadas (não só selecionar existentes)
- Compare agentes gerados vs agentes escritos manualmente por humanos
- Adicione um meta-governor que pode vetar agentes gerados perigosos

## Entrega
- Repositório com `meta_agent.py`, `generated_agents/`, `eval_results.md`, `meta_agent_analysis.md`
- Commit no padrão `ETHAGT15: lab-1 implementar meta-agente gerador`

## Rubrica
Avaliado pela rubrica em `08-Assignments/ETHAGT15/assignment-01.md` (Pilar Comportamental 20%: colaboração em labs).
