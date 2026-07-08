# ETHAGT07 — Checklist da Aula

> Checklist para o professor verificar antes, durante e depois da aula.

---

## Pré-Aula (24h antes)

### Preparação Técnica
- [ ] API key (OpenAI ou Anthropic) testada e funcionando
- [ ] Python 3.11+ instalado com dependências (`qdrant-client`, `neo4j`, `openai`, `langchain`)
- [ ] Neo4j rodando (Docker ou Neo4j Aura) e acessível
- [ ] Qdrant rodando (Docker) para referência no comparativo
- [ ] VS Code aberto com `05-Labs/ETHAGT07/Lab2-GraphRAG-Neo4j`
- [ ] Corpus técnico pré-carregado no Neo4j para DEMO (Slide 46)
- [ ] Terminal testado: a query Cypher multi-hop executa sem erro
- [ ] Screenshots do Neo4j Browser salvos (plano B se DEMO falhar)
- [ ] Projetor testado
- [ ] Slides exportados para PDF (plano B se apresentação falhar)

### Preparação de Conteúdo
- [ ] Revisar todas as notas do professor (80 slides)
- [ ] Ensaiar a DEMO do GraphRAG (Slide 46) — rodar pelo menos 2x antes
- [ ] Preparar a pergunta multi-hop que vector RAG falha e GraphRAG acerta
- [ ] Confirmar que todos os diagramas estão legíveis (especialmente os 3 .mmd)
- [ ] Preparar handout (opcional): storyboard impresso

### Preparação de Logística
- [ ] Sala reservada para 90 min + 15 min de buffer
- [ ] Quadro branco disponível (para desenhar grafos improvisados)
- [ ] Acesso ao repositório da especialização confirmado

---

## Durante a Aula

### Bloco 1 (45 min)
- [ ] **Slide 1-6 (8 min)**: Abertura — anotar quem já usou vector DB e quem já usou knowledge graph
- [ ] **Slide 5**: Fazer a pergunta de reflexão ("Quando similaridade não basta?")
- [ ] **Slide 8**: Destacar a diferença fundamental: similaridade ≠ igualdade
- [ ] **Slide 11**: Animar o HNSW — garantir que entendem as camadas (fly, drive, walk)
- [ ] **Slide 13**: Mostrar as 3 métricas — click para cada uma
- [ ] **Slide 19-23**: Comparar os 5 DBs rapidamente — não se prender a detalhes
- [ ] **Slide 24**: Discussão "MVP vs 1M usuários" — anotar respostas
- [ ] **Slide 25**: Destacar "quando NÃO usar vector DB" — anti-hype
- [ ] **Slide 28**: Animar as triplas — mostrar o encadeamento multi-hop
- [ ] **Slide 31**: Mostrar Cypher na prática — query + grafo resultante
- [ ] **Slide 33-34**: Destacar alucinação em extração com LLM
- [ ] **Slide 36 (2 min)**: Exercício de cardinalidade em duplas
- [ ] Intervalo (5 min)

### Bloco 2 (45 min)
- [ ] **Slide 38**: Criar tensão — vector RAG falha em perguntas globais
- [ ] **Slide 39**: Mostrar o pipeline GraphRAG completo (diagrama .mmd)
- [ ] **Slide 40-41**: Comunidades e sumarização — a mágica do GraphRAG
- [ ] **Slide 46 (3 min)**: DEMO AO VIVO — GraphRAG em Neo4j. Se falhar, screenshots
- [ ] **Slide 47 (2 min)**: Pergunta da DEMO em duplas
- [ ] **Slide 48**: Ser transparente sobre custo — bar chart
- [ ] **Slide 50**: Discussão "vale a pena?" — matriz valor vs custo
- [ ] **Slide 54**: Mostrar o diagrama híbrido (.mmd)
- [ ] **Slide 55-56**: RetrievalAgent e código do router
- [ ] **Slide 60 (2 min)**: Exercício em grupos — 5 cenários
- [ ] **Slide 62**: Benchmark — mostrar os números (vector 60%, graph 75%, híbrido 85%)
- [ ] **Slide 64-68**: Escala — mais rápido, não se prender
- [ ] **Slide 70-71**: Boas práticas e anti-patterns — pedir exemplos da turma
- [ ] **Slide 72**: Caso farmacêutica — destacar ROI
- [ ] **Slide 75-77 (3 min)**: Quiz — individual, sem consulta
- [ ] **Slide 80 (2 min)**: Q&A

---

## Pós-Aula

### Avaliação
- [ ] Contar resultados do quiz (≥2 acertos = compreensão básica)
- [ ] Anotar perguntas frequentes no Q&A para futuras iterações
- [ ] Pedir feedback informal: "Uma infraestrutura que você escolheria diferente"
- [ ] Verificar tempo real vs planejado por seção

### Follow-up
- [ ] Enviar leitura recomendada no Slack/email (Edge et al. GraphRAG, Lewis et al. RAG)
- [ ] Disponibilizar slides (PDF + repositório)
- [ ] Lembrar prazo do Lab 1 (Vector DB Bake-off — 1 semana)
- [ ] Lembrar prazo do Projeto (pipeline híbrido — 2 semanas)
- [ ] Preparar ETHAGT14 (a próxima aula aprofunda escala multi-tenant)

---

## Sinais de Alerta Durante a Aula

| Sinal | Ação |
|---|---|
| Alunos confusos no Slide 11 (HNSW) | Simplificar: focar só na analogia "fly, drive, walk" |
| DEMO falha (Neo4j ou LLM indisponível) | Screenshots do Neo4j Browser + trace pré-gravado |
| Tempo estourado no Bloco 1 | Cortar exercício do Slide 36 (cardinalidade); mover para homework |
| Tempo estourado no Bloco 2 | Reduzir quiz para 2 perguntas (Slides 75-76); escala como leitura |
| Nenhuma pergunta no Q&A | Pergunta inversa: "Qual parte foi menos clara — vector, grafo ou híbrido?" |
| Alunos sem pré-requisito de RAG (ETHAGT06) | Direcionar para ETHAGT06; recap rápido de embeddings no Slide 9 |
| Demora na extração de entidades na DEMO | Usar corpus menor pré-carregado; mostrar só a query multi-hop |
| Alunos querem "sempre híbrido" | Reforçar Slide 61: comece com vector, adicione grafo com evidência |
