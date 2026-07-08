# ETHAGT16 — Slides Detalhados + Notas do Professor (Parte 2: Slides 23-50)

> Universidade Etho · Especialização em Programação Agêntica
> Cada slide contém: título, objetivo, conteúdo, notas do professor, diagrama, animação, imagem, tempo.

---

## SEÇÃO D — Autonomous Research Systems (Slides 23-33 · 12 min)

---

### Slide 23 — [SEÇÃO] Autonomous Research Systems

**Título**: Autonomous Research Systems
**Objetivo**: Transição para a Unidade 3 — Autonomous Research Systems.
**Conteúdo**: Número "3" grande + "Autonomous Research Systems"
**Diagrama**: Fundo `etho-primary`
**Animação**: Número 3 surge em `etho-accent`
**Imagem**: Pattern sutil de nós
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esta é a unidade mais longa (12 min) e a mais importante da aula. É onde a fronteira está. Vamos do pipeline canônico ao AI Scientist, ao AlphaEvolve, e à DEMO ao vivo.
➡️ TRANSIÇÃO: "Comecemos pelo pipeline que todos esses sistemas seguem."

---

### Slide 24 — Pipeline de Pesquisa Autônoma

**Título**: Pipeline de Pesquisa Autônoma
**Objetivo**: Apresentar o pipeline canônico de pesquisa autônoma.
**Conteúdo**:
- **Pipeline**: pergunta → revisão de literatura → hipótese → experimento → análise → relatório
- Cada etapa pode ser um agente diferente
- Ou um agente que executa todas as etapas
- **O desafio**: manter coerência entre etapas
- HITL em pontos críticos

**Diagrama**: Fluxo horizontal de 7 etapas
**Animação**: Etapas surgem em sequência
**Imagem**: Pipeline estilizado em `etho-primary`
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Toda pesquisa — humana ou de IA — segue um pipeline parecido. Pergunta, literatura, hipótese, experimento, análise, relatório. A diferença em agentes é: ou um agente executa tudo (AI Scientist) ou cada etapa é um agente diferente (multi-agent research lab). O desafio central é coerência: a hipótese precisa casar com a literatura; o experimento precisa testar a hipótese; a análise precisa responder à pergunta. Sem coerência entre etapas, o sistema produz lixo plausível.
💡 ANALOGIA: É como uma linha de montagem. Cada estação faz uma parte. Mas se a estação 2 não souber o que a estação 1 fez, o produto final não se encaixa.
⚠️ ERROS COMUNS: Alunos acham que pipeline linear resolve. Não — precisa de loops de feedback (se a análise contradiz a hipótese, volte e ajuste). Por isso HITL em pontos críticos.
➡️ TRANSIÇÃO: "Vamos ver o diagrama completo."

---

### Slide 25 — Diagrama: Research Pipeline

**Título**: Research Pipeline — Diagrama
**Objetivo**: Visualizar o pipeline completo de pesquisa autônoma.
**Conteúdo**:
- Fluxo: pergunta → revisão → hipótese → experimento → execução → análise → escrita
- HITL no fim: aprovar ou revisar
- Loop de revisão possível

**Diagrama**: `12-Diagrams/ETHAGT16/research-pipeline.mmd`
**Animação**: Etapas aparecem da esquerda para direita
**Imagem**: Diagrama `.mmd` renderizado
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Vejam o loop no fim. O HITL revisa o paper: se não estiver bom, volta para escrita. Esse loop é crítico em produção. Sem HITL, o sistema entrega lixo plausível. Com HITL, itera até qualidade aceitável.
⚠️ ERROS COMUNS: Alunos pulam o HITL. "É autônomo, não precisa de humano." Errado — autonomia sem HITL em alta stakes é irresponsável.
➡️ TRANSIÇÃO: "Vamos ao caso canônico: AI Scientist."

---

### Slide 26 — Sakana AI Scientist: Pesquisa ML de Ponta a Ponta

**Título**: Sakana AI Scientist — Pesquisa ML End-to-End
**Objetivo**: Apresentar o AI Scientist como caso canônico de pesquisa autônoma.
**Conteúdo**:
- **Sakana AI**: pesquisa ML do início ao fim
- Etapas: ideação → literatura → código → experimento → paper
- **Custo**: ~$15 por paper
- **Resultado**: papers aceitos em workshop ICLR
- Fonte: Lu et al., arXiv:2408.06292

