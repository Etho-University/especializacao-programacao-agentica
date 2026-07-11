# ETHAGT01 — Slides Detalhados + Notas do Professor (Parte 2: Slides 32-62)

> Universidade Etho · Especialização em Programação Agêntica
> Continuação da Parte 1.

---

### Slide 32 — LangGraph: O Que Ele Abstrai

**Título**: LangGraph: Abstração Controlada
**Objetivo**: Mostrar o que o framework oferece e o que esconde.
**Conteúdo**:
- **O que LangGraph abstrai**:
  - Loop → `StateGraph` com nodes e edges
  - Estado → `Checkpointer` (Postgres, SQLite) embutido
  - Tools → `ToolNode` wrapper automático
  - Streaming → PEP nativo
- **O que LangGraph esconde**:
  - Prompt efetivo (framework adiciona system prompt)
  - Formato exato das messages (serialização interna)
  - Lógica de retry (precisa configurar explicitamente)
- **Snippet**:
```python
from langgraph.prebuilt import create_react_agent

agent = create_react_agent(model, tools=TOOLS)
result = agent.invoke({"messages": [{"role": "user", "content": "Quanto é 123*456+789?"}]})
```
- **Quando usar**: POC → produção, quando precisa de checkpointer mas quer controle do grafo

**Diagrama**: `12-Diagrams/ETHAGT01/framework-comparison.mmd` (lado direito — Framework)
**Animação**: Código aparece com syntax highlighting
**Imagem**: Diagrama framework-comparison (lado direito)
**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: LangGraph é o meio-termo. Ele abstrai o loop (você não escreve `for step in range`), abstrai o estado (checkpointer embutido), e abstrai as tools (ToolNode). Mas você ainda vê o grafo: sabe quais são os nodes, sabe as edges, sabe o fluxo. O que ele esconde é o prompt efetivo — o framework adiciona system prompts que você não escreveu. Isso pode ser bom (boas práticas embutidas) ou ruim (você não sabe exatamente o que o modelo está recebendo). A função `create_react_agent` é o atalho máximo: 2 linhas e você tem um agente ReAct funcional. Mas se precisar customizar o loop, pode usar StateGraph explicitamente.
💡 ANALOGIA: É como usar um framework web (Flask/FastAPI) vs HTTP puro. O framework abstrai routing, parsing, middleware — mas você ainda vê a lógica de negócio. Se precisar de controle total, pode descer até WSGI. LangGraph é assim: abstrai o repetitivo, deixa você ver o importante.
❓ PERGUNTA PARA A TURMA: "Qual a desvantagem de `create_react_agent` vs StateGraph custom?" (Resposta: menos controle sobre o loop — se precisar de lógica custom como "a cada 3 steps, fazer X", precisa do StateGraph)
⚠️ ERROS COMUNS: Alunos usam `create_react_agent` sem ler o código fonte. Quando o agente faz algo inesperado, não sabem onde procurar. Sempre ler o que o framework faz por baixo dos panos.
➡️ TRANSIÇÃO: "E se subirmos mais um nível de abstração?"

---

### Slide 33 — OpenAI Agents SDK: A Camada Mais Alta

**Título**: OpenAI Agents SDK: Máxima Produtividade
**Objetivo**: Mostrar a abstração mais alta e seus trade-offs.
**Conteúdo**:
- **O que o SDK abstrai**:
  - Tudo do LangGraph + orquestração multi-agente
  - Handoffs entre agentes
  - Guardrails embutidos
  - Tracing nativo
- **O que esconde**:
  - Quase tudo sobre o prompt efetivo
  - Lógica de loop (caixa preta)
  - Serialização de estado (opaca)
- **Snippet**:
```python
from agents import Agent, Runner

agent = Agent(
    name="Calculator Agent",
    instructions="Você é um agente ReAct. Use tools quando necessário.",
    tools=[calculator_tool]
)
result = Runner.run_sync(agent, "Quanto é 123 * 456 + 789?")
```
- **Quando usar**: POC rápido, demos, prototipagem
- **Quando NÃO usar**: produção com requisitos de auditoria, debug granular

**Diagrama**: 3 camadas empilhadas (Python puro → LangGraph → OpenAI SDK)
**Animação**: Camadas aparecem de baixo para cima
**Imagem**: Pirâmide de abstração invertida
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O OpenAI Agents SDK é a camada mais alta. Você define um Agent com nome, instructions e tools, chama Runner.run_sync, e pronto. O SDK cuida do loop, do estado, dos retries, do tracing, dos handoffs. É extremamente produtivo — em 5 linhas você tem um agente funcional com tracing nativo. MAS: você está em uma caixa preta. O prompt efetivo inclui system prompts do SDK que você não controla. A lógica de loop é interna — se quiser "a cada 5 steps, forçar HITL", precisa ver se o SDK suporta. Para POC é perfeito. Para produção com requisitos de auditoria (preciso provar para o compliance que o agente fez X porque Y), a caixa preta é um problema.
💡 ANALOGIA: É como usar Wix/WordPress vs codar um site do zero. Wix é extremamente produtivo — você tem um site em 1 hora. Mas se precisar de controle granular de SEO, performance, ou segurança, o código do zero dá mais poder. Tudo é trade-off.
⚠️ ERROS COMUNS: Alunos usam o SDK em produção sem entender o que ele faz. Quando o compliance pergunta "por que o agente tomou essa decisão?", a resposta "o SDK decidiu" não é aceitável.
➡️ TRANSIÇÃO: "Vamos sistematizar a comparação."

---

### Slide 34 — Comparação Estrutural

**Título**: Comparação Estrutural: 3 Abordagens
**Objetivo**: Sistematizar os trade-offs em uma tabela.
**Conteúdo**:

| Critério | Python Puro | LangGraph | OpenAI SDK |
|---|---|---|---|
| Controle do prompt | ✅ Total | ⚠️ Parcial | ❌ Mínimo |
| Transparência do loop | ✅ Total | ✅ Alto | ❌ Baixo |
| Estado/Checkpointer | ❌ Manual | ✅ Embutido | ✅ Embutido |
| Tools | ✅ Você valida | ⚠️ Wrapper | ⚠️ Wrapper |
| Curva de aprendizado | ✅ Baixa (sabe Python) | ⚠️ Média | ⚠️ Média |
| Linhas de código | ~50 | ~20 | ~15 |
| Produção-ready | ⚠️ Precisa construir | ✅ Sim | ✅ Sim |
| Debug granular | ✅ Total | ✅ Alto | ❌ Limitado |
| Multi-agente | ❌ Manual | ✅ Nativo | ✅ Nativo |
| Tracing | ❌ Manual | ✅ LangSmith | ✅ Nativo |

