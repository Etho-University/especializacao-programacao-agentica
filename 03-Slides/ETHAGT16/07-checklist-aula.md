# ETHAGT16 — Checklist da Aula

> Checklist para o professor verificar antes, durante e depois da aula.

---

## Pré-Aula (24h antes)

### Preparação Técnica
- [ ] API key (OpenAI ou Anthropic) testada e funcionando
- [ ] Python 3.11+ instalado e com dependências (`openai`, `langgraph`, `autogen` se usado)
- [ ] VS Code aberto com `05-Labs/ETHAGT16/Lab1-Mini-Sociedade/main.py`
- [ ] Terminal testado: `python main.py` executa sem erro
- [ ] Screenshot do trace da DEMO Mini Sociedade salvo (plano B se API falhar)
- [ ] Projetor testado
- [ ] Slides exportados para PDF (plano B se apresentação falhar)
- [ ] Paper fake do exercício do Slide 46 preparado

### Preparação de Conteúdo
- [ ] Revisar todas as notas do professor (50 slides)
- [ ] Ensaiar a DEMO Mini Sociedade (Slide 30) — rodar pelo menos 2x antes
- [ ] Preparar trace de interações para o exercício de emergência (Slide 41)
- [ ] Confirmar que todos os 3 diagramas `.mmd` existentes estão legíveis
- [ ] Preparar handout (opcional): storyboard impresso

### Preparação de Logística
- [ ] Sala reservada para 50 min + 15 min de buffer
- [ ] Quadro branco disponível
- [ ] Acesso ao repositório da especialização confirmado

---

## Durante a Aula

### Bloco 1 (25 min)
- [ ] **Slide 1-6 (6 min)**: Abertura — anotar quem participou do ETHAGT15
- [ ] **Slide 5**: Hook — "O que acontece quando 100 agentes interagem sem supervisão humana?"
- [ ] **Slide 9**: Anotar qual papel a turma considera mais difícil de automatizar
- [ ] **Slide 13**: Mostrar `society.mmd` — destacar normas governando a sociedade
- [ ] **Slide 15**: Exercício em duplas (1 min) — comitê editorial
- [ ] **Slide 17**: Mapa de Smallville — mencionar Valentine's Day emergente
- [ ] **Slide 18**: Animar o pipeline Memory → Reflection → Action
- [ ] **Slide 20**: Hook sobre simulação = predição?
- [ ] **Slide 22**: Exercício em duplas (1 min) — home office
- [ ] Intervalo (5 min)

### Bloco 2 (25 min)
- [ ] **Slide 23-25 (2 min)**: Seção Research + pipeline
- [ ] **Slide 26-27**: AI Scientist — mencionar $15/paper e ICLR
- [ ] **Slide 28**: AlphaEvolve — multiplicação de matrizes
- [ ] **Slide 30 (3 min)**: DEMO AO VIVO — se API falhar, usar screenshot
- [ ] **Slide 31**: Pergunta da DEMO — deixar 1 min em duplas
- [ ] **Slide 32-33**: Estudo de caso AI Scientist — o que funcionou / falhou
- [ ] **Slide 36**: Mostrar `emergence.mmd`
- [ ] **Slide 37**: Desejada vs indesejada — pedir exemplos da turma
- [ ] **Slide 41 (1 min)**: Exercício de detectar emergência indesejada
- [ ] **Slide 44**: Hook ético — "Onde você traça a linha?"
- [ ] **Slide 46 (3 min)**: Exercício em grupos — 3 critérios de qualidade científica
- [ ] **Slide 48 (1 min)**: Quiz — individual, sem consulta
- [ ] **Slide 49**: Conexão com Capstone (ETHAGT90)
- [ ] **Slide 50 (1 min)**: Q&A

---

## Pós-Aula

### Avaliação
- [ ] Contar resultados do quiz (≥2 acertos em 3 = compreensão básica)
- [ ] Anotar perguntas frequentes no Q&A para futuras iterações
- [ ] Pedir feedback informal: "O que vocês querem investigar no Capstone?"
- [ ] Verificar tempo real vs planejado por seção

### Follow-up
- [ ] Enviar leitura recomendada no Slack/email (Park et al., Lu et al., Chen et al.)
- [ ] Disponibilizar slides (PDF + repositório)
- [ ] Lembrar prazo do Lab 1 (Mini Sociedade)
- [ ] Lembrar prazo do Projeto (sistema de pesquisa autônoma)
- [ ] Preparar ETHAGT90 — Capstone: integrar tudo

---

## Sinais de Alerta Durante a Aula

| Sinal | Ação |
|---|---|
| Alunos confusos no Slide 8 (níveis) | Simplificar: focar só em Grupo vs Sociedade |
| DEMO falha | Screenshot do trace pré-gravado + seguir |
| Tempo estourado no Bloco 1 | Cortar Slide 22 (home office); mover para homework |
| Tempo estourado no Bloco 2 | Reduzir quiz para 1 pergunta (Slide 48) |
| Debate ético (Slide 44) tomam tempo demais | Limite de 2 min; coletar perguntas para o Q&A |
| Nenhuma pergunta no Q&A | Fazer pergunta inversa: "Qual parte foi menos clara?" |
| Alunos sem ETHAGT15 | Revisar multi-agent básico em 3 min antes do Slide 8 |
