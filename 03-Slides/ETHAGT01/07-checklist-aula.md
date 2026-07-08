# ETHAGT01 — Checklist da Aula

> Checklist para o professor verificar antes, durante e depois da aula.

---

## Pré-Aula (24h antes)

### Preparação Técnica
- [ ] API key (OpenAI ou Anthropic) testada e funcionando
- [ ] Python 3.11+ instalado e com dependências (`openai`, `python-dotenv`)
- [ ] VS Code aberto com `19-Examples/ETHAGT01/exemplo-01-react-loop/main.py`
- [ ] Terminal testado: `python main.py` executa sem erro
- [ ] Screenshot do trace de execução salvo (plano B se API falhar)
- [ ] Projetor testado
- [ ] Slides exportados para PDF (plano B se apresentação falhar)

### Preparação de Conteúdo
- [ ] Revisar todas as notas do professor (62 slides)
- [ ] Ensaiar a demo (Slide 21) — rodar pelo menos 2x antes
- [ ] Preparar o trace quebrado do exercício (Slide 47)
- [ ] Confirmar que todos os diagramas estão legíveis
- [ ] Preparar handout (opcional): storyboard impresso

### Preparação de Logística
- [ ] Sala reservada para 90 min + 15 min de buffer
- [ ] Quadro branco disponível
- [ ] Acesso ao repositório da especialização confirmado

---

## Durante a Aula

### Bloco 1 (45 min)
- [ ] **Slide 1-6 (8 min)**: Abertura — anotar nomes de alunos que participam
- [ ] **Slide 5**: Fazer a pergunta de mão levantada ("Quem já falhou com ChatGPT?")
- [ ] **Slide 8**: Anotar definições que a turma usa
- [ ] **Slide 9**: Mostrar o hexágono da taxonomia
- [ ] **Slide 12**: Destacar que este é o slide mais importante
- [ ] **Slide 18**: Animar o loop ReAct — garantir que todos entendem o ciclo
- [ ] **Slide 21 (5 min)**: DEMO AO VIVO — se API falhar, usar screenshot
- [ ] **Slide 22**: Pergunta da demo — deixar 2 min em duplas
- [ ] **Slide 25**: Mostrar os 5 workflows rapidamente
- [ ] **Slide 28**: Votação rápida — anotar resultados
- [ ] Intervalo (5 min)

### Bloco 2 (45 min)
- [ ] **Slide 30-35 (15 min)**: Comparação de frameworks
- [ ] **Slide 36**: Discussão aberta — deixar 3 min
- [ ] **Slide 38-41 (8 min)**: Observabilidade
- [ ] **Slide 43-44**: Boas práticas e anti-patterns — pedir exemplos da turma
- [ ] **Slide 45-46**: Caso SWE-bench — destacar a lição ACI
- [ ] **Slide 47 (3 min)**: Exercício de trace quebrado em duplas
- [ ] **Slide 48-49**: Resumo e checklist
- [ ] **Slide 50-54 (5 min)**: Quiz — individual, sem consulta
- [ ] **Slide 55**: Perguntas de discussão se houver tempo
- [ ] **Slide 56-61**: Conexão, leitura, projeto, labs, próximos passos
- [ ] **Slide 62 (2 min)**: Q&A

---

## Pós-Aula

### Avaliação
- [ ] Contar resultados do quiz (≥3 acertos = compreensão básica)
- [ ] Anotar perguntas frequentes no Q&A para futuras iterações
- [ ] Pedir feedback informal: "Uma coisa que você aprendeu hoje"
- [ ] Verificar tempo real vs planejado por seção

### Follow-up
- [ ] Enviar leitura recomendada no Slack/email
- [ ] Disponibilizar slides (PDF + repositório)
- [ ] Lembrar prazo do Lab 1 (1 semana)
- [ ] Lembrar prazo do Projeto (2 semanas)
- [ ] Preparar ETHAGT02 (a próxima aula aprofunda ACI)

---

## Sinais de Alerta Durante a Aula

| Sinal | Ação |
|---|---|
| Alunos confusos no Slide 9 (taxonomia) | Simplificar: focar só em Brain + Action + Tool Use |
| DEMO falha | Screenshot do trace + seguir |
| Tempo estourado no Bloco 1 | Cortar Slide 28 (votação), mover para homework |
| Tempo estourado no Bloco 2 | Reduzir quiz para 3 perguntas (Slides 50-52) |
| Nenhuma pergunta no Q&A | Fazer pergunta inversa: "Qual parte foi menos clara?" |
| Alunos sem pré-requisito de Python | Direcionar para ETHDEV07, oferecer pair programming |