**Diagrama**: Tabela comparativa colorida (verde/amarelo/vermelho)
**Animação**: Colunas aparecem uma a uma
**Imagem**: Tabela com ícones de check/warning/cross
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A tabela mostra que não há "vencedor". Python puro ganha em controle e transparência mas perde em produtividade. OpenAI SDK é o oposto. LangGraph é o meio-termo. A escolha depende do CONTEXTO: POC de 1 semana? SDK ou LangGraph. Produção com auditoria? Python puro ou LangGraph. Time júnior? LangGraph (abstrai complexidade). Time sênior que quer controle? Python puro. A regra da Anthropic: "se usar framework, entenda o código por baixo". Isso é não-negociável.
💡 ANALOGIA: É como escolher entre manual, automático e CVT. Não há "melhor" — há o certo para o motorista, para a estrada, e para o orçamento.
❓ PERGUNTA PARA A TURMA: "Qual critério da tabela é mais importante para o sistema de vocês?" (Deixar 2-3 responderem)
⚠️ ERROS COMUNS: Alunos focam em "linhas de código" como critério principal. Linhas de código é o critério MENOS importante. Controle, transparência e debug são muito mais valiosos em produção.
➡️ TRANSIÇÃO: "E quando você DEVE reduzir as camadas de abstração?"

---

### Slide 35 — Quando Reduzir Camadas de Abstração

**Título**: Quando Reduzir Camadas
**Objetivo**: Critério para decidir quando sair do framework.
**Conteúdo**:
- **Sinais de alerta** (se você disser qualquer um destes, reduza abstração):
  - "Não entendo por que o agente fez X"
  - "O prompt efetivo é diferente do que escrevi"
  - "Custo inesperado — não sei onde os tokens estão indo"
  - "Latência inexplicável — não sei qual step está lento"
  - "Não consigo reproduzir o bug localmente"
  - "O framework adiciona system prompts que eu não controlo"
- **Regra da Anthropic**: "Ensure you understand the underlying code"
- **Quando reduzir**:
  - Produção com SLA rigoroso
  - Compliance/auditoria requer rastreabilidade
  - Custo precisa ser otimizado beyond defaults
  - Bug que só reproduz em produção

**Diagrama**: Checklist de "sinais de alerta" com ícones de warning
**Animação**: Itens aparecem um a um (on click)
**Imagem**: Semáforo (verde = ok, amarelo = atenção, vermelho = reduzir)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Frameworks são ótimos para começar rápido. Mas em produção, a opacidade se torna um problema. Se você não consegue explicar POR QUE o agente tomou uma decisão, você tem um problema de auditoria. Se não sabe onde os tokens estão sendo gastos, você tem um problema de custo. Se não consegue reproduzir um bug, você tem um problema de confiabilidade. A Anthropic é explícita: "Incorrect assumptions about what's under the hood are a common source of customer error." A solução não é "nunca usar framework" — é "entender o que está sob o hood". Se não entende, ou aprende, ou desce para Python puro.
💡 ANALOGIA: É como dirigir um carro sem saber trocar pneu. Na cidade, tudo bem — chame o guincho. Na estrada remota, você precisa saber. Em produção, você está na estrada remota.
❓ PERGUNTA PARA A TURMA: "Vocês já disseram alguma dessas frases sobre um sistema de vocês?" (A maioria vai levantar a mão)
⚠️ ERROS COMUNS: Alunos acham que "framework X é transparente porque tem docs". Docs não são código. O código é o que roda. Ler o código fonte do framework pelo menos uma vez.
➡️ TRANSIÇÃO: "Discussão aberta sobre a escolha de framework."

---

### Slide 36 — Pergunta: Framework ou Não?

**Título**: Discussão: Qual Framework?
**Objetivo**: Discussão aberta sobre escolha de framework.
**Conteúdo**:
- **Pergunta 1**: "Qual framework dá mais controle? E mais produtividade?"
- **Pergunta 2**: "Em que cenário você NÃO usaria framework nenhum?"
- **Pergunta 3**: "Como convencer um PM de que Python puro é melhor que SDK?"
- **Discussão aberta** (3 min)
- **Síntese do professor** (1 min):
  - Controle: Python puro > LangGraph > SDK
  - Produtividade: SDK > LangGraph > Python puro
  - A resposta certa depende do contexto, não existe "sempre usar X"

**Diagrama**: 3 perguntas em destaque
**Animação**: Perguntas aparecem uma a uma
**Imagem**: Balões de discussão
**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Deixar a turma discutir por 3 minutos. Intervir apenas se a discussão ficar off-topic. A síntese deve reforçar: (1) não há "melhor framework" — há o certo para o contexto; (2) a Anthropic recomenda começar com LLM API direto e só usar framework se necessário; (3) se usar framework, LEIA o código fonte; (4) em produção, a transparência vale mais que a produtividade.
💡 ANALOGIA: É como a eterna debate "SQL vs NoSQL". A resposta sempre é "depende do seu caso de uso, dos seus dados, da sua equipe". Frameworks são iguais.
⚠️ ERROS COMUNS: Alunos transformam a discussão em "meu framework é melhor que o seu". Redirecionar: "não é sobre qual é melhor, é sobre qual é o certo para o seu contexto."
➡️ TRANSIÇÃO: "Último bloco de teoria antes do fechamento: observabilidade."

---

## SEÇÃO E — Observabilidade (Slides 37-41 · 8 min)

---

### Slide 37 — [SEÇÃO] Observabilidade Desde o Dia 1

**Título**: 6 — Observabilidade Desde o Dia 1
**Objetivo**: Transição para observabilidade.
**Conteúdo**: "6 — Observabilidade Desde o Dia 1"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "6" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Observabilidade não é "fase de produção". É algo que você adiciona na PRIMEIRA linha de código do seu agente. Sem observabilidade, você está dirigindo no escuro. O aprofundamento vem em ETHAGT12 (AgentOps), mas os conceitos básicos ficam hoje.
➡️ TRANSIÇÃO: "Por que desde o dia 1?"

---

### Slide 38 — Por Que Observabilidade desde o Início?

**Título**: Por Que Desde o Dia 1?
**Objetivo**: Justificar por que traces não são "nice to have".
**Conteúdo**:
- **Sem traces**: melhoria é adivinhação
  - "O agente errou" — por quê? Qual step? Qual tool? Qual prompt?
  - "Custo subiu" — onde? Qual step consumiu mais?
  - "Latência alta" — em qual step?
- **Com traces**: você vê o pensamento do agente
  - Cada Thought, Action, Observation logado
  - Custo e latência por step
  - Possível reproduzir e debugar
- **Analogia**: "Logar é como ligar as luzes antes de procurar algo no escuro"
- **Em produção**: debugging sem traces = impossível
  - "O que o agente fez às 14:32 quando o usuário X pediu Y?"
  - Sem trace, essa pergunta não tem resposta

