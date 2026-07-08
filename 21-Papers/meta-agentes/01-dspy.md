# DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines

> **Autores**: Omar Khattab, Arnav Singhvi, Paridhi Maheshwari, Zhiyuan Zhang, Keshav Santhanam, Sri Vardhamanan, Saiful Haq, Ashutosh Sharma, Thomas T. Liu, Bryan Tower, Mahir Labib, Ioannis Patras, Matei Zaharia, Christopher Potts, Percy Liang, Dan Roth, Carlos Guestrin  
> **Venue/Ano**: EMNLP 2024 · arXiv:2310.03714  
> **URL**: https://arxiv.org/abs/2310.03714

## TL;DR
DSPy desacopla **programas** (pipelines de LLM) de **parâmetros** (prompts/few-shot), permitindo otimização automática via compiladores (BootstrapFewShot, MIPRO).

## Contribuições
- Paradigma de programação para LLMs separando programa de parâmetros
- Compiladores automáticos que otimizam prompts/few-shot para métricas
- Reuso de módulos (ChainOfThought, ReAct, Retrieve) como building blocks

## Método
**Programa**: grafo de módulos (dspy.ChainOfThought, dspy.ReAct). **Parâmetros**: few-shot examples, instruções. **Compilador**: otimiza parâmetros para maximizar métrica (accuracy, F1) em dataset de validação.

## Resultados
- Supera few-shot manual em 10+ tarefas (QA, reasoning, classification)
- Compilação reduz sensibilidade a prompt engineering
- Generaliza entre modelos (GPT-4, Llama, Mistral)

## Limitações
- Requer dataset de validação com ground truth
- Compilação pode ser cara (muitas chamadas)
- Debugging de programas compilados é difícil

## Relação com a Especialização
**Fundamento de ETHAGT15** (Meta-Agentes). DSPy é o framework central para meta-programação de agentes. Padrão Strategy Evolver (`11-AgentPatterns/19-strategy-evolver.md`) implementa conceito similar. Laboratório de ETHAGT15 usa DSPy.
