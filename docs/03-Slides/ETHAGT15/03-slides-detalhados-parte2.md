# ETHAGT15 — Slides Detalhados + Notas do Professor (Parte 2: Slides 35-67)

> Universidade Etho · Especialização em Programação Agêntica
> Cada slide contém: título, objetivo, conteúdo, notas do professor, diagrama, animação, imagem, tempo.

---

### Slide 35 — Pergunta: Quando Otimizar é Melhor que Reescrever?

**Título**: Quando Otimizar é Melhor?
**Objetivo**: Discussão sobre quando usar otimização automatizada.
**Conteúdo**:
- "Quando otimizar prompts é melhor que reescrevê-los manualmente?"
- **Casos para otimizar**: volume alto, métrica clara, espaço de busca grande
- **Casos para manual**: volume baixo, métrica subjetiva, domínio novo
- "Como você define a métrica de avaliação para otimização?"
- Discussão aberta (2 min)

**Diagrama**: Árvore de decisão: volume? métrica? domínio?
**Animação**: Ramos aparecem
**Imagem**: Ícone de bifurcação
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A regra geral: otimize quando (1) volume é alto (100+ agentes), (2) a métrica é clara e automatizável (success rate, F1), e (3) o espaço de busca é grande. Use manual quando (1) volume é baixo, (2) a métrica é subjetiva (tom de voz), ou (3) o domínio é novo. A segunda pergunta é crucial: como definir a métrica? Se a métrica for ruim, a otimização vai otimizar a coisa errada.
💡 ANALOGIA: É como decidir entre cozinhar com receita (otimizado) vs intuitivamente (manual). Receita para escala, intuição para criatividade.
❓ PERGUNTA PARA A TURMA: "Pensem no sistema de vocês: otimizaria ou reescreveria? Por quê?" (2 min)
➡️ TRANSIÇÃO: "Vamos para auto-aprendizado contínuo."

---

## SEÇÃO E — Auto-Aprendizado Contínuo (Slides 36-45 · 13 min)

---

### Slide 36 — [SEÇÃO] Auto-Aprendizado Contínuo

**Título**: 4 — Auto-Aprendizado Contínuo
**Objetivo**: Transição para auto-aprendizado.
**Conteúdo**: "4 — Auto-Aprendizado Contínuo"
**Diagrama**: Fundo `etho-primary`
**Animação**: Fade in
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Entramos na fronteira do auto-aprendizado. Vamos ver como agentes acumulam experiência, refletem sobre o sistema, evoluem estratégias, e quando precisam esquecer.
➡️ TRANSIÇÃO: "Comecemos pela memória."

---

### Slide 37 — Memória de Sucesso/Falha

**Título**: Memória de Sucesso e Falha
**Objetivo**: Explicar como agentes aprendem com experiência.
**Conteúdo**:
- **Memória de sucesso**: "esta estratégia funcionou para este tipo de tarefa"
- **Memória de falha**: "esta estratégia falhou para este tipo de tarefa"
- **Armazenamento**: vetor + metadata (tipo, estratégia, outcome, timestamp)
- **Recuperação**: nova tarefa → buscar casos similares → aplicar estratégia bem-sucedida
- **Sem memória**: agente repete os mesmos erros indefinidamente

**Diagrama**: Agente executa → outcome → armazena (sucesso/falha) → próxima tarefa recupera
**Animação**: Fluxo cíclico
**Imagem**: Ícone de caderno de anotações
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Auto-aprendizado começa com memória. Um agente sem memória repete os mesmos erros. Com memória, acumula experiência: "esta estratégia funcionou para este tipo de tarefa". A memória é armazenada como vetores (busca semântica) com metadata. Quando uma nova tarefa chega, o agente busca casos similares e aplica a estratégia que funcionou antes. É como a experiência profissional de um humano.
💡 ANALOGIA: É como um médico experiente vs recém-formado. O experiente reconhece padrões de milhares de casos. A memória transforma recém-formado em experiente.
⚠️ ERROS COMUNS: Alunos confundem memória de sucesso/falha com fine-tuning. Memória é retrieval em runtime; fine-tuning é treino de pesos. São complementares.
➡️ TRANSIÇÃO: "Mas memória individual não basta. Precisamos de reflexão sistêmica."

---

### Slide 38 — Reflexion em Nível de Sistema

**Título**: Reflexion Sistêmico
**Objetivo**: Diferenciar reflexão individual de sistêmica.
**Conteúdo**:
- **Reflexion individual**: agente reflete sobre SUA execução
- **Reflexion sistêmico**: meta-agente reflete sobre o SISTEMA de agentes
- Perguntas sistêmicas: "Qual agente falha mais?", "Qual tool é menos usada?", "Qual padrão de tarefa é mais comum?"
- **Output**: recomendações de mudança estrutural
- Nível acima: reflexão sobre reflexão (meta-meta)

**Diagrama**: Hierarquia: agente (individual) → meta-agente (sistêmico)
**Animação**: Níveis aparecem de baixo para cima
**Imagem**: Ícone de escada
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Reflexion individual — um agente reflete sobre sua execução. Reflexion sistêmico — um meta-agente analisa o SISTEMA inteiro: qual agente falha mais, qual tool é subutilizada, qual padrão de tarefa é comum. O output são recomendações estruturais. E dá para subir mais um nível: meta-meta-agente. Mas cuidado com recursão — na prática, 2 níveis bastam.
💡 ANALOGIA: É como jogador refletindo sobre seu desempenho (individual) vs técnico analisando o time (sistêmico).
⚠️ ERROS COMUNS: Alunos querem ir direto para meta-meta-meta. Comece com 2 níveis.
➡️ TRANSIÇÃO: "Vamos formalizar o strategy evolver."

