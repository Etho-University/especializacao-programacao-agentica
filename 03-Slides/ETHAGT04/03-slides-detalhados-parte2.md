# ETHAGT04 — Slides Detalhados + Notas do Professor (Parte 2: Slides 46-90)

> Universidade Etho · Especialização em Programação Agêntica

---

## SEÇÃO E — Reflexion (Slides 46-55 · 12 min)

---

### Slide 46 — Reflexion: Auto-Crítica após Falha

**Título**: Reflexion
**Objetivo**: Apresentar auto-crítica com memória de erros.
**Conteúdo**:
- **Ciclo Reflexion**:
  1. Actor: agente tenta resolver o problema (ReAct)
  2. Evaluator: LLM avalia a tentativa (sucesso/falha + motivo)
  3. Self-Reflection: LLM gera reflexão verbal ("errei porque usei fórmula errada")
  4. Memory: reflexão é armazenada
  5. Actor: agente tenta novamente, com a reflexão no contexto
- **Fonte**: Shinn et al., NeurIPS 2023 (arXiv:2303.11366)

**Diagrama**: `12-Diagrams/ETHAGT04/reflexion-loop.mmd`
**Tempo**: 4 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Reflexion é talvez a técnica mais elegante desta aula. A ideia é simples: quando o agente falha, ele reflete SOBRE O PORQUÊ da falha e guarda essa reflexão. Na próxima tentativa, a reflexão está no contexto. É como um aluno que anota seus erros em um caderno e consulta antes da próxima prova. A memória de reflexão é VERBAL — texto em linguagem natural, não embeddings. Isso é importante: é legível por humanos e interpretável.
💡 ANALOGIA: É como um chef que erra uma receita, anota "excesso de sal", e na próxima vez consulta a nota. A memória não é a receita inteira — é a LIÇÃO.
❓ PERGUNTA: "Quantas tentativas até convergir?" (Tipicamente 3-5; mais que isso geralmente não ajuda)
⚠️ ERROS COMUNS: Alunos confundem Reflexion com "retry". Retry é tentar de novo sem refletir. Reflexion é refletir PRIMEIRO, ajustar, e só então tentar de novo.
➡️ TRANSIÇÃO: "Reflexion vs reflection pattern."

---

### Slide 47 — Reflexion vs Reflection Pattern

**Título**: Reflexion vs Reflection Pattern
**Objetivo**: Distinguir a técnica acadêmica do padrão arquitetural.
**Conteúdo**:
- **Reflection pattern** (genérico): agente gera resposta, depois auto-avalia e revisa
  - Uma passada: gerar → criticar → revisar
  - Sem memória entre tentativas
- **Reflexion** (paper): múltiplas tentativas com MEMÓRIA PERSISTENTE de reflexões
  - Erros anteriores são consultados
  - Aprendizado within-session

**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A diferença é sutil mas crítica. Reflection pattern é uma auto-revisão em uma passada. Reflexion é iterativo com memória. O reflection pattern ajuda em tarefas de uma tentativa. Reflexion ajuda em tarefas onde você pode tentar múltiplas vezes (benchmark, debugging iterativo).
➡️ TRANSIÇÃO: "E quando Reflexion não converge?"

---

### Slide 48 — Convergência e Limites

**Título**: Convergência e Limites da Reflexion
**Objetivo**: Discutir quando Reflexion para de ajudar.
**Conteúdo**:
- **Convergência**: tipicamente 3-5 tentativas melhoram; após isso, retorno marginal
- **Divergência**: se a reflexão é ruim ("errei porque sou burro"), piora as próximas tentativas
- **Mitigação**:
  - Limite de tentativas (max_reflections)
  - Resetar memória se performance piora
  - HITL na reflexão (humano valida a lição)

**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Reflexion nem sempre converge. Se a reflexão é incorreta — "errei porque a fórmula é X" quando na verdade é Y — a memória guia o agente para o erro. Por isso, em produção, é importante ter um limite (max_reflections) e opcionalmente HITL para validar reflexões em tarefas críticas.
➡️ TRANSIÇÃO: "E se o agente pudesse criar sua própria estratégia?"

---

## SEÇÃO F — Self-Discover (Slides 56-63 · 8 min)

---

### Slide 49 — [SEÇÃO] Self-Discover

**Tipo**: Seção
**Tempo**: 0.5 min

---

### Slide 50 — Self-Discover: Composição de Estratégia

