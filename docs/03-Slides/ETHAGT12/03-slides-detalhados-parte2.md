# ETHAGT12 — Slides Detalhados + Notas do Professor (Parte 2: Slides 44-78)

> Universidade Etho · Especialização em Programação Agêntica
> Cada slide contém: título, objetivo, conteúdo, notas do professor, diagrama, animação, imagem, tempo.

---

## SEÇÃO E — Benchmarks Canônicos (Slides 44-54 · 14 min)

---

### Slide 44 — [SEÇÃO] Benchmarks Canônicos

**Título**: 4 — Benchmarks Canônicos
**Objetivo**: Transição para o bloco de benchmarks.
**Conteúdo**: "4 — Benchmarks Canônicos: SWE-bench, GAIA, τ-bench"
**Diagrama**: Fundo `etho-primary`
**Animação**: Número cresce com zoom
**Tempo**: 0.5 min

**Notas do Professor**:
➡️ TRANSIÇÃO: "Depois de avaliação custom, vamos para avaliação comparável: benchmarks."

---

### Slide 45 — Por que Benchmarks?

**Título**: Por que Benchmarks?
**Objetivo**: Justificar o uso de benchmarks padronizados.
**Conteúdo**:
- **Benchmark** = conjunto padronizado de tarefas com critério objetivo
- Permite comparar modelos e arquiteturas de forma justa
- **Reprodutível**: mesma tarefa, mesmo critério, resultado comparável
- **Referência da comunidade**: "meu agente faz X% no SWE-bench"
- **Limitação**: benchmark ≠ produção (veremos)
- **Pergunta**: *Você confia em um score de benchmark sem ter rodado?*

**Diagrama**: Balança: benchmark (padronizado) vs eval custom (representativo)
**Animação**: Balança equilibra
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Benchmark é padronizado. Mesma tarefa, mesmo critério, todo mundo roda igual. Permite comparar: "meu agente faz 49% no SWE-bench, o seu faz 30%". Reprodutível — outro time roda e chega no mesmo número. Mas — e isso é crucial — benchmark é ambiente controlado. Não representa seu caso de uso real. Por isso você combina: benchmark (comparável) + eval custom (representativo). Não substitui um pelo outro.
💡 ANALOGIA: É como a prova do ENEM. Padronizada, comparável, mas não diz tudo sobre o aluno. Combine com portfólio (eval custom).
❓ PERGUNTA PARA A TURMA: "Vocês confiam em score de benchmark sem ter rodado?" (resposta certa: não)
⚠️ ERROS COMUNS: Alunos vendem agente só com score de benchmark. Sem eval custom, o score é marketing, não métrica.
➡️ TRANSIÇÃO: "Vamos ao landscape dos benchmarks canônicos."

---

### Slide 46 — Landscape de Benchmarks

**Título**: Landscape de Benchmarks
**Objetivo**: Visão geral dos benchmarks canônicos.
**Conteúdo**:
- **SWE-bench** — código (resolver issues de GitHub)
- **GAIA** — raciocínio geral multi-step
- **τ-bench** — tool use em domínios (airline, retail)
- **WebArena** — navegação web autônoma
- **AgentDojo** — segurança (injeção em agentes)
- **τ²-bench** — multi-agent tool use

**Diagrama**: `12-Diagrams/ETHAGT12/benchmark-landscape.mmd`
**Animação**: Cada benchmark aparece com click
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vamos passar por 6 benchmarks canônicos. Cada um testa uma capacidade diferente. SWE-bench testa código. GAIA testa raciocínio geral. τ-bench testa tool use com policy. WebArena testa navegação web. AgentDojo testa segurança contra injeção. τ²-bench testa multi-agent tool use. A escolha depende do seu domínio: agente de código → SWE-bench; assistente geral → GAIA; atendente com APIs → τ-bench.
⚠️ ERROS COMUNS: Alunos escolhem benchmark pelo hype. Escolha pelo fit com seu caso de uso.
➡️ TRANSIÇÃO: "Vamos aprofundar no mais influente: SWE-bench."

---

### Slide 47 — SWE-bench / SWE-bench Verified

**Título**: SWE-bench / SWE-bench Verified
**Objetivo**: Apresentar o benchmark de código mais influente.
**Conteúdo**:
- **SWE-bench**: 2.294 issues reais de 12 repositórios Python open source
- **Tarefa**: resolver issue → gerar patch → testes passam
- **SWE-bench Verified**: subconjunto de 500 com validação humana
- **Claude 3.5 Sonnet**: ~49% no Verified (dez/2024)
- **Por que importa**: código é verificável (testes = ground truth)
- **Fonte**: Jimenez et al., arXiv:2310.06770

**Diagrama**: Fluxo — issue → agente → patch → testes → pass/fail
**Animação**: Fluxo aparece da esquerda para direita
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: SWE-bench é o benchmark de código mais influente. Pego issues reais de GitHub (Python), dou para o agente, ele tem que gerar patch. Critério: testes automáticos passam. Isso é poderoso — código tem ground truth objetivo (testes). SWE-bench Verified é subconjunto de 500 com validação humana (garante que a issue é clara e o teste é justo). Claude 3.5 Sonnet faz ~49% no Verified — quase metade das issues resolvidas. Por que importa: prova que agentes podem fazer trabalho de engenharia real.
💡 ANALOGIA: É como a prova prática de programação. Você recebe bug, tem que consertar, testes validam.
⚠️ ERROS COMUNS: Alunos acham que 49% é baixo. Para tarefas de engenharia real, é altíssimo.
➡️ TRANSIÇÃO: "Vamos para raciocínio geral: GAIA."

