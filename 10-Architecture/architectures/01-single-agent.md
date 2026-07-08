# Single Agent

> Topologia 1/12 · ETHAGT01

## Descrição
Um único agente ReAct equipado com tools, operando em loop perceive → think → act → observe. É a unidade atômica de qualquer sistema agêntico — o Augmented LLM em sua forma mais pura.

## Estrutura
```
Input → [Augmented LLM: LLM + tools + memory] → Output
                ↑_______________|
```
- **1 agente**: decide, age, observa em loop
- **Tools**: conjunto de funções externas
- **Memory**: buffer de curto prazo (contexto) + persistência opcional

## Quando usar
- Baseline para qualquer problema
- Subtarefas únicas e bem definidas
- Prototipagem e validação inicial
- Quando a complexidade de múltiplos agentes não se justifica

## Quando evitar
- Especialização múltipla necessária
- Tarefas que exigem paralelismo real
- Sistemas com requisitos de escala vertical

## Trade-offs
| Prós | Contras |
|------|---------|
| Simples de implementar e debuggar | Capacidade limitada |
| Custo previsível (1 LLM por passo) | Sem paralelismo |
| Fácil de observabilizar | Gargalo cognitivo |

## Referências
- ETHAGT01 — Arquitetura Cognitiva de Agentes LLM
- Anthropic *Building Effective Agents* (Augmented LLM)
- ReAct: Yao et al. (arXiv:2210.03629)

## Diagramas relacionados
- `12-Diagrams/ETHAGT01/01-augmented-llm.mmd`
- `12-Diagrams/ETHAGT01/02-agent-loop.mmd`
