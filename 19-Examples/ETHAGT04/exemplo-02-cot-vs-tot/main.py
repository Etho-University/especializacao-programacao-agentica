import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("LLM_API_KEY"))
model = "gpt-4o-mini"

problem = "Use 3, 5, 7, 8 para fazer 24 usando +, -, *, /"

def cot_solve(problem):
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": f"Pense passo a passo: {problem}. Responda com a expressão final."}])
    return resp.choices[0].message.content

def tot_solve(problem, breadth=3, depth=3):
    candidates = [problem]
    for _ in range(depth):
        new_candidates = []
        for c in candidates:
            resp = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": f"Para o problema '{c}', gere {breadth} abordagens possíveis. Liste apenas as expressões."}])
            lines = resp.choices[0].message.content.strip().split("\n")
            new_candidates.extend(lines[:breadth])
        eval_resp = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": f"Destas opções: {new_candidates}, qual é a mais promissora para obter 24? Responda só com a melhor expressão."}])
        candidates = [eval_resp.choices[0].message.content]

    final = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": f"A expressão final para {problem} é: {candidates[0]}. Isso dá 24? Responda SIM e a expressão, ou NÃO."}])
    return final.choices[0].message.content

print(f"Problema: {problem}\n")
print(f"[CoT] {cot_solve(problem)}")
print(f"[ToT] {tot_solve(problem)}")