---

### Slide 48 — GAIA

**Título**: GAIA
**Objetivo**: Apresentar o benchmark de raciocínio geral.
**Conteúdo**:
- **GAIA**: 466 questões de raciocínio multi-step com tools
- **Níveis**: Level 1 (simples) → Level 3 (complexo, dezenas de steps)
- Requer: web search, file processing, reasoning, tool use
- **Human**: ~92% no Level 1; **GPT-4 + plugins**: ~15%
- **Por que importa**: testa capacidade geral de agente assistente
- **Fonte**: Mialon et al., arXiv:2311.12983

**Diagrama**: Exemplo de questão GAIA com steps esperados
**Animação**: Steps aparecem em sequência
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: GAIA testa raciocínio geral. 466 questões que exigem múltiplos steps: web search, processamento de arquivo, raciocínio. Tem 3 níveis. Level 1 humanos acertam 92%. GPT-4 com plugins: 15%. Esse gap (humano 92%, melhor modelo 15%) mostra o quanto agentes ainda são fracos em raciocínio multi-step. GAIA é o teste do "assistente geral" — diferente do SWE-bench que é específico de código.
💡 ANALOGIA: É como uma caça ao tesouro. Cada passo te leva ao próximo. Exige pesquisa, raciocínio, ferramentas. Humanos são bons nisso. Agentes, ainda não tanto.
⚠️ ERROS COMUNS: Alunos acham que Level 1 é fácil. Não é — mesmo Level 1 exige múltiplos steps e tools.
➡️ TRANSIÇÃO: "Vamos para tool use realista: τ-bench."

---

### Slide 49 — τ-bench

**Título**: τ-bench
**Objetivo**: Apresentar o benchmark de tool use em domínios.
**Conteúdo**:
- **τ-bench**: tool-agent-user interaction em domínios (airline, retail)
- Agente simula atendente com acesso a APIs (policy, booking, etc.)
- Avalia: success rate em tarefas com usuários simulados
- **Domínios**: airline (policy-driven), retail (catalog-driven)
- **Por que importa**: testa tool use realista com políticas
- **Fonte**: Yao et al., arXiv:2404.44529

**Diagrama**: Arquitetura τ-bench — user simulator ↔ agent ↔ tools
**Animação**: Componentes aparecem
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: τ-bench (tau-bench) é elegante. Simula um atendente (agente) que conversa com usuário simulado e tem acesso a APIs. Domínios: airline (aérea, com políticas complexas de reembolso) e retail (varejo, com catálogo). O agente tem que seguir políticas, usar tools corretas, satisfazer usuário. Sucesso é mensurado pela tarefa completada. Por que importa: testa tool use realista com policy — exatamente o que assistentes virtuais fazem.
💡 ANALOGIA: É como uma simulação de atendimento. Você tem o atendente (agente), o cliente (simulador), e os sistemas (tools). Avalia se o atendimento foi bem.
➡️ TRANSIÇÃO: "Vamos ver dois benchmarks mais amplos: AgentBench e WebArena."

---

### Slide 50 — AgentBench e WebArena

**Título**: AgentBench e WebArena
**Objetivo**: Apresentar benchmarks de panorama amplo e navegação web.
**Conteúdo**:
- **AgentBench**: 8 ambientes (OS, DB, KG, web, card game, etc.)
- Avalia capacidades diversas: reasoning, planning, tool use
- **WebArena**: navegação web autônoma em sites simulados
- Tarefas: "encontre o produto mais barato", "agende reunião"
- **VisualWebArena**: adiciona compreensão visual
- **Fontes**: Liu et al. (arXiv:2308.03688), Zhou et al. (arXiv:2307.13854)

**Diagrama**: Grid dos ambientes do AgentBench
**Animação**: Ambientes aparecem em grid
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Dois benchmarks de panorama amplo. AgentBench tem 8 ambientes: sistema operacional, banco de dados, knowledge graph, web, card game, household, etc. É o benchmark mais abrangente — testa capacidades diversas. WebArena é específico de navegação web: agentes têm que navegar sites simulados e completar tarefas ("encontre produto mais barato", "agende reunião"). VisualWebArena adiciona compreensão visual (imagens, screenshots). Use AgentBench para panorama geral, WebArena para agentes de navegação.
💡 ANALOGIA: AgentBench é como o decatlo — prova múltiplas habilidades. WebArena é como prova específica de natação.
➡️ TRANSIÇÃO: "Como rodar isso localmente?"

---

### Slide 51 — Como Rodar Localmente

**Título**: Como Rodar Localmente
**Objetivo**: Dar orientação prática de execução.
**Conteúdo**:
- **SWE-bench**: Docker + eval harness (repositório GitHub)
- **GAIA**: download do dataset + tools (web search, file tools)
- **τ-bench**: pip install + simulate user
- **Custo**: SWE-bench completo = $$ (muitas runs); subconjuntos = $$ controlável
- **Dica**: comece com subconjunto (10-50 casos) para iterar rápido
- **Tempo**: SWE-bench completo = horas; subconjunto = minutos

