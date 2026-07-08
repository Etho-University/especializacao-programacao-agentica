# Tree of Thoughts: Deliberate Problem Solving with Large Language Models

> **Autores**: Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, Karthik Narasimhan  
> **Venue/Ano**: NeurIPS 2023 · arXiv:2305.10601  
> **URL**: https://arxiv.org/abs/2305.10601

## TL;DR
ToT generaliza CoT permitindo exploração em árvore: múltiplos caminhos de raciocínio são explorados, avaliados e podados, com busca BFS/DFS.

## Contribuições
- Framework de raciocínio com busca em árvore (BFS/DFS) para LLMs
- Avaliação intermediária de "thoughts" com prompting ou valor numérico
- Supera CoT e ReAct em tarefas que exigem exploração planejada

## Método
Cada nó = parcial thought. **Avaliador** (LLM) pontua o nó. **Buscador** (BFS/DFS) expande nós promissores e poda fracos. Alternativas: avaliar por prompt ("sure/likely/impossible") ou por valor (escala 1-10).

## Resultados
- Game of 24: ToT resolve 74% vs 4% do CoT
- Crossword: ToT supera ReAct em 30+ pontos
- Creative writing: ToT produz textos melhores avaliados por humano

## Limitações
- Custo muito alto (N× chamadas por problema)
- Não escala para problemas muito abertos
- Critério de avaliação intermediária é frágil

## Relação com a Especialização
**Fundamento de ETHAGT04** (Reasoning & Planning). LATS (ETHAGT04) expande ToT adicionando aprendizado por reforço. Taxonomia completa de reasoning abordada no módulo.