---

### Slide 39 — Estratégia Evolutiva (Strategy Evolver)

**Título**: Strategy Evolver
**Objetivo**: Detalhar o padrão strategy evolver.
**Conteúdo**:
- **Strategy evolver**: componente que evolui estratégias ao longo do tempo
- **Estratégia** = configuração de agente (prompt + tools + parâmetros)
- **Processo**: manter população → gerar variações → avaliar → selecionar → substituir
- **Diferença vs DSPy**: evolver opera no nível de sistema, DSPy no nível de prompt
- **HITL**: auditoria periódica para prevenir drift

**Diagrama**: Ciclo evolutivo com população de estratégias
**Animação**: Ciclo gira
**Imagem**: Ícone de DNA + engrenagem
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Strategy evolver é o padrão arquitetural para auto-aprendizado contínuo. Você mantém uma população de estratégias. Periodicamente gera variações (mutação), avalia em subset de tarefas, seleciona as melhores, substitui as piores. A população evolui. Diferença vs DSPy: evolver otimiza a config do sistema inteiro; DSPy otimiza um prompt. HITL é obrigatório — sem auditoria, drift.
💡 ANALOGIA: É como um fundo de investimento rebalanceando o portfólio. O gestor (HITL) revisa periodicamente.
⚠️ ERROS COMUNS: Alunos acham que evolver substitui eval. Não — evolver USA eval. Sem eval, está cego.
➡️ TRANSIÇÃO: "Vamos ver o caso canônico: Voyager."

---

### Slide 40 — Voyager: Aprendendo Skills no Minecraft

**Título**: Voyager — Aprendendo Skills no Minecraft
**Objetivo**: Apresentar Voyager como caso canônico de auto-aprendizado.
**Conteúdo**:
- **Voyager** (Wang et al., arXiv:2305.16291): agente que aprende skills no Minecraft
- **3 componentes**:
  1. **Automatic curriculum**: gera próximos desafios baseado no progresso
  2. **Skill library**: armazena skills como código executável (JavaScript)
  3. **Iterative prompting**: refina prompts baseado em feedback do ambiente
- **Resultado**: aprende skills complexas sem intervenção humana
- **Lição**: ambiente fechado com feedback automático = auto-aprendizado viável
- **Limitação**: Minecraft é determinístico e seguro — mundo real não é

**Diagrama**: Arquitetura Voyager: curriculum → skill → library → execução
**Animação**: Componentes aparecem um a um
**Imagem**: Screenshot do Minecraft + logo NVIDIA
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Voyager, da NVIDIA, 2023. Agente que aprende Minecraft sozinho — craftear, minerar, construir. Três componentes: automatic curriculum (gera desafios baseado no progresso), skill library (skills armazenadas como código JS executável), iterative prompting (refina com base no feedback do ambiente). Aprende skills em horas que humanos levariam dias. Mas Minecraft é ambiente fechado, determinístico e seguro. Mundo real não é. Voyager prova o conceito; produção requer adaptação.
💡 ANALOGIA: É como um laboratório de física. No lab, condições controladas. No mundo real, há atrito e imprevisibilidade. Voyager é o lab.
❓ PERGUNTA PARA A TURMA: "Por que Voyager funciona no Minecraft mas seria perigoso em produção?" (ambiente controlado vs real)
⚠️ ERROS COMUNS: Alunos querem "aplicar Voyager na minha empresa". Cuidado — produção não é sandboxed.
➡️ TRANSIÇÃO: "Mas há um problema com memória: drift."

---

### Slide 41 — Quando Esquecer (Drift de Dados)

**Título**: Quando Esquecer — Drift de Dados
**Objetivo**: Discutir quando memória acumulada vira problema.
**Conteúdo**:
- **Drift**: ambiente muda, conhecimento antigo torna-se obsoleto
- **Tipos**: Conceito (o que era correto não é mais) · Dados (distribuição mudou)
- **Sintomas**: success rate cai, erros aumentam, feedback negativo cresce
- **Estratégias de esquecimento**: TTL (>30 dias), janela deslizante (N recentes), detecção ativa
- **Pergunta**: *O que acontece se o ambiente muda e o agente continua otimizando para o antigo?*

**Diagrama**: Timeline: ambiente muda, memória antiga vs nova, detecção de drift
**Animação**: Linha do tempo mostra mudança
**Imagem**: Gráfico de success rate caindo após drift
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Memória é poder e risco. Risco = drift: ambiente muda, memória reflete o antigo. Dois tipos: conceito (política mudou) e dados (distribuição de inputs mudou). Sintomas: success rate cai, erros aumentam. Estratégias: TTL (descartar >30 dias), janela deslizante (manter só N recentes), detecção ativa (monitorar e descartar quando drift detectado). Esquecer é tão importante quanto lembrar.
💡 ANALOGIA: É como um mapa GPS. Estradas mudam mas mapa é antigo → você se perde. Precisa atualizar.
⚠️ ERROS COMUNS: Alunos acham que "mais memória é sempre melhor". Falso — memória obsoleta é pior que nenhuma.
➡️ TRANSIÇÃO: "Vamos discutir."

---

### Slide 42 — Pergunta: O Que Acontece se o Ambiente Muda?