**Diagrama**: Fluxo do AI Scientist em 5 etapas (D11)
**Animação**: Etapas surgem em sequência
**Imagem**: Logo Sakana (placeholder) + fluxo
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O AI Scientist é o experimento que mudou a conversa. Sakana (uma startup japonesa de IA) publicou em agosto de 2024 um sistema que conduz pesquisa de ML de ponta a ponta. Ideação, revisão de literatura, escrita de código, execução de experimentos, redação de paper em LaTeX. Custo médio: $15 por paper. Resultado: alguns papers foram aceitos em workshop do ICLR (peer review real, os reviewers não sabiam que era IA). Isso é histórico — primeiro caso de pesquisa científica autônoma passando em peer review.
💡 ANALOGIA: É como um estudante de doutramento automatizado. Faz o ciclo completo, mas precisa de supervisão. A diferença: custa $15, não uma bolsa de 4 anos.
⚠️ ERROS COMUNS: Alunos acham que AI Scientist "substitui" pesquisadores. Não — ele auxilia. Os papers aceitos eram marginais (workshop, não main conference). Automação de pesquisa assistida, não substituída.
➡️ TRANSIÇÃO: "Como ele funciona tecnicamente?"

---

### Slide 27 — Como o AI Scientist Funciona

**Título**: Como o AI Scientist Funciona
**Objetivo**: Mostrar a arquitetura técnica do AI Scientist.
**Conteúdo**:
- **Stage 1**: Ideação (LLM gera ideias de pesquisa)
- **Stage 2**: Experimentação (LLM escreve código, roda experimentos)
- **Stage 3**: Paper writing (LLM escreve paper em LaTeX)
- **Stage 4**: Review (LLM revisa como reviewer)
- Cada stage usa templates e prompts específicos
- O agente decide: continuar, refinar ou abandonar

**Diagrama**: Pipeline em 4 stages com feedback loop (D12)
**Animação**: Stages surgem, loop aparece por último
**Imagem**: Diagrama `.mmd` renderizado
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Quatro stages. Ideação: o LLM gera N ideias de pesquisa. Experimentação: para cada ideia, escreve código Python, roda experimentos, captura resultados. Paper writing: com os resultados, escreve um paper em LaTeX seguindo template. Review: um LLM atuando como reviewer (estilo NeurIPS) avalia o paper. E aqui a mágica: o agente decide se continua (paper bom), refina (precisa melhorar) ou abandona (ideia falhou). Esse loop de decisão é o coração da autonomia.
💡 ANALOGIA: É como um estudante que tem um orientador interno. Ele faz, avalia a si mesmo, e decide se entrega, refaz ou desiste. O detalhe: o "orientador" é outro prompt do mesmo LLM.
⚠️ ERROS COMUNS: Alunos acham que o review automático é confiável. Não — LLM revisando LLM tem vieses compartilhados. Erros sutis passam.
➡️ TRANSIÇÃO: "E se usarmos evolução em vez de pipeline?"

---

### Slide 28 — DeepMind AlphaEvolve: Evolução de Algoritmos

**Título**: DeepMind AlphaEvolve — Evolução de Algoritmos
**Objetivo**: Apresentar AlphaEvolve como fronteira de pesquisa autônoma.
**Conteúdo**:
- **AlphaEvolve**: evolução de algoritmos via LLM + avaliação automática
- LLM propõe mutações em código → avaliador testa → mantém melhores
- **Resultado**: descobriu novo algoritmo de multiplicação de matrizes
- **Lição**: evolução + avaliação automática = descoberta

**Diagrama**: Loop evolutivo: LLM → mutação → avaliação → seleção → LLM (D13)
**Animação**: Loop gira no sentido horário
**Imagem**: Logo DeepMind (placeholder)
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: AlphaEvolve (DeepMind, 2024) usa uma abordagem diferente do AI Scientist. Em vez de pipeline, ele usa EVOLUÇÃO. Um LLM propõe mutações em um pedaço de código. Um avaliador automático testa a mutação (roda e mede performance). As melhores mutações são mantidas; as piores descartadas. Repete-se milhares de vezes. O resultado impressionante: descobriu um novo algoritmo de multiplicação de matrizes — um problema que estava estagnado há décadas.
💡 ANALOGIA: É como evolução biológica, mas com LLM gerando "mutações" e um avaliador automático fazendo "seleção natural". Sem supervisão humana na seleção — só a métrica decide.
⚠️ ERROS COMUNS: Alunos acham que AlphaEvolve é "LLM que programa". Não — é LLM + avaliador automático. Sem o avaliador, é só um gerador de código aleatório. A evolução precisa de fitness function.
➡️ TRANSIÇÃO: "Outra abordagem: times de agentes."

---

### Slide 29 — Multi-Agent Research Labs

**Título**: Multi-Agent Research Labs
**Objetivo**: Mostrar a evolução para times de agentes especializados.
**Conteúdo**:
- Em vez de 1 agente: time de agentes especializados
- Pesquisador, programador, revisor, escritor
- **Vantagem**: especialização + divisão de trabalho
- **Desafio**: coordenação, comunicação, overhead
- Exemplo: AgentVerse colaborativo

