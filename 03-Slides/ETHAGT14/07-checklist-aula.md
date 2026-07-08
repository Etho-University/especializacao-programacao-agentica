# ETHAGT14 — Checklist da Aula

> Checklist para o professor verificar antes, durante e depois da aula.

---

## Pré-Aula (24h antes)

### Preparação Técnica
- [ ] API key (Anthropic ou OpenAI) testada e funcionando
- [ ] Redis local testado: `redis-cli ping` → PONG
- [ ] Python 3.11+ instalado e com dependências (`anthropic`, `redis`, `openai`, `numpy`)
- [ ] VS Code aberto com `05-Labs/ETHAGT14/Lab1-Cache-Semantico/main.py`
- [ ] Terminal testado: `python main.py` executa sem erro
- [ ] Cache pré-populado (plano B robusto se rate limit na DEMO)
- [ ] Screenshot do before/after salvo (plano B se demo falhar)
- [ ] Projetor testado
- [ ] Slides exportados para PDF (plano B se apresentação falhar)
- [ ] Mockup de dashboard Grafana (Slide 59) salvo como imagem
- [ ] Diagramas Mermaid renderizados (3 existentes + verificação visual)

### Preparação de Conteúdo
- [ ] Revisar todas as notas do professor (75 slides)
- [ ] Ensaiar a DEMO (Slide 26) — rodar pelo menos 2x antes
- [ ] Preparar o exercício de routing (Slide 38) — 6 tarefas impressas
- [ ] Preparar o exercício de circuit breaker (Slide 62) — template de código
- [ ] Confirmar que todos os diagramas estão legíveis
- [ ] Preparar handout (opcional): storyboard impresso

### Preparação de Logística
- [ ] Sala reservada para 90 min + 15 min de buffer
- [ ] Quadro branco disponível (para diagramar sharding/FinOps improvisados)
- [ ] Acesso ao repositório da especialização confirmado
- [ ] Calculadora ou planilha para exercícios de custo em tempo real

---

## Durante a Aula

### Bloco 1 (45 min)
- [ ] **Slide 1-6 (8 min)**: Abertura — anotar nomes de alunos que participam
- [ ] **Slide 5**: Fazer a pergunta de mão levantada ("Qual o maior custo oculto?")
- [ ] **Slide 8**: Destacar TTFT vs TPOT — confusão comum
- [ ] **Slide 9**: Mostrar crescimento quadrático (cálculo soma triangular)
- [ ] **Slide 11**: Desenhar sharding no quadro se a turma estiver confusa
- [ ] **Slide 12**: Destacar que este é o diagrama-chave da aula
- [ ] **Slide 14**: Pergunta aberta — deixar 3 min, anotar respostas
- [ ] **Slide 16**: Estabelecer que caching = primeira otimização
- [ ] **Slide 19**: Mostrar código do cache semântico
- [ ] **Slide 20**: Duplas (2 min) — discutir threshold ideal
- [ ] **Slide 26 (5 min)**: DEMO AO VIVO — se rate limit, mostrar pré-populado
- [ ] **Slide 27**: Quantificar antes/depois (números reais da demo)
- [ ] **Slide 29**: Votação rápida — 5 cenários, anotar resultados
- [ ] Intervalo (5 min)

### Bloco 2 (45 min)
- [ ] **Slide 30-36 (8 min)**: Routing e otimização
- [ ] **Slide 36**: Matriz de otimização — defender ordem caching → routing → batching
- [ ] **Slide 38**: Votação rápida — 6 tarefas, anotar modelo escolhido
- [ ] **Slide 42**: Mostrar diagrama de sharding (sharding.mmd)
- [ ] **Slide 47**: Duplas (2 min) — stateless é sempre preferível?
- [ ] **Slide 53**: Pie chart — custo de LLM é só 65% do total
- [ ] **Slide 57**: Triângulo de trade-offs — qual eixo é prioritário?
- [ ] **Slide 58**: Fluxo FinOps — loop fechado medir → alertar → otimizar
- [ ] **Slide 59**: Mostrar mockup de dashboard
- [ ] **Slide 61**: Código do circuit breaker
- [ ] **Slide 62 (4 min)**: Exercício em duplas — circuit breaker
- [ ] **Slide 64-65**: Boas práticas e anti-patterns — pedir exemplos da turma
- [ ] **Slide 66**: Caso de estudo — destacar −73% de custo
- [ ] **Slide 67-68**: Resumo e checklist
- [ ] **Slide 69-71 (3 min)**: Quiz — individual, sem consulta
- [ ] **Slide 72**: Perguntas de discussão se houver tempo
- [ ] **Slide 73-74**: Conexão, leitura, projeto, labs
- [ ] **Slide 75 (2 min)**: Q&A

---

## Pós-Aula

### Avaliação
- [ ] Contar resultados do quiz (≥2 acertos = compreensão básica)
- [ ] Anotar perguntas frequentes no Q&A para futuras iterações
- [ ] Pedir feedback informal: "Qual técnica você vai aplicar primeiro?"
- [ ] Verificar tempo real vs planejado por seção
- [ ] Avaliar engajamento nos exercícios (Slide 38, 62)

### Follow-up
- [ ] Enviar leitura recomendada no Slack/email (Kleppmann cap. 5-6, 9; FinOps Foundation)
- [ ] Disponibilizar slides (PDF + repositório)
- [ ] Lembrar prazo do Lab 1 (Cache Semântico, 1 semana)
- [ ] Lembrar prazo do Lab 2 (Sharding por Tenant, 2 semanas)
- [ ] Lembrar prazo do Projeto (otimização ≥40%, 2 semanas)
- [ ] Preparar ETHAGT15 (Meta-Agentes — próxima aula)

---

## Sinais de Alerta Durante a Aula

| Sinal | Ação |
|---|---|
| Alunos confusos no crescimento quadrático (Slide 9) | Desenhar no quadro: step 1 = 1k, step 2 = 3k, step 3 = 6k... |
| DEMO falha por rate limit | Mostrar cache pré-populado (hit path apenas) |
| Discussão de pricing (Slide 60) drena tempo | Tabelar; prometer seguimento no Slack |
| Tempo estourado no Bloco 1 | Cortar exercício do Slide 29; mover para homework |
| Tempo estourado no Bloco 2 | Reduzir quiz para 2 perguntas; referências como leitura |
| Nenhuma pergunta no Q&A | Fazer pergunta inversa: "Qual técnica vão aplicar primeiro?" |
| Alunos sem background de K8s (Slide 50) | Focar em conceitos, não manifests; direcionar para ETHAGT11 |
| Confusão sobre stateless vs stateful (Slide 41) | Usar analogia do caixa de banco vs gerente de conta |