**Diagrama**: Antes (escuro, confuso) vs Depois (iluminado, claro)
**Animação**: Transição de escuro → iluminado (fade)
**Imagem**: Lâmpada acendendo
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A diferença entre um sistema observável e um não-observável é a diferença entre "o agente errou" e "o agente errou porque no step 3, a tool calculator recebeu args inválidos porque o modelo alucinou o parâmetro 'op' como 'multiply' em vez de '*'". Sem traces, você só sabe que errou. Com traces, você sabe por quê, onde e como corrigir. Em produção, isso é a diferença entre um hotfix de 5 minutos e 3 horas de debug.
💡 ANALOGIA: É como a caixa preta de um avião. Você não espera o avião cair para instalar a caixa preta. Ela está lá desde o primeiro voo. Se algo der errado, você tem os dados. Se não der errado, os dados te ajudam a otimizar.
❓ PERGUNTA PARA A TURMA: "Vocês têm traces nos sistemas de LLM de vocês hoje?" (A maioria não tem — este é o ponto)
⚠️ ERROS COMUNS: Alunos adicionam logs após o primeiro bug em produção. O problema: o bug já aconteceu e você não tem os dados. Logs são preventivos, não reativos.
➡️ TRANSIÇÃO: "Vamos ver o padrão mínimo de logging."

---

### Slide 39 — Logging Estruturado

**Título**: Logging Estruturado
**Objetivo**: Mostrar o padrão mínimo de logging para agentes.
**Conteúdo**:
- **Formato**: JSON estruturado com campos padronizados
- **Campos mínimos**:
  - `timestamp` — quando
  - `step` — qual iteração do loop
  - `thought` — o que o modelo pensou
  - `action` — qual tool chamou (ou "answer")
  - `action_args` — argumentos da tool
  - `observation` — resultado da tool
  - `tokens_in` / `tokens_out` — consumo
  - `cost_usd` — custo do step
  - `latency_ms` — tempo do step
- **Snippet**:
```python
import json, time

def log_step(step, thought, action, args, obs, usage):
    log = {
        "timestamp": time.isoformat(),
        "step": step,
        "thought": thought,
        "action": action,
        "args": args,
        "observation": obs,
        "tokens_in": usage.prompt_tokens,
        "tokens_out": usage.completion_tokens,
        "cost_usd": (usage.prompt_tokens * 0.15 + usage.completion_tokens * 0.60) / 1_000_000,
        "latency_ms": elapsed
    }
    print(json.dumps(log, ensure_ascii=False))
```
- **Evolução**: print → structured logs → LangSmith / Phoenix / Langfuse

**Diagrama**: Exemplo de JSON log com syntax highlighting
**Animação**: Campos do JSON aparecem um a um
**Imagem**: Terminal com JSON colorido
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O padrão mínimo é JSON estruturado com os campos do slide. Cada step do loop gera um log. O `thought` é a parte mais importante — sem ele, você sabe O QUE o agente fez mas não POR QUÊ. O custo e a latência por step permitem identificar gargalos. Em POC, `print(json.dumps(log))` é suficiente. Em produção, evolua para uma ferramenta de tracing (LangSmith, Phoenix, Langfuse) que oferece visualização, busca e alertas. O aprofundamento vem em ETHAGT12.
💡 ANALOGIA: É como o extrato de banco. Cada transação tem data, valor, descrição. Sem o extrato, você não sabe para onde o dinheiro foi. Sem logs estruturados, você não sabe para onde os tokens (e dólares) foram.
⚠️ ERROS COMUNS: Alunos logam só a Action e a Observation, esquecendo o Thought. Sem o Thought, o trace é um lista de chamadas sem contexto. Parece um robô executando comandos cegamente.
➡️ TRANSIÇÃO: "Acima do logging estruturado, há o conceito de trace."

---

### Slide 40 — Traces: O Que São

**Título**: Traces: O Que São
**Objetivo**: Introduzir o conceito de trace (aprofundamento em ETHAGT12).
**Conteúdo**:
- **Trace** = árvore de spans que representa a execução completa de um agente
- **Span** = unidade atômica do trace:
  - Nome (ex: "LLM call", "tool: calculator", "retrieval")
  - Duração (start → end)
  - Input (o que entrou)
  - Output (o que saiu)
  - Metadata (tokens, cost, model)
- **Visualização**: timeline de execução (cada span é uma barra horizontal)
- **Estrutura hierárquica**:
```
Agent Run (root span)
├── LLM Call #1 (step 0)
│   └── Tool: calculator (123, 456, *)
├── LLM Call #2 (step 1)
│   └── Tool: calculator (56088, 789, +)
└── LLM Call #3 (step 2 — final answer)
```
- **Ferramentas**: LangSmith, Phoenix (Arize), Langfuse, OpenTelemetry

**Diagrama**: Árvore de spans com timeline (cada span = barra horizontal colorida)
**Animação**: Spans aparecem na timeline sequencialmente
**Imagem**: Screenshot de trace do LangSmith ou Phoenix
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Um trace é como um profile de execução. Cada chamada de LLM, cada tool, cada retrieval é um span. Os spans formam uma árvore — o root span é a execução completa, e os child spans são as chamadas individuais. A visualização em timeline mostra não só o que aconteceu, mas QUANDO e QUANTO TEMPO levou. Isso é valioso para identificar gargalos: se o step 3 levou 80% do tempo total, você sabe onde otimizar. As ferramentas (LangSmith, Phoenix, Langfuse) oferecem isso out-of-the-box. Em ETHAGT12 vamos aprofundar em traces, avaliação e benchmarks.
💡 ANALOGIA: É como o DevTools do navegador mostrando o waterfall de uma página web. Cada recurso (CSS, JS, imagem) é uma barra na timeline. Você vê o que carregou rápido, o que demorou, o que bloqueou. O trace de agente é a mesma coisa, mas para chamadas de LLM e tools.
❓ PERGUNTA PARA A TURMA: "Quem aqui já usou LangSmith ou Phoenix?" (Calibrar experiência)
⚠️ ERROS COMUNS: Alunos confundem log com trace. Log é uma linha de texto (ou JSON). Trace é uma árvore estruturada com timing e hierarquia. Log é suficiente para POC; trace é necessário para produção.
➡️ TRANSIÇÃO: "Além de ver o que aconteceu, você precisa medir quanto custou."

---

### Slide 41 — Custo e Latência como Métricas de Primeira Classe

**Título**: Custo e Latência como Métricas de Primeira Classe
**Objetivo**: Fixar que custo e latência devem ser medidos desde o início.
**Conteúdo**:
- **Custo por step**:
  - `tokens_in × price_in + tokens_out × price_out`
  - Exemplo: gpt-4o-mini = $0.15/1M in + $0.60/1M out
  - 10 steps × 2k tokens in × 500 tokens out = $0.003 + $0.003 = $0.006 por execução
  - 1000 execuções/dia = $6/dia = $180/mês
- **Latência cumulativa**:
  - Serial: cada step espera o anterior → latência_total = Σ latência_step
  - 10 steps × 2s = 20s total
  - Paralelização reduz latência mas aumenta complexidade
- **Dashboard mínimo**:
  - Step, tokens in/out, custo, latência
  - Custo acumulado por execução
  - Latência p50/p95/p99
- **Em produção**: orçamento por execução (max_cost), alertas se exceder

