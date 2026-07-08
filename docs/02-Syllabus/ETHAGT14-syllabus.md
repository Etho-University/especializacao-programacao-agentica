# `ETHAGT14` — Escalabilidade & Sistemas Distribuídos de Agentes

> Fase D · Carga 30 h · Versão 1.0 · Julho 2026

## 1. Identificação

| Campo | Valor |
|---|---|
| Código | `ETHAGT14` |
| Título | Escalabilidade & Sistemas Distribuídos de Agentes |
| Fase interna | D |
| Carga horária | 30 h |
| Pré-requisitos | `ETHAGT11` |
| Módulos que dependem deste | `ETHAGT90` |

## 2. Objetivos

**Objetivo geral**: Levar sistemas de agentes a **escala de produção**, dominando distribuição, custo, latência, caching e FinOps de agentes.

**Objetivos específicos**:
1. Identificar gargalos em sistemas multi-agente (LLM, tools, memória, rede).
2. Aplicar caching (semântico, de prompts, de embeddings).
3. Distribuir agentes (sharding, replica, partitioning).
4. Otimizar custo e latência (model routing, batching, speculative).
5. Operar FinOps de agentes (orçamento, observabilidade de custo).

## 3. Competências desenvolvidas

| Competência | Nível ao final |
|---|---|
| C1 Programação Agêntica | **A** |
| C2 Multi-Agent Systems | **A** |
| C3 MCP & Tool Use | B |
| C4 Agent Memory | **A** |
| C5 AgentOps & Avaliação | **A** |

## 4. Conteúdo programático

### Unidade 1 — Onde agentes esbarram em escala (4 h)
- Latência de LLM como gargalo dominante
- Custo crescendo com contexto
- Concorrência e rate limits
- Estado distribuído

### Unidade 2 — Caching (5 h)
- Cache de prompts/exact match
- Cache semântico (similaridade de embedding)
- Cache de embeddings
- Cache de tool results
- Invalidade e consistência

### Unidade 3 — Model routing e otimização (5 h)
- Roteamento por complexidade (Haiku vs Sonnet)
- Batching de requests
- Speculative decoding / prediction
- Streaming para latência percebida
- Distilação e fine-tuning (panorama)

### Unidade 4 — Distribuição (5 h)
- Stateless vs stateful workers
- Sharding por usuário/sessão/domínio
- Replica e balanceamento
- Coordenação (consensus, leader election)

### Unidade 5 — Infraestrutura (5 h)
- Kubernetes para agentes
- Serverless vs dedicado
- GPUs para inferência local (opcional)
- Service mesh
- Custo de infra

### Unidade 6 — FinOps de agentes (6 h)
- Orçamento por execução, por usuário, por tenant
- Medição granular de custo (por step, por tool)
- Otimização contínua
- Trade-offs custo-latência-qualidade
- Pricing para clientes (se aplicável)

## 5. Bibliografia

### Fundamental
- Kleppmann, M. *Designing Data-Intensive Applications*.
- Richards, M. & Ford, N. *Fundamentals of Software Architecture*.
- Cloud provider docs (Anthropic, OpenAI, Bedrock, Vertex).

### Complementar
- *FinOps for ML/AI* (FinOps Foundation).
- Litellm docs (roteamento e custo).

## 6. Papers / docs canônicos

- *Serving LLMs* (vLLM, TGI)
- *Speculative Decoding* (arXiv:2211.17192)
- Kleppmann capítulos relevantes

## 7. Laboratórios

- **Lab 1** (4 h): "Cache semântico". Adicionar cache semântico a um agente; medir redução de custo/latência.
- **Lab 2** (5 h): "Sharding por tenant". Distribuir agente multi-tenant com isolamento.

## 8. Projeto do módulo

**Descrição**: otimizar custo/latência de um sistema agêntico existente em ≥40% sem perder qualidade mensurável.
**Entrega**: antes/depois + ADR de otimizações + FinOps dashboard.
**Critério de sucesso**: redução ≥40% em custo ou latência com success rate mantido (±2%).

## 9. Exercícios

1. Quando cache semântico falha?
2. Roteamento por complexidade: como medir?
3. Stateless é sempre preferível? Justifique.
4. Escreva um orçamento por execução com circuit breaker.
5. Verdadeiro/falso: "Streaming reduz latência total."

## 10. Avaliação

| Pilar | Peso | Instrumento |
|---|---|---|
| Técnico | 40% | Projeto + FinOps report |
| Consultivo | 30% | Defesa do ADR para "CTO" |
| Comportamental | 20% | Code review |
| Prático | 10% | Demo: antes/depois |

**Nota mínima**: 3,0.

## 11. Slides

- Slides: `03-Slides/ETHAGT14-slides.md` (~85 slides).

## 12. Leitura complementar

- Kleppmann; FinOps Foundation; vLLM.

## 13. Ferramentas

- Kubernetes, Redis, LiteLLM, OpenTelemetry, Grafana.

## 14. Diagramas

- Diagramas: `12-Diagrams/ETHAGT14/` — bottleneck-analysis.mmd, sharding.mmd, finops-flow.mmd.

## 15. Estudo de caso

- escalabilidade em assistentes de empresa (milhares de usuários).

## 16. Ficha de pesquisa

- Ficha: `20-Research/ETHAGT14-pesquisa.md`.

---

*Mantido por: Universidade Etho · Versão 1.0 · Julho 2026*
