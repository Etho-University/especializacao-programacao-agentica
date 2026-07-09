---
password: Etho-Prof-2026
---
# 26 — Capstone

O **Projeto Final** da Especialização — integra todos os 16 módulos em uma plataforma realista. Aprovação com nota ≥ 4,0 por painel é **pré-requisito de certificação**.

## Projeto: Plataforma de Pesquisa Autônoma (AutoResearch)

Sistema multi-agente que, dada uma pergunta de pesquisa técnica, executa:

```
Planejar → Buscar (web, GitHub, arXiv, Confluence) → Recuperar (RAG agêntico)
   → Sintetizar → Criticar (evaluator-optimizer) → Revisar → Publicar relatório
```

## Características obrigatórias

- **Topologia**: Hierarchical + Orchestrator-Workers + Evaluator-Optimizer
- **MCP**: ≥ 3 servers customizados (ex.: arXiv, GitHub, Confluence)
- **Memória**: longo prazo (Postgres checkpointer + vector store + KG)
- **Event-driven**: paralelismo via NATS/Kafka
- **Guardrails + HITL** em checkpoints críticos
- **Observabilidade**: traces + eval automatizado com rubrica LLM-as-judge + benchmark de regressão
- **Eval report** completo (template `24-Templates/template-eval-report.md`)

## Entregáveis

1. Código (repositório com Docker)
2. Documentação: ADRs + diagramas C4 + README
3. Eval report (resultados em benchmark próprio)
4. Apresentação (25 min) + defesa Q&A (20 min) para painel ≥ 3 especialistas

## Avaliação

Ver `24-Templates/template-rubrica-avaliacao.md` (seção Capstone). Exige nota ≥ 4,0 em **todos** os pilares.

## Cronograma sugerido

- Semana 1-2: proposta + arquitetura (ADRs)
- Semana 3-6: implementação incremental
- Semana 7: eval + hardening
- Semana 8: defesa
