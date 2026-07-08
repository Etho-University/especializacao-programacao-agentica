# ETHAGT12 — Perguntas para Discussão

> Perguntas para estimular debate durante e após a aula.
> Organizadas por profundidade: rápida (1-2 min) → média (3-5 min) → profunda (10+ min).

---

## Perguntas Rápidas (1-2 min)

### Q1 — Como Você Sabe?
"Como você sabe se seu agente está ficando melhor ou pior ao longo do tempo?"
- **Objetivo**: Criar tensão — a maioria não sabe responder
- **Slide**: 5
- **Resposta esperada**: Silêncio. Esse silêncio é o gancho da aula. Sem observabilidade e eval, você não sabe.

### Q2 — Falácias Pessoais
"Qual das 5 falácias de avaliação você já cometeu?"
- **Objetivo**: Quebrar gelo com honestidade
- **Slide**: 11
- **Ação**: Pedir mãos levantadas por falácia

### Q3 — Experiência com Tooling
"Quem aqui já usa LangSmith, Phoenix, Langfuse ou OpenLLMetry em produção?"
- **Objetivo**: Calibrar experiência da turma
- **Slide**: 19
- **Ação**: Contar mãos levantadas (geralmente <30%)

### Q4 — Vibes-Based Eval
"Vocês tomam decisões de deploy baseadas em 'parece bom'? Quanto isso já custou?"
- **Objetivo**: Conscientização sobre vibes-based eval
- **Slide**: 13
- **Resposta esperada**: Todos já fizeram. Histórias de regressão em produção.

### Q5 — Benchmarks Confiáveis
"Você confia em score de benchmark de um paper sem ter rodado você mesmo?"
- **Objetivo**: Questionar fé cega em benchmarks
- **Slide**: 45, 52
- **Resposta esperada**: Não. Score pode estar contaminado, mal medido, ou em versão diferente.

---

## Perguntas Médias (3-5 min)

### Q6 — Viés Mais Perigoso
"Qual dos 5 vieses do LLM-as-judge (positional, sycophancy, verbosity, self-preference, knowledge) é mais perigoso para o caso de uso de vocês?"
- **Objetivo**: Aplicar vieses ao contexto da turma
- **Slide**: 31
- **Dica**: Resposta varia por domínio. Em comparações A/B, positional é crítico. Em assistentes, sycophancy.

### Q7 — Custo de Eval
"Seu agente faz 30 chamadas de LLM por tarefa, cada uma $0.005. Você avalia 500 casos por semana. Qual o custo mensal?"
- **Objetivo**: Praticar cálculo de custo de eval
- **Slide**: 10
- **Cálculo**: 30 × $0.005 × 500 × 4 = $300/mês. Discussão: vale a pena? Como reduzir?

### Q8 — Threshold de CI
"Em um CI gate para agentes, qual threshold de regressão você usa? 0%? 5%? 10%?"
- **Objetivo**: Pensar em trade-offs de gate
- **Slide**: 57
- **Resposta esperada**: Depende. Casos críticos = 0%. Não-críticos = 5%. Threshold muito alto deixa passar regressão; muito baixo bloqueia dev por ruído.

### Q9 — LLM-as-Judge ou Métrica Programática?
"Para verificar se um agente de reserva de voo 'encontrou o voo mais barato', você usa LLM-as-judge ou string match no preço?"
- **Objetivo**: Praticar escolha de técnica de eval
- **Slide**: 30, 34
- **Resposta esperada**: String match (programático) — mais barato e confiável. LLM-as-judge só para aspectos subjetivos.

### Q10 — Benchmark Custom ou Canônico?
"Você está construindo um agente de atendimento bancário. Usa SWE-bench, GAIA, τ-bench, ou constrói eval custom?"
- **Objetivo**: Praticar escolha de benchmark
- **Slide**: 45, 53
- **Resposta esperada**: τ-bench (tool use com policy) + eval custom (domínio bancário). SWE-bench é código, GAIA é geral — não aplicáveis.

---

## Perguntas Profundas (10+ min)