**Título**: Self-Discover
**Objetivo**: Mostrar como o agente compõe sua própria estratégia.
**Conteúdo**:
- **Problema**: nem toda tarefa se encaixa em CoT, ToT ou Reflexion
- **Solução**: o agente DESCOBRE qual estratégia usar
- **Processo**:
  1. Selecionar: das primitivas disponíveis, quais são relevantes?
  2. Adaptar: como combinar para ESTE problema?
  3. Implementar: gerar o "raciocínio composto"
- **Fonte**: Major et al., 2024 (arXiv:2402.03620)

**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Self-Discover é meta-raciocínio. O agente não usa uma estratégia fixa — ele RACIOCINA sobre qual estratégia usar para o problema específico. É como um médico que não receita o mesmo remédio para todo paciente — ele diagnostica e escolhe. As primitivas são CoT, ToT, ReAct, decomposition, etc. O agente seleciona quais são relevantes, adapta para o problema, e compõe um plano de raciocínio.
💡 ANALOGIA: É como um cozinheiro que não segue uma receita fixa — ele prova o ingrediente e decide a técnica (assar, ferver, saltear) baseado no que tem.
⚠️ ERROS COMUNS: Self-Discover é mais caro que CoT. Não vale para tarefas onde a estratégia ótima é conhecida.
➡️ TRANSIÇÃO: "Vamos às primitivas."

---

### Slide 51 — Primitivas como Building Blocks

**Título**: Primitivas de Raciocínio
**Conteúdo**:
- **CoT**: pensar passo-a-passo
- **Decomposition**: quebrar em sub-problemas
- **ReAct**: pensar + agir
- **ToT**: explorar múltiplos caminhos
- **Reflexion**: aprender com erros
- O agente combina 2-3 primitivas relevantes para o problema

**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: As primitivas são os LEGO blocks do raciocínio. Self-Discover pega os blocks relevantes para o problema e monta uma estrutura. Para um problema matemático: decomposition + CoT. Para debugging: ReAct + Reflexion. Para planejamento de viagem: ToT + decomposition.
➡️ TRANSIÇÃO: "Agora, a fronteira: reasoning nativo."

---

## SEÇÃO G — Inference-Time Reasoning Nativo (Slides 64-75 · 14 min)

---

### Slide 52 — [SEÇÃO] Inference-Time Reasoning Nativo

**Tipo**: Seção
**Tempo**: 0.5 min

---

### Slide 53 — Modelos Treinados para Pensar

**Título**: Modelos com Reasoning Nativo
**Objetivo**: Apresentar a nova geração de modelos (o1, o3, Claude reasoning).
**Conteúdo**:
- **OpenAI o1/o3**: treinados com RL para raciocínio interno (chain-of-thought oculto)
- **Claude extended thinking**: raciocínio extendido antes de responder
- **Como funcionam**:
  - Geram tokens de raciocínio internos (não visíveis ao usuário)
  - Otimizados via RL para pensar antes de agir
  - "reasoning tokens" têm custo mas melhoram qualidade

**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esta é a maior mudança desde o CoT. Modelos como o1 e o3 são TREINADOS para raciocinar — não precisam de "let's think step by step" no prompt. Eles geram raciocínio interno automaticamente. É como a diferença entre um aluno que precisa ser lembrado de "mostre o cálculo" (CoT) e um aluno que já sabe que deve mostrar (modelo treinado). O custo é em "reasoning tokens" — tokens extras que o modelo gasta pensando antes de responder.
💡 ANALOGIA: É como a diferença entre um estagiário que você precisa instruir passo-a-passo e um sênior que já sabe como abordar o problema.
➡️ TRANSIÇÃO: "O que muda no design do agente?"

---

### Slide 54 — O Que Muda no Design do Agente

**Título**: Impacto no Design do Agente
**Conteúdo**:
- **Sem CoT promptado**: o modelo já raciocina — "let's think step by step" pode atrapalhar
- **Mais tools, menos prompting**: invista em tools e contexto, não em engenharia de prompt
- **Orçamento de reasoning tokens**: definir max_completion_tokens para o raciocínio
- **Menos steps no loop**: cada chamada é mais "pensada", precisa de menos iterações
- **Trade-off**: reasoning model é mais caro por chamada, mas pode precisar de menos chamadas

**Tempo**: 4 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Com reasoning models, o design muda. Você não precisa mais promptar CoT — o modelo faz internamente. Você investe mais em tools e retrieval (contexto) e menos em engenharia de prompt. O orçamento muda: você define quantos "reasoning tokens" o modelo pode gastar. E o loop pode ser mais curto — cada chamada é mais inteligente, então menos iterações.
⚠️ ERROS COMUNS: Alunos continuam usando "let's think step by step" com o1. Isso pode PIORAR a performance — o modelo já sabe pensar.
➡️ TRANSIÇÃO: "Quando escolher cada um?"

