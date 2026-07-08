# ETHAGT09 — Roteiro da Apresentação

> Universidade Etho · Especialização em Programação Agêntica
> Fase C — Sistemas Multi-Agente · 25 h

---

## Metadados

| Campo | Valor |
|---|---|
| Código | ETHAGT09 |
| Título | Comunicação e Coordenação Multi-Agente (A2A · blackboard · actor model) |
| Duração | 90 min (2 blocos de 45 min) |
| Total de slides | 72 |
| Competências | C1 (A), C2 (I), C3 (B), C4 (B), C5 (B) |
| Pré-requisito | ETHAGT04 (Reasoning & Planning) |
| Fontes canônicas | Wu et al. *AutoGen* (arXiv:2308.08155); Li et al. *CAMEL* (arXiv:2303.17760); Hewitt *Actor Model* (1973); OpenAI Swarm (2024); Google A2A Protocol (2024) |

---

## Fluxo da Aula

### BLOCO 1 — 45 min

| Seção | Slides | Tempo | Objetivo |
|---|---|---|---|
| A — Abertura | 1-7 | 8 min | Engajar, contextualizar e estabelecer objetivos |
| B — Espectro A2A | 8-15 | 10 min | Comunicação direta/assíncrona, topologias, schemas, garantias |
| C — Padrões de Conversação | 16-26 | 13 min | CAMEL, AutoGen GroupChat, Swarm handoff, MetaGPT |
| D — Blackboard | 27-33 | 10 min | Espaço compartilhado, quando usar, implementação |
| Intervalo | — | 5 min | — |

### BLOCO 2 — 45 min

| Seção | Slides | Tempo | Objetivo |
|---|---|---|---|
| E — Actor Model | 34-44 | 13 min | Atores, encapsulamento, concorrência, DEMO |
| F — Negociação e Conflito | 45-52 | 10 min | Bargaining, auction, voting, deadlock |
| G — Protocolos Emergentes | 53-59 | 8 min | A2A Protocol, MCP vs A2A, orquestração |
| H — Fechamento | 60-72 | 12 min | Boas práticas, MetaGPT, exercício, quiz, Q&A |
| Q&A extra | — | 2 min | Perguntas abertas |

---

## Pontos de Engajamento

| Slide | Tipo | Interação |
|---|---|---|
| 5 | Pergunta aberta | "Quantos agentes colaborando antes de virar caos?" |
| 9 | Pergunta aberta | "Qual topologia para 10 agentes debatendo um diagnóstico?" |
| 14 | Pergunta aberta | "Qual garantia para transferência bancária entre agentes?" |
| 15 | Votação | 4 cenários: escolher topologia + garantia |
| 21 | Pergunta aberta | "Qual estratégia para 5 especialistas debatendo?" |
| 23 | Pergunta aberta | "Handoff ou delegação para suporte ao cliente?" |
| 26 | Votação | 4 cenários: escolher padrão de conversação |
| 30 | Pergunta aberta | "Quando blackboard é preferível a mensagens diretas?" |
| 33 | Duplas (2 min) | 3 cenários: blackboard ou mensagens |
| 37 | Pergunta aberta | "Actor model vs shared state — qual mais seguro?" |
| 42 | V/F | "Actor model é mais lento que shared-state." |
| 43-44 | DEMO + Duplas | Duas arquiteturas ao vivo + discussão |
| 46 | Pergunta aberta | "O que acontece com objetivos parcialmente conflitantes?" |
| 50 | Pergunta aberta | "Voting ou mediator para diagnóstico divergente?" |
| 52 | Pergunta aberta | "Como evitar que agente de qualidade nunca aceite?" |
| 56 | Pergunta aberta | "MCP e A2A são complementares ou competidores?" |
| 64 | Duplas (3 min) | Schema de mensagem A2A com versionamento |
| 67-70 | Quiz individual | 4 perguntas de múltipla escolha |

---

## Materiais Necessários

- [ ] Projetor / tela de compartilhamento
- [ ] VS Code aberto com `05-Labs/ETHAGT09/Lab1-Duas-Arquiteturas` (DEMO Slide 43)
- [ ] Terminal com Python 3.11+ e `OPENAI_API_KEY` configurada
- [ ] Acesso ao repositório da especialização
- [ ] Quadro branco (para desenhar topologias improvisadas)
- [ ] Diagramas Mermaid renderizados: `actor-model.mmd`, `blackboard.mmd`, `handoff.mmd`, `negotiation.mmd`
- [ ] Handout: storyboard impresso (opcional)
- [ ] Template de schema JSON em branco (Slide 64)

---

## Riscos e Planos B

| Risco | Plano B |
|---|---|
| API LLM indisponível na DEMO (Slide 43) | Mostrar traces pré-gravados (screenshots das 2 arquiteturas) |
| Alunos sem ETHAGT04 (pré-requisito) | Revisar rapidamente ReAct no Slide 5; oferecer material complementar |
| Tempo estourado no Bloco 1 | Cortar exercício do Slide 26 (votação rápida); mover para homework |
| Tempo estourado no Bloco 2 | Reduzir quiz para 2 perguntas (Slides 67-68); FIPA como leitura |
| Diagramas Mermaid não renderizam | Ter versão PNG exportada de cada `.mmd` |
| Alunos confundem MCP com A2A | Reforçar Slide 56 com analogia (ferramentas vs agentes) |

---

## Avaliação da Aula

- Quiz ao final (Slides 67-70): ≥3 acertos = compreensão básica
- Exercício de schema A2A (Slide 64): discussão em duplas
- Exercício de topologia (Slide 15): votação com correção imediata
- Perguntas de discussão (se houver tempo): profundidade das respostas
- Feedback informal: "Um padrão de comunicação que você não conhecia"

---

## Conexão com o Projeto do Módulo

- **Projeto**: sistema de negociação entre agentes (comprador/vendedor ou especialistas)
- **Entrega**: código + traces + análise de convergência
- **Critério de sucesso**: convergência em ≥ 80% dos casos; análise de falhas documentada
- **Labs**: Lab 1 (Duas Arquiteturas) e Lab 2 (Actor Model com Handoffs)