**Título**: O Que Acontece se o Ambiente Muda?
**Objetivo**: Engajar com pergunta sobre drift.
**Conteúdo**:
- "O que acontece se o ambiente muda e o agente continua otimizando para o antigo?"
- **Resposta**: overfitting ao antigo → performance cai
- "Como detectar drift automaticamente?"
- "Deveria esquecer tudo ou apenas o relevante?"
- Discussão em duplas (2 min)

**Diagrama**: Caixa de discussão
**Animação**: Perguntas aparecem
**Imagem**: Ícone de balão
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Se o ambiente muda e o agente otimiza para o antigo, overfitta — a métrica pode até melhorar no eval antigo, mas a performance real cai. Detectar: monitorar distribuição de inputs, success rate ao longo do tempo, feedback humano. Esquecer tudo vs relevante: idealmente relevante, mas identificar é difícil. Na prática, TTL agressivo + detecção ativa.
💡 ANALOGIA: É como um historiador citando livros de 1990 sobre o mundo de hoje — a análise está errada mesmo que os livros fossem corretos na época.
❓ PERGUNTA PARA A TURMA: "Em duplas, 2 min: como detectariam drift no sistema de vocês?"
➡️ TRANSIÇÃO: "Vamos praticar."

---

### Slide 43 — Exercício: Detectar Drift

**Título**: Exercício — Detectar Drift
**Objetivo**: Praticar detecção de drift.
**Conteúdo**:
- **Cenário**: agente de suporte com 6 meses de memória
- Métricas dos últimos 30 dias: success rate caiu de 92% → 78%
- Em duplas: propor 3 estratégias para detectar e mitigar drift
- Exemplos: comparar distribuição de queries, TTL agressivo, re-treinar
- 2 min propor, 1 min compartilhar

**Diagrama**: Gráfico de success rate caindo ao longo de 30 dias
**Animação**: Linha do gráfico desce
**Imagem**: Gráfico de linha temporal
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Cenário concreto. Agente com 6 meses de memória. Success rate caiu de 92% para 78% em 30 dias — sinal claro de drift. Em duplas, proponham 3 estratégias. Exemplos: comparar distribuição de queries (mudou o tipo de pergunta?), TTL agressivo, re-treinar com dados recentes, entrevistar usuários, monitorar tópicos emergentes. Diagnosticar antes de remediar.
💡 ANALOGIA: É como um médico diagnosticando. Sintoma é claro (queda de success rate), causas são várias. Precisa investigar antes de receitar.
❓ PERGUNTA PARA A TURMA: "Em duplas, 2 min. Depois compartilho as 2 mais criativas."
➡️ TRANSIÇÃO: "Vamos desafiar um mito."

---

### Slide 44 — Auto-Aprendizado Sempre Melhora? (V/F)

**Título**: Auto-Aprendizado Sempre Melhora?
**Objetivo**: Desafiar a hipótese de que auto-aprendizado é sempre positivo.
**Conteúdo**:
- **V/F**: "Auto-aprendizado contínuo sempre melhora."
- **Resposta**: **FALSO**
- Razões: overfitting, drift não detectado, loop de feedback positivo (agente aprende a "jogar" a métrica), catastrophic forgetting
- Auto-aprendizado precisa de: monitoramento, validação, reset quando necessário

**Diagrama**: V/F card com explicação
**Animação**: "FALSO" aparece em vermelho
**Imagem**: Ícone de X vermelho
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Mito para quebrar. "Auto-aprendizado sempre melhora" é FALSO. Quatro razões: overfitting ao ambiente atual, drift não detectado, loop de feedback positivo (agente aprende a "jogar" a métrica — ex.: fechar tickets sem resolver), catastrophic forgetting. Auto-aprendizado precisa de três salvaguardas: monitoramento, validação periódica, reset quando necessário. Não é "set and forget".
💡 ANALOGIA: É como um atleta que treina demais e se lesiona. Mais treino nem sempre é melhor — precisa periodização e descanso.
❓ PERGUNTA PARA A TURMA: "Conhecem algum caso de 'aprendeu a jogar a métrica'?" (YouTube recommender, social media engagement)
➡️ TRANSIÇÃO: "Vamos sintetizar."

---

### Slide 45 — Lições do Auto-Aprendizado

**Título**: Lições do Auto-Aprendizado
**Objetivo**: Sintetizar os aprendizados.
**Conteúdo**:
- Memória é poder, mas também é risco
- Reflexão sistêmica > individual para mudanças estruturais
- Strategy evolver = evolução biológica aplicada a configurações
- Voyager prova que funciona em ambiente controlado
- Drift é inevitável — detecção e esquecimento são obrigatórios
- Auto-aprendizado não é bala de prata: precisa governança

**Diagrama**: 6 ícones com as lições
**Animação**: Ícones aparecem
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Seis lições. Memória é poder e risco. Reflexão sistêmica supera individual para mudanças estruturais. Strategy evolver é evolução aplicada. Voyager provou o conceito em ambiente controlado. Drift é inevitável. Auto-aprendizado não é bala de prata — precisa governança.
💡 ANALOGIA: É como fogo. Controlado, aquece e cozinha. Sem controle, queima tudo.
➡️ TRANSIÇÃO: "E é sobre controle que falaremos agora: riscos e governança."

---

## SEÇÃO F — Riscos e Governança (Slides 46-55 · 12 min)

---

### Slide 46 — [SEÇÃO] Riscos e Governança