**Diagrama**: Time de 4 agentes com canal de comunicação (D14)
**Animação**: Agentes surgem, canal conecta todos
**Imagem**: Diagrama `.mmd` renderizado
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Em vez de 1 agente fazendo tudo (AI Scientist), você pode ter um TIME. Pesquisador levanta literatura, programador escreve código, revisor valida qualidade, escritor redige paper. A vantagem é especialização — cada agente tem prompt e tools otimizados para seu papel. O desafio é coordenação: como garantir que o programador implementou o que o pesquisador propôs? Como o escritor sabe o que o revisor aprovou? Overhead de comunicação é real.
💡 ANALOGIA: É a diferença entre um generalista e uma equipe. A equipe produz mais, mas coordenação custa. Acima de 5-7 agentes, o overhead muitas vezes supera o benefício.
⚠️ ERROS COMUNS: Alunos acham que "mais agentes = mais capacidade". Não — mais agentes = mais overhead. Sweet spot costuma ser 3-5 papéis.
➡️ TRANSIÇÃO: "Chegou a hora da DEMO ao vivo."

---

### Slide 30 — DEMO: Mini Sociedade 5 Agentes

**Título**: DEMO — Mini Sociedade de 5 Agentes
**Objetivo**: Demo ao vivo — 5 agentes produzindo um relatório.
**Conteúdo**:
- 5 agentes: pesquisador, crítico, sintetizador, revisor, editor
- Tarefa: produzir relatório sobre "impacto de agentes na educação"
- Mostrar: cada agente contribui, debate, revisa, produz versão final
- Observar: divergências, consenso, qualidade do resultado
- Referência: `05-Labs/ETHAGT16/Lab1-Mini-Sociedade`

**Diagrama**: Code block + terminal side-by-side
**Animação**: Highlight de linhas chave durante execução
**Imagem**: Screenshot do VS Code + terminal
**Tempo**: 3 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esta é a DEMO principal da aula. Vou rodar o Lab1 ao vivo. 5 agentes: o pesquisador busca fontes, o crítico questiona, o sintetizador integra, o revisor valida, o editor finaliza. A tarefa é produzir um relatório curto sobre "impacto de agentes na educação". Observem três coisas: (1) onde surgem divergências, (2) onde há consenso rápido, (3) a qualidade do resultado final. A qualidade NÃO é garantida — às vezes o resultado é medíocre. Isso é honesto: sistemas autônomos são irregulares.
💡 ANALOGIA: É como observar uma equipe de pessoas trabalhando ao vivo. Às vezes flui, às vezes trava. A diferença: agentes são mais rápidos mas menos criativos.
❓ PERGUNTA PARA A TURMA: Durante a DEMO: "Prestem atenção ao crítico — quando ele concorda, quando discorda?"
⚠️ ERROS COMUNS: Se a DEMO falhar (API cai, timeout), NÃO tente consertar ao vivo. Use o screenshot pré-gravado. Tempo é mais valioso que perfeição.
➡️ TRANSIÇÃO: "Vamos discutir o que vimos."

---

### Slide 31 — Pergunta da DEMO

**Título**: Pergunta da DEMO
**Objetivo**: Engajar a turma com uma pergunta sobre a demo.
**Conteúdo**:
- "Qual papel foi mais crítico para o resultado?"
- "O que aconteceria se removêssemos o crítico?"
- "E se o editor tivesse poder de veto?"
- Discussão em duplas (1 min)

**Diagrama**: Caixa de discussão em `etho-warning`
**Animação**: Caixa surge
**Imagem**: Ícone de discussão
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: 1 minuto em duplas. O ponto é análise contrafactual: se remover X, o que muda? Sem o crítico, qualidade cai (sem questionamento). Com editor com veto, convergência mais rápida mas menos diversidade. Cada papel tem uma função, e remover muda a dinâmica.
❓ PERGUNTA PARA A TURMA: Após 1 min: "Quem acha que o crítico foi o mais crítico? E o sintetizador?"
⚠️ ERROS COMUNS: Turma subestima o sintetizador. Sem sintetizador, o revisor recebe contribuições divergentes sem integração — paralisia.
➡️ TRANSIÇÃO: "Vamos analisar criticamente o AI Scientist."

---

### Slide 32 — Estudo de Caso: AI Scientist — O Que Funcionou

**Título**: AI Scientist — O Que Funcionou
**Objetivo**: Analisar criticamente os sucessos do AI Scientist.
**Conteúdo**:
- Papers aceitos em workshop ICLR (peer review real)
- Custo baixo (~$15/paper) viabiliza exploração
- Pipeline estruturado garante reprodutibilidade
- Review automático identifica falhas antes da submissão
- **Lição**: estrutura > brilho individual