**Diagrama**: Mini-dashboard com métricas (gráfico de barras + números)
**Animação**: Métricas aparecem com wipe
**Imagem**: Dashboard mockup
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Custo e latência não são "detalhes de produção" — são métricas de primeira classe. Cada step do agente consome tokens e tempo. Sem medir, você não sabe se seu agente custa $0.01 ou $1.00 por execução. A diferença é 100x — em escala, isso é a diferença entre $1k/mês e $100k/mês. A latência é igualmente crítica: se o agente leva 20s para responder, o usuário desiste. O dashboard mínimo é: por step, tokens e custo; por execução, custo total e latência p50/p95. Em produção, defina orçamento: se custo > $X, abortar. Se latência > Ys, alertar.
💡 ANALOGIA: É como a conta de energia. Você não espera a conta chegar no fim do mês para descobrir que gastou muito. Você tem um medidor que mostra consumo em tempo real. Sem esse medidor, o gasto pode explodir sem você perceber.
⚠️ ERROS COMUNS: Alunos calculam custo apenas com a primeira chamada. Esquecem que o loop multiplica: 10 steps × 2k tokens = 20k tokens, não 2k. O contexto cresce a cada step porque as messages anteriores ficam no prompt.
➡️ TRANSIÇÃO: "Isso conclui a parte de teoria. Vamos ao fechamento."

---

## SEÇÃO F — Fechamento (Slides 42-62 · 12 min)

---

### Slide 42 — [SEÇÃO] Boas Práticas e Anti-Patterns

