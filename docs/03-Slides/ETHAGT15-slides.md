# ETHAGT15 — Meta-Agentes & Sistemas Autoaprendentes — Slides

> Apresentação para aula síncrona · ~50 min · 11 slides

## Estrutura da aula
- Abertura (5 min): gancho/motivação
- Teoria (25 min): conceitos principais com diagramas de referência
- Demonstração (10 min): código ao vivo ou walkthrough de lab
- Exercício (5 min): questão rápida ou discussão
- Fechamento (5 min): conexão com próximo módulo, leitura recomendada

## Slides

### Slide 1 — Título
- ETHAGT15 — Meta-Agentes & Sistemas Autoaprendentes (agents that build agents)
- Professor, data, Universität Etho
- Pré-requisito: ETHAGT10
- Carga: 15 h (módulo mais curto, fronteira)
- ~1 min

### Slide 2 — Agenda
1. O que é meta-agência
2. Geração de agentes (meta-agente que produz agentes)
3. Otimização automatizada (DSPy, Promptbreeder)
4. Auto-aprendizado contínuo (memória, reflexão, evolução)
5. Riscos e governança (recursão, goal drift, meta-governor)
- ~1 min

### Slide 3 — Gancho / Motivação
- Problema: prompts e ferramentas são otimizados manualmente — escala não
- Exemplo: equipe de 5 engenheiros mantendo prompts de 20 agentes → impraticável
- A solução: meta-agente que otimiza automaticamente
- Fronteira: agente que cria outro agente — onde está o limite?
- Pergunta: *Você deixaria um agente modificar o próprio prompt?*
- ~3 min

### Slide 4 — O que é Meta-Agência
- Agentes que operam sobre agentes: criar, configurar, otimizar, evoluir
- Estratégias: synthesis (criar do zero), evolution (mutar configuração), optimization (ajustar parâmetros)
- Exemplos: DSPy (otimiza prompts), Voyager (aprende skills), Meta-Prompting
- Risco vs benefício: ganho de escala vs perda de controle
- Diagrama: `12-Diagrams/ETHAGT15/meta-agent.mmd`
- ~4 min

### Slide 5 — Geração de Agentes
- Meta-agente que, dada uma tarefa, produz prompts/tools/agentes especializados
- Templates e composição: biblioteca de módulos reutilizáveis
- Validação do agente gerado: eval antes de deploy (testar em sandbox)
- Caso: sistema que gera agentes de suporte para diferentes produtos
- Pergunta: *Como garantir que o agente gerado não é pior que o manual?*
- ~4 min

### Slide 6 — Otimização Automatizada
- Otimização de prompts: DSPy (compilação declarativa), Atlas, Promptbreeder (evolução)
- Otimização de tools: reescrita de descrições baseada em taxa de erro
- Otimização de topologia: qual worker adicionar/remover?
- Loop: benchmark → identificar gargalo → ajustar → re-benchmark
- Diagrama: `12-Diagrams/ETHAGT15/evolution-loop.mmd`
- ~4 min

### Slide 7 — Auto-aprendizado Contínuo
- Memória de sucesso/falha (o que funcionou, o que não)
- Reflexion em nível de sistema (não apenas do agente individual)
- Estratégia evolutiva (strategy evolver): mutação + seleção das melhores estratégias
- Quando esquecer: drift de dados, mudança de domínio
- Pergunta: *O que acontece se o ambiente muda e o agente continua otimizando para o ambiente antigo?*
- ~4 min

### Slide 8 — DEMO: Agente que Escreve Agente
- Código ao vivo: meta-agente recebe descrição de tarefa
- Gera: prompt, tools, e configuração de agente especializado
- Avalia o agente gerado em 3 casos de teste
- Mostra resultado: aprovado/reprovado → itera
- Referência: `05-Labs/ETHAGT15/Lab1-Agente-que-Escreve-Agente`
- ~5 min

### Slide 9 — Riscos e Governança
- Recursão e loops de auto-modificação (agente que se modifica repetidamente sem convergência)
- Drift de objetivos (goal drift): agente otimiza métrica errada
- Segurança: meta-governor pattern (guardião que avalia modificações)
- Confiança incremental: sandbox antes de produção, aprovação humana para mudanças críticas
- Diagrama: `12-Diagrams/ETHAGT15/safety-fences.mmd`
- Discussão: *Em que ponto um meta-agente se torna perigoso?*
- ~4 min

### Slide 10 — Exercício: Meta-Governor
- Cenário: meta-agente quer modificar o próprio system prompt
- Em trios: projetar um meta-governor com regras de veto
- Exemplos de regra: "não pode remover constraints de segurança", "não pode aumentar custo >10%"
- 3 min, compartilhar regras mais criativas
- ~4 min

### Slide 11 — Conexão com Próximo Módulo
- ETHAGT16 — Sociedades de Agentes: meta-agentes em ecossistemas
- ETHAGT90 — Capstone: meta-agente como sistema de orquestração
- Leitura: Khattab et al. *DSPy* (arXiv:2310.03714)
- Fernando et al. *Promptbreeder* (arXiv:2309.16797)
- Hu et al. *Meta-Prompting* (arXiv:2311.11402)
- Wang et al. *Voyager* (auto-skills)
- ~2 min