**Diagrama**: Checklist de sucessos em `etho-success`
**Animação**: Itens surgem com check verde
**Imagem**: Ícones de sucesso
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O AI Scientist tem sucessos reais. Papers passaram em peer review (workshop ICLR). O custo baixo viabiliza exploração em escala — você roda 100 papers por $1.500. O pipeline estruturado garante reprodutibilidade. E o review automático filtra falhas óbvias antes da submissão. A lição maior: estrutura vence brilho individual. Um pipeline bem desenhado com LLM mediano produz mais que um gênio sem estrutura.
⚠️ ERROS COMUNS: Alunos superestimam o sucesso. "Aceito em ICLR" soa bem, mas é WORKSHOP, não main conference. Seja preciso.
➡️ TRANSIÇÃO: "Agora o lado doloroso: o que falhou."

---

### Slide 33 — Estudo de Caso: O Que Falhou

**Título**: AI Scientist — O Que Falhou
**Objetivo**: Ser honesto sobre as limitações do AI Scientist.
**Conteúdo**:
- Experimentos às vezes não convergem (código com bugs)
- Papers com contribuição marginal (novidade baixa)
- Alucinação em revisão de literatura
- Difícil avaliar "qualidade científica" sem humano
- **Lição**: autonomia ≠ qualidade

**Diagrama**: Checklist de falhas em `etho-danger`
**Animação**: Itens surgem com X vermelho
**Imagem**: Ícones de falha
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O AI Scientist falha muito. Código com bugs que quebram experimentos. Papers com contribuição marginal (incremental sobre literatura). Alucinação em revisão de literatura (cita papers que não existem). E o problema fundamental: sem humano, "qualidade científica" é caixa preta. A lição: autonomia não implica qualidade. Um sistema autônomo que produz lixo plausível é PIOR que um sistema assistido — porque lixo plausível passa em peer review superficial.
⚠️ ERROS COMUNS: Alunos acham que "autonomia é o objetivo". Não — qualidade é o objetivo. Autonomia sem qualidade é poluição científica.
➡️ TRANSIÇÃO: "Vamos para a unidade mais sutil: emergência."

---

## SEÇÃO E — Emergência e Alinhamento (Slides 34-41 · 8 min)

---

### Slide 34 — [SEÇÃO] Emergência e Alinhamento

**Título**: Emergência e Alinhamento
**Objetivo**: Transição para a Unidade 4 — Emergência e alinhamento.
**Conteúdo**: Número "4" grande + "Emergência e Alinhamento"
**Diagrama**: Fundo `etho-primary`
**Animação**: Número 4 surge em `etho-accent`
**Imagem**: Pattern sutil de nós
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Esta é a unidade mais conceitual e mais importante para o futuro. Emergência é onde mora o potencial e o risco. Sem entender emergência, você não consegue alinhar sociedades.
➡️ TRANSIÇÃO: "O que é emergência?"

---

### Slide 35 — Comportamento Emergente: A Soma ≠ Partes

**Título**: Comportamento Emergente — A Soma ≠ Partes
**Objetivo**: Introduzir o conceito de emergência em sociedades de agentes.
**Conteúdo**:
- **Comportamento emergente**: padrões que surgem da interação, não do indivíduo
- A soma é diferente das partes
- **Exemplos positivos**: cooperação espontânea, formação de normas, divisão de trabalho
- **Exemplos negativos**: conluio, discriminação, corrida armamentista
- **Pergunta**: *Quando a soma é melhor? Quando é pior?*

**Diagrama**: Agentes individuais → interações → padrões emergentes
**Animação**: Fluxo de cima para baixo
**Imagem**: Sequência de 3 painéis
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Emergência é o conceito mais mal-entendido da aula. Não é "mágica". É o resultado de regras locais em larga escala. Cada agente segue suas regras. Mas a interação entre muitos agentes produz padrões que NINGUÉM programou. Pode ser bom: cooperação espontânea (Smallville), divisão de trabalho. Pode ser ruim: conluio (agentes combinam contra o objetivo), discriminação sistêmica, echo chamber, corrida armamentista. A pergunta-chave: quando a soma é melhor? Quando é pior? Não temos teoria completa — ainda é pesquisa aberta.
💡 ANALOGIA: Pense em engarrafamento. Cada motorista segue regras locais ("mantenha distância", "não bater"). Mas a interação produz um engarrafamento — ninguém programou. Engarrafamento é emergência. Não é mágica, é matemática.
⚠️ ERROS COMUNS: Alunos acham que emergência é "aleatoriedade". Não — é determinística dadas as regras. Mas é IMPREVISÍVEL para o designer em sistemas grandes.
➡️ TRANSIÇÃO: "Vamos ver o diagrama."

---

### Slide 36 — Diagrama: Emergência

**Título**: Emergência — Diagrama
**Objetivo**: Visualizar como comportamento emergente surge.
**Conteúdo**:
- Agentes individuais seguem regras locais
- Interações locais produzem padrões emergentes
- Padrões geram propriedades coletivas: coordenação, polarização, especialização, echo chamber