---

### Slide 55 — Reasoning Model vs Prompting

**Título**: Quando Usar Reasoning Model vs Prompting
**Conteúdo**:

| Critério | Reasoning Model (o1/o3) | Prompting (CoT/ToT/Reflexion) |
|---|---|---|
| Problema difícil | ✅ Ideal | ⚠️ Funciona mas é mais frágil |
| Custo | ❌ Mais caro por chamada | ✅ Mais barato por chamada |
| Latência | ❌ Alta (raciocínio interno) | ⚠️ Variável |
| Controle | ❌ Caixa preta (raciocínio oculto) | ✅ Transparente |
| Simplicidade | ✅ Sem prompting complexo | ❌ Receita manual |
| Debugging | ❌ Não vê o raciocínio | ✅ Vê cada passo |

**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A escolha depende do contexto. Reasoning models são melhores para problemas difíceis onde o raciocínio opaco é aceitável. Prompting (CoT, ToT, Reflexion) é melhor quando você precisa de transparência, controle e debugging. Em produção com auditoria, a transparência do prompting vence. Em pesquisa de ponta, o reasoning model vence.
➡️ TRANSIÇÃO: "Mas reasoning models têm custo."

---

### Slide 56 — Custo e Latência: Estratégias de Mitigação

**Título**: Gerenciando Custo do Reasoning Nativo
**Conteúdo**:
- **Roteamento**: usar reasoning model só para problemas difíceis (classification → routing)
- **Caching de raciocínio**: se o mesmo problema aparece, reusar o resultado
- **Orçamento**: max_completion_tokens limita quanto o modelo pensa
- **Modelo cascata**: tentar modelo barato primeiro, escalar para reasoning model se falhar

**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Reasoning models são caros. o1 pode custar 5-10x mais que GPT-4o. Para gerenciar: (1) roteamento — classificar a dificuldade e usar reasoning model só para difícil; (2) caching — se a mesma query aparece, reusar; (3) cascata — tentar modelo barato, escalar se falhar. Isso reduz custo mantendo qualidade onde importa.
➡️ TRANSIÇÃO: "Vamos falar de falhas."

---

## SEÇÃO H — Falhas, Loops e Orçamento (Slides 76-84 · 12 min)

---

### Slide 57 — [SEÇÃO] Falhas, Loops e Orçamento

**Tipo**: Seção
**Tempo**: 0.5 min

---

### Slide 58 — Detecção e Quebra de Loops

**Título**: Detecção de Loops
**Conteúdo**:
- **Sintoma**: agente repete as mesmas ações (A→B→A→B ou A→A→A)
- **Detecção**:
  - Hash das últimas N ações — se repetidas, alerta
  - Embedding similarity — se ações semanticamente iguais, alerta
  - Contador de repetição — se mesma action > 3x, intervir
- **Quebra**:
  - Forçar resposta final
  - Disparar Reflexion (refletir sobre o loop)
  - HITL: humano decide

**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Loops são o bug mais comum em agentes. A detecção é simples: se a mesma ação (ou ação semanticamente similar) aparece 3+ vezes seguidas, algo está errado. A quebra pode ser: forçar resposta, refletir (Reflexion), ou HITL. Em produção, a detecção de loops é um guardrail obrigatório — sem ele, o agente pode gastar todo o orçamento em um loop inútil.
➡️ TRANSIÇÃO: "Orçamento."

---

### Slide 59 — Orçamento de Tokens e Passos

**Título**: Orçamento como Guardrail
**Conteúdo**:
- **max_steps**: limite de iterações do loop (obrigatório)
- **max_tokens**: limite de tokens totais por execução
- **max_cost**: limite em dólares por execução
- **max_time**: timeout em segundos
- **Orçamento por componente**: raciocínio vs tools vs retrieval

**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Orçamento não é otimização — é segurança. Sem max_steps, o agente pode iterar infinitamente. Sem max_cost, você descobre no fim do mês. Sem max_time, o usuário fica esperando para sempre. Defina TODOS desde o dia 1. Em produção, cada execução tem um orçamento e o agente é interrompido se exceder.
➡️ TRANSIÇÃO: "Re-planejamento supervisionado."

---

### Slide 60 — Re-planejamento Supervisionado