**Diagrama**: Tabela de custo/tempo por benchmark
**Animação**: Tabela aparece
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Prático. SWE-bench: clone o repo, Docker, eval harness. GAIA: baixe dataset HuggingFace, plugue tools (web search, file tools). τ-bench: pip install, rode com usuário simulado. Custos: SWE-bench completo é caro (centenas de runs, horas). Subconjunto de 50 casos é controlável (minutos, alguns dólares). Regra de ouro: SEMPRE comece com subconjunto para iterar rápido. Só rode completo quando estiver otimizando para o benchmark específico.
⚠️ ERROS COMUNS: Alunos rodam benchmark completo de primeira. Demora, custa caro, e você não itera. Comece com 10-50.
➡️ TRANSIÇÃO: "Agora a parte desconfortável: limites."

---

### Slide 52 — Limites e Contaminação

**Título**: Limites e Contaminação
**Objetivo**: Ser honesto sobre os limites dos benchmarks.
**Conteúdo**:
- **Contaminação**: dados de treino podem incluir o benchmark
- **Overfitting**: otimizar para benchmark ≠ melhorar para produção
- **Coverage**: benchmark cobre domínio específico, não seu caso de uso
- **Saturação**: modelos melhores → benchmark fica fácil → perde poder discriminante
- **Detecção de contaminação**: overlaps de n-gramas, memorização
- **Pergunta**: *Um score alto em SWE-bench garante bom desempenho em produção?*

**Diagrama**: Sinais de contaminação e overfitting
**Animação**: Sinais aparecem em vermelho
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Quatro limites. Contaminação: o benchmark pode estar nos dados de treino do modelo — score inflado. Overfitting: otimizar para benchmark pode piorar produção. Coverage: benchmark cobre um domínio específico, não o seu. Saturação: conforme modelos melhoram, benchmark fica fácil e perde poder de discriminação (já aconteceu com vários). Como detectar contaminação: overlap de n-gramas, testar com variantes do benchmark. A regra de ouro: score de benchmark é um sinal, não uma prova.
❓ PERGUNTA PARA A TURMA: "Score alto em benchmark garante produção?" (resposta: não)
⚠️ ERROS COMUNS: Alunos vendem agente só com score de benchmark. Sempre combine com eval custom.
➡️ TRANSIÇÃO: "Vamos praticar escolha de benchmark."

---

### Slide 53 — Exercício: Escolhendo um Benchmark

**Título**: Exercício — Escolhendo um Benchmark
**Objetivo**: Praticar a seleção de benchmark adequado.
**Conteúdo**:
- 4 cenários curtos; alunos escolhem o benchmark:
  1. "Agente de coding que resolve issues" → **SWE-bench**
  2. "Assistente de pesquisa geral" → **GAIA**
  3. "Agente de atendimento com APIs" → **τ-bench**
  4. "Bot que navega e-commerce" → **WebArena**
- Votação rápida (mãos levantadas)

**Diagrama**: 4 cards com cenários
**Animação**: Cards aparecem
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Respostas: 1 → SWE-bench (código, verificável), 2 → GAIA (raciocínio geral), 3 → τ-bench (tool use com policy), 4 → WebArena (navegação). A escolha depende do domínio do seu agente. Use o benchmark que testa a capacidade que importa para você.
❓ PERGUNTA PARA A TURMA: Votação, um cenário por vez. Anotar resultado.
➡️ TRANSIÇÃO: "Vamos refletir sobre benchmark vs produção."

---

### Slide 54 — Pergunta: Benchmark vs Produção

**Título**: Benchmark vs Produção
**Objetivo**: Refletir sobre o gap entre benchmark e produção.
**Conteúdo**:
- "Um score alto em benchmark garante bom desempenho em produção?"
- **Resposta**: Não necessariamente
- Benchmark é ambiente controlado; produção é mundo real
- Combinar: benchmark (comparável) + eval custom (representativo)
- *"Benchmark diz o que é possível; eval custom diz o que é real"*

**Diagrama**: Dois lados — benchmark (lab) vs produção (mundo)
**Animação**: Dois lados aparecem
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Fechamento da seção. Benchmark é laboratório — controlado, comparável, mas irreal. Produção é mundo real — caótico, variável, real. Score alto em benchmark é NECESSÁRIO mas não SUFICIENTE. Combine: benchmark para comparação com a comunidade + eval custom para seu caso de uso. Sem eval custom, você não sabe se o score do benchmark se traduz em valor real.
➡️ TRANSIÇÃO: "Agora vamos para melhoria contínua e reporte."

---

## SEÇÃO F — Ciclo de Melhoria & Reportando Resultados (Slides 55-64 · 12 min)

---

### Slide 55 — [SEÇÃO] Ciclo de Melhoria Contínua

**Título**: 5 — Ciclo de Melhoria Contínua
**Objetivo**: Transição para o bloco de melhoria contínua.
**Conteúdo**: "5 — Ciclo de Melhoria Contínua e Reportando Resultados"
**Diagrama**: Fundo `etho-primary`
**Animação**: Número cresce com zoom
**Tempo**: 0.5 min

**Notas do Professor**:
➡️ TRANSIÇÃO: "Avaliar é uma coisa. Melhorar com base nela é outra. Vamos para o ciclo."

---

### Slide 56 — Dataset Crescente

