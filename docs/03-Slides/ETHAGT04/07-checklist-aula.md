# ETHAGT04 — Checklist da Aula

> Checklist para o professor verificar antes, durante e depois da aula.

---

## Pré-Aula (24h antes)

### Preparação Técnica
- [ ] API key (OpenAI ou Anthropic) testada e funcionando
- [ ] Python 3.11+ instalado com `langgraph`, `openai`, `langchain`
- [ ] VS Code aberto com notebooks LangGraph (`plan-and-execute.ipynb`, `lats.ipynb`, `reflexion.ipynb`)
- [ ] Terminal testado: notebooks executam sem erro
- [ ] Subset de GSM8K carregado (5 problemas para demo de ToT/Reflexion)
- [ ] Screenshot da árvore de busca ToT salvo (plano B)
- [ ] Screenshot de trace de reasoning do o1/o3 salvo (plano B)
- [ ] Projetor testado
- [ ] Slides exportados para PDF (plano B)

### Preparação de Conteúdo
- [ ] Revisar todas as notas do professor (90 slides)
- [ ] Ensaiar a demo de ToT (Slide 35) — desenhar a árvore no quadro
- [ ] Ensaiar a demo de Reflexion (Slide 50) — mostrar 3 tentativas
- [ ] Preparar o exercício de trade-off (Slide 77) — cenários prontos
- [ ] Confirmar que todos os 16 diagramas estão legíveis
- [ ] Atualizar tabela de custos (o1, o3, Claude, GPT-4o) — preços mudam
- [ ] Preparar handout (opcional): storyboard impresso

### Preparação de Logística
- [ ] Sala reservada para 120 min + 15 min de buffer
- [ ] Quadro branco disponível (essencial para desenhar árvores de busca)
- [ ] Acesso ao repositório da especialização confirmado
- [ ] Pré-requisito ETHAGT03 confirmado nos alunos

---

## Durante a Aula

### Bloco 1 (60 min)
- [ ] **Slide 1-7 (8 min)**: Abertura — anotar nível de experiência com reasoning
- [ ] **Slide 5**: Fazer a pergunta de mão levantada ("Quem já viu loop infinito?")
- [ ] **Slide 9**: Mostrar o espectro do raciocínio — slide âncora
- [ ] **Slide 11**: Desenhar linear vs árvore vs grafo no quadro
- [ ] **Slide 14-15**: CoT e Self-Consistency — garantir fundamentos claros
- [ ] **Slide 17**: Pergunta em duplas — deixar 2 min
- [ ] **Slide 21**: Destacar o diagrama plan-execute.mmd
- [ ] **Slide 24**: ReWOO — usar o quadro para mostrar variáveis #E1, #E2
- [ ] **Slide 27**: Votação rápida — anotar resultados
- [ ] **Slide 33**: Mostrar a árvore ToT no quadro — animar a poda
- [ ] **Slide 35 (3 min)**: DEMO ToT ao vivo — se API falhar, screenshot
- [ ] **Slide 37-41**: LATS — o bloco mais denso; controlar o tempo
- [ ] Intervalo (5 min)

### Bloco 2 (60 min)
- [ ] **Slide 46-55 (12 min)**: Reflexion — mostrar 3 tentativas na demo
- [ ] **Slide 51**: Grupo — discutir convergência e limite de tentativas
- [ ] **Slide 56-63 (8 min)**: Self-Discover — manter conciso
- [ ] **Slide 64-75 (14 min)**: Inference-time reasoning — bloco mais atual
- [ ] **Slide 66**: Destacar a diferença promptado vs nativo
- [ ] **Slide 73**: Duplas — "quando reasoning model substitui ToT?"
- [ ] **Slide 76-79**: Falhas e loops — conectar com experiência dos alunos
- [ ] **Slide 77 (3 min)**: Exercício de trade-off em duplas
- [ ] **Slide 80-84 (5 min)**: Quiz — individual, sem consulta
- [ ] **Slide 82**: Perguntas de discussão se houver tempo
- [ ] **Slide 85**: Árvore de decisão — slide mais útil para o projeto
- [ ] **Slide 86-87**: Boas práticas, anti-patterns, projeto
- [ ] **Slide 90 (2 min)**: Q&A

---

## Pós-Aula

### Avaliação
- [ ] Contar resultados do quiz (≥3 acertos = compreensão básica)
- [ ] Anotar perguntas frequentes no Q&A para futuras iterações
- [ ] Pedir feedback informal: "Qual técnica você vai testar primeiro?"
- [ ] Verificar tempo real vs planejado por seção (LATS costuma estourar)

### Follow-up
- [ ] Enviar leitura recomendada: papers canônicos (links arXiv)
- [ ] Disponibilizar slides (PDF + repositório)
- [ ] Lembrar prazo do Lab 1 (Plan-and-Execute vs ReAct)
- [ ] Lembrar prazo do Projeto (GAIA subset com 3 padrões)
- [ ] Preparar ETHAGT05 (a próxima aula aprofunda memória — conecta com Reflexion)

---

## Sinais de Alerta Durante a Aula

| Sinal | Ação |
|---|---|
| Alunos confusos em LATS/MCTS (Slides 37-41) | Simplificar: focar só em "busca em árvore com backtracking"; pular detalhes de UCB-1 |
| Tempo estourado no Bloco 1 | Cortar detalhes de MCTS (Slides 40-41); mover para leitura |
| DEMO de ToT falha | Screenshot da árvore + seguir |
| Alunos não veem diferença Reflexion vs Reflection simples | Re-desenhar o loop com memória persistente no quadro |
| Alunos questionam custo de Self-Discover | Mostrar que é uma composição única no início; cache entre tarefas |
| Nenhuma pergunta no Q&A | Fazer pergunta inversa: "Qual técnica parece mais promissora para seu caso?" |
| Alunos sem pré-requisito de ETHAGT03 | Revisar ReAct em 3 min (Slide 18) e oferecer material de recuperação |