**Título**: 7 — Boas Práticas e Anti-Patterns
**Objetivo**: Transição para o fechamento.
**Conteúdo**: "7 — Boas Práticas e Anti-Patterns"
**Diagrama**: Fundo `etho-primary` (#1B3A5E)
**Animação**: Morph (400ms)
**Imagem**: Número "7" em fonte grande, branco
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vamos consolidar tudo que vimos em boas práticas (DO) e anti-patterns (DON'T). Esta é a parte que vocês devem anotar e levar para o trabalho.
➡️ TRANSIÇÃO: "Começando pelo que fazer."

---

### Slide 43 — Boas Práticas (DO)

**Título**: Boas Práticas
**Objetivo**: Checklist de boas práticas.
**Conteúdo**:
- ✅ **Comece simples** — single LLM call antes de agente
- ✅ **Documente tools** como se fosse para um desenvolvedor júnior
- ✅ **Defina max_steps** desde o dia 1
- ✅ **Log estruturado** desde a primeira linha de código
- ✅ **Sandbox** para execução de tools (especialmente código)
- ✅ **HITL** em pontos críticos (antes de ações irreversíveis)
- ✅ **Otimize o prompt efetivo**, não apenas o prompt que você escreve
- ✅ **Entenda o framework** — leia o código fonte
- ✅ **Meça custo e latência** por step desde o início
- ✅ **Teste em sandbox** antes de produção

**Diagrama**: Checklist verde (`etho-success` #2D8659)
**Animação**: Itens aparecem um a um (on click)
**Imagem**: Ícones de check verde
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Cada item desta lista é uma lição que alguém aprendeu da forma difícil em produção. "Comece simples" é o #1 — a Anthropic repete isso em todo documento. "Documente tools" é ACI. "max_steps" é o guardrail mais básico. "Log estruturado" é observabilidade. "Sandbox" é segurança. "HITL" é governança. "Prompt efetivo" é o que o modelo realmente recebe (não o que você escreveu — frameworks adicionam system prompts). "Entenda o framework" é a recomendação explícita da Anthropic. "Meça custo" é FinOps. "Teste em sandbox" é bom senso.
💡 ANALOGIA: É como o checklist de pré-voo do piloto. Cada item parece óbvio, mas pilotos ainda esquecem. Checklist existe porque a memória humana falha. Em agentes, o mesmo: cada item parece óbvio, mas em 6 meses você vai esquecer de um.
➡️ TRANSIÇÃO: "Agora o que NÃO fazer."

---

### Slide 44 — Anti-Patterns (DON'T)

**Título**: Anti-Patterns
**Objetivo**: Checklist do que NÃO fazer.
**Conteúdo**:
- ❌ **Começar com agente** quando workflow basta
- ❌ **Adicionar complexidade** sem evidência de necessidade
- ❌ **Confiar no framework cegamente** ("caixa preta")
- ❌ **Não definir max_steps** (loop infinito)
- ❌ **Não logar** (debug cego)
- ❌ **Tool mal documentada** (ACI fraca)
- ❌ **Prompt gigante** sem estrutura
- ❌ **Não testar em sandbox** (execução sem isolamento)
- ❌ **Não medir custo** ("descobri no fim do mês")
- ❌ **Esquecer error handling** (tool quebra → agente morre)
- ❌ **Não ter fallback** (se API cai, agente trava)

**Diagrama**: Checklist vermelho (`etho-danger` #C0392B)
**Animação**: Itens aparecem um a um (on click)
**Imagem**: Ícones de X vermelho
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Cada anti-pattern aqui é um bug que eu já vi em produção. "Começar com agente" é o mais comum — a equipe quer usar a tecnologia da moda e pula direto para agente quando um workflow resolveria. "Não definir max_steps" causa loops infinitos que custam milhares de dólares. "Tool mal documentada" causa chamadas erradas. "Não logar" torna debugging impossível. "Não testar em sandbox" causa danos reais (agente que deleta arquivo de produção). Cada um destes é evitável com as boas práticas do slide anterior.
💡 ANALOGIA: É como os erros de um cozinheiro iniciante. Colocar sal demais (complexidade desnecessária), não provar antes de servir (não testar), não ter cronômetro (sem max_steps), não ler a receita (não entender o framework). Cada erro é evitável.
❓ PERGUNTA PARA A TURMA: "Qual destes anti-patterns vocês já cometeram?" (Honestidade aqui é valiosa — todos cometem)
⚠️ ERROS COMUNS: Alunos acham que anti-patterns são "erros de iniciante". Mesmo times sênior cometem esses erros sob pressão de prazo.
➡️ TRANSIÇÃO: "Vamos ver todos esses conceitos em um caso real."

---

### Slide 45 — Caso de Estudo: Anthropic Coding Agent no SWE-bench

**Título**: Caso Real: Anthropic Coding Agent no SWE-bench
**Objetivo**: Mostrar todos os conceitos da aula em um caso real de produção.
**Conteúdo**:
- **O que é SWE-bench**: benchmark que mede capacidade de resolver issues reais de GitHub
  - Issues de Django, scikit-learn, sympy, etc.
  - Subconjunto "Verified" curado
- **O coding agent da Anthropic**:
  - Input: texto da issue (PR description)
  - Output: patch (diff) que passa nos testes
  - Arquitetura: **Augmented LLM + loop + ACI + sandbox**
  - Não há "magia" — é exatamente o que vimos hoje
- **Resultados**:
  - Claude 3.5 Sonnet: ~49% no SWE-bench Verified (out/2024)
  - Modelos mais recentes: substancialmente superior
- **Por que é um agente (não workflow)?**
  - Cada issue é diferente — não dá para predefinir passos
  - O modelo decide: ver arquivo, editar, rodar testes, etc.

**Diagrama**: Arquitetura do coding agent (issue → Augmented LLM → loop → patch)
**Animação**: Fluxo aparece step-by-step
**Imagem**: Diagrama de arquitetura (baseado em `09-CaseStudies/01-anthropic-swe-bench-coding-agent.md`)
**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Este é o caso que prova que os conceitos de hoje são reais. A Anthropic construiu um agente que resolve issues reais de GitHub — e a arquitetura é simples: Augmented LLM (Claude + tools + memória de repo) em um loop limitado (max_steps), com ACI trabalhada (tools bem desenhadas) e sandbox (container isolado). Não há framework mágico, não há arquitetura de 17 camadas. É o bloco fundamental que vimos hoje. Os 49% de acerto significam que em metade das issues, o agente produz um patch que passa nos testes — sem intervenção humana. Isso é impressionante e ao mesmo tempo mostra que ainda há muito a melhorar.
💡 ANALOGIA: É como ver um chef cozinhar. A receita é simples — os ingredientes são os mesmos que você tem. A diferença está na execução: na qualidade dos ingredientes (modelo), na técnica (ACI), e na prática (iteração). Não há ingrediente secreto.
❓ PERGUNTA PARA A TURMA: "Se a arquitetura é simples, por que nem todo mundo consegue 49%?" (Resposta: a qualidade das tools, do prompt, do sandbox, e do modelo faz a diferença. Simples ≠ fácil.)
➡️ TRANSIÇÃO: "Há uma lição específica do SWE-bench que quero destacar."

---

### Slide 46 — A Lição ACI do SWE-bench

**Título**: A Lição ACI do SWE-bench
**Objetivo**: Fixar o princípio de ACI com o caso real do coding agent.
**Conteúdo**:
- **Problema**: agente saía do diretório raiz e usava paths relativos errados
- **Solução ingênua**: "melhorar o prompt para dizer 'use paths absolutos'"
  - Frágil: modelo pode esquecer
  - Não escalável: um novo prompt para cada edge case
- **Solução robusta**: mudar a TOOL para exigir paths absolutos
  - Poka-yoke: erro impossível pela design
  - Escalável: funciona independentemente do prompt
- **Resultado**: erro desapareceu, sem mexer no prompt principal
- **Citação**: "We spent more time optimizing our tools than the overall prompt" — Anthropic
- **Princípio**: tempo em ACI > tempo no prompt principal

**Diagrama**: Antes (path relativo → erro) → Depois (path absoluto → sucesso)
**Animação**: Transformação antes → depois (morph)
**Imagem**: Ícone de chave de fenda ajustando uma tool
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esta é a lição mais importante do caso de estudo. A Anthropic enfrentou um bug real: o agente usava paths relativos errados após sair do diretório raiz. A solução óbvia seria "dizer no prompt para usar paths absolutos". Mas isso é frágil — o modelo pode esquecer, especialmente em conversas longas. A solução robusta foi mudar a TOOL: em vez de aceitar paths relativos, a tool passou a exigir paths absolutos. Aí o modelo NÃO PODE errar, mesmo que queira. Isso é poka-yoke — tornar o erro impossível pelo design. E a Anthropic foi explícita: gastaram MAIS tempo nas tools do que no prompt principal. Essa é a inversão que a maioria dos desenvolvedores precisa fazer.
💡 ANALOGIA: É como colocar uma proteção numa tomada para que uma criança não enfie o dedo. Você pode "ensinar a criança a não colocar o dedo" (prompt). Ou pode colocar a proteção (poka-yoke na tool). A proteção funciona mesmo se a criança esquecer a lição.
❓ PERGUNTA PARA A TURMA: "Vocês têm algum bug hoje que poderia ser resolvido redesenhando a tool em vez de melhorar o prompt?" (Deixar 1-2 responderem)
➡️ TRANSIÇÃO: "Último exercício antes do resumo."

---

### Slide 47 — Exercício: Identificando um Loop Quebrado

**Título**: Exercício: Debug de Trace Quebrado
**Objetivo**: Praticar debugging de agentes analisando um trace.
**Conteúdo**:
- **Trace quebrado** (mostrado no slide):
```
[STEP 0] Thought: "Vou buscar o preço do produto X"
         Action: search_price("Produto X")
         Observation: "Produto X: R$ 99,90"

[STEP 1] Thought: "Vou buscar o preço do produto X"
         Action: search_price("Produto X")
         Observation: "Produto X: R$ 99,90"

[STEP 2] Thought: "Vou buscar o preço do produto X"
         Action: search_price("Produto X")
         Observation: "Produto X: R$ 99,90"

[STEP 3] Thought: "Vou buscar o preço do produto X"
         Action: search_price("Produto X")
         Observation: "Produto X: R$ 99,90"

[STEP 4] Thought: "Vou buscar o preço do produto X"
         Action: search_price("Produto X")
         Observation: "Produto X: R$ 99,90"

[STEP 5] max_steps reached. Abortando.
```
- **Tarefa**:
  1. Em duplas, identificar onde o loop acontece
  2. Propor 2 correções diferentes
  - 2 min discussão, 1 min compartilhar
- **Resposta esperada**:
  - Problema: o agente não "percebe" que já tem a informação (falta de contexto ou prompt fraco)
  - Correção 1: adicionar a observation anterior no prompt ("Você já sabe que o preço é R$ 99,90")
  - Correção 2: adicionar lógica de detecção de repetição (se action == action_anterior, forçar resposta)

**Diagrama**: Trace de console com problema destacado em vermelho
**Animação**: Highlight dos steps repetidos (piscando em vermelho)
**Imagem**: Terminal com trace
**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Este é um bug real que acontece quando o agente não processa a Observation corretamente. O modelo recebe "Produto X: R$ 99,90" mas no próximo step, pensa "vou buscar o preço" de novo. Isso pode acontecer por: (1) prompt fraco que não instrui o modelo a usar informações já obtidas; (2) contexto não inclui as observations anteriores; (3) modelo fraco que não conecta a observation com o objetivo. As correções são: melhorar o prompt ("Use as informações já obtidas antes de buscar novamente"), garantir que as messages incluem as observations, e/ou adicionar detecção de loop no código (se a mesma action for chamada 3x seguidas, forçar resposta). Este exercício mostra a importância de traces — sem o trace, você só veria "o agente demorou muito e retornou erro".
💡 ANALOGIA: É como uma pessoa com amnésia de curto prazo que pergunta a mesma coisa repetidamente. Você precisa garantir que a informação "grude" — seja no prompt, no contexto, ou no código.
⚠️ ERROS COMUNS: Alunos propõem "aumentar max_steps" como correção. Isso não resolve — só faz o agente gastar mais tokens antes de falhar. A correção é tratar a CAUSA do loop, não o sintoma.
➡️ TRANSIÇÃO: "Vamos consolidar tudo."

---

### Slide 48 — Resumo da Aula

**Título**: Resumo da Aula
**Objetivo**: Sintetizar os 6 pontos-chave da aula.
**Conteúdo**:
1. **Augmented LLM** = bloco fundamental (LLM + retrieval + tools + memory)
   - O modelo decide quando usar cada capacidade
2. **ReAct** = padrão fundacional (Thought → Action → Observation em loop)
   - Grounding via observação do ambiente
3. **Workflow vs Agente** = decisão arquitetural
   - Previsibilidade (workflow) vs flexibilidade (agente)
4. **Comece simples** — só aumente complexidade com evidência
   - Nível 0 (single call) → Nível 4 (multi-agente)
5. **ACI é onde mora a confiabilidade**
   - Tempo em tools > tempo no prompt principal
6. **Observabilidade desde o dia 1**
   - Traces, custo, latência — não são opcionais

**Diagrama**: 6 ícones com os pontos-chave em grid 2x3
**Animação**: Ícones aparecem um a um
**Imagem**: 6 ícones minimalistas
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Se vocês só lembrarem de 6 coisas desta aula, devem ser estas. O Augmented LLM é o bloco. ReAct é o padrão. Workflow vs agente é a decisão. Comece simples é o princípio. ACI é a confiabilidade. Observabilidade é a operação. Tudo o que vimos hoje — as 6 seções, os 62 slides, a demo, os exercícios — converge para estes 6 pontos. Na próxima aula (ETHAGT02) vamos aprofundar ACI: como desenhar tools que são difíceis de errar.
➡️ TRANSIÇÃO: "Confirmem que tudo foi coberto."

---

### Slide 49 — Checklist da Aula

**Título**: Checklist da Aula
**Objetivo**: Confirmar que todos os tópicos foram cobertos.
**Conteúdo**:
- [ ] Definiu agente vs workflow (distinção canônica de Anthropic)
- [ ] Explicou Augmented LLM (4 componentes)
- [ ] Apresentou taxonomia unificada (6 componentes)
- [ ] Implementou ReAct do zero (demo ao vivo)
- [ ] Comparou 3 frameworks (Python puro, LangGraph, OpenAI SDK)
- [ ] Discutiu quando reduzir abstração
- [ ] Adicionou logging estruturado
- [ ] Introduziu traces e custo/latência
- [ ] Discutiu boas práticas (10 DOs) e anti-patterns (10 DON'Ts)
- [ ] Analisou caso real (SWE-bench coding agent)
- [ ] Fez exercício de debug de trace quebrado
- [ ] Conectou com próximos módulos

**Diagrama**: Checklist visual (caixas com checkmarks)
**Animação**: Checkmarks aparecem um a um
**Imagem**: Lista com checkboxes
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Este checklist serve para duas coisas: (1) confirmar que eu cobri tudo que prometi nos objetivos; (2) servir de auto-avaliação para vocês. Se algum item não está claro, é hora de perguntar no Q&A.
➡️ TRANSIÇÃO: "Agora o quiz rápido."

---

### Slide 50 — Quiz: Pergunta 1

**Título**: Quiz 1/5
**Objetivo**: Verificar compreensão do bloco fundamental.
**Conteúdo**:
- **Pergunta**: Qual é o bloco fundamental de qualquer sistema agêntico segundo Anthropic?
  - A) Um framework como LangGraph
  - B) O Augmented LLM (LLM + retrieval + tools + memory)
  - C) Um prompt bem escrito
  - D) Um modelo grande o suficiente
- **Resposta**: **B**
- **Justificativa**: A Anthropic é explícita — o bloco fundamental é o LLM enhanced with retrieval, tools, and memory. Frameworks são instanciações, não o bloco. Prompt é importante mas não é o bloco. Modelo é necessário mas sem as augmentations não é agêntico.

**Diagrama**: 4 opções com radio buttons
**Animação**: Opções aparecem; resposta revelada após click
**Imagem**: Ícone de pergunta
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A resposta é B. Se alguém marcou A, ainda confunde framework com arquitetura. Se marcou C, superestima o prompt. Se marcou D, acha que "modelo maior" resolve tudo — não resolve sem as augmentations.
➡️ TRANSIÇÃO: "Próxima pergunta."

---

### Slide 51 — Quiz: Pergunta 2

**Título**: Quiz 2/5
**Objetivo**: Verificar compreensão do ReAct.
**Conteúdo**:
- **Pergunta**: Em ReAct, o que força o "grounding" do modelo?
  - A) O prompt do sistema
  - B) A temperatura baixa
  - C) A Observation (resultado real da tool)
  - D) O max_steps
