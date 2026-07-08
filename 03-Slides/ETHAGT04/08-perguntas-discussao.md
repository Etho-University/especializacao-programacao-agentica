# ETHAGT04 — Perguntas para Discussão

> Perguntas para estimular debate durante e após a aula.
> Organizadas por profundidade: rápida (1-2 min) → média (3-5 min) → profunda (10+ min).

---

## Perguntas Rápidas (1-2 min)

### Q1 — Qual Padrão Vocês Usam Hoje?
"Na sua equipe hoje, qual padrão de raciocínio os agentes usam? ReAct puro? CoT? Algo mais?"
- **Objetivo**: Calibrar o nível da turma
- **Slide**: 10
- **Resposta esperada**: A maioria usa ReAct puro ou CoT. Poucos usam ToT/LATS/Reflexion em produção.

### Q2 — CoT Funciona para TUDO?
"Chain-of-Thought resolve a maioria dos problemas de raciocínio. Para quais casos ele falha?"
- **Objetivo**: Estabelecer os limites do CoT
- **Slide**: 14
- **Resposta esperada**: Falha em problemas que requerem backtracking (precisa voltar e tentar outro caminho), planejamento de longo horizonte, e quando o erro se propaga na cadeia.

### Q3 — Experiência com Reasoning Models
"Quem aqui já usou o1, o3 ou Claude com extended thinking em produção?"
- **Objetivo**: Calibrar experiência com inference-time reasoning nativo
- **Slide**: 65
- **Ação**: Contar mãos levantadas — a minoria terá usado

### Q4 — Custo de Self-Consistency
"Self-Consistency amostra N cadeias de pensamento. Se N=10 e cada chamada custa $0.002, quanto custa uma pergunta?"
- **Objetivo**: Praticar cálculo de custo de raciocínio
- **Slide**: 15
- **Cálculo**: 10 × $0.002 = $0.02 por pergunta. Em 10k perguntas/dia = $200/dia = $6k/mês.

---

## Perguntas Médias (3-5 min)

### Q5 — Plan-and-Execute ou ReAct?
"Para uma tarefa de 'analisar e corrigir um bug em produção': Plan-and-Execute ou ReAct? Por quê?"
- **Objetivo**: Aplicar a árvore de decisão ao caso real deles
- **Slide**: 27
- **Dica**: ReAct é melhor — debug é imprevisível, cada observação muda o próximo passo. Plan-and-Execute seria rígido demais.

### Q6 — Quando ToT Vale o Custo?
"Em que cenário da sua empresa Tree of Thoughts justificaria o custo 10x maior?"
- **Objetivo**: Pensar criticamente sobre trade-offs
- **Slide**: 35
- **Resposta esperada**: Quando o problema é de alto valor (decisão estratégica), tem espaço de busca grande, e uma resposta errada é cara. Ex: planejamento de rotas logísticas complexas, design de circuitos.

### Q7 — ReWOO vs ReAct
"Por que ReWOO reduz custo em relação a ReAct? Qual o trade-off?"
- **Objetivo**: Entender a economia de tokens do ReWOO
- **Slide**: 25
- **Resposta esperada**: ReWOO gera o plano completo uma vez (1 chamada grande) e executa workers em paralelo sem re-enviar o contexto a cada step. ReAct reenvia TODO o histórico a cada chamada. Trade-off: ReWOO é menos adaptativo — se uma evidência invalida o plano, precisa replanejar.

### Q8 — Reflexion Converge?
"Seu agente Reflexion falha na tentativa 1. E na 2. E na 3. Quantas tentativas você permite antes de escalar para humano?"
- **Objetivo**: Pensar em limites e guardrails
- **Slide**: 51
- **Resposta esperada**: 3-5 tentativas é o comum. Mais que isso indica que as reflexões não estão sendo úteis (memória está poluída) ou o problema está fora do alcance do modelo.

---

## Perguntas Profundas (10+ min)

