# ETHAGT10 — Checklist da Aula

> Checklist para o professor verificar antes, durante e depois da aula.

---

## Pré-Aula (24h antes)

### Preparação Técnica
- [ ] API key (OpenAI ou Anthropic) testada e funcionando
- [ ] Python 3.11+ instalado com dependências (`langgraph`, `openai`, `python-dotenv`)
- [ ] VS Code aberto com `05-Labs/ETHAGT10/Lab1-Hierarchical-Teams` e `Lab2-Swarm-vs-Supervisor`
- [ ] Terminal testado: ambos os labs executam sem erro
- [ ] Screenshot do trace hierarchical salvo (plano B se API falhar — Slide 24)
- [ ] Screenshot dos traces comparativos swarm vs supervisor salvos (plano B — Slide 51)
- [ ] Projetor testado
- [ ] Slides exportados para PDF (plano B se apresentação falhar)

### Preparação de Conteúdo
- [ ] Revisar todas as notas do professor (62 slides)
- [ ] Ensaiar a DEMO 1 (Slide 24 — hierarchical teams) — rodar pelo menos 2x antes
- [ ] Ensaiar a DEMO 2 (Slide 51 — swarm vs supervisor) — rodar pelo menos 2x antes
- [ ] Confirmar que todos os diagramas estão legíveis (32 diagramas)
- [ ] Revisar `10-Architecture/architectures/catalog.md` (12 topologias)
- [ ] Preparar handout (opcional): storyboard impresso

### Preparação de Logística
- [ ] Sala reservada para 90 min + 15 min de buffer
- [ ] Quadro branco disponível (para desenhar topologias)
- [ ] Acesso ao repositório da especialização confirmado
- [ ] Template de ADR disponível em `08-ADRs/ETHAGT10/`

---

## Durante a Aula

### Bloco 1 (45 min)
- [ ] **Slide 1-6 (8 min)**: Abertura — anotar nomes de alunos que participam
- [ ] **Slide 5**: Fazer a pergunta de mão levantada ("Qual topologia mais comum que usaram?")
- [ ] **Slide 8**: Mostrar o grid de 12 topologias — garantir visão panorâmica
- [ ] **Slide 9**: Destacar o eixo centralizado ↔ descentralizado
- [ ] **Slide 16**: Votação rápida de matching — anotar resultados
- [ ] **Slide 18**: Mostrar o diagrama supervisor (`supervisor-topology.mmd`)
- [ ] **Slide 19**: Destacar que supervisor = ReAct com tools (LangGraph)
- [ ] **Slide 20**: Mostrar hierarchical (`hierarchical-topology.mmd`)
- [ ] **Slide 24 (4 min)**: DEMO 1 AO VIVO — se API falhar, usar screenshot
- [ ] **Slide 25**: Pergunta da demo — deixar 2 min em duplas
- [ ] **Slide 26**: Conectar a MetaGPT (arXiv:2308.00352)
- [ ] **Slide 28**: Votação hierarchical vs flat — anotar resultados
- [ ] **Slide 30**: Mostrar swarm (`swarm-topology.mmd`)
- [ ] **Slide 33**: Tabela swarm vs supervisor — destacar que não há vencedor
- [ ] **Slide 34**: Discussão aberta — deixar 3 min
- [ ] Intervalo (5 min)

### Bloco 2 (45 min)
- [ ] **Slide 36-39 (6 min)**: Pipeline e orchestrator-workers
- [ ] **Slide 38**: Destacar composição (hybrid é a regra em produção)
- [ ] **Slide 40**: Exercício pipeline ou agente — votação
- [ ] **Slide 42-45 (6 min)**: Event-driven, actor, mesh, blackboard
- [ ] **Slide 46**: Discussão mesh vs hierarchical — deixar 3 min
- [ ] **Slide 48-50 (5 min)**: Tree e recursive
- [ ] **Slide 50**: Destacar que recursive precisa de guardrails (max_depth)
- [ ] **Slide 51 (4 min)**: DEMO 2 AO VIVO — swarm vs supervisor
- [ ] **Slide 52**: Discussão dos resultados — 2 min em duplas
- [ ] **Slide 54**: Mostrar a matriz de decisão (`decision-matrix.mmd`)
- [ ] **Slide 55**: Apresentar a estrutura do ADR
- [ ] **Slide 57**: Caso MetaGPT — destacar SOPs como chave
- [ ] **Slide 58 (4 min)**: Exercício 6 cenários + ADR em grupos
- [ ] **Slide 59**: Resumo + checklist
- [ ] **Slide 60 (2 min)**: Quiz — individual, sem consulta
- [ ] **Slide 61**: Conexões com próximos módulos + leitura
- [ ] **Slide 62 (2 min)**: Q&A

---

## Pós-Aula

### Avaliação
- [ ] Contar resultados do quiz (≥2 acertos = compreensão básica)
- [ ] Anotar perguntas frequentes no Q&A para futuras iterações
- [ ] Pedir feedback informal: "Uma topologia que você não conhecia"
- [ ] Verificar tempo real vs planejado por seção
- [ ] Avaliar qualidade dos ADRs produzidos no exercício (Slide 58)

### Follow-up
- [ ] Enviar leitura recomendada no Slack/email (MetaGPT paper)
- [ ] Disponibilizar slides (PDF + repositório)
- [ ] Lembrar prazo do Lab 1 (Hierarchical Teams) — antes da próxima aula
- [ ] Lembrar prazo do Lab 2 (Swarm vs Supervisor)
- [ ] Lembrar prazo do Projeto do módulo (topologia + ADR + benchmark)
- [ ] Preparar ETHAGT11 (a próxima aula aprofunda event-driven)

---

## Sinais de Alerta Durante a Aula

| Sinal | Ação |
|---|---|
| Alunos confusos no Slide 8 (12 topologias) | Simplificar: focar nos 5 grupos (centralizadas, fluxo, descentralizadas, estruturadas, híbridas) |
| DEMO 1 falha (Slide 24) | Screenshot do trace hierarchical + seguir |
| DEMO 2 falha (Slide 51) | Traces comparativos salvos + seguir |
| Tempo estourado no Bloco 1 | Cortar exercício Slide 28 (votação), mover para homework |
| Tempo estourado no Bloco 2 | Reduzir quiz para 2 perguntas; Slide 57 como leitura |
| Nenhuma pergunta no Q&A | Fazer pergunta inversa: "Qual topologia vocês usariam no projeto de vocês?" |
| Alunos sem pré-requisito de LangGraph | Direcionar para ETHAGT09; oferecer pair programming nos labs |
| Turma vota "supervisor" para tudo | Provocar: "E se não precisar síntese? Swarm não seria melhor?" |