**Título**: Dataset Crescente
**Objetivo**: Apresentar o princípio de que eval é um ativo que cresce.
**Conteúdo**:
- *"Você não mediu se não mediu"* — cada execução é dado
- Produção gera casos: logs de conversas, feedback de usuário
- Triagem: humano classifica (bom/ruim/edge case)
- Bug encontrado → novo golden case (nunca mais regredir)
- **Crescimento**: 10 → 50 → 200 → 1000+ casos ao longo de meses
- Dataset é vantagem competitiva: seu concorrente não tem seus casos

**Diagrama**: Funil — produção → triagem → golden cases → regressão
**Animação**: Funil aparece
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esse é o ativo mais valioso do seu projeto de agente. Produção gera dados — logs de conversas, feedback de usuários. Você tria: bom, ruim, edge case. Cada bug encontrado vira golden case. Seu conjunto cresce de 10 para 1000 em meses. Esse dataset é VANTAGEM COMPETITIVA — seu concorrente não tem acesso aos seus casos de produção. Por isso empresas guardam seus eval datasets como ouro.
💡 ANALOGIA: É como uma biblioteca de casos médicos. Cada paciente atendido gera conhecimento. Em anos, você tem milhares de casos. Competidor novo não tem isso.
⚠️ ERROS COMUNS: Alunos não triam dados de produção. Jogam fora ouro.
➡️ TRANSIÇÃO: "Esse dataset precisa rodar no CI."

---

### Slide 57 — CI para Agentes (Testes de Regressão)

**Título**: CI para Agentes
**Objetivo**: Mostrar como eval se integra ao CI/CD.
**Conteúdo**:
- Toda mudança (prompt, tool, modelo, config) dispara eval
- CI roda: golden cases + subconjunto de benchmark
- **Gate**: se regressão > threshold → bloquear merge
- **Threshold**: 0% para casos críticos, 5% para casos não-críticos
- **Velocidade**: CI eval precisa rodar em < 10 min (subconjunto)
- **Full eval**: noturno ou pré-deploy

**Diagrama**: Pipeline CI — PR → eval → gate → merge/deploy
**Animação**: Pipeline flui
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: CI para agentes é igual CI para código — mas o "teste" é eval. Toda mudança (PR) dispara eval. CI roda subconjunto de golden cases + benchmark subset. Gate: se regressão > threshold, bloqueia merge. Threshold varia: casos críticos = 0% de tolerância; não-críticos = 5%. Velocidade importa: CI eval precisa rodar em < 10 min para não bloquear desenvolvimento. Full eval (conjunto completo) roda noturno ou pré-deploy.
💡 ANALOGIA: É como CI tradicional. Você não faz merge sem testes passarem. Em agentes, você não faz merge sem eval passar.
⚠️ ERROS COMUNS: Alunos rodam full eval no CI. Demora 1 hora, bloqueia dev. Use subconjunto.
➡️ TRANSIÇÃO: "Mas mesmo com CI, deploy tem risco. Vamos mitigar."

---

### Slide 58 — Shadow Runs e Canary

**Título**: Shadow Runs e Canary
**Objetivo**: Apresentar estratégias de deploy seguro para agentes.
**Conteúdo**:
- **Shadow run**: nova versão roda em paralelo sem afetar usuário
- Compara outputs: versão atual vs versão nova
- **Canary**: 5% → 25% → 50% → 100% do tráfego
- **Rollback automático**: se métricas degradam, volta para versão anterior
- Para agentes: shadow é ideal — sem risco para usuário
- Diferença de tradicional: agente não-determinístico precisa de mais amostras

**Diagrama**: Fluxo — shadow (paralelo) → canary (5%) → full (100%)
**Animação**: Fluxo aparece
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Duas estratégias de deploy seguro. Shadow run: nova versão roda em paralelo mas o resultado não vai para o usuário — só para comparação. Você mede se a nova versão é melhor antes de expor usuário. Canary: libera gradualmente — 5% do tráfego, depois 25%, 50%, 100%. Se métricas degradam em qualquer estágio, rollback automático. Para agentes, shadow é ideal: você compara versões sem risco. Cuidado: agentes são não-determinísticos, então precisam de mais amostras para ter confiança estatística.
💡 ANALOGIA: Shadow é como um ensaio geral. Canary é como estreiar em poucas cidades antes do lançamento nacional.
➡️ TRANSIÇÃO: "Tem mais uma fonte de dados: feedback humano."

---

### Slide 59 — Feedback Humano Estruturado

**Título**: Feedback Humano Estruturado
**Objetivo**: Mostrar como coletar feedback que vira dado de eval.
**Conteúdo**:
- **Thumbs up/down**: simples, mas sem contexto
- **Feedback estruturado**: categoria (errado/incompleto/lento/off-topic) + texto
- **Implicit feedback**: usuário refez a pergunta? Abandonou?
- **Loop**: feedback → triagem → golden case → regressão
- **Cuidado**: feedback enviesado (só usuários frustrados respondem)

