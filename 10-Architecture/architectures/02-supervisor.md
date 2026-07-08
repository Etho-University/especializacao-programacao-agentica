# Supervisor

> Topologia 2/12 · ETHAGT10

## Descrição
Um supervisor central coordena workers especializados, decidindo qual chamar a cada passo via tool calls. O supervisor roteia, não executa conteúdo.

## Estrutura
```
                 [Supervisor LLM]
                /        |        \
        Worker A    Worker B    Worker C
```
- **Supervisor**: LLM com tools = `call_worker(name, task)`
- **Workers**: LLMs especializados (ou pipelines)

## Quando usar
- Sub-especializações claras (ex.: código, revisão, teste)
- Controle centralizado desejado
- Até ~10 workers

## Quando evitar
- Muitos workers (>10)
- Concorrência alta necessária
- Trabalho predominantemente criativo (supervisor pode limitar)

## Trade-offs
| Prós | Contras |
|------|---------|
| Controle centralizado forte | Supervisor é gargalo e SPOF |
| Decisão explícita visível | Custo: 1 chamada supervisor + 1 worker por passo |
| Fácil de auditar | Latência serial |

## Referências
- ETHAGT10 — Topologias Multi-Agente
- LangGraph *Supervisor* pattern

## Diagramas relacionados
- `12-Diagrams/ETHAGT10/01-supervisor.mmd`
