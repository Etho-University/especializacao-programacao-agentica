# ETHAGT01 — Gabarito

> Restrito a mentores. Cada resposta justificada com referência à apostila.

## Múltipla escolha

1. **b)** — O agent loop (raciocinar → agir → observar → repetir) é a unidade central do agente, conforme definido na Seção 1.1 da apostila ("Definição operacional").

2. **a)** — O Augmented LLM é composto de LLM + retrieval + tools + memory, conforme o bloco fundamental de Anthropic descrito no Capítulo 2 da apostila.

3. **b)** — Workflows orquestram LLMs e tools por caminhos de código predefinidos; agentes têm o LLM dirigindo dinamicamente seu próprio processo (Capítulo 4, Seção 4.1 — distinção canônica de Anthropic).

4. **b)** — ReAct pode entrar em loops infinitos, acumular custo e produzir alucinação em ação (Capítulo 3, Seção 3.4 — Limitações).

## Verdadeiro ou Falso (justificado)

1. **Falso.** A maioria das tarefas de LLM (resumir, traduzir, classificar) é melhor atendida por geração única ou workflows simples. Agentes trazem custo, latência e imprevisibilidade — só se justificam quando a tarefa exige decisão dinâmica e multi-etapas (Capítulo 1.1 e Capítulo 4.4).

2. **Verdadeiro.** A observação força o agente a raciocinar sobre o estado real do ambiente (*grounding*), reduzindo alucinação. É o mecanismo central que distingue ReAct de raciocínio puro (Capítulo 3.2 — "Por que funciona").

3. **Falso.** Adicionar ferramentas aumenta a superfície de decisão do LLM, podendo confundi-lo, aumentar custo (tokens de descrição) e gerar erros de seleção. Ferramentas devem ser adicionadas com propósito e testadas (Capítulo 2.3 e princípios de ACI do Capítulo 2).

4. **Falso.** A apostila recomenda observabilidade desde o dia 1 (Capítulo 6), pois sem logs estruturados e traces é impossível debugar loops, medir custo e iterar com confiança.

## Código curto

1. **Agent loop ReAct (esqueleto):**
```python
def agent_loop(task, max_iters=10):
    messages = [{"role": "user", "content": task}]
    for i in range(max_iters):
        response = llm_generate(messages)
        messages.append({"role": "assistant", "content": response})
        if "FINAL ANSWER:" in response:
            return response
        action = parse_action(response)
        result = execute_tool(action)
        observation = f"Observation: {result}"
        messages.append({"role": "user", "content": observation})
    return "Max iterations reached"
```
Referência: Capítulo 3.3 (Implementação mínima em Python puro).

2. **Log estruturado:**
```json
{
  "timestamp": "2026-07-08T10:30:00Z",
  "event_type": "action",
  "thought": "Preciso calcular o total",
  "action": "calculate",
  "args": {"expression": "150 + 230"},
  "observation": "380"
}
```
Referência: Capítulo 6.1 (Logging estruturado).

3. **Descrição de tool com ACI:**
```
calculate(expression: str) -> str
Avalia uma expressão matemática e retorna o resultado como string.
Use quando precisar de aritmética exata (o LLM pode errar em números grandes).

Formato da expressão: operandos e operadores com espaços.
Exemplos válidos: "2 + 2", "150 * 0.15", "sqrt(144)"
Exemplos inválidos: "2+2" (sem espaços), "calc 2 plus 2"

Retorna "ERROR: <motivo>" se a expressão for inválida.
```
Referência: Capítulo 2.4 (Interface bem documentada) e princípios ACI.

## Análise de trade-off

1. **Python puro vs framework:** Python puro oferece controle total, transparência e zero abstração oculta — ideal para aprender o mecanismo e para pipelines simples de produção. Frameworks (LangGraph) abstraem estado, retries e visualização — ideais quando há múltiplos nós, checkpointer e equipes grandes. Escolha puro quando a simplicidade é crítica ou quando precisa de controle fino; framework quando a complexidade do estado justifica (Capítulo 5).

2. **Responder direto vs. recuperar vs. buscar:** Fatores: (a) confiança do modelo no tópico — responder direto se factual e bem conhecido; (b) necessidade de informação atual — buscar se dados em tempo real; (c) privacidade — recuperar de base local se dados sensíveis; (d) custo/latência — responder direto é mais barato (Capítulo 2.2 — retrieval in-loop).

3. **Comece simples:** Complexidade prematura gera sistemas difíceis de debugar, com custo inesperado e baixa previsibilidade. Workflows simples resolvem a maioria dos casos; só migre para agentes quando houver evidência de que a flexibilidade é necessária (Capítulo 4.4 — escalada de complexidade).

## Debug / diagnóstico

1. **Problema:** Loop infinito — o agente repete a mesma ação sem alterar a estratégia. O grounding não está funcionando porque a observação não muda o raciocínio.
   **Correção 1:** Adicionar um limite de iterações (`max_iters`) e uma mensagem de falha estruturada.
   **Correção 2:** Incluir a observação no histórico e instruir o modelo a alterar a abordagem quando uma ação falha (ex.: reformular a query ou usar tool alternativa).
   Referência: Capítulo 3.4 e Capítulo 6.

2. **Hipóteses de causa raiz:**
   - **Histórico mal formatado:** a observação não está sendo incluída corretamente nas mensagens, então o modelo não "vê" o resultado.
   - **Prompt ambíguo:** as instruções não diferenciam claramente "ação necessária" de "ação já executada", levando o modelo a repetir.
   Referência: Capítulo 3.3 e 6.2.