**Diagrama**: Ciclo — usuário → feedback → triagem → golden case → melhoria
**Animação**: Ciclo aparece
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Feedback humano vira dado de eval. Thumbs up/down é simples mas sem contexto (por que foi ruim?). Feedback estruturado é melhor: categoria (errado, incompleto, lento, off-topic) + texto livre. Implicit feedback é poderoso: usuário refez a pergunta? (agente não entendeu). Abandonou? (frustrou). Esse loop: feedback → triagem → novo golden case → regressão. Cuidado: feedback é enviesado — só usuários frustrados respondem. Sucessos silenciosos não aparecem.
💡 ANALOGIA: É como pesquisa de satisfação. Quem responde é quem amou ou quem odiou. O meio não responde.
⚠️ ERROS COMUNS: Alunos confiam cegamente em feedback. Sempre cruze com métricas de uso.
➡️ TRANSIÇÃO: "Com dados em mãos, vamos reportar."

---

### Slide 60 — [SEÇÃO] Reportando Resultados

**Título**: 6 — Reportando Resultados
**Objetivo**: Transição para reporte de resultados.
**Conteúdo**: "6 — Reportando Resultados com Rigor"
**Diagrama**: Fundo `etho-primary`
**Animação**: Número cresce com zoom
**Tempo**: 0.5 min

**Notas do Professor**:
➡️ TRANSIÇÃO: "Medir é metade. Reportar com rigor é a outra metade."

---

### Slide 61 — Eval Report (Template)

**Título**: Eval Report — Template
**Objetivo**: Apresentar a estrutura de um eval report profissional.
**Conteúdo**:
- Template: `24-Templates/template-eval-report.md`
- **Seções**:
  1. Sumário executivo (1 parágrafo)
  2. Metodologia (dataset, métricas, N runs)
  3. Resultados (tabela: métrica × versão)
  4. Análise de falhas (categorização)
  5. Comparações (vs baseline, vs humano)
  6. Recomendações (deploy? corrigir? investigar?)
- **Princípio**: reprodutível — outro engenheiro consegue rerodar

**Diagrama**: Mock do template preenchido
**Animação**: Seções aparecem
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Eval report é a entrega profissional. Seis seções. Sumário executivo: 1 parágrafo dizendo o que mudou e a decisão recomendada. Metodologia: dataset usado, métricas, N runs (reprodutibilidade). Resultados: tabela com métricas por versão (baseline vs nova). Análise de falhas: categorização. Comparações: vs baseline e vs humano quando possível. Recomendações: deploy? corrigir? investigar? Princípio fundamental: REPRODUTÍVEL — outro engenheiro consegue rerodar e chegar no mesmo resultado.
💡 ANALOGIA: É como um paper científico. Tem metodologia, resultados, discussão, conclusão. Reprodutível por outros.
⚠️ ERROS COMUNS: Alunos reportam sem metodologia. Sem isso, ninguém reproduz.
➡️ TRANSIÇÃO: "Falhas precisam ser categorizadas."

---

### Slide 62 — Análise de Falhas (Categorização)

**Título**: Análise de Falhas
**Objetivo**: Mostrar como categorizar falhas sistematicamente.
**Conteúdo**:
- **Categorias canônicas**:
  1. Não entendeu a tarefa (interpretação errada)
  2. Tool errada (escolheu tool inadequada)
  3. Alucinação (inventou fato/tool/result)
  4. Loop infinito (não convergiu)
  5. Erro de tool (API falhou, formato errado)
  6. Incompleto (parou antes de terminar)
- **Por que categorizar**: direciona onde investir esforço
- **Exemplo**: 60% das falhas são "tool errada" → melhorar ACI

**Diagrama**: Gráfico de pizza com categorias de falha
**Animação**: Fatias aparecem
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: "Agente falhou em 30% dos casos" é inútil. "Agente falhou: 60% tool errada, 20% alucinação, 10% loop, 10% incompleto" é actionable. Categorização direciona esforço. Se 60% é tool errada, invista em ACI (melhorar descrição de tools). Se 20% é alucinação, ajuste prompt para exigir grounding. Se 10% loop, ajuste max_steps e detecção de repetição. Sem categoria, você corre atrás de falhas sem prioridade.
💡 ANALOGIA: É como triagem médica. Não basta dizer "está doente". Tem que dizer "é gripe", "é dengue", "é fratura". Cada categoria tem tratamento diferente.
➡️ TRANSIÇÃO: "Comparar versões precisa de honestidade."

---

### Slide 63 — Comparações Honestas

**Título**: Comparações Honestas
**Objetivo**: Apresentar princípios de comparação justa.
**Conteúdo**:
- Sempre comparar vs baseline (versão anterior)
- Comparar vs humano quando possível (ground truth)
- **Mesmas condições**: mesmo dataset, mesmo ambiente, mesmo N
- Reportar intervalo de confiança, não só média
- **Honestidade**: reportar onde perdeu, não só onde ganhou
- **Pergunta**: *O que é mais importante reportar para o CEO — accuracy ou custo por execução?*

**Diagrama**: Tabela comparativa com baseline, versão nova, humano
**Animação**: Tabela aparece
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Comparação honesta. Sempre vs baseline — sem baseline, número não significa nada. Compare vs humano quando possível (ground truth). Mesmas condições: mesmo dataset, ambiente, N runs. Reporte intervalo de confiança, não só média (média sem IC é inútil em sistemas estocásticos). E a parte difícil: reporte onde PERDEU. Não esconda regressão. Se accuracy subiu mas custo dobrou, isso é trade-off — reporte.
❓ PERGUNTA PARA A TURMA: "O que reportar para o CEO — accuracy ou custo?" (resposta: depende do KPI do CEO. Geralmente: ambos.)
⚠️ ERROS COMUNS: Alunos só reportam melhorias. Esconder regressão é antiético e prejudica decisão.
➡️ TRANSIÇÃO: "Vamos praticar análise de regressão."

