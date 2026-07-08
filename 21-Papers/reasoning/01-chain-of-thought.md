# Chain-of-Thought Prompting Elicits Reasoning in Large Language Models

> **Autores**: Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc V. Le, Denny Zhou  
> **Venue/Ano**: NeurIPS 2022 · arXiv:2201.11903  
> **URL**: https://arxiv.org/abs/2201.11903

## TL;DR
CoT adiciona **raciocínio intermediário** (step-by-step) ao prompt few-shot, melhorando drasticamente a capacidade de raciocínio matemático, lógico e simbólico de LLMs.

## Contribuições
- Técnica de prompting que elicia raciocínio passo a passo
- Demonstra que scale + CoT melhora reasoning quadraticamente
- Base para técnicas derivadas: Self-Consistency, ToT, LATS

## Método
Fornecer exemplos few-shot com raciocínio intermediário explícito (ex.: "She had 5 maçãs. Comprou 3 → 5+3 = 8 → depois comeu 2 → 8-2 = 6"). Na inferência, o modelo gera cadeia de pensamento antes da resposta final.

## Resultados
- GSM8K: 58% (CoT) vs 18% (standard)
- SVAMP, MAWPS, ASDiv: melhorias de 15-30 pontos
- Benefício aumenta com scale (modelos maiores se beneficiam mais)

## Limitações
- Sensível a prompt (exemplos few-shot mal escritos degradam)
- Pode gerar raciocínio plausível mas errado
- Custo adicional (N tokens de reasoning tokens)

## Relação com a Especialização
**Base de ETHAGT04**. CoT é o ponto de partida de toda a taxonomia de reasoning. Todos os métodos seguintes (ToT, Reflexion, LATS) estendem CoT. Laboratório 1 de ETHAGT04 implementa CoT.