- **Resposta**: **C**
- **Justificativa**: Grounding significa ancorar o raciocínio em fato real. A Observation é o resultado real da tool executada — não é alucinável. O prompt pode ser ignorado, a temperatura não garante correção, max_steps só limita iterações.

**Diagrama**: 4 opções com radio buttons
**Animação**: Opções aparecem; resposta revelada após click
**Imagem**: Ícone de pergunta
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A resposta é C. Grounding = ancorar em fato real. A Observation é o único componente não-alucinável do ReAct. Por isso que sem tools, o agente não tem grounding — só tem o próprio raciocínio, que pode alucinar.
➡️ TRANSIÇÃO: "Próxima."

---

### Slide 52 — Quiz: Pergunta 3

**Título**: Quiz 3/5
**Objetivo**: Verificar compreensão da decisão workflow vs agente.
**Conteúdo**:
- **Pergunta**: Quando você DEVERIA usar um agente em vez de um workflow?
  - A) Quando a tarefa tem passos predefinidos
  - B) Quando você precisa de previsibilidade total
  - C) Quando os passos são imprevisíveis e exigem flexibilidade
  - D) Quando o custo precisa ser mínimo
- **Resposta**: **C**
- **Justificativa**: Agentes são para problemas abertos onde não dá para predefinir o caminho. Se os passos são predefinidos (A), workflow. Se precisa de previsibilidade (B), workflow. Se custo é prioridade (D), workflow (mais barato). Agente é para flexibilidade (C).

**Diagrama**: 4 opções com radio buttons
**Animação**: Opções aparecem; resposta revelada após click
**Imagem**: Ícone de pergunta
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A resposta é C. Agentes trocam previsibilidade e custo por flexibilidade. Se você não precisa de flexibilidade, workflow é sempre melhor.
➡️ TRANSIÇÃO: "Próxima."

---

### Slide 53 — Quiz: Pergunta 4

**Título**: Quiz 4/5
**Objetivo**: Verificar compreensão de ACI.
**Conteúdo**:
- **Pergunta**: O que é ACI?
  - A) Agent Communication Interface
  - B) Agent-Computer Interface (design de tools)
  - C) Automated Code Injection
  - D) Agent Control Infrastructure