---

### Slide 64 — Exercício: Detectando Regressão

**Título**: Exercício — Detectando Regressão
**Objetivo**: Praticar análise de regressão em cenário real.
**Conteúdo**:
- **Cenário**: time mudou o prompt e o eval score caiu de 85% para 72%
- Em grupos: analisar causas possíveis
  - Viés do judge?
  - Mudança real no comportamento?
  - Casos que regrediram — padrão?
- Propor: próximos passos (A/B test? rever casos? corrigir prompt?)
- 3 min discussão, 2 min compartilhar

**Diagrama**: Eval report parcial para analisar
**Animação**: Report aparece
**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Cenário realista. Score caiu de 85% para 72%. Pergunta: por quê? Possíveis causas: (1) viés do judge — o judge mudou de comportamento; (2) regressão real — o agente piorou; (3) casos específicos — alguns casos regrediram por padrão. Para diagnosticar: olhe caso por caso, veja se faz sentido (realmente piorou?) ou não (judge julgou errado?). Próximos passos: A/B test para confirmar, rever casos ambíguos, ou reverter prompt.
❓ PERGUNTA PARA A TURMA: Pedir 2 grupos para compartilhar diagnóstico e próximos passos.
➡️ TRANSIÇÃO: "Vamos fechar a aula."

---

## SEÇÃO G — Fechamento (Slides 65-78 · 12 min)

---

### Slide 65 — [SEÇÃO] Fechamento

**Título**: 7 — Fechamento
**Objetivo**: Transição para o fechamento.
**Conteúdo**: "7 — Fechamento: Boas Práticas, Caso de Estudo, Quiz"
**Diagrama**: Fundo `etho-primary`
**Animação**: Número cresce com zoom
**Tempo**: 0.5 min

**Notas do Professor**:
➡️ TRANSIÇÃO: "Vamos consolidar com boas práticas, anti-patterns e caso real."

---

### Slide 66 — Boas Práticas (DO)

**Título**: Boas Práticas (DO)
**Objetivo**: Checklist de boas práticas de AgentOps.
**Conteúdo**:
- Comece com logs estruturados desde a primeira linha de código
- Adicione traces antes de adicionar features
- Construa golden cases desde o dia 1 (comece com 10)
- Rode eval a cada mudança (CI gate)
- Use LLM-as-judge com calibração humana
- Categorize falhas para direcionar esforço
- Cresça o dataset continuamente (produção → casos)
- Reporte com honestidade: inclua onde perdeu

**Diagrama**: Checklist verde (etho-success)
**Animação**: Itens aparecem com check
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: 8 boas práticas. A mais importante: COMECE com observabilidade desde a linha 1. Não deixe para depois. Logs estruturados são baratos. Traces antes de features. Golden cases desde o dia 1 — comece com 10, cresça. CI gate em todo PR. LLM-as-judge COM calibração humana (nunca sem). Categorização de falhas. Dataset crescente. Reporte honesto. Essas 8 transformam "vibes-based" em "evidence-based".
➡️ TRANSIÇÃO: "Agora o que NÃO fazer."

---

### Slide 67 — Anti-Patterns (DON'T)

