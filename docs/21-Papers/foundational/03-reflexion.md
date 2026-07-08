# Reflexion: An Autonomous Agent with Dynamic Memory and Self-Reflection

> **Autores**: Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao  
> **Venue/Ano**: NeurIPS 2023 · arXiv:2303.11366  
> **URL**: https://arxiv.org/abs/2303.11366

## TL;DR
Reflexion adiciona auto-reflexão ao loop ReAct: o agente avalia sua saída, gera memória textual da reflexão, e usa essa memória em tentativas futuras para melhorar.

## Contribuições
- Loop de auto-melhoria via reflexão textual
- Memória episódica (reflections armazenados e reusados)
- Aplica-se a coding tasks (program synthesis), raciocínio e decisão

## Método
**Actor** (ReAct) → **Evaluator** (avalia saída) → **Reflection** (texto de auto-crítica) → armazena em **Memory** → próxima tentativa com reflexão no contexto.

## Resultados
- Program synthesis (HumanEval): 91% pass@1 com GPT-4 (vs 80% sem)
- AlfWorld (decisão interativa): 100% success rate em tarefas sequenciais
- HotpotQA (raciocínio): melhora significativa sobre ReAct

## Limitações
- Reflexão depende de critic externo (evaluator)
- Memória textual não escala bem (contexto longo)
- Não aprende parâmetros do modelo (só melhora prompting)

## Relação com a Especialização
**Fundamento de ETHAGT04 e ETHAGT05**. Base para o padrão Reflection Agent (`11-AgentPatterns/12-reflection.md`). Conceito de auto-melhoria transversal a ETHAGT12 e ETHAGT15.
