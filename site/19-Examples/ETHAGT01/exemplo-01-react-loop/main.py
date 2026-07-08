import json, os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("LLM_API_KEY"))

TOOLS = [{
    "type": "function",
    "function": {
        "name": "calculator",
        "description": "Executa operação aritmética",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {"type": "number"},
                "b": {"type": "number"},
                "op": {"type": "string", "enum": ["+", "-", "*", "/"]}
            },
            "required": ["a", "b", "op"]
        }
    }
}]

def calculator(a, b, op):
    return {"+": a+b, "-": a-b, "*": a*b, "/": a/b if b else "erro"}[op]

messages = [{"role": "system", "content": "Você é um agente ReAct. Responda usando tools quando necessário."},
            {"role": "user", "content": "Quanto é 123 * 456 + 789?"}]

max_steps = 5
for step in range(max_steps):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=TOOLS,
        tool_choice="auto"
    )
    msg = response.choices[0].message
    messages.append(msg)

    if not msg.tool_calls:
        print(f"Resposta final: {msg.content}")
        break

    for tc in msg.tool_calls:
        args = json.loads(tc.function.arguments)
        result = calculator(**args)
        print(f"Passo {step}: {tc.function.name}({args}) = {result}")
        messages.append({
            "role": "tool",
            "tool_call_id": tc.id,
            "content": str(result)
        })
