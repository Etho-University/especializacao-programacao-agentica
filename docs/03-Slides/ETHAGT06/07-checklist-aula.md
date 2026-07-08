# ETHAGT06 — Checklist da Aula

> Checklist para o professor verificar antes, durante e depois da aula.

---

## Pré-Aula (24h antes)

### Preparação Técnica
- [ ] API key (OpenAI ou Anthropic) testada e funcionando
- [ ] Python 3.11+ instalado e com dependências (`langgraph`, `langchain`, `qdrant-client`, `ragas`, `cohere`)
- [ ] VS Code aberto com `05-Labs/ETHAGT06/Lab2-Agentic-RAG-Multi-Hop`
- [ ] Terminal testado: `python main.py` executa sem erro
- [ ] Vector DB (Qdrant ou Milvus) populado com corpus de exemplo
- [ ] Screenshot do trace multi-hop salvo (plano B se API falhar)
- [ ] Dataset de holdout de exemplo pronto para demo de avaliação (Slide 72)
- [ ] Resultado pré-computado do Ragas (caso demo ao vivo demore)
- [ ] Projetor testado
- [ ] Slides exportados para PDF (plano B se apresentação falhar)

### Preparação de Conteúdo
- [ ] Revisar todas as notas do professor (85 slides)
- [ ] Ensaiar a demo multi-hop (Slide 53) — rodar pelo menos 2x antes
- [ ] Preparar as 5 perguntas do exercício de routing (Slide 23)
- [ ] Preparar o cenário do exercício Adaptive vs Self-RAG (Slide 44)
- [ ] Preparar os 3 cenários do exercício de estratégia (Slide 66)
- [ ] Confirmar que todos os diagramas estão legíveis (especialmente adaptive-rag.mmd, crag-flow.mmd, eval-pipeline.mmd)
- [ ] Preparar handout (opcional): storyboard impresso

### Preparação de Logística
- [ ] Sala reservada para 110 min + 15 min de buffer
- [ ] Quadro branco disponível
- [ ] Acesso ao repositório da especialização confirmado

---

## Durante a Aula

### Bloco 1 (~58 min)
- [ ] **Slide 1-7 (8 min)**: Abertura — anotar nomes de alunos que participam
- [ ] **Slide 6**: Fazer a pergunta de mão levantada ("RAG com resposta errada e alta confiança?")
- [ ] **Slide 7**: Mostrar a timeline de evolução do RAG
- [ ] **Slide 9**: Destacar os 4 pontos de falha do pipeline ingênuo
- [ ] **Slide 14**: Pergunta de discussão — "Pior falha: não responder ou responder errado?"
- [ ] **Slide 19**: Mostrar o diagrama `adaptive-rag.mmd` — garantir que todos entendem os 3 caminhos
- [ ] **Slide 23**: Votação rápida — anotar resultados
- [ ] **Slide 28**: Mostrar o diagrama `crag-flow.mmd` — destacar o avaliador como coração
- [ ] **Slide 32**: Código do retrieval evaluator — explicar o Pydantic model
- [ ] **Slide 38**: Mostrar o fluxo Self-RAG com tokens de reflexão
- [ ] **Slide 42**: Tabela comparativa Adaptive/CRAG/Self-RAG — slide-chave
- [ ] **Slide 44**: Exercício em duplas (5 min) — FAQ jurídico
- [ ] Intervalo (5 min)

### Bloco 2 (~52 min)
- [ ] **Slide 46-48**: Agentic RAG — enfatizar a diferença pipeline fixo vs loop de agente
- [ ] **Slide 49**: Trace multi-hop detalhado — linhas aparecem em sequência
- [ ] **Slide 53 (2 min)**: DEMO AO VIVO — se API falhar, usar screenshot
- [ ] **Slide 54**: Pergunta da demo — deixar 2 min em duplas
- [ ] **Slide 55**: Escalada das 4 arquiteturas — slide-chave de sistematização
- [ ] **Slide 59**: Late chunking / Contextual Retrieval — novidade 2024
- [ ] **Slide 62**: HyDE — analogia resposta hipotética
- [ ] **Slide 66**: Exercício em duplas (2 min) — escolher estratégia
- [ ] **Slide 69-70**: Métricas faithfulness e context precision/recall
- [ ] **Slide 72**: Mostrar o diagrama `eval-pipeline.mmd`
- [ ] **Slide 75-76**: Boas práticas e anti-patterns — pedir exemplos da turma
- [ ] **Slide 79-81 (3 min)**: Quiz — individual, sem consulta
- [ ] **Slide 83**: Referências completas
- [ ] **Slide 84**: Projeto do módulo — explicar critério de sucesso (faithfulness ≥ 0.85)
- [ ] **Slide 85 (1 min)**: Q&A

---

## Pós-Aula

### Avaliação
- [ ] Contar resultados do quiz (≥2 acertos = compreensão básica)
- [ ] Anotar perguntas frequentes no Q&A para futuras iterações
- [ ] Pedir feedback informal: "Uma técnica de RAG que você vai aplicar esta semana"
- [ ] Verificar tempo real vs planejado por seção

### Follow-up
- [ ] Enviar leitura recomendada no Slack/email (Asai Self-RAG, Anthropic Contextual Retrieval)
- [ ] Disponibilizar slides (PDF + repositório)
- [ ] Lembrar prazo do Lab 1 ("Diagnosticando falhas" — 4h)
- [ ] Lembrar prazo do Lab 2 ("Agentic RAG Multi-Hop" — 5h)
- [ ] Lembrar prazo do Projeto (sistema RAG + eval report + ADR)
- [ ] Preparar ETHAGT07 (Knowledge Graphs & Vector DBs — GraphRAG em profundidade)

---

## Sinais de Alerta Durante a Aula

| Sinal | Ação |
|---|---|
| Alunos confundem Adaptive RAG com CRAG | Voltar ao Slide 42 (tabela comparativa) |
| DEMO multi-hop falha | Screenshot do trace + seguir |
| Vector DB não conecta | Usar FAISS em memória como fallback |
| Tempo estourado no Bloco 1 | Cortar Slide 23 (votação), mover para homework |
| Tempo estourado no Bloco 2 | Reduzir quiz para 2 perguntas (Slides 79-80) |
| Turma sem ETHAGT04 | Fazer recap de 5 min do pipeline retrieve→generate no Slide 9 |
| Nenhuma pergunta no Q&A | Fazer pergunta inversa: "Qual das 4 arquiteturas você aplicaria no seu projeto?" |
| Alunos perdidos em tokens de reflexão | Simplificar: focar só em `[Retrieve]` e `[Fully supported]` |
