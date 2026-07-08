# CoT vs ToT — Comparação

Compara Chain-of-Thought (raciocínio linear) com Tree of Thoughts (busca em árvore) no problema Game of 24.

## Como rodar

```bash
pip install openai python-dotenv
echo "LLM_API_KEY=sk-..." > .env
python main.py
```

## O que demonstra

- CoT: raciocínio passo a passo linear
- ToT: exploração de múltiplos caminhos com avaliação
- Trade-off: qualidade vs custo
