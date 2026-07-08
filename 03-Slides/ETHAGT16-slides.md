# ETHAGT16 — Sociedades de Agentes & Autonomous Research Systems — Slides

> Apresentação para aula síncrona · ~50 min · 11 slides

## Estrutura da aula
- Abertura (5 min): gancho/motivação
- Teoria (25 min): conceitos principais com diagramas de referência
- Demonstração (10 min): código ao vivo ou walkthrough de lab
- Exercício (5 min): questão rápida ou discussão
- Fechamento (5 min): conexão com Capstone, leitura recomendada

## Slides

### Slide 1 — Título
- ETHAGT16 — Sociedades de Agentes & Autonomous Research Systems
- Professor, data, Universität Etho
- Pré-requisito: ETHAGT15
- Carga: 15 h (módulo de fronteira)
- ~1 min

### Slide 2 — Agenda
1. Sociedades de agentes (papéis, normas, reputação)
2. Simulações sociais (Smallville, policy simulation)
3. Autonomous Research Systems (AI Scientist)
4. Emergência e alinhamento
5. Fronteira e ética
- ~1 min

### Slide 3 — Gancho / Motivação
- Problema: agentes isolados resolvem tarefas, mas sociedades de agentes podem gerar comportamento emergente
- Exemplo: Generative Agents (Stanford Smallville) — 25 agentes simulam vida social, organizam festa sozinhos
- A fronteira: AI Scientist (Sakana) — agente que conduz pesquisa científica do início ao fim
- Pergunta: *O que acontece quando 100 agentes interagem sem supervisão humana?*
- ~3 min

### Slide 4 — Sociedades de Agentes
- Pequenos grupos → instituições → sociedades
- Papéis (pesquisador, crítico, revisor, editor), normas (regras compartilhadas), reputação (confiança baseada em histórico)
- Modelos: Generative Agents (Stanford), AgentVerse, ChatArena
- Diagrama: `12-Diagrams/ETHAGT16/society.mmd`
- ~4 min

### Slide 5 — Simulações Sociais
- Sandbox social: ambiente onde agentes interagem (Smallville)
- Casos de uso: policy simulation (simular impacto de lei), mercado (agentes compram/vendem), opinião pública
- Limites e críticas: agentes são muito coerentes vs humanos, vieses dos LLMs se amplificam
- Pergunta: *Uma simulação social com LLMs pode prever comportamento humano real?*
- ~4 min

### Slide 6 — Autonomous Research Systems
- Pipeline completo: pergunta → revisão de literatura → hipótese → experimento → análise → relatório
- Stanford Generative Agents: vida social autônoma
- Sakana *AI Scientist*: pesquisa ML do início ao fim (gera código, roda experimentos, escreve paper)
- DeepMind *AlphaEvolve*: evolução de algoritmos
- Multi-agent research labs: times de agentes especializados colaboram
- Diagrama: `12-Diagrams/ETHAGT16/research-pipeline.mmd`
- ~5 min

### Slide 7 — DEMO: Mini Sociedade 5 Agentes
- Código ao vivo: 5 agentes com papéis (pesquisador, crítico, sintetizador, revisor, editor)
- Tarefa: produzir relatório sobre "impacto de agentes na educação"
- Mostrar: cada agente contribui, debate, revisa, produz versão final
- Observar: divergências, consenso, qualidade do resultado
- Referência: `05-Labs/ETHAGT16/Lab1-Mini-Sociedade`
- Pergunta: *Qual papel foi mais crítico para o resultado?*
- ~5 min

### Slide 8 — Emergência e Alinhamento
- Comportamento emergente: a soma é diferente das partes
- Exemplos: cooperação espontânea, formação de normas, mercados
- Quando emergência é indesejada: conluio, discriminação, corrida armamentista
- Alinhamento de valores em populações de agentes (constitution para sociedades)
- Avaliação de emergência: métricas de divergência, surpresa
- Diagrama: `12-Diagrams/ETHAGT16/emergence.mmd`
- ~4 min

### Slide 9 — Fronteira e Ética
- Onde a pesquisa está agora: AI Scientist (Sakana, 2024), AlphaEvolve (DeepMind, 2024), AutoGen research
- Questões éticas:
  - Automação de pesquisa: papers gerados por IA — autoria? revisão?
  - Responsible AI: viés amplificado em sociedades
  - Autopropagação: agente que cria cópias de si mesmo
- O que NÃO fazer: sistemas sem supervisão, auto-modificação irrestrita, deploy sem avaliação de risco
- Discussão: *Onde você traça a linha entre agente útil e perigoso?*
- ~4 min

### Slide 10 — Exercício: Avaliar Qualidade de um AI Scientist
- Cenário: AI Scientist gerou paper sobre "otimização de prompts"
- Em grupos: definir 3 critérios para avaliar a qualidade científica
- Exemplos: reprodutibilidade, novidade, corretude metodológica
- 3 min, compartilhar critérios
- ~4 min

### Slide 11 — Conexão com Capstone e Encerramento
- ETHAGT90 — Capstone: projeto final integrador
- O espectro completo: de Augmented LLM a Sociedades de Agentes
- Leitura: Park et al. *Generative Agents* (arXiv:2304.03442)
- Lu et al. *The AI Scientist* (Sakana, arXiv:2408.06292)
- Chen et al. *AgentVerse* (arXiv:2308.10848)
- Convite: onde vocês querem levar isso? Pesquisa, produto, impacto social?
- ~2 min