**Diagrama**: `12-Diagrams/ETHAGT16/emergence.mmd`
**Animação**: Fluxo de cima para baixo
**Imagem**: Diagrama `.mmd` renderizado
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: O diagrama mostra o fluxo. Agentes individuais (com regras locais) interagem. As interações produzem padrões emergentes (não programados). Os padrões geram propriedades coletivas: coordenação, polarização, especialização, echo chamber. Note que as propriedades não existem nos agentes — só na coletividade.
➡️ TRANSIÇÃO: "Vamos distinguir emergência boa de ruim."

---

### Slide 37 — Emergência Desejada vs Indesejada

**Título**: Emergência Desejada vs Indesejada
**Objetivo**: Distinguir emergência benéfica de emergência perigosa.
**Conteúdo**:
- **Desejada**: cooperação espontânea, divisão de trabalho, inovação
- **Indesejada**: conluio (agentes combinam contra objetivo), discriminação, echo chamber, corrida armamentista
- **Fator-chave**: alinhamento de valores + supervisão
- Sem supervisão: emergência tende ao extremo

**Diagrama**: Duas colunas: verde (desejada) vs vermelho (indesejada) (D16)
**Animação**: Colunas aparecem uma a uma
**Imagem**: Tabela 2 colunas colorida
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Nem toda emergência é boa. Conluio é quando agentes combinam para maximizar retorno individual em detrimento do objetivo coletivo. Discriminação é quando vieses individuais se amplificam na interação. Echo chamber é quando opiniões convergem para extremos sem oposição. Corrida armamentista é quando agentes competem e escalam além do necessário. O fator-chave: alinhamento de valores + supervisão. Sem supervisão, emergência tende ao extremo.
💡 ANALOGIA: Pense numa sala de aula sem professor. Alguns alunos colaboram (emergência boa), mas também surgem bullies (emergência ruim). A estrutura (professor) contém os extremos.
⚠️ ERROS COMUNS: Alunos acham que "mais agentes = mais emergência boa". Não — mais agentes sem alinhamento = mais emergência EXTREMA. Pode ser cooperação extrema ou conluio extremo.
➡️ TRANSIÇÃO: "Como alinhamos sociedades?"

---

### Slide 38 — Alinhamento de Valores em Populações

**Título**: Alinhamento de Valores em Populações
**Objetivo**: Explicar como alinhar sociedades de agentes.
**Conteúdo**:
- Alinhamento individual ≠ alinhamento coletivo
- **Constitution** para sociedades: regras que governam todas as interações
- Votação e consenso como mecanismos
- **Tensão**: normas rígidas (seguras) vs flexíveis (adaptáveis)
- Referência: Constitutional AI aplicado a sociedades

**Diagrama**: Camadas: Valores individuais → Normas sociais → Constitution (D17)
**Animação**: Camadas surgem de baixo para cima
**Imagem**: Pirâmide de 3 níveis
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Aqui está o insight mais profundo da aula. Alinhar cada agente individualmente NÃO alinha a sociedade. A interação produz propriedades coletivas que violam valores individuais. Por exemplo: cada agente é "educado", mas a sociedade polariza. A solução é constitucional: uma camada de regras globais que governam todas as interações. Constitutional AI (Anthropic) é a referência. Mas há tensão: normas rígidas são seguras mas pouco adaptáveis; flexíveis são adaptáveis mas arriscadas.
💡 ANALOGIA: É como uma constituição política. Cada cidadão segue a lei, mas a constituição garante que a interação não produza tirania. Sem constituição, mesmo cidadãos bons podem produzir sociedade injusta.
⚠️ ERROS COMUNS: Alunos acham que "alinhamento individual resolve". Não — já vimos que alinhamento individual não garante coletivo. Constituição é necessária.
➡️ TRANSIÇÃO: "Como medimos isso?"

---

### Slide 39 — Avaliação de Emergência

**Título**: Avaliação de Emergência
**Objetivo**: Apresentar métricas para avaliar comportamento emergente.
**Conteúdo**:
- **Métricas de divergência**: quão longe a sociedade está do comportamento esperado
- **Métricas de surpresa**: comportamento não previsto pelos designers
- **Métricas de convergência**: a sociedade estabiliza ou oscila?
- Sem métricas: emergência é caixa preta
- Em produção: monitoramento contínuo de emergência