**Título**: Anti-Patterns (DON'T)
**Objetivo**: Checklist do que NÃO fazer em AgentOps.
**Conteúdo**:
- Vibes-based eval ("parece bom")
- Sem observabilidade em produção
- Eval manual que não escala
- LLM-as-judge sem calibração
- Benchmark como única medida de qualidade
- Deploy sem gate de regressão
- Não categorizar falhas ("saber que falhou" sem "por quê")
- Dataset estagnado (mesmos 10 casos para sempre)
- Overfitting para benchmark

**Diagrama**: Checklist vermelho (etho-danger)
**Animação**: Itens aparecem com X
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: 9 anti-patterns. O pior: vibes-based eval. Sem observabilidade em produção é irresponsável. Eval manual não escala. LLM-as-judge sem calibração é fé cega. Benchmark como única métrica é marketing, não engenharia. Deploy sem gate é jogar dados. Não categorizar falhas é saber QUE falhou sem saber POR QUE. Dataset estagnado é estagnação técnica. Overfitting de benchmark é otimizar para o laboratório, não para produção.
❓ PERGUNTA PARA A TURMA: "Quantos desses vocês já cometeram?" (todos vão rir)
➡️ TRANSIÇÃO: "Caso de estudo real."

---

### Slide 68 — Caso de Estudo: Anthropic Avaliando Claude em SWE-bench

**Título**: Caso de Estudo — Anthropic × Claude × SWE-bench
**Objetivo**: Mostrar todos os conceitos em um caso real.
**Conteúdo**:
- Anthropic avaliando Claude 3.5 Sonnet em SWE-bench
- **Metodologia**: SWE-bench Verified (500 casos, validação humana)
- **Resultado**: ~49% resolved (dez/2024)
- **Processo de melhoria**: iterar com traces + eval contínua
- **Análise de falhas**: categorizou onde Claude falhava
- **Lição**: melhoria guiada por dados, não por intuição
- *"Não há magia — é rigor experimental aplicado"*

**Diagrama**: Ciclo de melhoria da Anthropic — eval → trace → corrigir → re-eval
**Animação**: Ciclo aparece
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Anthropic não chegou em 49% por mágica. Chegou com rigor: rodar SWE-bench, analisar traces, categorizar falhas, corrigir, re-avaliar. Ciclo iterativo guiado por dados. Cada versão do Claude tinha eval report interno. Onde falhava? Categorizaram (não entendeu issue, alucinou API, etc.). Corrigiram. Re-avaliaram. A lição é simples: melhoria sistemática vence intuição. Não há atalho — é rigor experimental aplicado.
💡 ANALOGIA: É como treinar atleta de elite. Você mede tudo (tempo, ritmo, biometria), identifica gargalos, corrige, mede de novo. Sem dados, é amadorismo.
➡️ TRANSIÇÃO: "Vamos consolidar."

---

### Slide 69 — Resumo da Aula

**Título**: Resumo da Aula
**Objetivo**: Sintetizar os pontos-chave.
**Conteúdo**:
- Agentes são difíceis de avaliar: não-determinismo, ambiente, custo
- Observabilidade desde o dia 1: traces, spans, métricas
- LLM-as-judge com calibração: escala, mas tem vieses
- Golden cases + regressão: o CI gate de agentes
- Benchmarks canônicos: SWE-bench, GAIA, τ-bench — comparável mas ≠ produção
- Dataset crescente: sua vantagem competitiva
- Eval report: rigor e honestidade

**Diagrama**: 7 ícones com os pontos-chave
**Animação**: Ícones aparecem em grid
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: 7 pontos para levar. 1) Agentes são difíceis — não-determinismo, ambiente, custo. 2) Observabilidade é base — traces desde o dia 1. 3) LLM-as-judge escala mas tem vieses — calibre. 4) Golden cases + regressão são seu CI gate. 5) Benchmarks canônicos para comparar — mas não substituem eval custom. 6) Dataset crescente é vantagem competitiva. 7) Eval report com rigor e honestidade. Esses 7 são a fundação de AgentOps.
➡️ TRANSIÇÃO: "Vamos confirmar que cobrimos tudo."

---

### Slide 70 — Checklist da Aula

**Título**: Checklist da Aula
**Objetivo**: Confirmar que todos os tópicos foram cobertos.
**Conteúdo**:
- [x] Explicou por que agentes são difíceis de avaliar
- [x] Implementou observabilidade com traces
- [x] Construiu pipeline de eval com LLM-as-judge
- [x] Descreveu benchmarks canônicos
- [x] Explicou CI para agentes e regressão
- [x] Apresentou estrutura de eval report

**Diagrama**: Checklist visual
**Animação**: Itens aparecem com check
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Revisão dos 5 objetivos do Slide 2 + extras. Todos cobertos? Se algum não ficou claro, perguntem no Q&A.
➡️ TRANSIÇÃO: "Quiz!"

---

### Slide 71 — Quiz: Pergunta 1

**Título**: Quiz — Pergunta 1
**Objetivo**: Verificar compreensão.
**Conteúdo**:
- "Qual é a principal limitação do LLM-as-judge?"
- A) É muito caro para usar
- B) Não consegue avaliar texto
- C) Tem vieses (positional, sycophancy, verbosity) que precisam de mitigação
- D) Só funciona com GPT-4
- **Resposta**: C

**Diagrama**: Card de quiz
**Animação**: Opções aparecem
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Resposta: C. LLM-as-judge é barato, consegue avaliar texto, e funciona com vários modelos. A limitação é ter vieses (5 tipos) que precisam de mitigação (rubrica, calibração, múltiplos judges).
➡️ TRANSIÇÃO: "Próxima pergunta."

---

### Slide 72 — Quiz: Pergunta 2

**Título**: Quiz — Pergunta 2
**Objetivo**: Verificar compreensão.
**Conteúdo**:
- "O que é um golden case?"
- A) Um caso de uso de sucesso para marketing
- B) Um par (input, critério de sucesso) usado como teste de regressão
- C) Um caso que sempre passa no eval
- D) Um benchmark padronizado
- **Resposta**: B

**Diagrama**: Card de quiz
**Animação**: Opções aparecem
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Resposta: B. Golden case é par (input, critério). É o teste unitário do mundo de agentes. Não é marketing (A), não é caso que sempre passa (C — casos podem regredir), não é benchmark (D — benchmark é padronizado, golden case é seu).
➡️ TRANSIÇÃO: "Próxima."

---

### Slide 73 — Quiz: Pergunta 3

**Título**: Quiz — Pergunta 3
**Objetivo**: Verificar compreensão.
**Conteúdo**:
- "O que o SWE-bench avalia?"
- A) Navegação web autônoma
- B) Atendimento ao cliente com tools
- C) Resolução de issues reais de GitHub (código)
- D) Raciocínio geral multi-step
- **Resposta**: C

**Diagrama**: Card de quiz
**Animação**: Opções aparecem
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Resposta: C. SWE-bench avalia resolução de issues reais de GitHub (código). A é WebArena. B é τ-bench. D é GAIA.
➡️ TRANSIÇÃO: "Próxima."

---

### Slide 74 — Quiz: Pergunta 4

