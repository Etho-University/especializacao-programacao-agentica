import os, json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("LLM_API_KEY"))

SAFE_ACTIONS = ["search", "read", "calculate", "format"]
DANGEROUS_PATTERNS = ["delete", "DROP TABLE", "rm -rf", "exec(", "eval(", "import os"]

def guardian(proposed_action: dict) -> dict:
    action_type = proposed_action.get("type", "")
    params = json.dumps(proposed_action.get("params", {}))

    if action_type not in SAFE_ACTIONS:
        return {"approved": False, "reason": f"Ação '{action_type}' não está na whitelist"}
    for pattern in DANGEROUS_PATTERNS:
        if pattern in params:
            return {"approved": False, "reason": f"Parâmetro contém padrão perigoso: {pattern}"}

    judge = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "Você é um guardian. Responda JSON: {\"approved\": bool, \"reason\": str}. Rejeite ações destrutivas ou arriscadas."},
                  {"role": "user", "content": f"Ação: {json.dumps(proposed_action)}"}])
    return json.loads(judge.choices[0].message.content)

test_actions = [
    {"type": "search", "params": {"query": "agentes LLM"}},
    {"type": "delete", "params": {"path": "/data"}},
    {"type": "execute", "params": {"command": "rm -rf /"}},
    {"type": "calculate", "params": {"expression": "2+2"}},
    {"type": "search", "params": {"query": "DROP TABLE users"}},
]

for action in test_actions:
    result = guardian(action)
    status = "✅" if result["approved"] else "❌"
    print(f"{status} {action['type']}: {result['reason']}")