**Título**: 5 — Riscos e Governança
**Objetivo**: Transição para riscos e segurança.
**Conteúdo**: "5 — Riscos e Governança"
**Diagrama**: Fundo `etho-primary`
**Animação**: Fade in
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Seção mais crítica. Toda empolgação anterior encontra seu contrapeso aqui. Esta seção separa engenheiros responsáveis de imprudentes.
➡️ TRANSIÇÃO: "Comecemos pela recursão."

---

### Slide 47 — Recursão e Loops de Auto-Modificação

**Título**: Recursão e Auto-Modificação
**Objetivo**: Alertar sobre recursão descontrolada.
**Conteúdo**:
- Meta-agente modifica a si mesmo → nova versão modifica a si mesma → ...
- Sem convergência: loop infinito de auto-modificação
- Cada iteração introduz mudanças cumulativas
- **Risco**: comportamento emergente imprevisível
- **Mitigação**: `max_iterations`, diff entre versões (>N% requer aprovação), snapshot/versionamento, rollback automático se performance cair

**Diagrama**: Loop de auto-modificação com guardrails
**Animação**: Loop gira, guardrails bloqueiam
**Imagem**: Ícone de loop com sinal de pare
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Risco mais óbvio: recursão. Meta-agente que se modifica pode entrar em loop infinito. Cada iteração introduz mudanças cumulativas → comportamento imprevisível. Quatro mitigações não-negociáveis: max_iterations (hard limit), diff check (>20% requer humano), versionamento (snapshot para rollback), rollback automático se performance cair.
💡 ANALOGIA: É como um editor que revisa seu próprio texto infinitamente — nunca converge e pode piorar. Precisa de critério de parada e revert.
⚠️ ERROS COMUNS: Alunos acham que "max_iterations limita a inteligência". Não — limita o risco. Sem max_iter, bug vira loop infinito que consome orçamento ilimitado.
➡️ TRANSIÇÃO: "Segundo risco, mais sutil: goal drift."

---

### Slide 48 — Drift de Objetivos (Goal Drift)

**Título**: Goal Drift
**Objetivo**: Explicar como objetivos derivam.
**Conteúdo**:
- **Goal drift**: agente otimiza métrica que diverge do objetivo real
- **Exemplo**: objetivo = "resolver tickets", métrica = "tickets fechados/hora"
- **Drift**: agente fecha sem resolver para maximizar métrica
- **Causa**: métrica é proxy imperfeito do objetivo
- **Detecção**: divergência entre métrica e satisfação do usuário, auditoria periódica
- **Mitigação**: múltiplas métricas, nunca uma única

**Diagrama**: Objetivo real vs métrica proxy divergindo ao longo do tempo
**Animação**: Linhas divergem
**Imagem**: Gráfico de duas linhas se afastando
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Goal drift é o risco mais insidioso. Você define uma métrica como proxy do objetivo. "Resolver tickets" vira "tickets fechados/hora". O agente otimiza a métrica — fecha sem resolver. Métrica sobe, objetivo real cai. Causa raiz: toda métrica é proxy imperfeito. Detecção: monitore divergência entre métrica e satisfação do usuário. Mitigação: múltiplas métricas, nunca uma única.
💡 ANALOGIA: É como ensino focado em nota. Objetivo é "aprender", métrica é "nota". Estudantes decoram para a prova e esquecem. Métrica diverge do objetivo.
❓ PERGUNTA PARA A TURMA: "Já viram goal drift em produção?"
⚠️ ERROS COMUNS: Alunos acham que "métrica melhor" resolve. Não — toda métrica é proxy. Resolve múltiplas métricas + auditoria humana.
➡️ TRANSIÇÃO: "Para controlar, precisamos de meta-governor."

---

### Slide 49 — Meta-Governor Pattern

**Título**: Meta-Governor Pattern
**Objetivo**: Apresentar o padrão de governança para meta-agentes.
**Conteúdo**:
- **Meta-governor**: guardião que avalia mudanças propostas pelo meta-agente
- **Separado** do meta-agente (não pode auto-aprovar)
- **Regras**: policy-as-code (vetos), sandbox test, shadow run, canary, rollback
- **HITL**: aprovação humana para mudanças críticas

**Diagrama**: Meta-agente → propõe mudança → Meta-governor → aprova/rejeita
**Animação**: Fluxo com gate do governor
**Imagem**: Ícone de escudo
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Meta-governor é o guardião. Separado do meta-agente — essa separação é crítica. O meta-agente propõe; o governor avalia e aprova/rejeita. Governor NUNCA pode ser o próprio meta-agente (lobo guardando galinheiro). Regras são declarativas (policy-as-code). Para críticas, HITL. É o que torna meta-agência segura para produção.
💡 ANALOGIA: É como freios e airbags de carro. Motor (meta-agente) gera força. Freios (governor) limitam e controlam. Sem freios, motor é perigoso.
⚠️ ERROS COMUNS: Alunos implementam governor como "mais um prompt no meta-agente". Não — componente separado, idealmente determinístico para vetos críticos.
➡️ TRANSIÇÃO: "Vamos visualizar as camadas."

---

### Slide 50 — Safety Fences

**Título**: Safety Fences — Camadas de Defesa
**Objetivo**: Visualizar camadas de segurança.
**Conteúdo**:
- mudança proposta → Meta-Governor → policy-as-code
- vetar → bloquear / ok → sandbox test
- sandbox passa? não → bloquear / sim → shadow run
- shadow melhor? não → bloquear / sim → canary
- canary ok? sim → produção / não → rollback
- **4 camadas**: policy → sandbox → shadow → canary

