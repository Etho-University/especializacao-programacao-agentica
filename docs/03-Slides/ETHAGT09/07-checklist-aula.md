# ETHAGT09 — Checklist da Aula

> Checklist para o professor verificar antes, durante e depois da aula.

---

## Pré-Aula (24h antes)

### Preparação Técnica
- [ ] API key (OpenAI ou Anthropic) testada e funcionando
- [ ] Python 3.11+ instalado e com dependências (`openai`, `langgraph`, `python-dotenv`)
- [ ] VS Code aberto com `05-Labs/ETHAGT09/Lab1-Duas-Arquiteturas`
- [ ] Terminal testado: as 2 versões da DEMO (group chat + blackboard) executam sem erro
- [ ] Traces pré-gravados da DEMO salvos (plano B se API falhar)
- [ ] Projetor testado
- [ ] Slides exportados para PDF (plano B se apresentação falhar)
- [ ] Diagramas Mermaid renderizados (PNG): `actor-model.mmd`, `blackboard.mmd`, `handoff.mmd`, `negotiation.mmd`

### Preparação de Conteúdo
- [ ] Revisar todas as notas do professor (72 slides)
- [ ] Ensaiar a DEMO (Slide 43) — rodar pelo menos 2x antes
- [ ] Confirmar 3 padrões de conversação (CAMEL, AutoGen, Swarm) com exemplos
- [ ] Preparar template de schema JSON em branco para o exercício (Slide 64)
- [ ] Confirmar que todos os diagramas estão legíveis no projetor
- [ ] Preparar handout (opcional): storyboard impresso

### Preparação de Logística
- [ ] Sala reservada para 90 min + 15 min de buffer
- [ ] Quadro branco disponível (para desenhar topologias improvisadas)
- [ ] Acesso ao repositório da especialização confirmado

---

## Durante a Aula

### Bloco 1 (45 min)
- [ ] **Slide 1-7 (8 min)**: Abertura — anotar nomes de alunos que participam
- [ ] **Slide 5**: Pergunta de mão levantada ("Quantos agentes antes do caos?")
- [ ] **Slide 9**: Mostrar as 3 topologias — confirmar se todos entenderam
- [ ] **Slide 10**: Mostrar o schema JSON — destacar o campo `version`
- [ ] **Slide 15**: Votação rápida dos 4 cenários — anotar resultados
- [ ] **Slide 17**: Mostrar os 3 padrões canônicos rapidamente
- [ ] **Slide 19**: Mostrar trace CAMEL — destacar inception prompting
- [ ] **Slide 20-21**: Mostrar GroupChat + selector vs round-robin
- [ ] **Slide 22-23**: Handoff vs delegação — é a distinção mais confundida
- [ ] **Slide 26**: Votação rápida — anotar resultados
- [ ] **Slide 29**: Mostrar o diagrama `blackboard.mmd` — destacar ausência de comunicação direta
- [ ] **Slide 31**: Tabela comparativa blackboard vs mensagens diretas
- [ ] **Slide 33**: Exercício em duplas (2 min) — blackboard ou mensagens
- [ ] Intervalo (5 min)

### Bloco 2 (45 min)
- [ ] **Slide 34-36 (3 min)**: Abertura do Actor Model + diagrama
- [ ] **Slide 37-38**: Encapsulamento e concorrência sem locks — conceito central
- [ ] **Slide 40**: Comparar Akka / Erlang / asyncio
- [ ] **Slide 42**: V/F "Actor model é mais lento" — votação rápida
- [ ] **Slide 43 (4 min)**: DEMO AO VIVO — se API falhar, usar screenshots
- [ ] **Slide 44**: Pergunta da DEMO — deixar 2 min em duplas
- [ ] **Slide 45-49 (5 min)**: Negociação — bargaining, auction, diagrama
- [ ] **Slide 50**: Voting vs mediator — votação rápida
- [ ] **Slide 51**: Convergência e deadlock — destacar max_rounds
- [ ] **Slide 54-56**: A2A Protocol + MCP vs A2A — é a comparação mais importante
- [ ] **Slide 61-62**: Boas práticas e anti-patterns — pedir exemplos da turma
- [ ] **Slide 63**: Caso MetaGPT — destacar SOPs > chat livre
- [ ] **Slide 64 (4 min)**: Exercício de schema A2A em duplas
- [ ] **Slide 65-66**: Resumo e checklist
- [ ] **Slide 67-70 (4 min)**: Quiz — individual, sem consulta
- [ ] **Slide 71-72**: Conexão, projeto, labs e Q&A

---

## Pós-Aula

### Avaliação
- [ ] Contar resultados do quiz (≥3 acertos = compreensão básica)
- [ ] Anotar perguntas frequentes no Q&A para futuras iterações
- [ ] Pedir feedback informal: "Um padrão de comunicação que você não conhecia"
- [ ] Verificar tempo real vs planejado por seção

### Follow-up
- [ ] Enviar leitura recomendada no Slack/email (AutoGen + CAMEL papers)
- [ ] Disponibilizar slides (PDF + repositório)
- [ ] Lembrar prazo do Lab 1 (1 semana) — Duas Arquiteturas
- [ ] Lembrar prazo do Projeto (2 semanas) — sistema de negociação
- [ ] Preparar ETHAGT10 (Padrões de Arquitetura Multi-Agente — a próxima aula aprofunda topologias completas)

---

## Sinais de Alerta Durante a Aula

| Sinal | Ação |
|---|---|
| Alunos confundem handoff com delegação (Slide 22-23) | Refazer no quadro: handoff = "transfere a chamada", delegação = "coloca em espera" |
| DEMO falha (Slide 43) | Screenshots dos traces + seguir |
| Tempo estourado no Bloco 1 | Cortar Slide 26 (votação), mover para homework |
| Tempo estourado no Bloco 2 | Reduzir quiz para 2 perguntas (Slides 67-68); FIPA (Slide 58) como leitura |
| Nenhuma pergunta no Q&A | Fazer pergunta inversa: "Qual parte foi menos clara?" |
| Alunos sem ETHAGT04 | Revisar rapidamente o loop ReAct no Slide 5 |
| Confusão sobre MCP vs A2A | Reforçar Slide 56: MCP = agent↔ferramentas, A2A = agent↔agent |