**Título**: HITL no Planejamento
**Conteúdo**:
- Em tarefas de alto risco: humano aprova o plano antes da execução
- Checkpoints de validação: após cada passo crítico, humano valida
- Se humano rejeita: agente re-planeja com o feedback
- Frameworks: LangGraph interrupt_before, OpenAI handoffs

**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Em tarefas de alto risco (finanças, saúde, operações irreversíveis), o plano não deve ser executado sem aprovação humana. O humano vê o plano, aprova ou ajusta, e só então o executor age. Checkpoints adicionais permitem validação após passos críticos. Se o humano rejeita, o agente re-planeja com o feedback. Isso é essencial em compliance.
➡️ TRANSIÇÃO: "Vamos fechar."

---

## SEÇÃO I — Fechamento (Slides 85-90 · 8 min)

---

### Slide 61 — Comparação Geral das Estratégias

**Título**: Quadro Comparativo Final
**Conteúdo**:

| Técnica | Estrutura | Custo | Melhor para |
|---|---|---|---|
| ReAct | Linear | Baixo | Tarefas adaptativas |
| Plan-and-Execute | Linear + plano | Médio | Tarefas estruturadas |
| ReWOO | Paralelo | Baixo | Tarefas independentes |
| ToT | Árvore | Alto | Problemas de busca |
| LATS | Grafo (MCTS) | Muito alto | Problemas muito difíceis |
| Reflexion | Linear + memória | Médio | Tarefas iterativas |
| Self-Discover | Composição | Médio-Alto | Problemas sem padrão |
| Reasoning nativo | Interno | Alto | Problemas difíceis |

**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Este quadro é o resumo da aula. Cada técnica tem seu lugar. A arte do arquiteto de agentes é saber escolher. Não existe "melhor técnica" — existe a técnica certa para o problema, o orçamento e o risco.
➡️ TRANSIÇÃO: "Anti-patterns."

---

### Slide 62 — Anti-Patterns

**Título**: Anti-Patterns (DON'T)
**Conteúdo**:
- ❌ Usar ToT/LATS para problemas simples (overkill)
- ❌ Reflexion sem limite de tentativas (loop de reflexão)
- ❌ Plan-and-Execute sem Replanner (plano rígido)
- ❌ ReWOO quando as tools são dependentes (não paralelizável)
- ❌ "let's think step by step" com reasoning model (atrapalha)
- ❌ Sem orçamento de tokens/custo (descoberta no fim do mês)
- ❌ Sem detecção de loops (gasto infinito)

**Tempo**: 2 min

---

### Slide 63 — Quiz Final

**Título**: Quiz
**Conteúdo**: 5 perguntas (ver arquivo 10-quiz-final.md)

**Tempo**: 2 min

---

### Slide 64 — Conexão com Próximos Módulos

**Título**: Próximos Passos
**Conteúdo**:
- ETHAGT05 — Memória de Agentes: estende Reflexion com memória persistente
- ETHAGT06 — RAG Agêntico: raciocínio + recuperação combinados
- ETHAGT09 — Multi-Agente: múltiplos agentes raciocinando juntos

**Tempo**: 1 min

---

### Slide 65 — Leitura Recomendada

**Título**: Leitura Recomendada
**Conteúdo**:
- Yao et al. *Tree of Thoughts* (arXiv:2305.10601)
- Shinn et al. *Reflexion* (arXiv:2303.11366)
- Zhou et al. *LATS* (arXiv:2310.01757)
- Major et al. *Self-Discover* (arXiv:2402.03620)
- OpenAI *Learning to Reason with LLMs* (o1 paper)

**Tempo**: 1 min

---

### Slide 66 — Q&A / Encerramento

**Título**: Perguntas?
**Conteúdo**: "Na próxima aula: ETHAGT05 — Memória de Agentes"
**Tempo**: 2 min

---

## Resumo das Notas do Professor

| Slide | Conceito-chave | Analogia |
|---|---|---|
| 5 | ReAct falha sem backtracking | Beco sem saída sem ré |
| 8 | CoT = pensar em voz alta | Aluno mostrando o cálculo |
| 10 | Antes vs Durante | GPS (antes) vs espelho (durante) |
| 14 | Plan-and-Execute | Arquiteto + pedreiro |
| 15 | ReWOO | 3 pesquisadores em paralelo |
| 20 | ToT | Xadrez: considerar múltiplas jogadas |
| 21 | LATS/MCTS | Explorador marcando trilhas no mapa |
| 46 | Reflexion | Chef anotando erros no caderno |
| 50 | Self-Discover | Médico diagnosticando antes de receitar |
| 53 | Reasoning nativo | Sênior vs estagiário |

---

> Fim da Parte 2.
