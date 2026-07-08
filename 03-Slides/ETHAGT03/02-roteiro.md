# ETHAGT03 — Roteiro da Apresentação

> Universidade Etho · Especialização em Programação Agêntica
> Fase A — Fundamentos Agênticos · 30 h

---

## Metadados

| Campo | Valor |
|---|---|
| Código | ETHAGT03 |
| Título | Padrões de Workflow Agêntico (os 5 da Anthropic + composições) |
| Duração | 90 min (2 blocos de 45 min) |
| Total de slides | 63 |
| Competências | C1 (I), C2 (B), C3 (B), C5 (B) |
| Fontes canônicas | Anthropic *Building Effective Agents* (2024); arXiv:2601.12560 (2026); Plan-and-Solve (2305.17126); ReWOO (2305.04091); LLMCompiler (2310.01757) |

---

## Fluxo da Aula

### BLOCO 1 — 45 min

| Seção | Slides | Tempo | Objetivo |
|---|---|---|---|
| A — Abertura | 1-5 | 6 min | Engajar, contextualizar e estabelecer objetivos |
| B — Por Que Workflows | 6-10 | 7 min | Princípio "comece simples", 5 padrões, panorama |
| C — Prompt Chaining | 11-16 | 8 min | Estrutura, gates, trade-off latência/accuracy |
| D — Routing | 17-23 | 9 min | Classificação, routing por modelo/prompt/tools |
| Intervalo | — | 5 min | — |

### BLOCO 2 — 45 min

| Seção | Slides | Tempo | Objetivo |
|---|---|---|---|
| E — Parallelization | 24-32 | 15 min | Sectioning, voting, guardrails, DEMO de latência |
| F — Orchestrator-Workers | 33-39 | 10 min | Subtarefas dinâmicas, implementação |
| G — Evaluator-Optimizer | 40-46 | 10 min | Loop de refinamento, critérios, convergência |
| H — Composições e Limites | 47-51 | 8 min | Composição, quando vira agente, trade-offs |
| I — Fechamento | 52-63 | 17 min | Caso, resumo, quiz, projeto, Q&A |
| Q&A extra | — | 10 min | Perguntas abertas |

---

## Pontos de Engajamento

| Slide | Tipo | Interação |
|---|---|---|
| 5 | Mão levantada | "Quem já viu projeto que usou agente onde um if bastava?" |
| 16 | Duplas (2 min) | Descrever gate programático útil em tradução |
| 23 | Duplas (2 min) | "Como saber se o roteador está errando? O que medir?" |
| 31 | DEMO | Latência = max vs sum ao vivo com timer no terminal |
| 32 | Votação | Voting vs sectioning em 3 cenários |
| 39 | V/F | "Orchestrator-workers é sempre melhor?" |
| 46 | Duplas (2 min) | Condição de parada para tradução literária |
| 49 | Discussão aberta | "O que diferencia workflow composto de agente?" |
| 56-59 | Quiz individual | 4 perguntas de múltipla escolha |
| 60 | Grupo | 5 cenários: indicar workflow + justificar |
| 63 | Q&A | Perguntas abertas da turma |

---

## Materiais Necessários

- [ ] Projetor / tela de compartilhamento
- [ ] VS Code aberto com snippets de cada um dos 5 workflows
- [ ] Terminal com Python 3.11+, `asyncio`, e `OPENAI_API_KEY` configurada
- [ ] Acesso ao repositório da especialização
- [ ] Quadro branco (para diagramas improvisados e matriz de trade-offs)
- [ ] Handout: storyboard impresso (opcional)
- [ ] Diagramas `.mmd` de `12-Diagrams/ETHAGT03/` renderizados

---

## Riscos e Planos B

| Risco | Plano B |
|---|---|
| API LLM indisponível na DEMO (Slide 31) | Mostrar timer pré-gravado (screenshot serial vs paralelo) |
| Alunos sem ETHAGT01 | Revisar recap workflow vs agente (Slide 8) com mais tempo; oferecer material de apoio |
| Tempo estourado no Bloco 1 | Cortar exercício do Slide 16; mover gates de tradução para homework |
| Tempo estourado no Bloco 2 | Reduzir quiz para 2 perguntas; deixar composições como leitura |
| Confusão parallelization vs orchestrator | Reapresentar Slide 34 com exemplo no quadro |

---

## Avaliação da Aula

- Quiz ao final (Slides 56-59): ≥3 acertos = compreensão básica
- Exercício de 5 cenários (Slide 60): profundidade da justificativa
- Perguntas de discussão (Slide 49): qualidade do debate
- Feedback informal: "Um padrão que você não conhecia e vai usar amanhã"
