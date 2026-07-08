# AgentOps — Eval de Agente

Mede sucesso, custo e latência de um agente simples.

## Como rodar

```bash
pip install openai python-dotenv
echo "LLM_API_KEY=sk-..." > .env
python main.py
```

## O que demonstra

- Traces de execução (passos, custo, latência)
- LLM-as-judge para avaliar qualidade
- Eval report simplificado