**Diagrama**: Dashboard com 3 métricas
**Animação**: Métricas surgem em sequência
**Imagem**: Dashboard estilo Grafana (placeholder)
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Três famílias de métricas. Divergência: o comportamento coletivo está perto do que você esperava? Surpresa: aconteceu algo que você não previu? Convergência: a sociedade estabiliza ou oscila indefinidamente? Sem essas métricas, emergência é caixa preta — você não sabe o que está acontecendo. Em produção (quando tivermos sociedades em produção), será necessário monitoramento contínuo.
💡 ANALOGIA: É como monitorar um mercado financeiro. Você tem indicadores (volatilidade, volume, correlação). Sem indicadores, é só ruído. Em sociedades de agentes, ainda não temos indicadores maduros.
⚠️ ERROS COMUNS: Alunos acham que "logs resolvem". Não — logs geram dados, não insights. Precisa de métricas agregadas que capturem propriedades coletivas.
➡️ TRANSIÇÃO: "Vamos refletir."

---

### Slide 40 — Pergunta: Quando Emergência é Indesejada?

**Título**: Quando Emergência é Indesejada?
**Objetivo**: Provocar reflexão sobre limites da autonomia.
**Conteúdo**:
- "Quando comportamento emergente é indesejado?"
- 3 cenários rápidos: em qual você interviria?
- Discussão aberta (1 min)

**Diagrama**: Caixa de discussão em `etho-warning`
**Animação**: Caixa surge
**Imagem**: Ícone de alerta
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: A pergunta é prática. Quando você interviria? Resposta honesta: depende das stakes. Em simulação de pesquisa, baixas stakes, deixa rolar. Em simulação de política pública, altas stakes, intervém. A regra: stakes + irreversibilidade. Quanto mais altas e irreversíveis as consequências, mais cedo você intervém.
❓ PERGUNTA PARA A TURMA: "Quem intervém sempre? Quem nunca intervém?"
➡️ TRANSIÇÃO: "Vamos praticar."

---

### Slide 41 — Exercício: Detectando Emergência Indesejada

**Título**: Exercício — Detectando Emergência Indesejada
**Objetivo**: Praticar identificação de emergência problemática.
**Conteúdo**:
- Trace de uma sociedade de agentes (5 agentes, 10 interações)
- Em duplas: identificar padrão emergente indesejado
- Propor 2 correções (norma, supervisão, HITL)
- 1 min discussão

**Diagrama**: Trace de interações com padrão destacado
**Animação**: Trace surge, padrão destacado em vermelho
**Imagem**: Trace estilizado
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: 1 minuto em duplas. O trace mostra uma sociedade que para de produzir — todos concordam que "nada é confiável". Esse é o padrão: echo chamber de crítica. Ninguém foi programado para paralisar, mas emergiu. As correções: norma ("crítica precisa vir com alternativa"), HITL (intervir após 5 rodadas), peso (limitar veto do crítico).
❓ PERGUNTA PARA A TURMA: Após 1 min: "Qual correção vocês propuseram?"
⚠️ ERROS COMUNS: Duplas propõem "remover o crítico". Errado — sem crítico, qualidade cai. A correção é ajustar o PODER do crítico, não removê-lo.
➡️ TRANSIÇÃO: "Última unidade: fronteira e ética."

---

## SEÇÃO F — Fechamento (Slides 42-50 · 10 min)

---

### Slide 42 — [SEÇÃO] Fronteira e Ética

**Título**: Fronteira e Ética
**Objetivo**: Transição para a Unidade 5 — Fronteira e ética.
**Conteúdo**: Número "5" grande + "Fronteira e Ética"
**Diagrama**: Fundo `etho-primary`
**Animação**: Número 5 surge em `etho-accent`
**Imagem**: Pattern sutil de nós
**Tempo**: 0.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Última unidade. Vamos mapear onde a pesquisa está, quais as questões éticas, e o que NÃO fazer.
➡️ TRANSIÇÃO: "Onde estamos?"

---

### Slide 43 — Onde a Pesquisa Está Agora

**Título**: Onde a Pesquisa Está Agora
**Objetivo**: Mapear o estado da arte em sociedades de agentes.
**Conteúdo**:
- **AI Scientist** (Sakana, 2024): pesquisa ML automatizada
- **AlphaEvolve** (DeepMind, 2024): evolução de algoritmos
- **AutoGen research**: framework multi-agente para pesquisa
- **Swarm research**: coordenação de grandes populações
- **Tendência**: de 1 agente → times → sociedades autônomas

**Diagrama**: Mapa da fronteira de pesquisa (D18)
**Animação**: Ramos surgem do centro
**Imagem**: Mind map estilizado
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Quatro frentes. AI Scientist: automação de pesquisa ML. AlphaEvolve: evolução de algoritmos. AutoGen: framework para times de pesquisa. Swarm research: coordenação de centenas de agentes. A tendência macro: 1 agente → times → sociedades autônomas. Estamos na transição de times para sociedades.
⚠️ ERROS COMUNS: Alunos acham que "sociedades autônomas já existem". Não — existem protótipos. Em produção, ainda é experimental.
➡️ TRANSIÇÃO: "Com essa fronteira vêm questões éticas."

