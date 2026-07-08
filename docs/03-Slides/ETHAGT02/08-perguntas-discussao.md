# ETHAGT02 — Perguntas para Discussão

> Perguntas para estimular debate durante e após a aula.
> Organizadas por profundidade: rápida (1-2 min) → média (3-5 min) → profunda (10+ min).

---

## Perguntas Rápidas (1-2 min)

### Q1 — Tool vs Prompt
"Já tiveram algum bug onde a solução parecia ser melhorar o prompt, mas o problema era a tool mal desenhada?"
- **Objetivo**: Conectar a experiência da turma com o princípio ACI
- **Slide**: 5
- **Ação**: Deixar 2-3 alunos compartilharem experiências

### Q2 — Quantas Tools é Demais?
"Quantas tools vocês têm no agente de produção de vocês hoje? Sentem degradação de qualidade?"
- **Objetivo**: Conectar com o trade-off de Gorilla (degradação com muitas tools)
- **Slide**: 12
- **Resposta esperada**: >15-20 tools começa a degradar; contexto necessário para MCP (ETHAGT08)

### Q3 — Poka-yoke na Prática
"Qual tool de vocês poderia ser redesenhada com poka-yoke hoje?"
- **Objetivo**: Pensar em poka-yoke aplicado a caso real
- **Slide**: 21
- **Ação**: Deixar 1-2 responderem rapidamente

### Q4 — HITL em Produção
"Vocês têm HITL em algum agente de produção hoje? Como funciona?"
- **Objetivo**: Calibrar maturidade da turma em governança
- **Slide**: 36
- **Resposta esperada**: <30% tem HITL estruturado; a maioria tem "humano revisa depois"

---

## Perguntas Médias (3-5 min)

### Q5 — Schema Frouxo vs Apertado
"Vocês preferem um schema permissivo (qualquer string) ou restritivo (enum + pattern)? Qual o trade-off?"
- **Objetivo**: Pensar sobre validação de schema como poka-yoke
- **Slide**: 9
- **Resposta esperada**: Restritivo é mais seguro mas menos flexível. Enum/pattern reduz erros do modelo. Comece restritivo, abra só com evidência.

### Q6 — 1 Tool com Mode vs 2 Separadas
"Para `create_user` e `update_user`: 1 tool com `mode` ou 2 tools separadas? Por quê?"
- **Objetivo**: Aplicar a regra dos 80%
- **Slide**: 33
- **Resposta esperada**: Se >80% dos casos usam ambas (ex.: admin panel), consolidar em 1 com mode. Se raramente se sobrepõem, separar.

### Q7 — Erro Tratado ou Propagado
"Quando uma tool falha, o que o modelo recebe? Traceback cru ou mensagem estruturada?"
- **Objetivo**: Pensar em error handling como parte de ACI
- **Slide**: 40
- **Resposta esperada**: Mensagem estruturada (`{"error": "...", "suggestion": "..."}`). Traceback cru confunde o modelo.

### Q8 — Custo de Tools em Escala
"Seu agente tem 10 tools com descrições de 200 tokens cada. A $0.15/1M tokens (input), quanto custa a descrição das tools por chamada? E com 1000 chamadas/dia?"
- **Objetivo**: Praticar cálculo de custo de tokens de descrição
- **Slide**: 12
- **Cálculo**: 10 × 200 = 2000 tokens × $0.15/1M = $0.0003/chamada. 1000/dia = $0.30/dia = $9/mês. Com 30 tools: $27/mês só em descrição.

---

## Perguntas Profundas (10+ min)

### Q9 — Toda Tool Destrutiva Precisa de HITL?
"Toda tool irreversível precisa de HITL? Existem exceções? Como decidir?"
- **Objetivo**: Pensar criticamente sobre a matriz de risco
- **Slide**: 35
- **Resposta esperada**: HITL é obrigatório quando irreversível E impactante. Exceção: tool irreversível mas de baixo impacto (ex.: `log_event` que sobrescreve) pode não precisar. O critério é reversibilidade × impacto, não só reversibilidade.

### Q10 — Idempotência é Sempre Necessária?
"Quando a idempotência é ESSENCIAL e quando é over-engineering?"
- **Objetivo**: Distinguir necessidade real de padrão aplicado cegamente
- **Slide**: 29
- **Resposta esperada**: Essencial em: writes com external side-effect (email, payment, deploy), retry automático, ambientes instáveis. Over-engineering em: reads puros (search, get), tools sem estado, calls que nunca são retentadas.

### Q11 — Versionamento sem Quebrar Agentes
"Como você versiona uma tool sem quebrar agentes já em produção?"
- **Objetivo**: Pensar em compatibilidade retroativa de tools
- **Slide**: 32
- **Resposta esperada**: (1) adições não-quebram (novo parâmetro opcional); (2) remoções quebram — usar deprecation com sobreposição; (3) mudança de tipo quebra — criar `search_product_v2`; (4) manter ambas ativas por um ciclo de depreciação; (5) log de uso para saber quando desligar a versão antiga.

### Q12 — Workbench: Quando Parar de Iterar?
"Você refatorou uma tool 3 vezes no workbench e a taxa de uso correto passou de 60% → 80% → 85%. Vale a pena iterar mais?"
- **Objetivo**: Pensar em diminishing returns
- **Slide**: 42
- **Resposta esperada**: Depende do critério de sucesso. Se meta é ≥85%, parar. Se meta é ≥95%, analisar onde os 15% de erro acontecem — se são edge cases raros, parar. Se são sistemáticos, iterar mais. Lei dos diminishing returns: cada iteração rende menos que a anterior.

---

## Perguntas Bônus (para alunos avançados)

### Q13 — MCP vs Tools Customizadas
"Qual a diferença entre uma tool customizada e uma tool exposta via MCP? Quando usar cada?"
- **Objetivo**: Introduzir ETHAGT08 (MCP)
- **Resposta**: MCP padroniza a descoberta e descrição de tools, permitindo reuso entre agentes e provedores. Tool customizada é mais simples para casos isolados. MCP brilha quando múltiplos agentes precisam das mesmas tools ou quando integra com terceiros.

### Q14 — Structured Outputs vs Function Calling
"Structured outputs e function calling são a mesma coisa? Qual a diferença?"
- **Objetivo**: Esclarecer dois mecanismos frequentemente confundidos
- **Resposta**: Function calling é o modelo decidir CHAMAR uma tool (produz tool_call JSON). Structured outputs é forçar a RESPOSTA inteira a seguir um schema (não envolve execução). Ambos usam JSON Schema, mas o propósito é diferente: um é para ação, outro é para formato.

### Q15 — HITL vs Guardrails
"Qual a diferença entre HITL e guardrails programáticos? Quando cada um é melhor?"
- **Objetivo**: Pensar em camadas de proteção
- **Resposta**: HITL exige aprovação humana explícita antes da ação (caro, lento, mas máximo controle). Guardrails são validações programáticas (regex, allowlist, limites) executadas sem humano (rápido, barato, mas não captura nuances). HITL para ações destrutivas/irreversíveis. Guardrails para validação de formato e limites.
