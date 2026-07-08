# ETHAGT04 — Roteiro da Apresentação

> Universidade Etho · Especialização em Programação Agêntica
> Fase B — Razão, Memória e Conhecimento · 30 h

---

## Metadados

| Campo | Valor |
|---|---|
| Código | ETHAGT04 |
| Título | Reasoning & Planning (do CoT ao inference-time reasoning) |
| Duração | 120 min (2 blocos de 60 min) |
| Total de slides | 90 |
| Competências | C1 (I), C2 (B), C4 (B), C5 (B) |
| Pré-requisitos | ETHAGT03 (Composição de Workflows) |
| Fontes canônicas | CoT (Wei et al., 2022); ToT (Yao et al., 2023); Reflexion (Shinn et al., 2023); LATS (Zhou et al., 2024); Self-Discover (Major et al., 2024); OpenAI *Learning to Reason with LLMs* (2024) |

---

## Fluxo da Aula

### BLOCO 1 — 60 min

| Seção | Slides | Tempo | Objetivo |
|---|---|---|---|
| A — Abertura | 1-7 | 8 min | Engajar, contextualizar e estabelecer o espectro do raciocínio |
| B — Tipologia do Raciocínio | 8-18 | 14 min | CoT, Self-Consistency, linear vs árvore, antes vs durante a ação |
| C — Plan-and-Execute e ReWOO | 19-30 | 16 min | Planner/Executor, ReWOO, trade-offs, quando replanejar |
| D — Tree of Thoughts e LATS | 31-45 | 18 min | Busca em árvore, MCTS+LLM, backtracking, custo vs qualidade |
| Intervalo | — | 5 min | — |

### BLOCO 2 — 60 min

| Seção | Slides | Tempo | Objetivo |
|---|---|---|---|
| E — Reflexion | 46-55 | 12 min | Auto-crítica, memória de erros, convergência |
| F — Self-Discover | 56-63 | 8 min | Composição de estratégia, primitivas como building blocks |
| G — Inference-Time Reasoning Nativo | 64-75 | 14 min | o1/o3/Claude reasoning, reasoning model vs prompting, custo |
| H — Falhas, Loops e Orçamento | 76-84 | 12 min | Detecção de loops, orçamento de tokens, benchmarks |
| I — Fechamento | 85-90 | 8 min | Comparação geral, anti-patterns, quiz, Q&A |
| Q&A extra | — | 6 min | Perguntas abertas |

---

## Pontos de Engajamento

| Slide | Tipo | Interação |
|---|---|---|
| 5 | Mão levantada | "Quem já viu um agente ficar em loop sem sair?" |
| 10 | Discussão rápida | "Qual padrão de raciocínio vocês usam hoje?" |
| 17 | Duplas (2 min) | "CoT funciona para TUDO? Qual caso quebra?" |
| 27 | Votação | 5 cenários: Plan-and-Execute ou ReAct? |
| 38 | Duplas (3 min) | "Quando ToT vale o custo? Dê um exemplo." |
| 51 | Grupo | "Quantas tentativas até a Reflexion convergir?" |
| 60 | Discussão aberta | "Self-Discover sempre supera CoT? V/F?" |
| 73 | Duplas (3 min) | "Quando reasoning model substitui ToT?" |
| 80 | Quiz individual | 5 perguntas de múltipla escolha |
| 82 | Grupo | 4 perguntas de discussão profunda |

---

## Materiais Necessários

- [ ] Projetor / tela de compartilhamento
- [ ] VS Code aberto com notebooks LangGraph (`plan-and-execute.ipynb`, `lats/lats.ipynb`, `reflexion/reflexion.ipynb`)
- [ ] Terminal com Python 3.11+, `langgraph`, `openai` e `OPENAI_API_KEY` configurada
- [ ] Subset de GSM8K para demo (5 problemas)
- [ ] Acesso ao repositório da especialização
- [ ] Quadro branco (para desenhar árvores de busca)
- [ ] Handout: storyboard impresso (opcional)
- [ ] Tabela de custos atualizada (o1, o3, Claude, GPT-4o)

---

## Riscos e Planos B

| Risco | Plano B |
|---|---|
| API LLM indisponível no Lab de ToT (Slide 38) | Mostrar trace pré-gravado da árvore de busca |
| Alunos sem pré-requisito de ETHAGT03 | Revisar ReAct em 3 min (Slide 18) antes de seguir |
| Tempo estourado no Bloco 1 (LATS complexo) | Cortar detalhes de MCTS (Slide 40-41); focar no conceito |
| Tempo estourado no Bloco 2 | Reduzir quiz para 3 perguntas; Self-Discover como leitura |
| Modelo o1 indisponível para demo | Mostrar screenshot de trace de reasoning do o1 |
| Alunos confusos sobre Self-Discover | Simplificar: focar só em "compor primitivas", pular detalhes de transferência |

---

## Avaliação da Aula

- Quiz ao final (Slides 80-84): ≥3 acertos = compreensão básica
- Exercício de trade-off (Slide 77): discussão em duplas
- Perguntas de discussão (Slide 82): profundidade das respostas
- Feedback informal: "Qual técnica você vai testar primeiro no seu projeto?"
