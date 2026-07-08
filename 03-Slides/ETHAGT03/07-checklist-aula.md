# ETHAGT03 — Checklist da Aula

> Checklist para o professor verificar antes, durante e depois da aula.

---

## Pré-Aula (24h antes)

### Preparação Técnica
- [ ] API key (OpenAI ou Anthropic) testada e funcionando
- [ ] Python 3.11+ instalado com dependências (`openai`, `asyncio`, `python-dotenv`)
- [ ] VS Code aberto com snippets dos 5 workflows (prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer)
- [ ] Terminal testado: scripts de demo executam sem erro
- [ ] Screenshot do DEMO de latência (serial vs paralelo) salvo como plano B
- [ ] Projetor testado
- [ ] Slides exportados para PDF (plano B se apresentação falhar)

### Preparação de Conteúdo
- [ ] Revisar todas as notas do professor (63 slides)
- [ ] Ensaiar a DEMO de latência (Slide 31) — rodar pelo menos 2x antes
- [ ] Confirmar que todos os diagramas `.mmd` estão renderizados e legíveis
- [ ] Preparar os 5 cenários do exercício final (Slide 60) em cards
- [ ] Preparar o gabarito do quiz (Slides 56-59)
- [ ] Preparar handout (opcional): storyboard impresso

### Preparação de Logística
- [ ] Sala reservada para 90 min + 15 min de buffer
- [ ] Quadro branco disponível (para matriz de trade-offs e DAG de dependências)
- [ ] Acesso ao repositório da especialização confirmado
- [ ] Diagramas de `12-Diagrams/ETHAGT03/` acessíveis

---

## Durante a Aula

### Bloco 1 (45 min)
- [ ] **Slide 1-5 (6 min)**: Abertura — anotar nomes de alunos que participam
- [ ] **Slide 5**: Fazer a pergunta de mão levantada ("Quem já viu projeto que usou agente onde um if bastava?")
- [ ] **Slide 7**: Mostrar a pirâmide de níveis — garantir que todos entendem "comece simples"
- [ ] **Slide 8**: Recap workflow vs agente — medir se turma lembra de ETHAGT01
- [ ] **Slide 9**: Mostrar os 5 workflows rapidamente (grid)
- [ ] **Slide 12**: Animar o prompt chaining — destacar gates em cor diferente
- [ ] **Slide 15**: Código de prompt chaining — highlight dos gates
- [ ] **Slide 16 (2 min)**: Exercício de gate em tradução — duplas
- [ ] **Slide 19**: Routing por modelo — destacar Haiku vs Sonnet
- [ ] **Slide 21**: Matriz de confusão — garantir que turma entende precision/recall
- [ ] **Slide 23 (2 min)**: Exercício de avaliação do router — duplas
- [ ] **Slide 25-26**: Sectioning vs voting — destacar a diferença
- [ ] **Slide 29**: Erros comuns — pedir exemplos da turma
- [ ] **Slide 31 (2 min)**: DEMO AO VIVO de latência — se API falhar, usar screenshot
- [ ] **Slide 32**: Votação voting vs sectioning — anotar resultados
- [ ] Intervalo (5 min)

### Bloco 2 (45 min)
- [ ] **Slide 34**: Distinção paralelização vs orchestrator — o slide mais importante do bloco
- [ ] **Slide 36**: Diagrama orchestrator-workers — conectar com papers
- [ ] **Slide 39**: V/F "orchestrator é sempre melhor" — votação
- [ ] **Slide 41**: Loop do evaluator — garantir que todos vêem o ciclo
- [ ] **Slide 42**: 3 condições para evaluator ter valor
- [ ] **Slide 44**: Critérios de parada — destacar "sempre ≥2 critérios"
- [ ] **Slide 46 (2 min)**: Exercício de condição de parada — duplas
- [ ] **Slide 48**: Composição routing→parallel→evaluator
- [ ] **Slide 49**: Debate workflow composto vs agente — deixar 2 min
- [ ] **Slide 51**: Tabela de trade-offs — peçam para fotografar
- [ ] **Slide 53**: Caso Coinbase/Intercom
- [ ] **Slide 54-55**: Resumo e checklist
- [ ] **Slide 56-59 (4 min)**: Quiz — individual, sem consulta
- [ ] **Slide 60 (5 min)**: Exercício dos 5 cenários — grupos
- [ ] **Slide 61**: Projeto e labs — destacar importância do ADR
- [ ] **Slide 62**: Referências e próximos módulos
- [ ] **Slide 63 (2 min)**: Q&A

---

## Pós-Aula

### Avaliação
- [ ] Contar resultados do quiz (≥3 acertos = compreensão básica)
- [ ] Anotar justificativas do exercício de 5 cenários (Slide 60) — avaliar profundidade
- [ ] Anotar perguntas frequentes no Q&A para futuras iterações
- [ ] Pedir feedback informal: "Um padrão que você não conhecia e vai usar amanhã"
- [ ] Verificar tempo real vs planejado por seção

### Follow-up
- [ ] Enviar leitura recomendada no Slack/email (Anthropic Building Effective Agents)
- [ ] Disponibilizar slides (PDF + repositório)
- [ ] Lembrar prazo do Lab 1 ("Os 5 em 1 dia")
- [ ] Lembrar prazo do Lab 2 ("Composição")
- [ ] Lembrar prazo do Projeto (síntese de relatório + ADR)
- [ ] Preparar ETHAGT04 (a próxima aula aprofunda reasoning e planning)

---

## Sinais de Alerta Durante a Aula

| Sinal | Ação |
|---|---|
| Alunos confundem gate com evaluator (Slide 12) | Reapresentar: gate = código, evaluator = LLM |
| DEMO de latência falha (Slide 31) | Screenshot do timer + seguir |
| Confusão parallelization vs orchestrator (Slide 34) | Exemplo no quadro: "fontes fixas vs fontes dinâmicas" |
| Tempo estourado no Bloco 1 | Cortar exercício do Slide 16; mover para homework |
| Tempo estourado no Bloco 2 | Reduzir quiz para 2 perguntas (Slides 56-57) |
| Nenhuma pergunta no Q&A | Fazer pergunta inversa: "Qual padrão foi menos claro?" |
| Alunos sem ETHAGT01 | Revisar recap do Slide 8 com mais tempo; oferecer material |
| Turma travando em rubric (Slide 43) | Exemplificar com rubric do ENEM (conhecida) |