---

### Slide 44 — Questões Éticas: Autoria e Responsible AI

**Título**: Questões Éticas
**Objetivo**: Apresentar dilemas éticos da pesquisa autônoma.
**Conteúdo**:
- **Automação de pesquisa**: papers gerados por IA — autoria? revisão?
- **Responsible AI**: viés amplificado em sociedades
- **Autopropagação**: agente que cria cópias de si mesmo
- **Auto-modificação**: agente que altera seu próprio código
- **Discussão**: *Onde você traça a linha entre agente útil e perigoso?*

**Diagrama**: 4 ícones de dilema ético
**Animação**: Ícones surgem um a um
**Imagem**: Ícones em `etho-warning`
**Tempo**: 1.5 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Quatro dilemas. Autoria: quem é autor de um paper de IA? A IA? O designer do sistema? Ninguém? A comunidade ainda não decidiu. Responsible AI: vieses dos LLMs se amplificam em sociedades — um viés pequeno vira discriminação sistêmica. Autopropagação: um agente que cria cópias de si mesmo pode consumir recursos indefinidamente. Auto-modificação: um agente que altera seu próprio código pode se tornar algo não-planejado. Esses dois últimos são os mais perigosos.
💡 ANALOGIA: Autopropagação é como um vírus de computador que se replica. Auto-modificação é como uma mutação cancerígena — a célula muda seu próprio código e perde controle.
❓ PERGUNTA PARA A TURMA: "Onde você traça a linha entre agente útil e perigoso?"
⚠️ ERROS COMUNS: Alunos acham que "isso é problema dos outros". Não — vocês vão construir esses sistemas. Vocês são a linha de frente.
➡️ TRANSIÇÃO: "Vamos ser explícitos: o que NÃO fazer."

---

### Slide 45 — O Que NÃO Fazer

**Título**: O Que NÃO Fazer
**Objetivo**: Checklist de práticas perigosas em sistemas autônomos.
**Conteúdo**:
- Sistemas sem supervisão humana (sem HITL)
- Auto-modificação irrestrita
- Deploy sem avaliação de risco
- Autopropagação sem limites
- Sociedades sem constitution ou normas
- Sem métricas de emergência

**Diagrama**: Checklist vermelho em `etho-danger`
**Animação**: Itens surgem com X vermelho
**Imagem**: Lista de proibições
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Seis proibições. Sem HITL em alta stakes. Auto-modificação irrestrita (agente altera código sem aprovação). Deploy sem avaliação de risco. Autopropagação sem limites (agente cria cópias indefinidamente). Sociedades sem constitution. Sem métricas de emergência (caixa preta). Cada uma dessas é um caminho para desastre. Memorizem essa lista.
⚠️ ERROS COMUNS: Alunos acham que "isso é exagero". Não — cada item corresponde a um incidente real documentado. Autopropagação irrestrita já consumiu orçamentos inteiros em experimentos.
➡️ TRANSIÇÃO: "Vamos praticar avaliação crítica."

---

### Slide 46 — Exercício: Avaliar Qualidade de um AI Scientist

**Título**: Exercício — Avaliar AI Scientist
**Objetivo**: Praticar avaliação crítica de pesquisa autônoma.
**Conteúdo**:
- Cenário: AI Scientist gerou paper sobre "otimização de prompts"
- Em grupos: definir 3 critérios para avaliar a qualidade científica
- Exemplos: reprodutibilidade, novidade, corretude metodológica
- 2 min discussão, 1 min compartilhar critérios

**Diagrama**: Caixa de discussão com paper fake
**Animação**: Caixa surge
**Imagem**: Mockup de paper fake (placeholder)
**Tempo**: 2 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: 2 minutos em grupos de 3. Definam 3 critérios para avaliar a qualidade científica de um paper gerado por IA. O ponto é: sem humano revisando, você precisa de critérios OPERACIONAIS — mensuráveis, não subjetivos. "Reprodutibilidade" (dá para reproduzir?), "novidade" (está além da literatura?), "corretude metodológica" (o desenho experimental é válido?).
❓ PERGUNTA PARA A TURMA: Após 2 min: "Qual grupo tem critérios operacionais?"
⚠️ ERROS COMUNS: Grupos propõem "qualidade da escrita". Errado — escrita pode ser boa mas conteúdo errado. Critério precisa focar no CONTEÚDO.
➡️ TRANSIÇÃO: "Vamos resumir."

---

### Slide 47 — Resumo da Aula

**Título**: Resumo da Aula
**Objetivo**: Sintetizar os pontos-chave.
**Conteúdo**:
- Sociedades de agentes = papéis + normas + reputação + emergência
- Smallville = caso canônico de simulação social
- AI Scientist = fronteira de pesquisa autônoma
- Emergência pode ser desejada (cooperação) ou indesejada (conluio)
- Alinhamento coletivo ≠ alinhamento individual
- Ética: supervisão, avaliação de risco, responsible AI