- **Resposta**: **B**
- **Justificativa**: ACI = Agent-Computer Interface, análogo a HCI (Human-Computer Interface). É o design das tools — descrição, parâmetros, validação. A Anthropic dedica tanto esforço a ACI quanto a HCI.

**Diagrama**: 4 opções com radio buttons
**Animação**: Opções aparecem; resposta revelada após click
**Imagem**: Ícone de pergunta
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A resposta é B. ACI é Agent-Computer Interface. É o design das tools. A lição do SWE-bench: invista tanto em ACI quanto em HCI. Poka-yoke suas tools.
➡️ TRANSIÇÃO: "Última pergunta."

---

### Slide 54 — Quiz: Pergunta 5

**Título**: Quiz 5/5
**Objetivo**: Verificar compreensão de prioridades de produção.
**Conteúdo**:
- **Pergunta**: Qual é a PRIMEIRA coisa que você deve adicionar a um agente em produção?
  - A) Um framework
  - B) Múltiplas tools
  - C) Observabilidade (logs estruturados + traces)
  - D) HITL (Human-in-the-Loop)
- **Resposta**: **C**
- **Justificativa**: Sem observabilidade, você não pode debugar, medir custo, ou reproduzir bugs. Framework (A) é opcional. Múltiplas tools (B) vêm depois da observabilidade. HITL (D) é importante mas você precisa ver o que o agente faz antes de decidir onde intervir.

**Diagrama**: 4 opções com radio buttons
**Animação**: Opções aparecem; resposta revelada após click
**Imagem**: Ícone de pergunta
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A resposta é C. Observabilidade é a #1 prioridade em produção. Sem ela, tudo o resto é opaco. Você não pode otimizar o que não pode medir. Não pode debugar o que não pode ver. Não pode auditar o que não pode rastrear.
➡️ TRANSIÇÃO: "Agora perguntas para discussão profunda."

---

### Slide 55 — Perguntas para Discussão

**Título**: Perguntas para Discussão
**Objetivo**: Estimular debate profundo sobre os conceitos da aula.
**Conteúdo**:
1. "Toda aplicação de LLM deveria ser um agente?" (V/F justificado)
   - *Dica: o que a Anthropic recomenda?*
2. "Em que cenário Python puro é melhor que LangGraph? E o inverso?"
   - *Dica: pense em controle vs produtividade, POC vs produção.*
3. "Como você convenceria um PM de que workflow basta e agente é overkill?"
   - *Dica: use custo, latência e previsibilidade como argumentos.*
4. "Qual o maior risco de começar com framework sem entender o básico?"
   - *Dica: caixa preta, debugging, custo inesperado.*

**Diagrama**: 4 perguntas em destaque
**Animação**: Perguntas aparecem uma a uma
**Imagem**: Balões de discussão
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Respostas esperadas: (1) Falso — a Anthropic é explícita: "consider not building agentic systems at all". A maioria dos casos é resolvida com single LLM call + retrieval. (2) Python puro é melhor em produção com auditoria, customização extrema, ou debugging granular. LangGraph é melhor em POC→produção rápida, quando precisa de checkpointer e multi-agente. (3) Custo: agente custa 5-10x mais que workflow. Latência: agente leva 10-30s vs 2-5s do workflow. Previsibilidade: workflow é testável, agente não. (4) Caixa preta — quando o framework falha, você não sabe por quê. Pode ser o prompt oculto, a serialização, o retry logic. Sem entender o básico, você não consegue isolar o problema.
➡️ TRANSIÇÃO: "Vamos ver como hoje conecta com o resto da especialização."

---

### Slide 56 — Conexão com Próximos Módulos