### Q11 — Vibes-Based vs Evidence-Based
"Como você convence sua liderança a investir em AgentOps (observabilidade + eval) se eles acham que é custo desnecessário?"
- **Objetivo**: Estruturar argumento de ROI
- **Slide**: 27, 67
- **Argumentos**:
  - Custo de regressão não detectada (churn de usuários)
  - Custo de debugging sem traces (10x mais tempo)
  - Vantagem competitiva do dataset
  - Compliance e auditoria
- **Ação**: Role-play — um aluno é a liderança, outro defende AgentOps

### Q12 — Eval em Agentes Multi-Agent
"Em um sistema multi-agente (3+ agentes), como você avalia? Métricas por agente ou do sistema todo?"
- **Objetivo**: Pensar em complexidade de eval
- **Slide**: 36, 37
- **Resposta esperada**: Ambos. Métricas de sistema (success rate, custo, latência totais) + métricas por agente (qual agente falhou? qual consumiu mais tokens?). Trace com spans por agente é essencial.

### Q13 — LLM-as-Judge em Tarefas Críticas
"Você usaria LLM-as-judge para aprovar um agente que faz diagnóstico médico? Por quê?"
- **Objetivo**: Pensar em limites éticos
- **Slide**: 31, 32
- **Resposta esperada**: Não isoladamente. Tarefas críticas exigem: (1) métricas programáticas quando possível; (2) calibração humana rigorosa; (3) múltiplos judges; (4) humano no loop. LLM-as-judge pode apoiar mas não decidir sozinho.

### Q14 — Contaminação de Benchmark
"Você descobriu que 30% do seu benchmark está nos dados de treino do modelo. O que faz?"
- **Objetivo**: Lidar com problema realista
- **Slide**: 52
- **Resposta esperada**: (1) Remover casos contaminados; (2) gerar variantes (paráfrases); (3) usar eval custom com dados próprios; (4) reportar score apenas em casos não-contaminados.

### Q15 — Dataset como Vantagem Competitiva
"Seu concorrente tem 1000 golden cases e você tem 50. Como você alcança?"
- **Objetivo**: Pensar em estratégia de eval
- **Slide**: 56
- **Resposta esperada**: (1) Comece com casos críticos (alta prioridade); (2) triagem agressiva de produção; (3) gere casos sintéticos com LLM (com curadoria humana); (4) foque em qualidade > quantidade.

---

## Perguntas Bônus (para alunos avançados)

### Q16 — Online vs Offline Eval
"Qual a diferença entre online eval (em produção) e offline eval (em conjunto de testes)? Quando cada um?"
- **Objetivo**: Aprofundar conceito
- **Resposta**: Offline eval = conjunto de golden cases antes do deploy (reproduzível, controlado). Online eval = métricas em produção (real, mas ruidoso). Offline para iterar; online para detectar drift e falhas no mundo real.

### Q17 — Tail Sampling vs Head Sampling
"Quando tail sampling é melhor que head sampling?"
- **Objetivo**: Aprofundar estratégia de amostragem
- **Resposta**: Tail sampling é melhor quando você quer priorizar erros (decide no fim do trace). Head sampling é mais barato (decide no início) mas cego ao resultado. Em agentes, tail é geralmente melhor — você sempre captura traces com erro.

### Q18 — Regression Detection em Sistemas Não-Determinísticos
"Seu eval score caiu de 85% para 80%. É regressão real ou ruído?"
- **Objetivo**: Pensar em significância estatística
- **Resposta**: Depende do N. Com 50 casos, 5% pode ser ruído (1-2 casos). Com 500 casos, 5% é significativo. Regra: reporte intervalo de confiança. Se IC das duas versões se sobrepõe, diferença não é significativa.

### Q19 — Eval de Segurança
"Como você avalia robustez contra prompt injection no seu agente?"
- **Objetivo**: Conectar com ETHAGT13
- **Resposta**: Use benchmarks de segurança (AgentDojo). Construa golden cases adversariais (tentativas de injeção). Avalie se o agente executa instrução maliciosa. Cobrimos a fundo em ETHAGT13.

### Q20 — Eval vs Monitoring
"Qual a diferença entre eval e monitoring?"
- **Objetivo**: Clarificar conceitos
- **Resposta**: Eval = avaliar versões em conjunto controlado (antes do deploy, com critério). Monitoring = observar comportamento em produção (depois do deploy, em tempo real). Eval é proativo; monitoring é reativo. Ambos necessários.