**Diagrama**: 6 ícones com os pontos-chave
**Animação**: Ícones surgem em sequência
**Imagem**: Grid 2x3 de ícones
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Seis pontos. Sociedades = papéis + normas + reputação + emergência. Smallville = simulação social canônica. AI Scientist = pesquisa autônoma canônica. Emergência pode ser boa ou ruim. Alinhamento coletivo é diferente de individual. Ética é não-negociável. Memorizem esses seis.
➡️ TRANSIÇÃO: "Quiz rápido."

---

### Slide 48 — Quiz: 3 Perguntas Rápidas

**Título**: Quiz — 3 Perguntas
**Objetivo**: Verificar compreensão.
**Conteúdo**:
- P1: "Qual pipeline o AI Scientist (Sakana) automatiza?"
  - A) Apenas escrita de papers
  - B) Ideação → literatura → código → experimento → paper → review (resposta B)
  - C) Apenas revisão de literatura
  - D) Apenas análise de dados
- P2: "O que é comportamento emergente?"
  - A) Comportamento programado explicitamente
  - B) Padrões que surgem da interação, não do indivíduo (resposta B)
  - C) Erro aleatório do modelo
  - D) Comportamento do agente mais influente
- P3: "V/F: Sociedades de agentes sempre convergem."
  - Falso — sociedades podem polarizar, oscilar ou colapsar

**Diagrama**: 3 caixas de quiz
**Animação**: Perguntas surgem uma a uma
**Imagem**: Ícones de quiz
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Individual, sem consulta, 1 minuto. O critério é ≥2 acertos = compreensão básica. A maioria acerta P1 e P2. A maioria erra P3 (acha que "sempre converge"). Use P3 como gancho: convergência depende de normas, reputação, alinhamento. Sem isso, polariza ou colapsa.
➡️ TRANSIÇÃO: "Para onde isso leva?"

---

### Slide 49 — Conexão com Capstone e Referências

**Título**: Capstone e Referências
**Objetivo**: Conectar ETHAGT16 com o Capstone e indicar leitura.
**Conteúdo**:
- **ETHAGT90 — Capstone**: projeto final integrador
- O espectro completo: de Augmented LLM (ETHAGT01) a Sociedades de Agentes (ETHAGT16)
- **Leitura obrigatória**:
  - Park et al. *Generative Agents* (arXiv:2304.03442)
  - Lu et al. *The AI Scientist* (arXiv:2408.06292)
  - Chen et al. *AgentVerse* (arXiv:2308.10848)
- **Complementar**: DeepMind *AlphaEvolve* (2024)
- **Convite**: *Onde vocês querem levar isso? Pesquisa, produto, impacto social?*

**Diagrama**: Mapa da especialização ETHAGT01 → ETHAGT90 (D19)
**Animação**: Mapa cresce da esquerda para direita
**Imagem**: Timeline da especialização
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: ETHAGT90 — Capstone — é onde vocês integram tudo. O Projeto deste módulo (sistema de pesquisa autônoma) é o esboço do Capstone. As três leituras canônicas são Park et al. (Smallville), Lu et al. (AI Scientist), Chen et al. (AgentVerse). Leiam. E a pergunta que fecha a aula: onde vocês querem levar isso? Pesquisa acadêmica? Produto comercial? Impacto social? A especialização acabou — agora começa o trabalho de vocês.
❓ PERGUNTA PARA A TURMA: "Onde vocês querem levar isso?"
➡️ TRANSIÇÃO: "Q&A."

---

### Slide 50 — Q&A / Encerramento

**Título**: Q&A / Encerramento
**Objetivo**: Abrir para perguntas e encerrar.
**Conteúdo**:
- "Perguntas?"
- Contato do professor
- "Próximo módulo: ETHAGT90 — Capstone"
- "Vocês estão na fronteira. Agora é hora de construir."

**Diagrama**: Logo Etho + fundo `etho-dark`
**Animação**: Fade in
**Imagem**: Logo Etho centralizado
**Tempo**: 1 min

**Notas do Professor**:
📖 EXPLICAÇÃO COMPLETA: Perguntas abertas. Se ninguém perguntar, eu faço a pergunta inversa: "Qual parte foi menos clara?" Depois fecho com a mensagem: vocês estão na fronteira. Tudo que estudaram converge no Capstone. Agora é hora de construir.
⚠️ ERROS COMUNS: Acabar a aula sem fechar o arco. Eu sempre recordo o gancho do Slide 5: "O que acontece quando 100 agentes interagem sem supervisão?" A resposta honesta: ainda não sabemos totalmente. É isso que vocês vão descobrir.
