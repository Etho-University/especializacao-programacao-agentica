# Supervisor Multi-Agente — Exemplo Mínimo

Supervisor coordena 3 workers especializados via tool calls.

## Como rodar

```bash
pip install openai python-dotenv
echo "LLM_API_KEY=sk-..." > .env
python main.py
```

## O que demonstra

- Topologia Supervisor (decisão centralizada)
- Workers especializados (pesquisa, cálculo, formatação)
- Tool calls como mecanismo de delegação
