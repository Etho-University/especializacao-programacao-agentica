# ETHAGT14 — Roteiro da Apresentação

> Universidade Etho · Especialização em Programação Agêntica
> Fase D — Sistemas Distribuídos · 30 h

---

## Metadados

| Campo | Valor |
|---|---|
| Código | ETHAGT14 |
| Título | Escalabilidade & Sistemas Distribuídos de Agentes |
| Duração | 90 min (2 blocos de 45 min) |
| Total de slides | 75 |
| Competências | C1 (A), C2 (A), C3 (B), C4 (A), C5 (A) |
| Pré-requisitos | ETHAGT11 |
| Fontes canônicas | Kleppmann *Designing Data-Intensive Applications*; Richards & Ford *Fundamentals of Software Architecture*; FinOps Foundation *FinOps for ML/AI*; Speculative Decoding (arXiv:2211.17192) |

---

## Fluxo da Aula

### BLOCO 1 — 45 min

| Seção | Slides | Tempo | Objetivo |
|---|---|---|---|
| A — Abertura | 1-6 | 8 min | Engajar, contextualizar custo da escala, objetivos |
| B — Gargalos de Escala | 7-14 | 10 min | Latência, custo de contexto, rate limits, estado, bottleneck |
| C — Caching | 15-29 | 22 min | Exact, semântico, embeddings, tools, invalidação, DEMO |
| Intervalo | — | 5 min | — |

### BLOCO 2 — 45 min

| Seção | Slides | Tempo | Objetivo |
|---|---|---|---|
| D — Model Routing & Otimização | 30-39 | 12 min | Haiku/Sonnet/Opus, batching, speculative, streaming |
| E — Distribuição | 40-48 | 10 min | Stateless, sharding, replica, balanceamento, consensus |
| F — Infraestrutura | 49-53 | 5 min | K8s, serverless, GPU, service mesh, custo total |
| G — FinOps | 54-62 | 8 min | Orçamento, medição, trade-offs, circuit breaker |
| H — Fechamento | 63-75 | 10 min | Boas práticas, anti-patterns, caso, quiz, Q&A |

---

## Pontos de Engajamento

| Slide | Tipo | Interação |
|---|---|---|
| 5 | Mão levantada | "Qual o maior custo oculto que já viram em LLMs?" |
| 14 | Discussão aberta | Maior custo oculto em produção |
| 20 | Duplas (2 min) | Threshold ideal do cache semântico |
| 26 | DEMO ao vivo | Cache semântico — antes/depois |
| 29 | Votação | 5 cenários: cache semântico falha? |
| 38 | Discussão aberta | "Se tivesse 1 semana, por onde começar?" |
| 39 | Votação | 6 tarefas: qual modelo? |
| 47 | Duplas (2 min) | Stateless é sempre preferível? |
| 62 | Duplas (3 min) | Circuit breaker de custo |
| 69-71 | Quiz individual | 3 perguntas de múltipla escolha |
| 72 | Grupo | 4 perguntas de discussão profunda |

---

## Materiais Necessários

- [ ] Projetor / tela de compartilhamento
- [ ] VS Code aberto com `05-Labs/ETHAGT14/Lab1-Cache-Semantico/main.py`
- [ ] Terminal com Python 3.11+, Redis local e `OPENAI_API_KEY` / `ANTHROPIC_API_KEY` configuradas
- [ ] Acesso ao repositório da especialização
- [ ] Quadro branco (para diagramas improvisados de sharding / FinOps)
- [ ] Dashboard Grafana mockup (Slide 59) — screenshot salva como plano B
- [ ] Handout: storyboard impresso (opcional)

---

## Riscos e Planos B

| Risco | Plano B |
|---|---|
| Redis indisponível na DEMO do cache semântico (Slide 26) | Mostrar before/after pré-gravado (screenshot) |
| API LLM excede rate limit durante a DEMO | Pré-popular cache e mostrar hit path apenas |
| Alunos sem background de K8s | Direcionar para ETHAGT11; focar em conceitos, não manifests |
| Tempo estourado no Bloco 1 | Cortar exercício do Slide 29; mover para homework |
| Tempo estourado no Bloco 2 | Reduzir quiz para 2 perguntas; referências como leitura |
| Discussão sobre pricing (Slide 60) drena tempo | Tabelar; prometer seguimento no Slack |

---

## Avaliação da Aula

- Quiz ao final (Slides 69-71): ≥2 acertos = compreensão básica
- Exercício de routing (Slide 39): votação rápida com feedback imediato
- Exercício de circuit breaker (Slide 62): discussão em duplas
- Perguntas de discussão (Slide 72): profundidade das respostas
- Feedback informal: "Qual otimização você vai aplicar no seu sistema primeiro?"