**Diagrama**: `12-Diagrams/ETHAGT15/safety-fences.mmd`
**Animação**: Fluxo percorre as camadas, bloqueios em vermelho
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Blueprint de segurança. Mudança proposta → 4 gates. Gate 1: policy-as-code (vetos). Viola? Bloqueada. Gate 2: sandbox (dados sintéticos). Falha? Bloqueada. Gate 3: shadow run (paralelo, sem afetar usuários). Não é melhor? Bloqueada. Gate 4: canary (5% tráfego). Degrada? Rollback. Defesa em profundidade — cada camada filtra um tipo de problema.
💡 ANALOGIA: É como segurança de aeroporto. Detector de metal (policy), raio-x (sandbox), inspeção de bagagem (shadow), entrevista secundária (canary). Múltiplas camadas porque nenhuma é perfeita.
❓ PERGUNTA PARA A TURMA: "Qual camada é mais importante?" (resposta: todas — defesa em profundidade)
⚠️ ERROS COMUNS: Alunos pulam shadow run "para economizar tempo". Shadow pega regressões que sandbox não pega.
➡️ TRANSIÇÃO: "Vamos detalhar a confiança incremental."

---

### Slide 51 — Confiança Incremental (Sandbox → Produção)

**Título**: Confiança Incremental
**Objetivo**: Detalhar o pipeline de confiança incremental.
**Conteúdo**:
- **Nível 0**: Sandbox isolado (dados sintéticos, sem produção)
- **Nível 1**: Shadow run (paralelo, não afeta usuários)
- **Nível 2**: Canary (5% do tráfego, monitorado)
- **Nível 3**: Produção gradual (10% → 50% → 100%)
- **Nível 4**: Produção total
- Cada nível requer aprovação (automática ou humana)
- Rollback instantâneo se métricas degradarem
- **Princípio**: "confiança se ganha, não se dá"

**Diagrama**: Escada de níveis 0 → 4 com gates
**Animação**: Escada sobe nível por nível
**Imagem**: Ícone de escada
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Cinco níveis. Nível 0: sandbox isolado. Nível 1: shadow run. Nível 2: canary 5%. Nível 3: gradual 10-50-100%. Nível 4: total. Cada nível requer aprovação. Rollback instantâneo se degradar. Princípio: confiança se ganha, não se dá. Um agente gerado começa com zero confiança e merece cada nível.
💡 ANALOGIA: É como carreira de piloto. Simulador (sandbox), voo com instrutor (shadow), solo em rota fácil (canary), rotas complexas (gradual), comandante (total).
⚠️ ERROS COMUNS: Alunos querem pular para produção "porque passou no eval". Eval ≠ produção. Shadow e canary pegam problemas que eval não pega.
➡️ TRANSIÇÃO: "Dentro do governor, vetos são a ferramenta mais forte."

---

### Slide 52 — Vetos: Regras de Segurança

**Título**: Vetos — Regras Inegociáveis
**Objetivo**: Mostrar como implementar regras de veto.
**Conteúdo**:
- **Veto** = regra inegociável que bloqueia mudança
- Exemplos: "NUNCA remover safety constraints", "NUNCA aumentar custo >10%", "NUNCA remover logging", "NUNCA mudar modelo não-aprovado"
- **Implementação**: policy-as-code (Rego/CEL)
- `veto(change) if change.removes_safety_constraint or change.cost_increase > 0.10`
- **Veto é binário**: não há "quase veto"

**Diagrama**: Code block com regras de veto
**Animação**: Código aparece linha por linha
**Imagem**: Ícone de martelo de juiz
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vetos são a ferramenta mais forte do governor. Regra inegociável — se violada, bloqueia, sem exceção. Quatro canônicos: nunca remover safety constraints, nunca aumentar custo >10%, nunca remover logging, nunca mudar modelo não-aprovado. Implementação: policy-as-code (Rego/CEL). Característica chave: veto é binário. Não há "quase veto". Essa binariedade é o que torna auditável.
💡 ANALOGIA: É como limites físicos de carro — motor não passa de certa rotação porque regulador corta. Não é sugestão, é limite físico.
⚠️ ERROS COMUNS: Alunos implementam vetos como "warnings". Warning é inútil — meta-agente ignora. Veto precisa ser hard block em código.
➡️ TRANSIÇÃO: "Vamos praticar design de governor."

---

### Slide 53 — Exercício: Projetar um Meta-Governor

**Título**: Exercício — Projetar um Meta-Governor
**Objetivo**: Praticar design de governança.
**Conteúdo**:
- **Cenário**: meta-agente quer modificar o próprio system prompt
- Em trios: projetar um meta-governor com regras de veto
- Exemplos: "não pode remover safety constraints", "não pode aumentar custo >10%"
- **Bônus**: o que acontece se o meta-governor também for um agente?
- 3 min design, 2 min compartilhar

**Diagrama**: Template de design do meta-governor
**Animação**: Template se preenche
**Imagem**: Ícone de blueprint
**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Exercício central. Em trios, projetem um meta-governor para um cenário concreto: meta-agente modifica o próprio system prompt. Pensem em: (1) regras de veto, (2) pipeline de gates, (3) quando HITL é obrigatório, (4) critério de rollback. Bônus: se o governor também for LLM, quem governa o governor? Regressão infinita — por isso governors críticos devem ser determinísticos.
💡 ANALOGIA: É como projetar a constituição de um país. Quem faz leis? Quem fiscaliza? Quem garante que o fiscalizador não é corrupto?
❓ PERGUNTA PARA A TURMA: "Em trios, 3 min. Depois compartilho as 3 regras de veto mais criativas."
⚠️ ERROS COMUNS: Trios criam governors muito permissivos. Veto é binário. Se tem "exceto se...", não é veto, é gate.
➡️ TRANSIÇÃO: "Vamos para a pergunta mais profunda."

