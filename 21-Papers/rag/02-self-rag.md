# Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

> **Autores**: Akari Asai, Zeqiu Wu, Yizhong Wang, Avirup Sil, Hannaneh Hajishirzi  
> **Venue/Ano**: ICLR 2024 · arXiv:2310.11511  
> **URL**: https://arxiv.org/abs/2310.11511

## TL;DR
Self-RAG treina o LLM a gerar **tokens especiais de reflexão** que indicam: (1) se precisa recuperar, (2) se os retrieved docs são relevantes, (3) se a geração é suportada pelos docs.

## Contribuições
- Decisão *on-demand*: o modelo decide quando recuperar (não toda query)
- Auto-crítica: o modelo avalia retrieved docs e sua própria geração
- Critic: avaliador treinado por regressão (Reward Model)

## Método
LLM treinado com tokens especiais: `Retrieve` (sim/não), `IsRel` (doc relevante), `IsSup` (geração suportada), `IsUse` (geração útil). Durante inferência: recupera só quando `Retrieve=sim`, gera, critica, e escolhe a melhor segment-level generation.

## Resultados
- Open-domain QA, reasoning, fact verification, e generation tasks
- Supera RAG original e CoT em facticidade e qualidade
- Reduz recuperações desnecessárias (custo menor que RAG fixo)

## Limitações
- Requer fine-tuning com dados anotados (tokens especiais)
- Crítica é limitada a tokens pré-definidos
- Não itera (recupera uma vez)

## Relação com a Especialização
**Fundamento de ETHAGT06**. Self-RAG é ponto de partida para RAG agêntico: a decisão "recuperar ou não" é o primeiro passo de autonomia. Padrões `15-RAG/` cobrem Self-RAG em contraste com CRAG e Adaptive RAG.
