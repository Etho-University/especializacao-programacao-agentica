# ETHAGT10 — Roteiro da Apresentação

> Universidade Etho · Especialização em Programação Agêntica
> Fase C — Sistemas Multi-Agente · 30 h

---

## Metadados

| Campo | Valor |
|---|---|
| Código | ETHAGT10 |
| Título | Padrões de Arquitetura Multi-Agente (topologias) |
| Duração | 90 min (2 blocos de 45 min) |
| Total de slides | 62 |
| Competências | C1 (A), C2 (A), C3 (B), C4 (B), C6 (B) |
| Fontes canônicas | Hong et al. *MetaGPT* (arXiv:2308.00352); Chen et al. *AgentVerse* (arXiv:2308.10848); Wu et al. *AutoGen* (arXiv:2308.08155); OpenAI Swarm (2024); LangGraph *Multi-Agent*; arXiv:2601.12560 |

---

## Fluxo da Aula

### BLOCO 1 — 45 min

| Seção | Slides | Tempo | Objetivo |
|---|---|---|---|
| A — Abertura | 1-6 | 8 min | Engajar, contextualizar e estabelecer objetivos |
| B — Catálogo das 12 Topologias | 7-16 | 12 min | Panorama das 12 topologias, espectro centralizado↔descentralizado |
| C — Supervisor e Hierarchical | 17-28 | 15 min | Supervisor pattern, tool calls, hierarchical, MetaGPT, DEMO |
| D — Swarm e Handoffs | 29-34 | 10 min | OpenAI Swarm, handoffs, swarm vs supervisor, limites |
| Intervalo | — | 5 min | — |

### BLOCO 2 — 45 min

| Seção | Slides | Tempo | Objetivo |
|---|---|---|---|
| E — Pipeline e Orchestrator-Workers | 35-40 | 10 min | Pipeline fixo vs dinâmico, composição hierarchical |
| F — Event-Driven, Actor Model, Mesh | 41-46 | 10 min | Event-driven, actor model, mesh, blackboard |
| G — Tree, Recursive + DEMO | 47-52 | 10 min | Tree of Agents (LATS), recursive, anti-pattern, DEMO |
| H — Fechamento | 53-62 | 15 min | Matriz de decisão, ADR, sinais, MetaGPT, quiz, Q&A |

---

## Pontos de Engajamento

| Slide | Tipo | Interação |
|---|---|---|
| 5 | Mão levantada | "Qual foi a topologia mais comum que vocês já usaram em projetos?" |
| 16 | Votação | 6 cenários: matching cenário → topologia |
| 25 | Duplas (2 min) | "Em quantos níveis de hierarquia o supervisor se torna gargalo?" |
| 27 | Pergunta | "Como você montaria uma crew para revisar um PR?" |
| 28 | Votação | 4 cenários: hierarchical ou flat? |
| 34 | Discussão aberta | "Swarm ou supervisor para revisão de PR?" (3 min) |
| 40 | Exercício | 3 cenários: pipeline ou agente? |
| 46 | Discussão aberta | "Mesh é sempre a topologia mais escalável?" (3 min) |
| 50 | Pergunta | "Recursive é sempre anti-pattern? Quando não?" |
| 52 | Discussão (2 min) | Análise dos resultados da DEMO swarm vs supervisor |
| 58 | Exercício em grupos | 6 cenários + esqueleto de ADR (5 min) |
| 60 | Quiz individual | 3 perguntas de verificação rápida |

---

## Materiais Necessários

- [ ] Projetor / tela de compartilhamento
- [ ] VS Code aberto com `05-Labs/ETHAGT10/Lab1-Hierarchical-Teams` e `Lab2-Swarm-vs-Supervisor`
- [ ] Terminal com Python 3.11+, LangGraph, OpenAI SDK e `OPENAI_API_KEY` configurada
- [ ] Acesso ao repositório da especialização (`10-Architecture/architectures/`)
- [ ] Quadro branco (para desenhar topologias improvisadas)
- [ ] Handout: storyboard impresso (opcional)
- [ ] Screenshots de traces das DEMOs (Slide 24 e 51) — plano B

---

## Riscos e Planos B

| Risco | Plano B |
|---|---|
| API LLM indisponível na DEMO (Slide 24) | Mostrar trace pré-gravado (screenshot) |
| API LLM indisponível na DEMO (Slide 51) | Mostrar traces comparativos salvos |
| Alunos sem pré-requisito de LangGraph | Direcionar para ETHAGT09; oferecer pair programming nos labs |
| Tempo estourado no Bloco 1 | Cortar exercício do Slide 28 (votação); mover para homework |
| Tempo estourado no Bloco 2 | Reduzir quiz para 2 perguntas (Slides 60-61); referências como leitura |
| Nenhuma pergunta no Q&A | Fazer pergunta inversa: "Qual topologia vocês usariam no projeto de vocês?" |

---

## Avaliação da Aula

- Quiz ao final (Slide 60): ≥2 acertos = compreensão básica
- Exercício de matching (Slide 16): votação rápida com discussão
- Exercício de ADR (Slide 58): esqueleto em grupos — profundidade das justificativas
- Perguntas de discussão (Slides 34, 46): qualidade do debate
- Feedback informal: "Uma topologia que você não conhecia e quer explorar"
