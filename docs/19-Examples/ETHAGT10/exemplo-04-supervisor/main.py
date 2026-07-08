import json, os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("LLM_API_KEY"))
model = "gpt-4o-mini"

TOOLS = [
    {"type": "function", "function": {"name": "pesquisar", "description": "Busca informação factual", "parameters": {"type": "object", "properties": {"query": {"type": "string"}}, "required": ["query"]}}},
    {"type": "function", "function": {"name": "calcular", "description": "Executa cálculo", "parameters": {"type": "object", "properties": {"expr": {"type": "string"}}, "required": ["expr"]}}},
    {"type": "function", "function": {"name": "formatar", "description": "Formata resposta final", "parameters": {"type": "object", "properties": {"texto": {"type": "string"}}, "required": ["texto"]}}}
]

def pesquisar(query):
    dados = {"população SP": "11.5 milhões", "população RJ": "6.7 milhões", "população BH": "2.5 milhões"}
    return dados.get(query.lower(), f"Sem dados para: {query}")

def calcular(expr):
    allowed = set("0123456789+-*/.() ")
    return str(eval(expr, {"__builtins__": {}}, {})) if all(c in allowed for c in expr) else "Erro"

def formatar(texto):
    return f"=== RESULTADO ===\n{texto}\n================="

messages = [{"role": "system", "content": "Você é um supervisor. Delegue a tool certa e coordene até ter a resposta final."},
            {"role": "user", "content": "Qual a diferença populacional entre SP e RJ? E isso dividido por 2?"}]

for step in range(6):
    resp = client.chat.completions.create(model=model, messages=messages, tools=TOOLS, tool_choice="auto")
    msg = resp.choices[0].message
    messages.append(msg)
    if not msg.tool_calls:
        print(f"Resposta: {msg.content}"); break
    for tc in msg.tool_calls:
        args = json.loads(tc.function.arguments)
        fn = {"pesquisar": pesquisar, "calcular": calcular, "formatar": formatar}[tc.function.name]
        result = fn(**args)
        print(f"[{tc.function.name}] {args} -> {result}")
        messages.append({"role": "tool", "tool_call_id": tc.id, "content": str(result)})
