# ETHAGT11 — Checklist da Aula

> Checklist para o professor verificar antes, durante e depois da aula.

---

## Pré-Aula (24h antes)

### Preparação Técnica
- [ ] Docker Compose com Kafka testado e funcionando (para DEMO do Slide 26)
- [ ] Temporal Server local em execução (para DEMO do Slide 44)
- [ ] Temporal Web UI acessível em localhost:8080
- [ ] Python 3.11+ com dependências (`confluent-kafka`, `temporalio`, `redis`)
- [ ] `OPENAI_API_KEY` testada e funcionando (para agentes nos labs)
- [ ] VS Code aberto com `05-Labs/ETHAGT11/Lab1-Agente-Kafka`
- [ ] VS Code aberto com `05-Labs/ETHAGT11/Lab2-Workflow-Temporal`
- [ ] Terminal testado: producer/consumer Kafka executam sem erro
- [ ] Terminal testado: worker Temporal executa workflow sem erro
- [ ] Screenshots da Temporal Web UI salvos (plano B se demo falhar)
- [ ] Logs pré-gravados do Kafka producer/consumer (plano B)
- [ ] Projetor testado
- [ ] Slides exportados para PDF (plano B se apresentação falhar)

### Preparação de Conteúdo
- [ ] Revisar todas as notas do professor (76 slides)
- [ ] Ensaiar a DEMO Kafka (Slide 26) — rodar pelo menos 2x antes
- [ ] Ensaiar a DEMO Temporal (Slide 44) — rodar pelo menos 2x antes
- [ ] Preparar o exercício de saga compensatória (Slide 62) — gabarito pronto
- [ ] Preparar o exercício de HITL (Slide 46) — template pronto
- [ ] Confirmar que todos os diagramas estão legíveis
- [ ] Preparar handout (opcional): storyboard impresso

### Preparação de Logística
- [ ] Sala reservada para 90 min + 15 min de buffer
- [ ] Quadro branco disponível (para diagramas de partição, saga)
- [ ] Acesso ao repositório da especialização confirmado
- [ ] Wi-Fi estável (DEMOs dependem de rede)

---

## Durante a Aula

### Bloco 1 (45 min)
- [ ] **Slide 1-6 (8 min)**: Abertura — anotar alunos que participam da pergunta do Slide 5
- [ ] **Slide 5**: Fazer a pergunta "Qual o pior crash que você já viu em produção?"
- [ ] **Slide 8**: Destacar os limites do síncrono — conectar com experiência dos alunos
- [ ] **Slide 9**: Mostrar o diagrama event-driven — garantir que entendem producer/broker/consumer
- [ ] **Slide 15**: Destacar que este é o conceito fundacional (O Log)
- [ ] **Slide 17**: Mostrar particionamento — garantir que entendem hash(key) % partitions
- [ ] **Slide 21**: Comparação dos 3 brokers — deixar turma opinar
- [ ] **Slide 26 (3 min)**: DEMO KAFKA AO VIVO — se falhar, usar screenshots/logs
- [ ] **Slide 27**: Pergunta da demo — deixar 2 min em duplas
- [ ] **Slide 30-31**: Conceitos do Temporal — destacar durable execution como mágica
- [ ] **Slide 35**: Comparação Temporal/Prefect/Airflow — votação rápida
- [ ] Intervalo (3 min)

### Bloco 2 (45 min)
- [ ] **Slide 38-39 (3 min)**: Sobreviver a crashes + long-running
- [ ] **Slide 40**: HITL via signals — destacar pausa durável sem consumo de recursos
- [ ] **Slide 42-43**: Non-determinism — destacar como regra de ouro
- [ ] **Slide 44 (3 min)**: DEMO TEMPORAL AO VIVO — kill do worker, reiniciar, mostrar retomada
- [ ] **Slide 45**: Pergunta da demo — discussão aberta
- [ ] **Slide 46 (3 min)**: Exercício HITL em duplas
- [ ] **Slide 48-50**: Retries + idempotência — mostrar code block do enviar email
- [ ] **Slide 51-52**: Saga — usar o diagrama saga.mmd
- [ ] **Slide 53**: Circuit breaker — state machine
- [ ] **Slide 56**: Exactly-once vs at-least-once — pergunta provocativa
- [ ] **Slide 60**: V/F "Event-driven é sempre mais escalável" — votação
- [ ] **Slide 62 (5 min)**: Exercício saga compensatória em duplas
- [ ] **Slide 63-64**: Boas práticas e anti-patterns — pedir exemplos da turma
- [ ] **Slide 65**: Caso de estudo — destacar composição de todos os patterns
- [ ] **Slide 66-67**: Resumo e checklist
- [ ] **Slide 68-72 (5 min)**: Quiz — individual, sem consulta
- [ ] **Slide 73-75**: Conexão, projeto, labs, leitura
- [ ] **Slide 76 (2 min)**: Q&A

---

## Pós-Aula

### Avaliação
- [ ] Contar resultados do quiz (≥3 acertos = compreensão básica)
- [ ] Avaliar exercício de saga compensatória (Slide 62) — coletar respostas
- [ ] Anotar perguntas frequentes no Q&A para futuras iterações
- [ ] Pedir feedback informal: "Um conceito que vocês vão aplicar no trabalho"
- [ ] Verificar tempo real vs planejado por seção

### Follow-up
- [ ] Enviar leitura recomendada no Slack/email (Temporal primer + Kreps The Log)
- [ ] Disponibilizar slides (PDF + repositório)
- [ ] Lembrar prazo do Lab 1 — "Agente com Kafka" (1 semana)
- [ ] Lembrar prazo do Lab 2 — "Workflow durável em Temporal" (1 semana)
- [ ] Lembrar prazo do Projeto (2 semanas)
- [ ] Preparar ETHAGT12 (a próxima aula aprofunda AgentOps e tracing)

---

## Sinais de Alerta Durante a Aula

| Sinal | Ação |
|---|---|
| Alunos confusos no Slide 15 (O Log) | Simplificar: focar só em append-only + offset |
| DEMO Kafka falha (Slide 26) | Screenshots + logs pré-gravados + seguir |
| DEMO Temporal falha (Slide 44) | Vídeo do workflow recuperando + seguir |
| Alunos travados em particionamento (Slide 17) | Desenhar no quadro: 3 partições, hash(key), setas |
| Tempo estourado no Bloco 1 | Cortar exercício do Slide 13 (votação); mover para homework |
| Tempo estourado no Bloco 2 | Reduzir quiz para 3 perguntas (Slides 68-70); referências como leitura |
| Nenhuma pergunta no Q&A | Fazer pergunta inversa: "Qual parte foi menos clara?" |
| Alunos sem conhecimento de Kafka/Temporal | Direcionar para Labs com setup guiado; oferecer pair programming |
| Confusão sobre non-determinism (Slide 42) | Usar analogia do filme + reassistir; mostrar code side-by-side |
