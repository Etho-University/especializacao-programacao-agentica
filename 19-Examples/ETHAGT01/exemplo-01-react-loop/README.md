# ReAct Loop — Exemplo Mínimo

Demonstra o agent loop ReAct (Thought → Action → Observation) em ~50 linhas de Python puro.

## Como rodar

```bash
pip install openai python-dotenv
echo "LLM_API_KEY=sk-..." > .env
python main.py
```

## O que demonstra

- Ciclo perceive → think → act → observe
- Tool use sem framework
- Loop controlado por `max_steps`
