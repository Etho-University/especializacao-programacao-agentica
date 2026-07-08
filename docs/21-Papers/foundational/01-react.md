# ReAct: Synergizing Reasoning and Acting in Language Models

> **Autores**: Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao  
> **Venue/Ano**: ICLR 2023 · arXiv:2210.03629  
> **URL**: https://arxiv.org/abs/2210.03629

## TL;DR
ReAct intercala **raciocínio** (thought) e **ação** (tool call) em um loop, permitindo que o LLM use ferramentas externas e raciocine sobre observações para resolver tarefas que requerem informação externa.

## Contribuições
- Paradigma de intercalar reasoning traces (thoughts) com ações (tool calls)
- Demonstra que ReAct supera CoT em tarefas factuais e raciocínio com ferramentas
- Estabelece o padrão canônico para agentes LLM

## Método
ReAct alterna: `Thought` (raciocínio em linguagem natural) → `Action` (tool call: ferramenta, argumentos) → `Observation` (resultado da ferramenta) → repetir até resposta final.

## Resultados
- HotpotQA: ReAct supera CoT em 15+ pontos
- Feverous (verificação de fatos): ReAct reduz alucinação vs CoT
- Decisões interativas (ALFWorld): ReAct alcança 88% success rate

## Limitações
- Loop pode ser longo (muitos passos)
- Sem planejamento explícito antes de agir
- Pode oscilar entre ações sem progresso

## Relação com a Especialização
**Fundamento de ETHAGT01** e base de todos os agentes implementados. Labs 1 e 2 são implementações ReAct do zero. Referência transversal a ETHAGT02-04, ETHAGT08.