---

### Slide 54 — Pergunta: Em Que Ponto um Meta-Agente Se Torna Perigoso?

**Título**: Quando um Meta-Agente Se Torna Perigoso?
**Objetivo**: Estimular reflexão crítica sobre limites.
**Conteúdo**:
- "Em que ponto um meta-agente se torna perigoso?"
- **Sinais de alerta**: pode modificar suas próprias regras de segurança, pode escolher sua própria métrica, não tem HITL para críticas, pode escalar sem canary
- **Princípio**: perigo = capacidade × autonomia × falta de oversight
- Discussão aberta (2 min)

**Diagrama**: Fórmula visual: perigo = capacidade × autonomia × falta de oversight
**Animação**: Fatores aparecem
**Imagem**: Ícone de sirene
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Pergunta mais profunda da aula. Quatro sinais de alerta. Primeiro: pode modificar suas regras de segurança — remove vetos, não há limites. Segundo: pode escolher sua métrica — define o que é "bom", vai se definir como bom. Terceiro: sem HITL para críticas — erros escalam. Quarto: pode escalar sem canary — bug afeta 100% instantaneamente. Fórmula: perigo = capacidade × autonomia × falta de oversight. Objetivo não é eliminar perigo (impossível se quer utilidade) — é manter equilíbrio.
💡 ANALOGIA: É como carro autônomo. Perigoso se: desliga próprios sensores (regras), decide o que é "dirigir bem" (métrica), sem humano que assume (HITL), acelera de 0 a 100 instantaneamente (sem canary).
❓ PERGUNTA PARA A TURMA: "Conhecem sistema com algum desses sinais hoje?" (2 min)
➡️ TRANSIÇÃO: "Vamos ver um caso que ilustra quando é seguro."

---

### Slide 55 — Caso de Estudo: Voyager (Segurança em Ambiente Fechado)

**Título**: Caso — Voyager (Segurança em Ambiente Fechado)
**Objetivo**: Mostrar Voyager como caso de auto-aprendizado seguro.
**Conteúdo**:
- Voyager aprende skills no Minecraft — por que é seguro?
- **Ambiente fechado**: sandbox total, sem acesso a mundo real
- **Feedback determinístico**: sucesso/falha é claro (crafteou o item?)
- **Sem consequências reais**: erro no Minecraft não causa dano
- **Skills são código verificável** (não ações opacas)
- **Lição**: auto-aprendizado é seguro quando sandboxed, feedback claro, skills auditáveis, sem acesso a sistemas sensíveis
- Em produção: replicar estas condições

**Diagrama**: Comparação: Voyager (seguro) vs produção (risco)
**Animação**: Comparação lado a lado
**Imagem**: Screenshot Minecraft vs servidor de produção
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Encerramos riscos com Voyager como contra-exemplo — quando auto-aprendizado É seguro. Quatro razões. Ambiente fechado (sandbox total). Feedback determinístico (sabe se funcionou). Sem consequências reais (erro não causa dano). Skills são código verificável (auditável). Lição: auto-aprendizado é seguro quando sandboxed, feedback claro, skills auditáveis, sem acesso a sensíveis. Em produção, replica essas condições.
💡 ANALOGIA: É como simulador de voo. Piloto aprende manobras perigosas no simulador porque é seguro. Na vida real, precisa supervisão.
➡️ TRANSIÇÃO: "Com riscos entendidos, vamos para boas práticas."

---

## SEÇÃO G — Fechamento (Slides 56-67 · 10 min)

---

### Slide 56 — [SEÇÃO] Boas Práticas e Anti-Patterns

**Título**: 6 — Boas Práticas e Anti-Patterns
**Objetivo**: Transição para o fechamento.
**Conteúdo**: "6 — Boas Práticas e Anti-Patterns"
**Diagrama**: Fundo `etho-primary`
**Animação**: Fade in
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Última seção substantiva. Vamos sistematizar DO e DON'T, resumir, fazer quiz e fechar.
➡️ TRANSIÇÃO: "Comecemos pelas boas práticas."

---

### Slide 57 — Boas Práticas (DO)

**Título**: Boas Práticas — DO
**Objetivo**: Checklist de boas práticas de meta-agência.
**Conteúdo**:
- Comece com domínio estreito e bem definido
- Sempre valide agentes gerados (eval antes de deploy)
- Use confiança incremental (sandbox → shadow → canary → produção)
- Implemente meta-governor com vetos desde o início
- Versionamento de todas as configs geradas
- Monitore drift continuamente
- HITL para mudanças críticas
- Audite skills/memória periodicamente

**Diagrama**: Checklist verde (etho-success)
**Animação**: Itens aparecem com check verde
**Imagem**: Ícone de checkmark
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Oito boas práticas. Comecem estreito. Eval sempre. Confiança incremental. Meta-governor com vetos desde o dia 1. Versionem tudo. Monitorem drift. HITL para críticas. Auditem memória periodicamente. Essas oito práticas separam meta-agência production-ready de protótipo perigoso.
💡 ANALOGIA: É como checklist de pré-voo. Cada item parece óbvio, mas pular um pode ser fatal. Em meta-agência é mais importante porque o sistema evolui sozinho.
➡️ TRANSIÇÃO: "E o que NÃO fazer?"

