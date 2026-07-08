# ETHAGT10 — Perguntas para Discussão

> Perguntas para estimular debate durante e após a aula.
> Organizadas por profundidade: rápida (1-2 min) → média (3-5 min) → profunda (10+ min).

---

## Perguntas Rápidas (1-2 min)

### Q1 — Topologia Mais Comum
"Qual foi a topologia mais comum que vocês já usaram em projetos? Sabiam o nome dela?"
- **Objetivo**: Calibrar o nível da turma
- **Slide**: 5
- **Resposta esperada**: A maioria usou supervisor sem saber o nome. Alguns usaram pipeline. Poucos usaram swarm ou mesh.

### Q2 — Supervisor em Produção
"Já usou supervisor em produção? Funcionou bem? Teve gargalo?"
- **Objetivo**: Conectar teoria com experiência prática
- **Slide**: 10
- **Resposta esperada**: Experiências mistas. Alguns reportarão latência crescente; outros, roteamento errado.

### Q3 — Conhece os Frameworks
"Quem aqui já usou LangGraph multi-agent, CrewAI, ou OpenAI Swarm?"
- **Objetivo**: Calibrar experiência prática com frameworks multi-agente
- **Slide**: 27
- **Ação**: Contar mãos levantadas

### Q4 — Crew para Revisar PR
"Como você montaria uma crew para revisar um PR?"
- **Objetivo**: Aplicar crew formation a um caso real
- **Slide**: 27
- **Resposta esperada**: Code reviewer, security reviewer, docs reviewer; processo hierarchical.

---

## Perguntas Médias (3-5 min)

### Q5 — Matching Cenário → Topologia
"Para cada um destes 6 cenários, qual topologia e por quê?"
- **Objetivo**: Praticar a decisão de topologia
- **Slide**: 16, 58
- **Cenários**: suporte com escalonamento, revisão de PR, relatório financeiro, simulação de mercado, assistente pessoal, pesquisa autônoma

### Q6 — Supervisor Gargalo
"Em quantos níveis de hierarquia o supervisor se torna gargalo? Como você detectaria isso em produção?"
- **Objetivo**: Pensar sobre escala e observabilidade
- **Slide**: 25, 56
- **Resposta esperada**: 3+ níveis. Detectar via métricas de latência (P95) e contagem de LLM calls por requisição.

### Q7 — Swarm vs Supervisor para PR
"Para o caso de revisão de PR com 3 especialistas: swarm ou supervisor? E se precisar sintetizar as 3 revisões?"
- **Objetivo**: Aplicar o critério (síntese necessária?)
- **Slide**: 34
- **Resposta esperada**: Sem síntese → swarm (independentes). Com síntese → supervisor (agregar).

### Q8 — Hierarchical ou Flat?
"Para estes 4 cenários, hierarchical ou flat? Quantos níveis?"
- **Objetivo**: Praticar a decisão de profundidade
- **Slide**: 28
- **Critério**: >7 workers em um supervisor → adicionar nível. Senão, flat.

---

## Perguntas Profundas (10+ min)

### Q9 — Mesh é Sempre a Mais Escalável?
"Verdadeiro ou falso: 'Mesh é sempre a topologia mais escalável.' Justifique."
- **Objetivo**: Pensamento crítico sobre escalabilidade
- **Slide**: 46
- **Resposta esperada**: Falso. Mesh escala em número de agentes autônomos, mas conexões crescem O(N²). Hierarchical é O(N). Para muitos agentes, hierarchical escala melhor.
- **Contraponto**: Mesh é melhor quando poucos agentes altamente colaborativos e sem ponto de falha.

### Q10 — Recursive é Sempre Anti-Pattern?
"Recursive é sempre anti-pattern? Em que cenário recursive é a topologia correta?"
- **Objetivo**: Pensar sobre quando recursive é justificado
- **Slide**: 50
- **Resposta esperada**: Não é sempre. É anti-pattern sem guardrails (max_depth, orçamento, validação). É correto quando: (1) o problema se decompõe naturalmente, (2) o conjunto de especialistas é desconhecido a priori, (3) max_depth está definido.

### Q11 — Quando Trocar de Topologia?
"Como você decide quando é hora de trocar de topologia? Que métricas você monitoraria?"
- **Objetivo**: Aplicar sinais de evolução
- **Slide**: 56
- **Resposta esperada**: Monitore métricas, não intuição. Latência P95 crescendo, custo por requisição crescendo, workers > 7, loops de handoff. Escreva um novo ADR para a mudança.

### Q12 — MetaGPT e SOPs
"MetaGPT usa SOPs de software house. Como você adaptaria isso para outro domínio (ex.: hospital, escritório de advocacia)?"
- **Objetivo**: Generalizar o conceito de SOPs para outros domínios
- **Slide**: 57
- **Resposta esperada**: Identificar os papéis humanos, os artefatos que fluem entre eles, e codificar tudo em agentes. Hospital: triagem → diagnóstico → tratamento → alta. Advocacia: intake → pesquisa → petição → audiência.

---

## Perguntas Bônus (para alunos avançados)

### Q13 — Orchestrator vs Supervisor
"Qual a diferença precisa entre orchestrator-workers e supervisor? Dê um exemplo onde escolheria um sobre o outro."
- **Objetivo**: Dominar a distinção sutil
- **Resposta**: Orchestrator PARTICIONA uma tarefa em sub-tarefas distintas e sintetiza. Supervisor ROTEIA a tarefa inteira para um worker. Exemplo: "Escreva relatório" → orchestrator divide (intro, corpo, conclusão). "Traduza documento" → supervisor escolhe o tradutor certo.

### Q14 — Hybrid Sempre em Produção?
"É verdade que todo sistema multi-agente em produção é hybrid? Você consegue pensar em um caso onde uma topologia pura é melhor?"
- **Objetivo**: Pensar sobre quando hybrid é necessário vs over-engineering
- **Resposta**: Quase sempre é hybrid em produção (pipeline + hierarchical + event-driven). Topologia pura é melhor em protótipos e casos simples (ex.: chatbot com supervisor puro, pipeline de geração de relatório fixo).

### Q15 — Blackboard vs Event-Driven
"Blackboard é o precursor do event-driven. Quando você escolheria blackboard sobre event-driven hoje?"
- **Objetivo**: Conhecer when-to-use de padrões clássicos
- **Resposta**: Blackboard é melhor quando o estado compartilhado persistente é mais natural que eventos efêmeros. Exemplos: diagnóstico médico incremental, brainstorming estruturado, análise de código com múltiplas perspectivas acumulando no mesmo quadro.
