# ETHAGT12 — Roteiro da Apresentação

> Universidade Etho · Especialização em Programação Agêntica
> Fase D — Produção, Governança e Fronteira · 30 h

---

## Metadados

| Campo | Valor |
|---|---|
| Código | ETHAGT12 |
| Título | AgentOps, Observabilidade & Avaliação (LLMOps para agentes) |
| Duração | 90 min (2 blocos de 45 min) |
| Total de slides | 78 |
| Competências | C1 (A), C2 (B), C4 (B), C5 (A) |
| Pré-requisitos | ETHAGT11 |
| Fontes canônicas | Jimenez et al. *SWE-bench* (arXiv:2310.06770); Mialon et al. *GAIA* (arXiv:2311.12983); Yao et al. *τ-bench* (arXiv:2404.44529) |

---

## Fluxo da Aula

### BLOCO 1 — 45 min

| Seção | Slides | Tempo | Objetivo |
|---|---|---|---|
| A — Abertura | 1-6 | 8 min | Engajar, contextualizar e estabelecer objetivos |
| B — Por que difícil | 7-14 | 10 min | Não-determinismo, ambiente, custo, falácias |
| C — Observabilidade | 15-27 | 16 min | Traces, spans, OTel, tooling, DEMO ao vivo |
| Intervalo | — | 5 min | — |

### BLOCO 2 — 45 min

| Seção | Slides | Tempo | Objetivo |
|---|---|---|---|
| D — Avaliação | 28-43 | 18 min | LLM-as-judge, golden cases, métricas, CI, DEMO |
| E — Benchmarks | 44-54 | 14 min | SWE-bench, GAIA, τ-bench, AgentBench, WebArena |
| F — Melhoria & Report | 55-64 | 12 min | Dataset, CI, shadow, canary, eval report, falhas |
| G — Fechamento | 65-78 | 12 min | Boas práticas, caso de estudo, quiz, projeto, Q&A |

---

## Pontos de Engajamento

| Slide | Tipo | Interação |
|---|---|---|
| 5 | Pergunta aberta | "Como você sabe se seu agente está ficando melhor ou pior?" |
| 11 | Pergunta aberta | "Qual falácia de avaliação você já cometeu?" |
| 14 | Votação | Identificando falácias em 4 afirmações |
| 24 | DEMO ao vivo | Traces Everywhere — adicionar observabilidade |
| 25-26 | Duplas | Lendo um trace: identificar loop |
| 31 | Pergunta conceitual | "Qual viés do LLM-as-judge é mais perigoso?" |
| 40 | DEMO ao vivo | Eval automatizado — detectar regressão |
| 42 | Duplas | Escrevendo golden cases com critério mensurável |
| 52 | Pergunta provocativa | "Score alto em benchmark garante produção?" |
| 64 | Grupos | Detectando regressão: análise de causas |
| 71-75 | Quiz individual | 5 perguntas de múltipla escolha |

---

## Materiais Necessários

- [ ] Projetor / tela de compartilhamento
- [ ] VS Code aberto com `05-Labs/ETHAGT12/Lab1-Traces-Everywhere` e `Lab2-Eval-Automatizado`
- [ ] Terminal com Python 3.11+ e `OPENAI_API_KEY` configurada
- [ ] Conta LangSmith (ou Phoenix/Langfuse local) configurada
- [ ] Screenshot de trace real e eval report preenchido (planos B)
- [ ] Acesso ao repositório da especialização
- [ ] Quadro branco (para diagramas improvisados)
- [ ] Handout: storyboard impresso (opcional)

---

## Riscos e Planos B

| Risco | Plano B |
|---|---|
| API LLM indisponível na DEMO (Slides 24, 40) | Mostrar trace/eval pré-gravado (screenshot) |
| LangSmith/Phoenix indisponível | Mostrar traces do arquivo JSONL exportado |
| Alunos sem ETHAGT11 (LLMOps básico) | Reforçar conceitos de traces no Slide 16-17 |
| Tempo estourado no Bloco 1 | Cortar exercício Slide 26 (mover para homework) |
| Tempo estourado no Bloco 2 | Reduzir quiz para 3 perguntas (Slides 71-73) |
| Discussão longa no Slide 64 | Encerrar com 1-2 compartilhamentos |

---

## Avaliação da Aula

- Quiz ao final (Slides 71-75): ≥3 acertos = compreensão básica
- Exercício de golden cases (Slide 42): profundidade dos critérios
- Exercício de regressão (Slide 64): análise de causas
- Feedback informal: "Um conceito que você vai aplicar na segunda-feira"
