# ETHAGT16 — Perguntas para Discussão

> Perguntas para estimular debate durante e após a aula.
> Organizadas por profundidade: rápida (1-2 min) → média (3-5 min) → profunda (10+ min).

---

## Perguntas Rápidas (1-2 min)

### Q1 — O Agente Isolado
"Qual problema que vocês enfrentam hoje um agente isolado NÃO resolve, mas uma sociedade de agentes poderia?"
- **Objetivo**: Conectar com a dor real da turma
- **Slide**: 5
- **Resposta esperada**: Tarefas que exigem múltiplas perspectivas, debate, validação por pares, especialização de papéis.

### Q2 — Papel Mais Difícil
"Qual dos 5 papéis (pesquisador, crítico, sintetizador, revisor, editor) vocês acham que é o mais difícil de automatizar bem?"
- **Objetivo**: Fazer alunos pensarem sobre qualidade de cada papel
- **Slide**: 9
- **Resposta esperada**: Costuma ser o crítico (exige julgamento) ou o sintetizador (exige integração de perspectivas divergentes).

### Q3 — Experiência com Simulação Social
"Quem aqui já rodou uma simulação multi-agente (Smallville-like, AgentVerse, ChatArena)?"
- **Objetivo**: Calibrar experiência prática
- **Slide**: 12
- **Ação**: Contar mãos levantadas

### Q4 — Custo de uma Sociedade
"Se 1 agente custa $0.05 por interação, quanto custa uma simulação de 25 agentes × 100 interações?"
- **Objetivo**: Praticar cálculo de custo em escala
- **Slide**: 20
- **Cálculo**: 25 × 100 × $0.05 = $125 por execução. Em 10 execuções/dia = $1.250/dia.

---

## Perguntas Médias (3-5 min)

### Q5 — Simulação = Predição?
"Uma simulação social com LLMs pode prever comportamento humano real? Em quais condições sim e em quais não?"
- **Objetivo**: Pensamento crítico sobre validação
- **Slide**: 20, 21
- **Dica**: Validar onde há ground truth (mercado com dados reais); duvidar onde não há (opinião pública).

### Q6 — Papel Crítico na DEMO
"Qual papel da Mini Sociedade (Slide 30) foi mais crítico para o resultado? O que aconteceria se removêssemos o crítico? E se o editor tivesse poder de veto?"
- **Objetivo**: Análise contrafactual
- **Slide**: 31
- **Resposta esperada**: Sem o crítico, qualidade cai (sem questionamento). Com veto do editor, convergência mais rápida mas menos diversidade.

### Q7 — Normas Explícitas vs Emergentes
"Em uma sociedade de agentes, quando você prefere normas explícitas (programadas) e quando prefere normas emergentes (adaptativas)?"
- **Objetivo**: Aplicar o trade-off controle vs adaptabilidade
- **Slide**: 10, 14
- **Resposta esperada**: Explícitas em alta stakes (segurança, ética). Emergentes em exploração (descoberta, criatividade).

### Q8 — AI Scientist: Como Avaliar
"Como vocês avaliariam a qualidade científica de um paper gerado pelo AI Scientist?"
- **Objetivo**: Praticar avaliação crítica de pesquisa autônoma
- **Slide**: 33, 46
- **Resposta esperada**: Reprodutibilidade, novidade, corretude metodológica, validade estatística. Sem humano revisando, autonomia ≠ qualidade.

---

## Perguntas Profundas (10+ min)

### Q9 — Quando a Soma é Pior?
"Quando o comportamento emergente de uma sociedade é PIOR do que a soma dos agentes isolados? Dê 3 exemplos."
- **Objetivo**: Pensar criticamente sobre emergência indesejada
- **Slide**: 37
- **Resposta esperada**: Conluio (agentes combinam contra o objetivo), echo chamber (polarização), discriminação sistêmica, corrida armamentista. Sem supervisão, emergência tende ao extremo.

### Q10 — Alinhamento Individual ≠ Coletivo
"Como você alinha uma sociedade de 100 agentes de forma que NÃO colapse? Constituição? Votação? Reputação?"
- **Objetivo**: Estruturar mecanismos de alinhamento coletivo
- **Slide**: 38
- **Argumentos**: Constitution garante consistência global; votação agrega preferências; reputação penaliza free-riders. Nenhum mecanismo isolado é suficiente.

### Q11 — O Maior Risco de Pesquisa Autônoma
"Qual o maior risco de um AI Scientist operando sem supervisão humana em loop fechado?"
- **Objetivo**: Conscientização sobre limites da autonomia
- **Slide**: 44, 45
- **Resposta esperada**: Auto-modificação irrestrita, propagação de erros metodológicos em escala, papers com erros sutis mas plausíveis que passam peer review, automação de pesquisa com viés amplificado.

### Q12 — O Que NÃO Fazer
"Listem 3 práticas que vocês consideram inaceitáveis em sociedades de agentes em produção."
- **Objetivo**: Aplicar a checklist ética
- **Slide**: 45
- **Ação**: Em duplas, 5 min para listar. Compartilhar 2 exemplos.
- **Resposta esperada**: Sem HITL em alta stakes, auto-modificação irrestrita, autopropagação sem limites, deploy sem avaliação de risco, sociedades sem constitution.

---

## Perguntas Bônus (para alunos avançados)

### Q13 — Sociedade vs Agente com Muitos Tools
"Quando é melhor ter uma sociedade de 5 agentes especializados vs 1 agente com 25 tools?"
- **Objetivo**: Aprofundar o trade-off da Seção B
- **Resposta**: 5 agentes especializados quando as tarefas são distintas e cada uma exige contexto amplo (próprio prompt e tools). 1 agente com muitas tools quando as tarefas se sobrepõem e o overhead de comunicação supera o benefício. Ver ETHAGT09-10.

### Q14 — Simulação Social e Política
"Você foi convidado para assessorar um governo com simulações sociais de LLM. Em qual política você confiaria? Em qual não?"
- **Objetivo**: Discutir limites da simulação social em alta stakes
- **Resposta**: Confiança maior onde há ground truth validável (impacto econômico, formação de preços). Desconfiança em previsões de comportamento humano individual, opinião pública, polarização (sem ground truth).

### Q15 — Futuro: Capstone
"Para o Capstone (ETHAGT90), vocês preferem construir: (a) uma simulação social, (b) um sistema de pesquisa autônoma, (c) uma sociedade com papéis? Por quê?"
- **Objetivo**: Conectar ETHAGT16 ao Capstone
- **Ação**: Discussão aberta para calibrar expectativas do projeto final.
