# ETHAGT06 — Perguntas para Discussão

> Perguntas para estimular debate durante e após a aula.
> Organizadas por profundidade: rápida (1-2 min) → média (3-5 min) → profunda (10+ min).

---

## Perguntas Rápidas (1-2 min)

### Q1 — Experiência com RAG em Produção
"Quantos de vocês já usaram RAG em produção e obtiveram resposta errada com alta confiança?"
- **Objetivo**: Calibrar o nível da turma e criar tensão
- **Slide**: 6
- **Resposta esperada**: A maioria que usou RAG já passou por isso. É o ponto de partida da aula.

### Q2 — Vector DB Resolve Tudo?
"Vocês já ouviram a frase 'só joga no vector DB e funciona'? O que aconteceu quando tentaram?"
- **Objetivo**: Desconstruir o mito
- **Slide**: 14
- **Resposta esperada**: Vector DB é uma peça, não a solução. Falha em tabular, multilingual, multimodal.

### Q3 — Pior Tipo de Falha
"Qual o pior tipo de falha — não responder ou responder errado com confiança?"
- **Objetivo**: Discutir alucinação silenciosa
- **Slide**: 14
- **Resposta esperada**: Responder errado com confiança — o usuário age sobre informação falsa.

### Q4 — Routing na Prática
"Em qual cenário da sua aplicação atual você responderia direto sem recuperar?"
- **Objetivo**: Aplicar Adaptive RAG ao caso real deles
- **Slide**: 20
- **Ação**: Deixar 1-2 alunos compartilharem

### Q5 — Avaliação Hoje
"Vocês têm dataset de holdout para avaliar RAG hoje? Quantos têm?"
- **Objetivo**: Mostrar que a maioria não tem — motivar Seção H
- **Slide**: 68
- **Resposta esperada**: <30% tem holdout estruturado

---

## Perguntas Médias (3-5 min)

### Q6 — Adaptive RAG vs CRAG
"Para o sistema de vocês hoje: Adaptive RAG basta ou precisam de CRAG? Por quê?"
- **Objetivo**: Aplicar a comparação ao caso real
- **Slide**: 33
- **Dica**: Se a base tem gaps de cobertura ou dados que envelhecem, CRAG brilha.

### Q7 — Custo de Self-RAG
"Self-RAG adiciona múltiplas chamadas de LLM (avaliador + hallucination check + regeneração). Em que caso vale o custo?"
- **Objetivo**: Pensar em trade-off custo/qualidade
- **Slide**: 43
- **Resposta esperada**: Jurídico, médico, financeiro — onde alucinação é inaceitável.

### Q8 — Estratégia de Chunking
"Seus chunks hoje são de tamanho fixo? Qual estratégia melhoraria seu RAG?"
- **Objetivo**: Praticar escolha de chunking
- **Slide**: 58
- **Ação**: Deixar 1-2 alunos compartilharem

### Q9 — HyDE Vale a Pena?
"HyDE adiciona uma chamada de LLM para gerar resposta hipotética. Em que caso o ganho compensa a latência?"
- **Objetivo**: Trade-off latência/qualidade
- **Slide**: 62
- **Resposta esperada**: Perguntas abstratas onde a query é muito diferente dos docs.

### Q10 — Cálculo de Custo de CRAG
"CRAG adiciona 1-2 chamadas de LLM (avaliador + refinement). Seu agente custa $0.02 sem CRAG. Com CRAG, quanto? Em 10k queries/dia?"
- **Objetivo**: Praticar cálculo de custo
- **Slide**: 33
- **Cálculo**: $0.02 + $0.005 (avaliador) = $0.025 por query. 10k/dia = $250/dia = $7.500/mês extra.

---

## Perguntas Profundas (10+ min)

### Q11 — Comece Simples ou Vá Direto ao Agentic?
"Por que começar com Adaptive RAG se Agentic RAG é mais poderoso? Justifique para um PM."
- **Objetivo**: Pensamento crítico sobre complexidade
- **Slide**: 55, 77
- **Resposta esperada**: Adaptive é mais simples, previsível e barato. Agentic só quando há evidência de insuficiência. Regra Anthropic: comece simples, suba com evidência.

### Q12 — LLM-as-Judge Confiável?
"Ragas usa LLM-as-judge para calcular faithfulness. O LLM que julga pode estar errado. Como mitigar?"
- **Objetivo**: Crítica metodológica
- **Slide**: 73
- **Resposta esperada**: (1) usar modelo diferente do gerador; (2) randomizar ordem; (3) normalizar por tamanho; (4) validar com dataset humano-curado.

### Q13 — Multi-Hop Sempre Necessário?
"Toda pergunta complexa precisa de multi-hop? Quando single-hop basta?"
- **Objetivo**: Evitar over-engineering
- **Slide**: 48
- **Resposta esperada**: Single-hop basta quando a resposta está em um chunk. Multi-hop só quando a resposta exige combinar informações de múltiplas fontes encadeadas.

### Q14 — GraphRAG vs Vector RAG
"Quando GraphRAG é melhor que vector RAG? E quando é overkill?"
- **Objetivo**: Critério de escolha
- **Slide**: 52
- **Resposta esperada**: GraphRAG brilha em perguntas globais ("quais os temas deste corpus?"). Overkill para perguntas locais factuais.

### Q15 — Avaliação Contínua
"Como vocês integrariam Ragas no CI/CD para bloquear deploy em regressão?"
- **Objetivo**: Pensar em produção
- **Slide**: 73
- **Resposta esperada**: Batch eval em holdout a cada PR; gate de qualidade (faithfulness ≥ 0.85); bloquear merge se métrica cair.

---

## Perguntas Bônus (para alunos avançados)

### Q16 — Self-RAG Treinado vs Prompting
"O Self-RAG original é um modelo fine-tuned. Adaptar via prompting é equivalente? O que se perde?"
- **Objetivo**: Profundidade técnica
- **Resposta**: Prompting replica a lógica mas com múltiplas chamadas (mais caro, mais lento). Modelo treinado emite tokens em uma passada. Prompting é mais flexível (funciona com qualquer modelo).

### Q17 — Late Chunking vs RAG com Janela Grande
"Se a context window crescesse para 10M tokens, late chunking ainda seria necessário?"
- **Objetivo**: Pensar sobre limites
- **Resposta**: Sim. Janela maior reduz summarization mas não resolve: (1) custo cresce; (2) lost in the middle; (3) retrieval ainda precisa ser preciso para perguntas específicas.

### Q18 — Re-Ranking em Tempo Real
"Re-ranking adiciona latência. Em qual caso você abriria mão do re-rank?"
- **Objetivo**: Trade-off latência/qualidade
- **Resposta**: Chatbots de alta concorrência com SLA agressivo de latência (<500ms). Nesses casos, top-k puro + base curada pode bastar.

### Q19 — Agentic RAG sem max_steps
"O que acontece se um Agentic RAG multi-hop não tiver max_steps?"
- **Objetivo**: Conexão com ETHAGT01
- **Resposta**: O agente pode entrar em loop infinito, gastando orçamento ilimitado. max_steps é guardrail de segurança (lição de ETHAGT01).

### Q20 — Quando RAG Não É a Resposta
"Existe caso onde NÃO usar RAG é melhor? Qual?"
- **Objetivo**: Evitar over-engineering
- **Resposta**: Quando a resposta está no conhecimento paramétrico do modelo ("Quem escreveu Dom Casmurro?") ou quando fine-tuning é mais apropriado (tarefas repetitivas com padrão estável).
