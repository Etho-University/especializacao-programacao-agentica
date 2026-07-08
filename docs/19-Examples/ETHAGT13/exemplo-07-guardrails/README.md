# Guardrails — Exemplo Mínimo

Implementa Guardian pattern: valida ações antes da execução.

## Como rodar

```bash
pip install openai python-dotenv
echo "LLM_API_KEY=sk-..." > .env
python main.py
```

## O que demonstra

- Guardian agent que aprova/rejeita ações
- Regras de segurança (não deletar, não executar código arbitrário)
- Log de veto e rastreabilidade
