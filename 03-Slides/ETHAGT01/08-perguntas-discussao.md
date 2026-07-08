# ETHAGT01 — Perguntas para Discussão

> Perguntas para estimular debate durante e após a aula.
> Organizadas por profundidade: rápida (1-2 min) → média (3-5 min) → profunda (10+ min).

---

## Perguntas Rápidas (1-2 min)

### Q1 — Definição de Agente
"Qual definição de 'agente' sua equipe usa hoje? Vocês distinguem workflow de agente?"
- **Objetivo**: Calibrar o nível da turma
- **Slide**: 8
- **Resposta esperada**: A maioria usa "agente" para tudo. Introduzir a distinção de Anthropic.

### Q2 — Componente Mais Fraco
"Qual dos 6 componentes da taxonomia (Perception, Brain, Planning, Action, Tool Use, Collaboration) vocês acham que é o mais fraco hoje em dia?"
- **Objetivo**: Fazer alunos pensarem sobre o estado da arte
- **Slide**: 9
- **Resposta esperada**: Planning — LLMs ainda são ruins em planejamento de longo prazo

### Q3 — Experiência com Framework
"Quem aqui já usou LangGraph, CrewAI ou OpenAI Agents SDK em produção?"
- **Objetivo**: Calibrar experiência prática
- **Slide**: 30
- **Ação**: Contar mãos levantadas

### Q4 — Traces em Produção
"Vocês têm traces nos sistemas de LLM de vocês hoje?"
- **Objetivo**: Mostrar que a maioria não tem — motivar observabilidade
- **Slide**: 38
- **Resposta esperada**: <30% tem traces estruturados

---

## Perguntas Médias (3-5 min)

### Q5 — Workflow ou Agente?
"Para o sistema de vocês hoje: workflow ou agente? Por quê?"
- **Objetivo**: Aplicar a árvore de decisão ao caso real deles
- **Slide**: 26
- **Dica**: Usar a árvore de decisão como framework para a resposta

### Q6 — Cenário de Edge Case
"O que acontece se a tool retornar erro? Quem trata — o modelo ou o código?"
- **Objetivo**: Pensar em error handling
- **Slide**: 22
- **Resposta esperada**: O código deve capturar o erro e retornar uma Observation estruturada. O modelo decide o que fazer com ela.

### Q7 — Tool Mal Documentada
"Vocês têm algum bug hoje que poderia ser resolvido redesenhando a tool em vez de melhorar o prompt?"
- **Objetivo**: Praticar o princípio ACI
- **Slide**: 46
- **Ação**: Deixar 1-2 alunos compartilharem experiências

### Q8 — Custo em Escala
"Seu agente custa $0.01 por execução. Você tem 10k usuários/dia. Quanto custa por mês? E se o agente fizer 10 steps em vez de 1?"
- **Objetivo**: Praticar cálculo de custo
- **Slide**: 41
- **Cálculo**: $0.01 × 10k × 30 = $3k/mês (1 step). Com 10 steps: $30k/mês.

---

## Perguntas Profundas (10+ min)

### Q9 — Toda Aplicação Deveria Ser um Agente?
"Toda aplicação de LLM deveria ser um agente? Justifique."
- **Objetivo**: Pensamento crítico sobre quando NÃO usar agentes
- **Slide**: 55
- **Resposta esperada**: Falso. Anthropic: "consider not building agentic systems at all". 90% dos casos = single LLM call + retrieval.
- **Contraponto**: Quando a tarefa é multi-step E imprevisível, agente é justificado.

### Q10 — Python Puro vs Framework em Produção
"Em que cenário Python puro é melhor que LangGraph? E o inverso? Como você convenceria um PM?"
- **Objetivo**: Estruturar argumentos de trade-off
- **Slide**: 55
- **Argumentos a favor do Python puro**: controle total, transparência, auditoria, debug granular
- **Argumentos a favor do LangGraph**: produtividade, checkpointer embutido, multi-agente nativo
- **Para o PM**: custo de manutenção vs custo de desenvolvimento; risco de caixa preta vs velocidade de entrega

### Q11 — O Maior Risco de Framework
"Qual o maior risco de começar com framework sem entender o básico?"
- **Objetivo**: Conscientização sobre armadilhas
- **Slide**: 55
- **Resposta esperada**: Caixa preta — quando o framework falha, você não sabe por quê. Pode ser o prompt oculto, a serialização, o retry logic. Sem entender o básico (loop, estado, tools), você não consegue isolar o problema.

### Q12 — ACI na Prática
"Pensem em uma tool que vocês usam hoje. Como vocês a redesenhariam aplicando poka-yoke?"
- **Objetivo**: Aplicar ACI a um caso real
- **Slide**: 46
- **Ação**: Em duplas, 5 min para redesenhar uma tool. Compartilhar 2 exemplos.

---

## Perguntas Bônus (para alunos avançados)

### Q13 — ReAct vs Plan-and-Execute
"ReAct decide a cada step. Plan-and-Execute planeja tudo antes e executa. Qual é melhor e quando?"
- **Objetivo**: Introduzir ETAGT04
- **Resposta**: ReAct é mais adaptativo mas menos eficiente (reescolhe a cada step). Plan-and-Execute é mais eficiente mas menos flexível (se o plano falha, precisa replanejar). ReAct para tarefas imprevisíveis, Plan-and-Execute para tarefas estruturadas.

### Q14 — Context Window vs Persistent Memory
"Se a context window crescesse para 10M tokens, precisaríamos de persistent memory?"
- **Objetivo**: Pensar sobre os limites da memória
- **Resposta**: Sim. Context window maior reduz a necessidade de summarization mas não resolve: (1) custo cresce linearmente; (2) qualidade cai com muito contexto (lost in the middle); (3) memória persistente é entre sessões, não dentro de uma.

### Q15 — Multi-Agente vs Agente com Muitas Tools
"Quando é melhor ter 3 agentes especializados vs 1 agente com 15 tools?"
- **Objetivo**: Introduzir ETHAGT09-10
- **Resposta**: 3 agentes especializados quando as tarefas são distintas e o contexto de cada uma é grande (cada agente tem seu próprio prompt e tools). 1 agente com muitas tools quando as tarefas se sobrepõem e o overhead de comunicação entre agentes é maior que o benefício.
