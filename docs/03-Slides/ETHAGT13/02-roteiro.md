# ETHAGT13 — Roteiro da Apresentação

> Universidade Etho · Especialização em Programação Agêntica
> Fase D — Produção, Governança e Fronteira · 25 h

---

## Metadados

| Campo | Valor |
|---|---|
| Código | ETHAGT13 |
| Título | Segurança & Governança de Agentes |
| Duração | 90 min (2 blocos de 45 min) |
| Total de slides | 77 |
| Competências | C1 (A), C2 (B), C3 (A), C5 (I), C6 (A) |
| Fontes canônicas | OWASP Top 10 for LLM Applications (2025); Greshake et al. arXiv:2302.12173; Anthropic Many-shot Jailbreaking |

---

## Fluxo da Aula

### BLOCO 1 — 45 min

| Seção | Slides | Tempo | Objetivo |
|---|---|---|---|
| A — Abertura | 1-6 | 8 min | Engajar, contextualizar incidentes reais, estabelecer objetivos |
| B — Threat Modeling | 7-14 | 10 min | Ativos, superfícies, STRIDE/LINDDUN adaptado, multi-agente |
| C — Prompt Injection | 15-27 | 15 min | Sem separação instr/dados, direta, indireta, jailbreak, defesas, DEMO |
| D — Guardrails | 28-37 | 12 min | Input/output filter, structured outputs, constitutional AI, defense in depth |
| Intervalo | — | 5 min | — |

### BLOCO 2 — 45 min

| Seção | Slides | Tempo | Objetivo |
|---|---|---|---|
| E — HITL | 38-44 | 8 min | Quando exigir, checkpoints, UX, logging, classificação de risco |
| F — Red Team | 45-55 | 11 min | Casos sistematizados, AgentDojo, InjecAgent, Garak/PyRIT, métricas |
| G — Governança | 56-63 | 8 min | Policy-as-code (OPA), auditoria, LGPD/EU AI Act, ADRs |
| H — Fechamento | 64-77 | 18 min | Boas práticas, anti-patterns, caso de estudo, quiz, Q&A |
| Q&A extra | — | 10 min | Perguntas abertas |

---

## Pontos de Engajamento

| Slide | Tipo | Interação |
|---|---|---|
| 5 | Discussão | "Qual o pior que pode acontecer se um agente seu for comprometido?" |
| 8 | Reflexão | "Qual superfície de ataque você não havia considerado?" |
| 10 | Mão levantada | "Quantas das tools do seu agente são destrutivas?" |
| 14 | Duplas (3 min) | Modelar ameaças de agente de atendimento |
| 26 | DEMO ao vivo | Red team de agente RAG — 5 vetores de injeção indireta |
| 27 | Duplas (2 min) | "Qual vetor foi mais surpreendente? Como defender?" |
| 36 | Duplas (3 min) | Desenhar 5 camadas de defesa para agente de suporte |
| 41 | Reflexão | "Você já aprovou algo sem ler? Por quê?" |
| 54 | Duplas (3 min) | Escrever 3 casos de red team |
| 63 | Duplas (3 min) | Escrever política OPA em Rego |
| 70-74 | Quiz individual | 5 perguntas de múltipla escolha |
| 75 | Grupo | 4 perguntas de discussão profunda |

---

## Materiais Necessários

- [ ] Projetor / tela de compartilhamento
- [ ] VS Code aberto com `05-Labs/ETHAGT13/Lab1-Red-Team-RAG`
- [ ] Terminal com Python 3.11+, `OPENAI_API_KEY` configurada e agente RAG rodando
- [ ] Documento RAG malicioso preparado (5 payloads de injeção indireta)
- [ ] OPA / Rego CLI instalado (para exercício do Slide 63)
- [ ] Acesso ao repositório da especialização
- [ ] Quadro branco (para desenhar defense in depth improvisado)
- [ ] Handout: storyboard impresso (opcional)

---

## Riscos e Planos B

| Risco | Plano B |
|---|---|
| API LLM indisponível na DEMO (Slide 26) | Mostrar trace pré-gravado com prints dos 5 vetores explorados |
| Alunos sem pré-requisito de ETHAGT12 | Recap rápido de traces/observabilidade no Slide 5 |
| Tempo estourado no Bloco 1 | Cortar exercício do Slide 36 (camadas de defesa); mover para homework |
| Tempo estourado no Bloco 2 | Reduzir quiz para 3 perguntas (Slides 70-72); governança como leitura |
| Exercício OPA (Slide 63) muito lento | Mostrar política pré-escrita e focar na discussão |

---

## Avaliação da Aula

- Quiz ao final (Slides 70-74): ≥3 acertos = compreensão básica
- Exercício de threat modeling (Slide 14): profundidade da análise em duplas
- Exercício de casos de red team (Slide 54): qualidade dos casos escritos
- Perguntas de discussão (Slide 75): profundidade das respostas
- Feedback informal: "Uma vulnerabilidade que você não considerava antes desta aula"
