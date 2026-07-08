# Pipeline

> Topologia 6/12 · ETHAGT01, ETHAGT03

## Descrição
Agentes organizados em sequência fixa — a saída de um é a entrada do próximo. Cada agente é uma etapa especializada do processo.

## Estrutura
```
[A] → [B] → [C] → [D]
```
Cada etapa é um LLM com instrução específica.

## Quando usar
- Etapas bem definidas e imutáveis
- Ordem de processamento conhecida a priori
- Baixa variabilidade no fluxo
- Latência previsível

## Quando evitar
- Etapas dinâmicas (dependem do resultado)
- Necessita branching ou iteração
- Etapas podem pular ou repetir

## Trade-offs
| Prós | Contras |
|------|---------|
| Simples e previsível | Rígido |
| Fácil de debugar | Sem adaptação |
| Baixo custo de coordenação | Gargalo na etapa mais lenta |

## Referências
- ETHAGT01 — Arquitetura Cognitiva
- ETHAGT03 — Workflows & Planejamento
- Anthropic *Prompt Chaining* workflow

## Diagramas relacionados
- `12-Diagrams/ETHAGT03/01-prompt-chaining.mmd`
