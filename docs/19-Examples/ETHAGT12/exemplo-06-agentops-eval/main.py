import os, json, time
from openai import OpenAI

client = OpenAI(api_key=os.getenv("LLM_API_KEY"))

def run_agent(prompt: str, max_steps: int = 5) -> dict:
    messages = [{"role": "user", "content": prompt}]
    steps, total_cost, start = 0, 0, time.time()

    for _ in range(max_steps):
        t0 = time.time()
        resp = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
        latency = time.time() - t0
        cost = resp.usage.completion_tokens * 0.0000006 + resp.usage.prompt_tokens * 0.00000015
        total_cost += cost
        msg = resp.choices[0].message
        messages.append(msg)
        steps += 1
        if not msg.tool_calls:
            break

    return {
        "prompt": prompt,
        "response": msg.content,
        "steps": steps,
        "cost": round(total_cost, 5),
        "latency": round(time.time() - start, 2),
        "tokens": resp.usage.completion_tokens + resp.usage.prompt_tokens
    }

def evaluate_response(prompt, response):
    judge = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "Avalie a resposta em: correção (1-5), completude (1-5), clareza (1-5). Responda JSON."},
                  {"role": "user", "content": f"Pergunta: {prompt}\nResposta: {response}"}])
    return json.loads(judge.choices[0].message.content)

test_cases = [
    "Quanto é 2+2?",
    "Explique o que é um Augmented LLM em uma linha.",
    "Quem foi Alan Turing?"
]

for tc in test_cases:
    result = run_agent(tc)
    eval_result = evaluate_response(tc, result["response"])
    print(f"\nPrompt: {tc}")
    print(f"  Steps: {result['steps']}, Custo: ${result['cost']}, Latência: {result['latency']}s")
    print(f"  Avaliação: {eval_result}")
