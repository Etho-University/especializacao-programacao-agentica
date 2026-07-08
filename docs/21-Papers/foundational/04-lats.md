# LATS: Language Agent Tree Search

> **Autores**: Andy Zhou, Kai Yan, Michal Shlapentokh-Rothman, Haohan Wang, Yu-Xiong Wang  
> **Venue/Ano**: ICLR 2024 · arXiv:2310.01757  
> **URL**: https://arxiv.org/abs/2310.01757

## TL;DR
LATS combina ToT (árvore) com aprendizado por reforço (MCTS): seleciona nós promissores, expande com múltiplas actions, simula/avalia, e backpropaga valores. Unifica raciocínio, planejamento e atuação.

## Contribuições
- Framework unificado que integra planejamento, raciocínio e atuação
- Adaptação do MCTS (Monte Carlo Tree Search) para agentes LLM
- Supera ReAct, ToT, Reflexion em tarefas complexas

## Método
**Selection**: UCT para escolher nó. **Expansion**: LLM gera N continuations. **Simulation**: rollouts rápidos. **Backpropagation**: atualiza valor. Loop até orçamento ou solução encontrada.

## Resultados
- Programming (HumanEval): success rate superior a Reflexion e ToT
- Web navigation (WebArena): melhorias significativas
- HotpotQA: supera ReAct e CoT-SC

## Limitações
- Custo computacional muito alto (N expansões × M simulações)
- UCT sensível a calibração
- Não adequado para tempo real

## Relação com a Especialização
**Fundamento de ETHAGT04** — LATS fecha a taxonomia de reasoning. Implementação prática coberta nos labs de planejamento. Topologia Tree of Agents (`10-Architecture/architectures/09-tree-of-agents.md`) inspirada em LATS.
