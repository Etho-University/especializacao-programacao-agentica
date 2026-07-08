# Building Effective Agents (Anthropic)

> **Autores**: Erik Schluntz, Ben Packer, et al. (Anthropic)  
> **Venue/Ano**: Anthropic Engineering Blog, Dezembro 2024  
> **URL**: https://docs.anthropic.com/en/docs/build-with-claude/agentic

## TL;DR
Guia prático da Anthropic sobre quando e como construir agentes. Define workflow (código orquestra LLMs) vs agente (LLM dirige o processo). Apresenta Augmented LLM como bloco fundamental e 5 workflows canônicos.

## Contribuições
- Distinção clara workflow vs agente (a definição mais citada do campo)
- Framework Augmented LLM (LLM + retrieval + tools + memory)
- 5 workflows canônicos: Prompt Chaining, Routing, Parallelization, Orchestrator-Workers, Evaluator-Optimizer

## Método
Abordagem prática baseada em experiências de produção na Anthropic (Block, Notion, Discord, etc). Recomenda: começar simples, medir, aumentar complexidade só quando necessário.

## Resultados
- Principio "menos é mais" para agentes — a maioria dos problemas resolve com workflow
- Casos de produção documentados (Block, Notion, Discord)

## Limitações
- Não cobre topologias multi-agente avançadas (hierarchical, mesh)
- Foco em Claude, mas princípios são gerais
- Ausência de métricas quantitativas de sucesso

## Relação com a Especialização
**Base de ETHAGT01 e ETHAGT03**. A definição workflow vs agente é usada em toda a Especialização. Os 5 workflows são implementados nos labs. Princípio "menos é mais" é ênfase transversal.
