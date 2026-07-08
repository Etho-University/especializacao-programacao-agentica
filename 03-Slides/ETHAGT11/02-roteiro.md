# ETHAGT11 — Roteiro da Apresentação

> Universidade Etho · Especialização em Programação Agêntica
> Fase C — Orquestração & Produção · 25 h

---

## Metadados

| Campo | Valor |
|---|---|
| Código | ETHAGT11 |
| Título | Event-Driven Agents & Workflow Orchestration |
| Duração | 90 min (2 blocos de 45 min) |
| Total de slides | 76 |
| Competências | C1 (A), C2 (A), C3 (B), C4 (B), C5 (I) |
| Pré-requisitos | ETHAGT10 |
| Fontes canônicas | Temporal.io *Durable Execution*; Narkhede et al. *Kafka: The Definitive Guide*; Kreps *The Log*; Richards & Ford *Fundamentals of Software Architecture* |

---

## Fluxo da Aula

### BLOCO 1 — 45 min

| Seção | Slides | Tempo | Objetivo |
|---|---|---|---|
| A — Abertura | 1-6 | 8 min | Engajar, estabelecer objetivos e contextualizar evolução event-driven |
| B — Por que Event-Driven | 7-13 | 9 min | Limites do síncrono, paradigma event-driven, trade-offs, exercício |
| C — Mensageria | 14-27 | 15 min | O Log, Kafka (partições, ordering, consumer groups), RabbitMQ, NATS, CQRS, saga, CloudEvents, DEMO Kafka |
| D — Workflows | 28-36 | 10 min | Workflow vs agente, Temporal, Prefect, Airflow, comparação, decisão |
| Intervalo | — | 3 min | — |

### BLOCO 2 — 45 min

| Seção | Slides | Tempo | Objetivo |
|---|---|---|---|
| E — Durable Execution | 37-46 | 12 min | Crashes, long-running, HITL (timers/signals), replays, non-determinism, DEMO Temporal |
| F — Resiliência & Produção | 47-60 | 12 min | Retries, idempotência, saga, circuit breakers, exactly-once, sharding, tracing, custo, V/F |
| G — Fechamento | 61-76 | 18 min | Exercício saga, boas práticas, anti-patterns, caso de estudo, quiz, projeto, Q&A |
| Q&A extra | — | 3 min | Perguntas abertas |

---

## Pontos de Engajamento

| Slide | Tipo | Interação |
|---|---|---|
| 5 | Pergunta aberta | "Qual o pior crash que você já viu em produção?" |
| 13 | Votação | 4 cenários: síncrono ou assíncrono? |
| 17 | Pergunta conceitual | "Como garantir ordering de mensagens do mesmo agente em Kafka?" |
| 26 | DEMO ao vivo | Agente com Kafka — dois agentes coordenados via tópicos |
| 27 | Duplas (2 min) | "O que acontece se processar a mesma mensagem 2x?" |
| 29 | Pergunta aberta | "Você orquestra via código ou via agente supervisor?" |
| 44 | DEMO ao vivo | Workflow durável em Temporal — sobrevivendo a kill |
| 45 | Discussão aberta | "Replay quebra se tool externa mudou de comportamento?" |
| 46 | Duplas (3 min) | HITL com signal: esboçar workflow de aprovação |
| 50 | Pergunta conceitual | "Como garantir idempotência em tool de enviar email?" |
| 56 | Pergunta provocativa | "Exactly-once existe de verdade ou é mito?" |
| 60 | V/F | "Event-driven é sempre mais escalável" |
| 62 | Duplas (5 min) | Saga compensatória: transferência entre contas |
| 68-72 | Quiz individual | 5 perguntas de múltipla escolha |

---

## Materiais Necessários

- [ ] Projetor / tela de compartilhamento
- [ ] Docker Compose com Kafka (para DEMO do Slide 26)
- [ ] Temporal Server local em execução (para DEMO do Slide 44)
- [ ] VS Code aberto com `05-Labs/ETHAGT11/Lab1-Agente-Kafka` e `Lab2-Workflow-Temporal`
- [ ] Python 3.11+ com dependências (`confluent-kafka`, `temporalio`, `redis`)
- [ ] `OPENAI_API_KEY` configurada (para agentes nos labs)
- [ ] Acesso ao repositório da especialização
- [ ] Temporal Web UI acessível no browser (localhost:8080)
- [ ] Quadro branco (para diagramas improvisados)
- [ ] Handout: storyboard impresso (opcional)

---

## Riscos e Planos B

| Risco | Plano B |
|---|---|
| Kafka indisponível na DEMO (Slide 26) | Mostrar screenshots da execução + logs pré-gravados |
| Temporal Server indisponível (Slide 44) | Mostrar vídeo do workflow recuperando após kill |
| API LLM indisponível para agentes dos labs | Usar tool simulada (mock) nos consumers/workers |
| Tempo estourado no Bloco 1 | Cortar exercício do Slide 13 (votação); mover para homework |
| Tempo estourado no Bloco 2 | Reduzir quiz para 3 perguntas (Slides 68-70); referências como leitura |
| Alunos sem conhecimento de Kafka/Temporal | Direcionar para Labs 1 e 2 com setup guiado; oferecer pair programming |

---

## Avaliação da Aula

- Quiz ao final (Slides 68-72): ≥3 acertos = compreensão básica
- Exercício de saga compensatória (Slide 62): discussão em duplas
- DEMO Kafka (Slide 26): verificação de ordering e reprocessamento
- DEMO Temporal (Slide 44): verificação de recuperação após crash
- Feedback informal: "Um conceito que vocês vão aplicar no trabalho"
