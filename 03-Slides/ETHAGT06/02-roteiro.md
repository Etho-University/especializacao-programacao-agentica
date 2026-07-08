# ETHAGT06 — Roteiro da Apresentação

> Universidade Etho · Especialização em Programação Agêntica
> Fase B — RAG Avançado · 30 h

---

## Metadados

| Campo | Valor |
|---|---|
| Código | ETHAGT06 |
| Título | RAG Agêntico (Adaptive · Corrective · Self-RAG · Agentic) |
| Duração | 110 min (2 blocos de ~55 min + intervalo) |
| Total de slides | 85 |
| Competências | C1 (A), C3 (B), C4 (I), C5 (I) |
| Fontes canônicas | Lewis et al. *RAG* (arXiv:2005.11401); Asai *Self-RAG* (arXiv:2310.11511); Yan *CRAG* (arXiv:2401.15884); Edge *GraphRAG* (arXiv:2404.16130) |
| Pré-requisitos | ETHAGT04 (RAG Systems do Framework Etho recomendado) |

---

## Fluxo da Aula

### BLOCO 1 — ~58 min

| Seção | Slides | Tempo | Objetivo |
|---|---|---|---|
| A — Abertura | 1-7 | 8 min | Engajar, contextualizar e estabelecer objetivos |
| B — RAG Ingênuo Falha | 8-14 | 10 min | Diagnosticar 4 classes de falha e o mito do vector DB |
| C — Adaptive RAG | 15-23 | 12 min | Decidir quando/quanto recuperar + routing |
| D — Corrective RAG | 24-34 | 15 min | Avaliar relevância, 3 caminhos, web fallback |
| E — Self-RAG | 35-44 | 13 min | Reflexão sobre docs e resposta, tokens de reflexão |
| Intervalo | — | 5 min | — |

### BLOCO 2 — ~52 min

| Seção | Slides | Tempo | Objetivo |
|---|---|---|---|
| F — Agentic RAG | 45-55 | 15 min | Agente dirige, multi-hop, GraphRAG, DEMO |
| G — Engenharia de Qualidade | 56-66 | 15 min | Chunking, re-rank, HyDE, hybrid, ColBERT |
| H — Avaliação de RAG | 67-73 | 10 min | Métricas, Ragas, LLM-as-judge, holdout |
| I — Fechamento | 74-85 | 12 min | Boas práticas, anti-patterns, quiz, projeto, Q&A |

---

## Pontos de Engajamento

| Slide | Tipo | Interação |
|---|---|---|
| 6 | Mão levantada | "Quem já usou RAG e obteve resposta errada com alta confiança?" |
| 14 | Discussão rápida | "Pior falha: não responder ou responder errado com confiança?" |
| 23 | Votação | 5 perguntas: responder direto ou recuperar? |
| 44 | Duplas (5 min) | Adaptive RAG vs Self-RAG em FAQ jurídico |
| 53 | DEMO ao vivo | Agentic RAG Multi-Hop (Lab 2) |
| 54 | Duplas (2 min) | "Como o agente decide parar em multi-hop?" |
| 66 | Duplas (2 min) | Escolher estratégia de qualidade para 3 cenários |
| 79-81 | Quiz individual | 3 perguntas de múltipla escolha |
| 85 | Q&A | Perguntas abertas e encerramento |

---

## Materiais Necessários

- [ ] Projetor / tela de compartilhamento
- [ ] VS Code aberto com `05-Labs/ETHAGT06/Lab2-Agentic-RAG-Multi-Hop`
- [ ] Terminal com Python 3.11+ e `OPENAI_API_KEY` configurada
- [ ] Vector DB (Qdrant ou Milvus) populado com corpus de exemplo
- [ ] Cohere API key (para demo de re-ranking) — opcional
- [ ] Dataset de holdout de exemplo para demo de avaliação
- [ ] Acesso ao repositório da especialização
- [ ] Quadro branco (para diagramas improvisados)
- [ ] Handout: storyboard impresso (opcional)

---

## Riscos e Planos B

| Risco | Plano B |
|---|---|
| API LLM indisponível na DEMO (Slide 53) | Mostrar trace pré-gravado do Lab 2 (screenshot) |
| Vector DB não conecta | Usar FAISS em memória como fallback |
| Alunos sem ETHAGT04 | Iniciar aula com recap rápido (5 min) do pipeline retrieve→generate |
| Tempo estourado no Bloco 1 | Cortar exercício do Slide 23 (votação rápida); mover para homework |
| Tempo estourado no Bloco 2 | Reduzir quiz para 2 perguntas (Slides 79-80); referências como leitura |
| Demo de avaliação (Ragas) demora | Mostrar resultado pré-computado em dashboard |

---

## Avaliação da Aula

- Quiz ao final (Slides 79-81): ≥2 acertos = compreensão básica
- Exercício de routing (Slide 23): votação rápida em sala
- Exercício Adaptive vs Self-RAG (Slide 44): discussão em duplas
- DEMO Multi-Hop (Slide 53): profundidade das perguntas da turma
- Feedback informal: "Uma técnica de RAG que você vai aplicar esta semana"