### Q9 — Reasoning Model Substitui ToT?
"Com modelos como o1/o3 que raciocinam nativamente, Tree of Thoughts ainda faz sentido? Quando?"
- **Objetivo**: Pensamento crítico sobre o futuro do prompt-based reasoning
- **Slide**: 73
- **Resposta esperada**: Parcialmente. Reasoning models internalizam parte da busca. Mas ToT ainda vale quando: (1) precisa de transparency/auditorabilidade do raciocínio; (2) precisa de backtracking explícito com estado observável; (3) o problema requer integração com tools durante a busca. ToT dá controle; reasoning nativo é caixa preta.

### Q10 — Self-Discover é Sempre Superior a CoT?
"Verdadeiro ou falso: Self-Discover é sempre melhor que CoT. Justifique."
- **Objetivo**: Desconstrair a expectativa de "mais complexo = melhor"
- **Slide**: 60
- **Resposta esperada**: **Falso**. Self-Discover tem overhead (fase de descoberta consome tokens). Para problemas que CoT já resolve bem, Self-Discover é desperdício. Vale para problemas novos, complexos, onde não há padrão pronto. Em benchmarks simples, CoT + Self-Consistency é mais barato e igualmente eficaz.

### Q11 — O Maior Risco de LATS
"Qual o maior risco de usar LATS em produção?"
- **Objetivo**: Conscientização sobre custo e complexidade
- **Slide**: 41
- **Resposta esperada**: Custo explodindo. LATS faz MCTS com LLM como política E valor — cada nó da árvore é uma chamada. Uma árvore de profundidade 5 com branching 3 = até 243 chamadas. Sem orçamento rígido, uma execução pode custar $10+. Segundo risco: latência — minutos para responder.

### Q12 — Orçamento de Reasoning
"Você tem um orçamento de $0.05 por execução. Como aloca entre CoT, ToT e reasoning model nativo?"
- **Objetivo**: Praticar alocação de orçamento
- **Slide**: 79
- **Ação**: Em duplas, 5 min para alocar. Compartilhar 2-3 estratégias.
- **Dica**: Depende do problema. Para 90% dos casos: CoT ($0.002). Para 9%: Self-Consistency com N=5 ($0.01). Para 1% crítico: ToT com orçamento controlado ($0.05). Reasoning model nativo para o mais crítico.

---

## Perguntas Bônus (para alunos avançados)

### Q13 — Reflexion vs Fine-Tuning
"Reflexion aprende com falhas anteriores usando memória verbal. Como isso se compara a fine-tuning? Quando cada um é melhor?"
- **Objetivo**: Conectar com aprendizado de máquina
- **Resposta**: Reflexion é "reinforcement learning verbal" — aprende sem atualizar pesos, em runtime. Vantagem: zero custo de treino, adapta-se a cada instância. Desvantagem: memória é episódica (não generaliza entre sessões sem persistência). Fine-tuning é melhor quando há padrões recorrentes em larga escala; Reflexion é melhor para adaptação rápida a instâncias específicas.

### Q14 — Context Window vs Árvore de Busca
"Se a context window crescesse para 10M tokens, Tree of Thoughts ainda seria necessário?"
- **Objetivo**: Pensar sobre os limites da memória vs busca estruturada
- **Resposta**: Sim. Context window maior não elimina a necessidade de poda. Mais contexto não ajuda a decidir QUAL caminho explorar. ToT resolve o problema de busca, não de armazenamento. Uma árvore de profundidade 10 com branching 5 = 9.7M nós — nem 10M tokens comportam tudo, e mesmo se comportassem, o modelo se perderia.

### Q15 — Quando NÃO Usar Reasoning
"Para quais tarefas adicionar raciocínio (CoT, ToT, etc.) PIORA o resultado?"
- **Objetivo**: Identificar casos onde raciocínio é contraproducente
- **Resposta**: (1) Tarefas simples onde a resposta é direta — raciocínio introduz ruído e alucinação. (2) Classificação com labels restritos — raciocínio pode "superpensar" e sair do label. (3) Geração criativa curta — raciocínio torna o output mais estéril. (4) Tarefas onde a intuição do modelo já é melhor que a deliberação (pattern matching em dados de treino abundantes).