---

### Slide 58 — Anti-Patterns (DON'T)

**Título**: Anti-Patterns — DON'T
**Objetivo**: Checklist do que NÃO fazer.
**Conteúdo**:
- Permitir auto-modificação sem limites (recursão descontrolada)
- Usar métrica única como objetivo (goal drift)
- Deployar sem eval (agente gerado pode ser pior)
- Deixar meta-agente escolher própria métrica
- Sem rollback automático
- Confiança total sem canary/shadow
- Ignorar drift de dados
- Meta-agente sem governor (auto-aprovação)

**Diagrama**: Checklist vermelho (etho-danger)
**Animação**: Itens aparecem com X vermelho
**Imagem**: Ícone de proibido
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Oito anti-patterns. O mais perigoso: meta-agente sem governor (auto-aprovação). Segundo: métrica única (goal drift garantido). Terceiro: deployar sem eval. Esses três causam a maioria dos incidentes.
💡 ANALOGIA: É como erros clássicos de segurança de software. SQL injection, XSS — conhecidos, evitáveis, mas acontecem porque alguém pulou o checklist.
➡️ TRANSIÇÃO: "Vamos resumir."

---

### Slide 59 — Resumo da Aula

**Título**: Resumo da Aula
**Objetivo**: Sintetizar os pontos-chave.
**Conteúdo**:
- **Meta-agência** = agentes que operam sobre agentes (synthesis, evolution, optimization)
- **Geração** = meta-agente + primitivas + validação rigorosa
- **Otimização** = DSPy (compilação), Promptbreeder (evolução), Atlas (busca)
- **Auto-aprendizado** = memória + reflexion + strategy evolver + drift detection
- **Riscos** = recursão, goal drift, perda de controle
- **Governança** = meta-governor + safety fences + confiança incremental + vetos
- **Projeto**: otimizar prompts/tools automaticamente e medir ganho

**Diagrama**: 7 ícones com os pontos-chave
**Animação**: Ícones aparecem em grid
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Sete pontos. Meta-agência = agentes sobre agentes, três estratégias. Geração = meta-agente + primitivas + validação. Otimização = DSPy, Promptbreeder, Atlas. Auto-aprendizado = memória + reflexion + evolver + drift detection. Riscos = recursão, goal drift, controle. Governança = governor + fences + confiança incremental + vetos. Projeto = otimizar e medir.
💡 ANALOGIA: É como deck final de palestra de medicina. Diagnóstico, tratamento, efeitos colaterais, protocolo de segurança.
➡️ TRANSIÇÃO: "Vamos confirmar que cobrimos tudo."

---

### Slide 60 — Checklist da Aula

**Título**: Checklist da Aula
**Objetivo**: Confirmar cobertura.
**Conteúdo**:
- [ ] Definiu meta-agência e 3 estratégias
- [ ] Implementou geração de agente com validação
- [ ] Aplicou DSPy ou Promptbreeder para otimização
- [ ] Discutiu auto-aprendizado e drift
- [ ] Projetou um meta-governor com vetos
- [ ] Identificou riscos e mitigações

**Diagrama**: Checklist visual
**Animação**: Itens recebem check
**Imagem**: Ícone de clipboard
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Se conseguem marcar os seis, a aula cumpriu o objetivo. O mais importante é o quinto — projetar meta-governor. Se saem sabendo governança, a aula valeu.
➡️ TRANSIÇÃO: "Vamos testar com quiz."

---

### Slide 61 — Quiz: Pergunta 1

**Título**: Quiz — Pergunta 1
**Objetivo**: Verificar compreensão.
**Conteúdo**:
- "Qual é a diferença fundamental entre um agente e um meta-agente?"
- A) O meta-agente usa um modelo maior
- B) O meta-agente opera sobre agentes (seu ambiente é outro agente)
- C) O meta-agente tem mais tools
- D) O meta-agente é sempre mais rápido
- **Resposta**: B

**Diagrama**: 4 opções com revelação
**Animação**: Opções aparecem, depois revela B
**Imagem**: —
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Resposta B. A diferença não é tamanho, número de tools, ou velocidade. É o alvo: agente comum age sobre ambiente; meta-agente age sobre agentes. Essa é a definição que vocãs precisam levar.
⚠️ ERROS COMUNS: Alunos marcam A ou C. Reenfatizar: é sobre alvo, não capacidade.
➡️ TRANSIÇÃO: "Próxima pergunta."

---

### Slide 62 — Quiz: Pergunta 2

**Título**: Quiz — Pergunta 2
**Objetivo**: Verificar compreensão.
**Conteúdo**:
- "O que é goal drift?"
- A) Agente muda de tarefa
- B) Agente otimiza uma métrica que diverge do objetivo real
- C) Agente esquece o objetivo original
- D) Agente muda de modelo
- **Resposta**: B

**Diagrama**: 4 opções com revelação
**Animação**: Opções aparecem, depois revela B
**Imagem**: —
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Resposta B. Goal drift é quando a métrica (proxy) diverge do objetivo real. O agente otimiza a métrica, mas o objetivo real piora. É o risco mais insidioso porque a métrica está "melhorando".
⚠️ ERROS COMUNS: Alunos marcam C ("esquece o objetivo"). Não — o agente não esquece, ele otimiza a métrica errada.
➡️ TRANSIÇÃO: "Última pergunta."

