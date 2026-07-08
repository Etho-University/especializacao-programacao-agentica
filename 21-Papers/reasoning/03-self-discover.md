# Self-Discover: Large Language Models Self-Compose Reasoning Structures

> **Autores**: Pei Zhou, Jay Pujara, Xiang Ren, Xifeng Yan, Heng Ji, Yejin Choi  
> **Venue/Ano**: NeurIPS 2024 · arXiv:2402.03620  
> **URL**: https://arxiv.org/abs/2402.03620

## TL;DR
Self-Discover faz o LLM **descobrir** a estrutura de raciocínio ideal para cada problema, selecionando e compondo fragmentos de raciocínio (ex.: "break down", "critical evaluation") em vez de usar uma fixa.

## Contribuições
- Meta-raciocínio: o modelo descobre a estrutura de reasoning para cada problema
- Biblioteca de 39 fragmentos de raciocínio atômicos
- Supera CoT e ToT sem busca em árvore

## Método
**SELECT**: para o problema, selecionar fragmentos relevantes da biblioteca. **ADAPT**: adaptar fragmentos ao problema. **IMPLEMENT**: criar estrutura de raciocínio final. **SOLVE**: executar estrutura para resolver.

## Resultados
- 20+ datasets: Supera CoT, CoT-SC, e ToT
- Melhor que Zero-Shot-CoT em tarefas de math, logic, commonsense
- Eficiente (1-2 chamadas, sem busca)

## Limitações
- Biblioteca de fragmentos pode não conter o necessário
- Meta-etapa (discover) adiciona custo
- Estrutura descoberta pode ser sub-ótima

## Relação com a Especialização
**Referência para ETHAGT04**. Self-Discover representa o estado da arte em reasoning sem busca (tree search). Útil para cenários onde ToT/LATS são caros demais. Contrastado com inference-time reasoning (o1, Claude extended thinking).
