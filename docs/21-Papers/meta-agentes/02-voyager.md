# Voyager: An Open-Ended Embodied Agent with Large Language Models

> **Autores**: Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, Anima Anandkumar  
> **Venue/Ano**: NeurIPS 2023 · arXiv:2305.16291  
> **URL**: https://arxiv.org/abs/2305.16291

## TL;DR
Voyager é um agente incorporado no Minecraft que **aprende e acumula skills automaticamente**, usando LLM para gerar código executável de habilidades e armazená-las em uma biblioteca de skills.

## Contribuições
- Ciclo completo de aprendizado autônomo: explorar → skill → biblioteca → reuso
- Biblioteca de skills com verificação de conflitos e similaridade
- Curriculum automático baseado em estado do jogo

## Método
**Curriculum**: LLM gera próximos objetivos baseado em estado atual e skills disponíveis. **Skill Library**: código gerado é indexado por embedding, verificado (sintaxe + semântica). **Iterative Prompting**: código é refinado até executar corretamente.

## Resultados
- Skills 3× mais diversas que baseline; 4× mais itens obtidos
- Agente melhora autonomamente sem intervenção humana
- Generaliza para novos cenários no Minecraft

## Limitações
- Depende de ambiente simulado com feedback claro
- Verificação de skills é ambiente-específica
- Risco de acumular skills incorretas

## Relação com a Especialização
**Fundamento de ETHAGT15 e ETHAGT16**. Voyager é o exemplo mais completo de meta-agente que evolui. Padrões Learning Agent e Strategy Evolver (`11-AgentPatterns/20-*, 19-*`) baseados em Voyager. Conceito de biblioteca de skills reusado no Capstone.
