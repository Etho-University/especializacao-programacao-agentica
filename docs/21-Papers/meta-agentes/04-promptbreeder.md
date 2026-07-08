# Promptbreeder: Self-Referential Self-Improvement via Prompt Evolution

> **Autores**: Chrisantha Fernando, Dylan Banarse, Henryk Michalewski, Simon Osindero, Tim Rocktäschel  
> **Venue/Ano**: arXiv, Setembro 2023 · arXiv:2309.16797  
> **URL**: https://arxiv.org/abs/2309.16797

## TL;DR
Promptbreeder aplica **algoritmos evolucionários** para evoluir prompts: mutate, crossover, evaluate, select — o prompt "muta" para melhorar performance na tarefa.

## Contribuições
- Evolução automática de prompts sem intervenção humana
- Operadores de mutação (pensar, brainstorming, zero-shot chain-of-thought)
- *Prompt Mutation Prompt*: LLM sugere como mutar prompts

## Método
População inicial de prompts → avaliar performance → selecionar top-k → aplicar mutações → crossover → nova geração. Mutações incluem: "give a bad example", "think step by step", etc.

## Resultados
- Supera prompts escritos por humanos em diversas tarefas
- MELBA (mathematical reasoning): melhora de 20+ pontos vs hand-crafted
- Generaliza entre modelos (GPT-3, GPT-4, Llama)

## Limitações
- Custo alto (muitas gerações para evoluir)
- Pode convergir para prompt super-específico que não generaliza
- Sem garantia de monotonicidade

## Relação com a Especialização
**Referência para ETHAGT15**. Promptbreeder é o exemplo mais puro de meta-agente (LLM otimiza LLM). Padrão Strategy Evolver (`11-AgentPatterns/19-strategy-evolver.md`) usa algoritmo similar. Contrastado com DSPy (otimização por compilação vs evolução).