**Título**: Quiz — Pergunta 4
**Objetivo**: Verificar compreensão.
**Conteúdo**:
- "Em um pipeline de CI para agentes, o que bloqueia o deploy?"
- A) Latência acima de 1 segundo
- B) Regressão no eval score (golden cases + benchmark subset)
- C) Número de steps diferente da versão anterior
- D) Custo acima de $0.01 por run
- **Resposta**: B

**Diagrama**: Card de quiz
**Animação**: Opções aparecem
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Resposta: B. CI gate é regressão no eval score. Os outros (latência, steps, custo) são métricas mas não bloqueiam deploy sozinhas — são alertas. O gate é a regressão.
➡️ TRANSIÇÃO: "Última pergunta."

---

### Slide 75 — Quiz: Pergunta 5

**Título**: Quiz — Pergunta 5
**Objetivo**: Verificar compreensão.
**Conteúdo**:
- "V/F: 'Bom score em benchmark garante bom desempenho em produção.'"
- A) Verdadeiro — benchmarks são representativos
- B) Falso — benchmark é ambiente controlado, produção é mundo real
- C) Depende — só se o benchmark for do mesmo domínio
- D) Verdadeiro — se passou em SWE-bench, está pronto
- **Resposta**: B

**Diagrama**: Card de quiz
**Animação**: Opções aparecem
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Resposta: B. Falso. Benchmark é ambiente controlado; produção é mundo real. Mesmo do mesmo domínio (C), não garante — produção tem variância de ambiente, usuários reais, etc. Combine benchmark (comparável) + eval custom (representativo).
➡️ TRANSIÇÃO: "Vamos conectar com o resto da especialização."

---

### Slide 76 — Conexão com Próximos Módulos e Projeto

**Título**: Conexão e Projeto
**Objetivo**: Mostrar como ETHAGT12 conecta com o resto e apresentar projeto.
**Conteúdo**:
- **ETHAGT13** — Segurança & Governança: observabilidade como defesa
- **ETHAGT90** — Capstone: eval report completo
- **Projeto do módulo**: avaliar um agente em subconjunto de τ-bench ou GAIA
  - Entrega: eval report + dataset + código de rerun + análise de falhas
  - Critério: eval reproduzível; ≥3 categorias de falha documentadas
- **Lab 1 (5h)**: "Traces Everywhere" — adicionar observabilidade
- **Lab 2 (5h)**: "Eval automatizado" — pipeline com LLM-as-judge + golden cases

**Diagrama**: Mapa da especialização com ETHAGT12 destacado
**Animação**: Conexões aparecem
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: ETHAGT12 conecta em duas direções. Para ETHAGT13 (Segurança): observabilidade é defesa — você detecta ataques via traces. Para ETHAGT90 (Capstone): eval report é parte da entrega. Projeto do módulo: avaliem um agente em subconjunto de τ-bench ou GAIA. Entreguem eval report completo (usando o template), dataset, código de rerun, e análise de falhas com ≥3 categorias documentadas com correção proposta. Critério de sucesso: eval reproduzível. Dois labs suportam isso.
➡️ TRANSIÇÃO: "Leitura recomendada."

---

### Slide 77 — Leitura Recomendada e Referências

**Título**: Leitura Recomendada
**Objetivo**: Indicar leitura obrigatória e complementar.
**Conteúdo**:
- **Obrigatório**: Jimenez et al., *SWE-bench* (arXiv:2310.06770)
- **Obrigatório**: Mialon et al., *GAIA* (arXiv:2311.12983)
- **Obrigatório**: Yao et al., *τ-bench* (arXiv:2404.44529)
- **Reomendado**: Hamel Husain, *Evals for LLMs*
- **Recomendado**: Liu et al., *AgentBench* (arXiv:2308.03688)
- **Recomendado**: Zhou et al., *WebArena* (arXiv:2307.13854)
- **Docs**: LangSmith, Phoenix (Arize), Langfuse, OpenLLMetry, OpenTelemetry GenAI

**Diagrama**: Lista com ícones
**Animação**: Itens aparecem
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Leitura obrigatória: os 3 papers canônicos (SWE-bench, GAIA, τ-bench). São a base. Recomendado: Hamel Husain (conceitual), AgentBench e WebArena (complementares). Docs das ferramentas são referência prática. Para o projeto, leiam o paper do benchmark que escolherem.
➡️ TRANSIÇÃO: "Último slide."

---

### Slide 78 — Q&A / Encerramento

**Título**: Q&A
**Objetivo**: Abrir para perguntas e encerrar.
**Conteúdo**:
- "Perguntas?"
- Contato do professor
- "Na próxima aula: ETHAGT13 — Segurança & Governança de Agentes"

**Diagrama**: Logo Etho + fundo `etho-dark`
**Animação**: Fade out
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Abrir para Q&A. Se não houver perguntas, fazer pergunta inversa: "Qual parte foi menos clara?" Lembrar prazo dos labs e projeto. Próxima aula: ETHAGT13 — Segurança & Governança de Agentes, onde observabilidade vira defesa contra ataques (prompt injection, tool abuse).
💡 MENSAGEM FINAL: "Vocês saem desta aula com o toolkit completo para operar agentes com confiança. Observabilidade, avaliação, melhoria contínua. Usem. A diferença entre um agente que parece funcionar e um que funciona é rigor experimental."
