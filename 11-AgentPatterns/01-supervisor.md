# Supervisor

> Padrão 1/23 · Categoria A — Orquestração

## Intenção
Orquestrar workers especializados atuando como roteador via tool calls; o supervisor decide qual worker chamar a cada passo.

## Estrutura
`supervisor` LLM com tools = `call_worker(name, task)`. Workers são LLMs especializados.

## Quando usar
Tarefas com sub-especializações claras; quer controle centralizado.

## Anti-patterns
- Supervisor gargalo (todos os pedidos passam por ele)
- Workers redundantes

## Custo
1 chamada supervisor + 1 worker por passo.

## Referências
- LangGraph *Multi-Agent Supervisor* pattern
- ETHAGT10 — Topologias Multi-Agente