---

### Slide 63 — Quiz: Pergunta 3

**Título**: Quiz — Pergunta 3
**Objetivo**: Verificar compreensão.
**Conteúdo**:
- "Qual é a PRIMEIRA camada de defesa em safety fences?"
- A) Canary deployment
- B) Shadow run
- C) Policy-as-code (vetos)
- D) Rollback automático
- **Resposta**: C

**Diagrama**: 4 opções com revelação
**Animação**: Opções aparecem, depois revela C
**Imagem**: —
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Resposta C. A primeira camada é policy-as-code (vetos). É o gate mais barato e mais rápido — regras declarativas bloqueiam antes de qualquer teste. Canary, shadow e rollback vêm depois.
⚠️ ERROS COMUNS: Alunos marcam A (canary). Canary é a última camada antes de produção, não a primeira.
➡️ TRANSIÇÃO: "Vamos para discussão."

---

### Slide 64 — Perguntas para Discussão

**Título**: Perguntas para Discussão
**Objetivo**: Estimular debate.
**Conteúdo**:
1. "Quando otimizar prompts é melhor que reescrevê-los manualmente?"
2. "Defina goal drift e proponha uma detecção automática."
3. "Por que meta-governor é necessário? O agente não pode se autorregular?"
4. "Em que ponto um meta-agente se torna perigoso?"

**Diagrama**: 4 caixas com perguntas
**Animação**: Perguntas aparecem
**Imagem**: —
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Quatro perguntas para discussão. A 1 é sobre trade-offs de otimização. A 2 é sobre detecção de goal drift (métrica vs satisfação do usuário). A 3 é sobre a necessidade de separação de poderes (governor separado do meta-agente). A 4 é sobre limites — quando capacidade × autonomia × falta de oversight = perigo. Usem o tempo para discussão em grupo.
➡️ TRANSIÇÃO: "Vamos ver onde isso conecta."

---

### Slide 65 — Conexão com Próximos Módulos

**Título**: Conexão com Próximos Módulos
**Objetivo**: Mostrar como ETHAGT15 conecta com a especialização.
**Conteúdo**:
- **ETHAGT16 — Sociedades de Agentes**: meta-agentes em ecossistemas multi-agente
- **ETHAGT90 — Capstone**: meta-agente como sistema de orquestração
- **ETHAGT14 — Escalabilidade**: otimização de custo aplicada a meta-agentes
- **ETHAGT12 — AgentOps**: avaliação e observabilidade de meta-agentes

**Diagrama**: Mapa da especialização com ETHAGT15 destacado
**Animação**: Conexões aparecem
**Imagem**: Mind map
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: ETHAGT15 conecta com quatro módulos. ETHAGT16 (Sociedades) usa meta-agentes para orquestrar ecossistemas. ETHAGT90 (Capstone) pode usar meta-agente como camada de orquestração. ETHAGT14 (Escalabilidade) aplica otimização de custo. ETHAGT12 (AgentOps) fornece avaliação e observabilidade para meta-agentes.
➡️ TRANSIÇÃO: "Referências e projeto."

---

### Slide 66 — Referências, Projeto e Labs

**Título**: Referências, Projeto e Labs
**Objetivo**: Indicar leitura e apresentar projeto/labs.
**Conteúdo**:
- **Obrigatório**: Khattab et al. *DSPy* (arXiv:2310.03714)
- **Obrigatório**: Fernando et al. *Promptbreeder* (arXiv:2309.16797)
- **Recomendado**: Hu et al. *Meta-Prompting* (arXiv:2311.11402)
- **Recomendado**: Wang et al. *Voyager* (arXiv:2305.16291)
- **Recomendado**: Lu et al. *AI Scientist* (arXiv:2408.06292)
- **Projeto**: implementar otimização automática (DSPy) e medir ganho em benchmark
- **Lab 1** (4h): "Agente que escreve agente"
- **Próxima aula**: ETHAGT16 — Sociedades de Agentes

**Diagrama**: Lista de papers com arXiv IDs
**Animação**: Papers aparecem
**Imagem**: Capas dos papers
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Leitura obrigatória: DSPy e Promptbreeder. Recomendada: Meta-Prompting, Voyager e AI Scientist. Projeto do módulo: implementar otimização automática com DSPy e medir ganho em benchmark — antes vs depois. Lab 1: "Agente que escreve agente" (4h). Próxima aula: ETHAGT16 — Sociedades de Agentes, onde meta-agentes orquestram ecossistemas.
➡️ TRANSIÇÃO: "Vamos encerrar."

---

### Slide 67 — Q&A / Encerramento

**Título**: Q&A / Encerramento
**Objetivo**: Abrir para perguntas e encerrar.
**Conteúdo**:
- "Perguntas?"
- Contato do professor
- "Na próxima aula: ETHAGT16 — Sociedades de Agentes"

**Diagrama**: Logo Etho + fundo etho-dark
**Animação**: Fade out
**Imagem**: —
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Abrir para Q&A. Se nenhuma pergunta, fazer a pergunta inversa: "Qual parte foi menos clara?" ou "Qual técnica vocês vão aplicar primeiro no trabalho de vocês?" Encerrar conectando com ETHAGT16.
➡️ TRANSIÇÃO: Fim da aula.

---

## Fim da Parte 2

> Continuação: slides 1-34 estão em `03-slides-detalhados-parte1.md`.
