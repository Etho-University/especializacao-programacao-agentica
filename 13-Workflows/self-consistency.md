# Variação: Self-Consistency

## Intenção
Variação de **voting** que amostra N cadeias de raciocínio (temperatura alta) e faz **maioria** nas respostas finais. Reduz variância e melhora accuracy.

## Estrutura
```
input ─► (N amostras com temp alta) ─┬─► cadeia 1 ─► resposta 1
                                     ├─► cadeia 2 ─► resposta 2
                                     └─► cadeia N ─► resposta N
                                                            │
                                                            ▼
                                                    majority vote
```

## Quando usar
- Tarefas de raciocínio (matemática, lógica).
- Modelo é capaz mas variável.
- Custo extra compensa ganho.

## Quando evitar
- Tarefas subjetivas (sem resposta "certa").
- Volume alto com custo sensível.

## Custo
N× chamadas LLM. Tipicamente N=5 a 20.

## Referências
- Wang et al. *Self-Consistency Improves Chain of Thought Reasoning* (arXiv:2203.11171, ICLR 2023).