**Título**: Conexão com a Especialização
**Objetivo**: Mostrar como ETHAGT01 conecta com o resto do programa.
**Conteúdo**:
- **ETHAGT02** — Tool Calling e ACI: aprofunda o design de tools
- **ETHAGT03** — Padrões de Workflow: os 5 padrões em detalhe
- **ETHAGT04** — Reasoning & Planning: evolução do ReAct (Reflexion, ToT, LATS)
- **ETHAGT05** — Memória de Agentes: working vs persistente em profundidade
- **ETHAGT06** — RAG Agêntico: retrieval in-loop aprofundado
- **ETHAGT08** — MCP: Model Context Protocol
- **ETHAGT09-10** — Multi-Agentes: Collaboration (taxonomia componente #6)
- **ETHAGT12** — AgentOps: observabilidade, traces, avaliação
- **ETHAGT13** — Segurança: prompt injection, red team
- **ETHAGT16** — Sociedades de Agentes: pesquisa autônoma

**Diagrama**: Mapa da especialização com ETHAGT01 no centro e conexões radiais
**Animação**: Conexões aparecem uma a uma do centro para fora
**Imagem**: Mind map radial
**Tempo**: 1 min

**Rodapé**: `LATS` = Language Agent Tree Search — Busca em Árvore com LLM (combina MCTS com LLM para explorar árvores de ações)

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: ETHAGT01 é a fundação. Todo módulo seguinte expande um aspecto do que vimos hoje. ACI em ETHAGT02. Workflows em ETHAGT03. Planejamento (o componente da taxonomia) em ETHAGT04. Memória em ETHAGT05. RAG em ETHAGT06. MCP em ETHAGT08. Multi-agente em ETHAGT09-10. Observabilidade em ETHAGT12. Segurança em ETHAGT13. A especialização é um zoom progressivo em cada componente do Augmented LLM.
➡️ TRANSIÇÃO: "O que ler antes da próxima aula."

---

### Slide 57 — Leitura Recomendada

**Título**: Leitura Recomendada
**Objetivo**: Indicar o que ler antes da próxima aula.
**Conteúdo**:
- **Obrigatório** (antes de ETHAGT02):
  - Anthropic. *Building Effective Agents*. 2024.
    - URL: anthropic.com/engineering/building-effective-agents
    - Foco: Apêndice 2 "Prompt Engineering your Tools"
  - Yao, S. et al. *ReAct*. ICLR 2023.
    - arXiv:2210.03629
    - Foco: Seção 3 (method) e Seção 4 (experiments)
- **Recomendado**:
  - arXiv:2601.12560 — survey de arquiteturas
  - Schluntz & Albert. *Building more effective AI agents* (YouTube)
- **Opcional**:
  - Karpathy, A. *Software 3.0* (talks)
  - HuggingFace Agents Course

**Diagrama**: Lista com ícones de livro
**Animação**: Itens aparecem um a um
**Imagem**: Ícones de livro/video
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A leitura obrigatória é o artigo da Anthropic e o paper do ReAct. São curtos (15-20 min cada) e fundamentais. O Apêndice 2 da Anthropic é especialmente importante porque prepara para ETHAGT02 (ACI). O paper do ReAct vai dar a base teórica que a demo mostrou na prática.
➡️ TRANSIÇÃO: "Referências completas."

---

### Slide 58 — Referências Completas

**Título**: Referências
**Objetivo**: Listar todas as fontes usadas na aula.
**Conteúdo**:
1. Anthropic. *Building Effective Agents*. dez/2024.
   URL: https://www.anthropic.com/engineering/building-effective-agents
2. Yao, S. et al. *ReAct: Synergizing Reasoning and Acting in Language Models*. ICLR 2023.
   arXiv:2210.03629
3. Arunkumar V, Gangadharan G.R., Buyya R. *Agentic AI: Architectures, Taxonomies, and Evaluation of LLM Agents*. arXiv:2601.12560, jan/2026.
4. Schick, T. et al. *Toolformer: Language Models Can Teach Themselves to Use Tools*. NeurIPS 2023. arXiv:2302.04761
5. Jimenez, C. et al. *SWE-bench: Can Language Models Resolve Real-World GitHub Issues?* arXiv:2310.06770
6. Shinn, N. et al. *Reflexion: Language Agents with Verbal Reinforcement Learning*. NeurIPS 2023. arXiv:2303.11366
7. Wang, L. et al. *A Survey on Large Language Model based Autonomous Agents*. arXiv:2308.11432
8. OpenAI. *Practical Guide to Building Agents*. 2024.
9. LangGraph docs. URL: https://github.com/langchain-ai/langgraph
10. Anthropic. *Effective Context Engineering for AI Agents*. 2025.

**Diagrama**: Lista numerada com links
**Animação**: Lista aparece com fade
**Imagem**: Ícones de documento/external link
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Todas as fontes estão no repositório: `20-Research/ETHAGT01-pesquisa.md` tem o fichamento completo. As 3 canônicas (1, 2, 3) são leitura obrigatória. As demais são complementares.
➡️ TRANSIÇÃO: "O projeto do módulo."

---

### Slide 59 — Projeto do Módulo

**Título**: Projeto: Research Assistant em 3 Versões
**Objetivo**: Apresentar o projeto que os alunos devem entregar.
**Conteúdo**:
- **Descrição**: implementar um agente "research assistant" que, dada uma pergunta factual:
  - Decide entre: (a) responder direto, (b) recuperar de base local, ou (c) usar tool de busca
  - Compara 3 versões: Python puro, LangGraph, e um terceiro framework à escolha
- **Entrega**: repositório Git + README comparativo + traces de execução
- **Critério de sucesso**:
  - Agente funcional nas 3 versões
  - Comparação justifica escolha com ≥3 critérios (controle, transparência, esforço)
  - Traces demonstram o loop ReAct em ação
- **Prazo**: 2 semanas
- **Avaliação**: rubrica de 4 pilares (Técnico 40%, Consultivo 30%, Comportamental 20%, Prático 10%)

**Diagrama**: 3 caixas representando as 3 versões + tabela comparativa
**Animação**: Versões aparecem uma a uma
**Imagem**: Ícones das 3 abordagens
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O projeto é a aplicação prática de tudo que vimos hoje. A chave não é "funcionar" — é a COMPARAÇÃO. Vocês precisam justificar com dados qual abordagem escolheriam em produção e por quê. Os critérios mínimo são 3: controle (quanto você controla o prompt/loop/estado), transparência (quanto você vê do que acontece), e esforço (quanto tempo levou para implementar). Pode adicionar outros: custo, latência, escalabilidade. O README comparativo é tão importante quanto o código.
➡️ TRANSIÇÃO: "Os labs."

---

### Slide 60 — Labs do Módulo

**Título**: Laboratórios
**Objetivo**: Apresentar os laboratórios práticos.
**Conteúdo**:
- **Lab 1** (4h): "ReAct em 50 linhas"
  - Implementar o agent loop em Python puro
  - Tool de cálculo (calculator)
  - Entrega: repo + trace de exemplo
  - Pré-requisito: Python 3.11+, OpenAI/Anthropic API key
- **Lab 2** (4h): "Augmented LLM"
  - Adicionar retrieval (vector store simples — ChromaDB/Qdrant)
  - Adicionar 2 tools ao agente do Lab 1
  - O agente deve decidir quando recuperar vs usar tool
  - Entrega: agente funcional + traces

**Diagrama**: 2 cards com info dos labs
**Animação**: Cards aparecem lado a lado
**Imagem**: Ícones de laboratório
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Lab 1 é obrigatório antes do projeto. Vocês podem usar o exemplo do repositório (`19-Examples/ETHAGT01/exemplo-01-react-loop/main.py`) como ponto de partida, mas precisam estendê-lo. Lab 2 adiciona retrieval e mais tools — é onde o Augmented LLM fica completo. Ambos são individuais.
➡️ TRANSIÇÃO: "Próximos passos."

---

### Slide 61 — Próximos Passos

**Título**: Próximos Passos
**Objetivo**: O que fazer antes da próxima aula.
**Conteúdo**:
1. **Ler**: Anthropic *Building Effective Agents* (15 min)
   - Foco no Apêndice 2 (ACI)
2. **Ler**: ReAct paper — arXiv:2210.03629 (20 min)
   - Foco na Seção 3 (method)
3. **Rodar**: exemplo ReAct do repositório
   - `19-Examples/ETHAGT01/exemplo-01-react-loop/main.py`
4. **Iniciar**: Lab 1 — "ReAct em 50 linhas"
5. **Próxima aula**: ETHAGT02 — Tool Calling e ACI
   - Vamos aprofundar o design de tools
   - Poka-yoke, schemas, error handling
   - Caso: Anthropic SWE-bench tool redesign

**Diagrama**: Checklist numerado com prazos
**Animação**: Itens aparecem um a um
**Imagem**: Ícone de checklist
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O mais importante é ler o Apêndice 2 da Anthropic — é a base da próxima aula. Se não lerem, ETHAGT02 vai ser difícil de acompanhar. O Lab 1 pode ser feito em paralelo com a leitura.
➡️ TRANSIÇÃO: "Último slide."

---

### Slide 62 — Q&A / Encerramento

**Título**: Perguntas?
**Objetivo**: Abrir para perguntas e encerrar a aula.
**Conteúdo**:
- "Perguntas?"
- Contato do professor (email / Slack)
- "Na próxima aula: ETHAGT02 — Tool Calling e ACI"
- "Obrigado!"
- Universidade Etho · Especialização em Programação Agêntica

**Diagrama**: Logo Etho + fundo `etho-dark` (#0F1E2D)
**Animação**: Fade in
**Imagem**: Logo Etho centralizado
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Abrir para Q&A. Se não houver perguntas, fazer uma pergunta inversa: "Qual parte da aula vocês acharam menos clara?" Isso geralmente gera discussão. Encerrar com a mensagem: "O bloco fundamental é o Augmented LLM. Tudo o que vem depois é composição. Se vocês entenderam isso hoje, a especialização vai fluir."
➡️ TRANSIÇÃO: Fim da aula.

---

## Fim dos Slides Detalhados — ETHAGT01

> 62 slides · 90 min · 6 seções · 15 diagramas · 5 questões de quiz · 2 exercícios · 1 demo
