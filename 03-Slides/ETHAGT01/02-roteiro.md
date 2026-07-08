# ETHAGT01 — Roteiro da Apresentação

> Universidade Etho · Especialização em Programação Agêntica
> Fase A — Fundamentos Agênticos · 25 h

---

## Metadados

| Campo | Valor |
|---|---|
| Código | ETHAGT01 |
| Título | Arquitetura Cognitiva de Agentes LLM |
| Duração | 90 min (2 blocos de 45 min) |
| Total de slides | 62 |
| Competências | C1 (I), C3 (B), C4 (B), C5 (B) |
| Fontes canônicas | Anthropic *Building Effective Agents* (2024); Yao et al. *ReAct* (ICLR 2023); arXiv:2601.12560 |

---

## Fluxo da Aula

### BLOCO 1 — 45 min

| Seção | Slides | Tempo | Objetivo |
|---|---|---|---|
| A — Abertura | 1-6 | 8 min | Engajar, contextualizar e estabelecer objetivos |
| B — Fundamentos | 7-22 | 22 min | Augmented LLM, Agent Loop (ReAct), DEMO ao vivo |
| C — Workflows vs Agentes | 23-28 | 10 min | Distinção canônica, 5 padrões, exercício de decisão |
| Intervalo | — | 5 min | — |

### BLOCO 2 — 45 min

| Seção | Slides | Tempo | Objetivo |
|---|---|---|---|
| D — Frameworks | 29-36 | 15 min | Python puro vs LangGraph vs OpenAI SDK |
| E — Observabilidade | 37-41 | 8 min | Traces, logs, custo, latência |
| F — Fechamento | 42-62 | 12 min | Boas práticas, anti-patterns, caso de estudo, quiz, Q&A |
| Q&A extra | — | 10 min | Perguntas abertas |

---

## Pontos de Engajamento

| Slide | Tipo | Interação |
|---|---|---|
| 5 | Mão levantada | "Quem já tentou tarefa multi-step com ChatGPT e falhou?" |
| 8 | Discussão rápida | "Qual definição de agente sua equipe usa?" |
| 22 | Duplas (2 min) | "O que acontece se a tool retornar erro?" |
| 28 | Votação | 6 cenários: workflow ou agente? |
| 36 | Discussão aberta | "Qual framework dá mais controle?" |
| 47 | Duplas (3 min) | Debugar trace quebrado |
| 50-54 | Quiz individual | 5 perguntas de múltipla escolha |
| 55 | Grupo | 4 perguntas de discussão profunda |

---

## Materiais Necessários

- [ ] Projetor / tela de compartilhamento
- [ ] VS Code aberto com `19-Examples/ETHAGT01/exemplo-01-react-loop/main.py`
- [ ] Terminal com Python 3.11+ e `OPENAI_API_KEY` configurada
- [ ] Acesso ao repositório da especialização
- [ ] Quadro branco (para diagramas improvisados)
- [ ] Handout: storyboard impresso (opcional)

---

## Riscos e Planos B

| Risco | Plano B |
|---|---|
| API LLM indisponível na DEMO (Slide 21) | Mostrar trace pré-gravado (screenshot) |
| Alunos sem pré-requisito de Python | Direcionar para ETHDEV07; oferecer pair programming nos labs |
| Tempo estourado no Bloco 1 | Cortar exercício do Slide 28 (votação rápida); mover para homework |
| Tempo estourado no Bloco 2 | Reduzir quiz para 3 perguntas; referências como leitura |

---

## Avaliação da Aula

- Quiz ao final (Slides 50-54): ≥3 acertos = compreensão básica
- Exercício de trace quebrado (Slide 47): discussão em duplas
- Perguntas de discussão (Slide 55): profundidade das respostas
- Feedback informal: "Um coisa que você aprendeu hoje que não sabia"
