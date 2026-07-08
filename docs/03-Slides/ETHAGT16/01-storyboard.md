# ETHAGT16 — Sociedades de Agentes & Autonomous Research Systems
## Storyboard da Apresentação

> **Universidade Etho · Especialização em Programação Agêntica**
> Fase D — Fronteira · 15 h
> Storyboard v1.0 · Julho 2026

---

## Metadados da Apresentação

| Campo | Valor |
|---|---|
| Código | ETHAGT16 |
| Título | Sociedades de Agentes & Autonomous Research Systems |
| Duração estimada | 50 min (2 blocos de 25 min) |
| Total de slides | 50 |
| Público | Arquitetos, Engenheiros de IA, Cientistas de Dados, Pesquisadores, Tech Leads |
| Pré-requisitos | ETHAGT15 |
| Competências | C1 (A), C2 (A), C3 (B), C4 (A), C5 (I), C6 (I) |

---

## Mapa Visual da Apresentação

```
BLOCO 1 (25 min)                              BLOCO 2 (25 min)
┌──────────────────────────────┐              ┌──────────────────────────────┐
│ SEÇÃO A — Abertura (6 min)   │              │ SEÇÃO D — Research Sys (12m) │
│  Capa · Objetivos · Agenda   │              │  Pipeline · AI Scientist     │
│  Motivação · Contexto        │              │  AlphaEvolve · DEMO          │
├──────────────────────────────┤              ├──────────────────────────────┤
│ SEÇÃO B — Sociedades (8 min) │              │ SEÇÃO E — Emergência (8 min) │
│  Papéis · Normas · Reputação │              │  Comportamento emergente     │
│  Modelos · Diagrama · Exerc. │              │  Alinhamento · Avaliação     │
├──────────────────────────────┤              ├──────────────────────────────┤
│ SEÇÃO C — Simulações (6 min) │              │ SEÇÃO F — Fechamento (10 min)│
│  Smallville · Casos de uso   │              │  Ética · Exercício · Resumo  │
│  Limites · Exercício         │              │  Quiz · Capstone · Q&A       │
└──────────────────────────────┘              └──────────────────────────────┘
```

---

## Storyboard Detalhado

### SEÇÃO A — Abertura (Slides 1-6 · 6 min)

---

#### Slide 1 — Capa
- **Tipo**: Capa
- **Objetivo**: Identificar a aula, professor e contexto
- **Conteúdo**:
  - ETHAGT16 — Sociedades de Agentes & Autonomous Research Systems
  - Universidade Etho · Especialização em Programação Agêntica
  - Fase D — Fronteira
  - Professor · Data
  - Último módulo antes do Capstone (ETHAGT90)
- **Diagrama**: Logo Etho + imagem de fundo abstrata (rede de agentes interconectados)
- **Animação**: Fade in do título
- **Tempo**: 1 min

---

#### Slide 2 — Objetivos do Módulo
- **Tipo**: Conteúdo
- **Objetivo**: Deixar claro o que o aluno deve conseguir fazer ao final
- **Conteúdo**:
  - Objetivo geral: Atingir a fronteira do estado da arte — sociedades de agentes, simulações sociais, sistemas de pesquisa autônoma
  - 5 objetivos específicos (1 linha cada):
    1. Modelar sociedades de agentes (papéis, instituições, normas)
    2. Aplicar simulações multi-agente (Smallville-like)
    3. Construir um sistema de pesquisa autônoma
    4. Discutir emergência, convergência e alinhamento
    5. Conhecer a fronteira de pesquisa (AI Scientist, AlphaEvolve)
  - Ponte para o Capstone: esboço do projeto final
- **Diagrama**: Ícones representando cada objetivo
- **Animação**: Aparecer objetivos um a um (on click)
- **Tempo**: 1.5 min

---

#### Slide 3 — Competências Desenvolvidas
- **Tipo**: Conteúdo
- **Objetivo**: Conectar a aula ao Framework Etho de competências
- **Conteúdo**:
  - Tabela: 6 competências com nível
  - C1 Programação Agêntica → A
  - C2 Multi-Agent Systems → A
  - C3 MCP & Tool Use → B
  - C4 Agent Memory → A
  - C5 AgentOps & Avaliação → I
  - C6 Agent Security → I
  - Badge visual por competência
- **Diagrama**: Radar chart dos 6 pilares
- **Animação**: Radar aparece com wipe
- **Tempo**: 0.5 min

---

#### Slide 4 — Agenda
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar o roteiro da aula com tempos
- **Conteúdo**:
  - Bloco 1: Abertura → Sociedades de Agentes → Simulações Sociais
  - Bloco 2: Research Systems → Emergência → Fechamento
  - Tempos estimados por seção
- **Diagrama**: Timeline horizontal com 6 seções
- **Animação**: Timeline cresce da esquerda para direita
- **Tempo**: 0.5 min

---

#### Slide 5 — Motivação: O Problema do Agente Isolado
- **Tipo**: Conteúdo
- **Objetivo**: Criar tensão — agentes isolados não escalam para problemas complexos
- **Conteúdo**:
  - Agente isolado: resolve uma tarefa bem
  - Sociedade de agentes: pode resolver problemas que nenhum agente resolve sozinho
  - Exemplo: Generative Agents (Stanford Smallville) — 25 agentes simulam vida social, organizam festa sozinhos
  - A fronteira: AI Scientist (Sakana) — agente que conduz pesquisa científica do início ao fim
  - Pergunta: *O que acontece quando 100 agentes interagem sem supervisão humana?*
- **Diagrama**: Crescimento visual: 1 agente (ponto) → 5 agentes (grupo) → 25 agentes (sociedade) → 100 agentes (emergência)
- **Animação**: Pontos surgem e se conectam em rede
- **Tempo**: 1.5 min

---

#### Slide 6 — Contexto: Por Que Sociedades Agora
- **Tipo**: Conteúdo
- **Objetivo**: Explicar a confluência histórica que tornou sociedades de agentes viáveis
- **Conteúdo**:
  - Linha do tempo: 2022 (ReAct) → 2023 (tool calling, multi-agent frameworks) → 2023 (Generative Agents, Smallville) → 2024 (AI Scientist, AlphaEvolve)
  - Confluência: reasoning + tools + memory + context window + cost reduction
  - Smallville (abr/2023, arXiv:2304.03442) e AI Scientist (ago/2024, arXiv:2408.06292) como marcos
  - Próxima fronteira: sociedades autônomas
- **Diagrama**: Timeline horizontal com marcos
- **Animação**: Marcos aparecem sequencialmente
- **Tempo**: 1 min

---

### SEÇÃO B — Sociedades de Agentes (Slides 7-15 · 8 min)

---

#### Slide 7 — [SEÇÃO] Sociedades de Agentes
- **Tipo**: Seção
- **Objetivo**: Transição para Unidade 1 — Sociedades de agentes
- **Conteúdo**: Número "1" grande + "Sociedades de Agentes"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 8 — Do Agente Individual à Sociedade
- **Tipo**: Comparação
- **Objetivo**: Mostrar a evolução de 1 agente → sociedade
- **Conteúdo**:
  - Nível 0: Agente individual (LLM + tools + memory)
  - Nível 1: Pequeno grupo (2-5 agentes, colaboração direta)
  - Nível 2: Instituição (papéis, normas, hierarquia)
  - Nível 3: Sociedade (25+ agentes, emergência, normas emergentes)
  - Cada nível adiciona: complexidade, potencial e risco
- **Diagrama**: Escada de 4 níveis
- **Animação**: Níveis aparecem de baixo para cima
- **Tempo**: 1 min

---

#### Slide 9 — Papéis em Sociedades de Agentes
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar papéis canônicos em sociedades de agentes
- **Conteúdo**:
  - Pesquisador: explora, levanta informações
  - Crítico: identifica falhas, questiona premissas
  - Sintetizador: integra contribuições divergentes
  - Revisor: valida qualidade e coerência
  - Editor: finaliza, formata, publica
  - Análogo a um time de pesquisa humano
  - Papéis podem ser dinâmicos (agentes trocam de papel)
- **Diagrama**: 5 ícones de papéis em círculo
- **Animação**: Papéis aparecem um a um
- **Tempo**: 1 min

---

#### Slide 10 — Normas e Instituições
- **Tipo**: Conteúdo
- **Objetivo**: Explicar como sociedades de agentes estabelecem regras
- **Conteúdo**:
  - Normas: regras compartilhadas (explícitas ou emergentes)
  - Instituições: estruturas que mantêm normas (ex: revisão por pares)
  - Análogo a instituições humanas (tribunais, mercados, universidades)
  - Em sociedades de agentes: constituição, votação, reputação
  - Tensão: normas explícitas (controláveis) vs emergentes (adaptáveis)
- **Diagrama**: Estrutura hierárquica: Sociedade → Instituições → Normas
- **Tempo**: 1 min

---

#### Slide 11 — Reputação e Confiança
- **Tipo**: Conteúdo
- **Objetivo**: Explicar como agentes decidem em quem confiar
- **Conteúdo**:
  - Reputação: histórico de interações de um agente
  - Confiança: função da reputação + contexto
  - Em sociedades: agentes podem "votar" em quem confiar
  - Análogo a PageRank: confiança propagada pela rede
  - Sem reputação: sociedade colapsa (free-riders, manipulação)
- **Diagrama**: Grafo de agentes com pesos de confiança
- **Tempo**: 1 min

---

#### Slide 12 — Modelos: Generative Agents, AgentVerse, ChatArena
- **Tipo**: Comparação
- **Objetivo**: Apresentar os 3 modelos canônicos de sociedade
- **Conteúdo**:
  - Generative Agents (Stanford): 25 agentes, Smallville, vida social simulada
  - AgentVerse (arXiv:2308.10848): framework multi-agente, papéis flexíveis, tarefas colaborativas
  - ChatArena: ambientes de jogo/diálogo multi-agente
  - Cada modelo resolve um problema diferente
- **Diagrama**: 3 colunas comparativas
- **Animação**: Colunas aparecem uma a uma
- **Tempo**: 1 min

---

#### Slide 13 — Diagrama: Arquitetura de uma Sociedade
- **Tipo**: Diagrama
- **Objetivo**: Visualizar a arquitetura de uma sociedade de agentes
- **Conteúdo**:
  - Ambiente compartilhado (sandbox)
  - Agentes com papéis (pesquisador, crítico, sintetizador, revisor, editor)
  - Normas governando a sociedade
  - Saída: comportamento emergente
- **Diagrama**: `12-Diagrams/ETHAGT16/society.mmd`
- **Animação**: Componentes surgem do centro para fora
- **Tempo**: 1 min

---

#### Slide 14 — Comparação: Grupo vs Instituição vs Sociedade
- **Tipo**: Comparação
- **Objetivo**: Sistematizar a distinção entre níveis de organização
- **Conteúdo**:
  - Grupo: colaboração ad-hoc, sem normas fixas
  - Instituição: papéis fixos, normas explícitas, hierarquia
  - Sociedade: normas emergentes, reputação, comportamento não programado
  - Trade-off: controle (grupo) vs adaptabilidade (sociedade)
- **Diagrama**: 3 colunas com eixos: controle, adaptabilidade, previsibilidade, risco
- **Tempo**: 0.5 min

---

#### Slide 15 — Exercício Rápido: Definindo Papéis
- **Tipo**: Exercício
- **Objetivo**: Praticar design de papéis para um problema
- **Conteúdo**:
  - Cenário: "Simular um comitê editorial de revista científica"
  - Em duplas: definir 5 papéis e suas responsabilidades
  - Qual norma deve ser compartilhada?
  - Como reputação é acumulada?
  - 1 min discussão, share rápido
- **Diagrama**: Caixa de discussão
- **Tempo**: 1 min

---

### SEÇÃO C — Simulações Sociais (Slides 16-22 · 6 min)

---

#### Slide 16 — [SEÇÃO] Simulações Sociais
- **Tipo**: Seção
- **Objetivo**: Transição para Unidade 2 — Simulações sociais
- **Conteúdo**: Número "2" grande + "Simulações Sociais"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 17 — Sandbox Social: Smallville
- **Tipo**: Diagrama
- **Objetivo**: Apresentar Smallville como caso canônico de simulação social
- **Conteúdo**:
  - Smallville: mundo virtual com 25 agentes
  - Cada agente: perfil, rotina, memória, objetivos
  - Ambiente: mapas, locais, recursos compartilhados
  - Resultado: agentes organizam festa de Valentine's Day sozinhos
  - Fonte: Park et al., arXiv:2304.03442
- **Diagrama**: Mapa de Smallville com agentes em locais
- **Tempo**: 1.5 min

---

#### Slide 18 — Como Smallville Funciona
- **Tipo**: Conteúdo
- **Objetivo**: Explicar a arquitetura técnica de Smallville
- **Conteúdo**:
  - Memory stream: log cronológico de experiências
  - Retrieval: relevância + recência + importância
  - Reflection: síntese de memórias em insights de alto nível
  - Planning: planos diários baseados em rotina + objetivos
  - Action: geração de ação baseada em contexto + reflexão
- **Diagrama**: Pipeline: Memory → Retrieval → Reflection → Planning → Action
- **Tempo**: 1 min

---

#### Slide 19 — Casos de Uso: Policy, Mercado, Opinião
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar aplicações práticas de simulações sociais
- **Conteúdo**:
  - Policy simulation: simular impacto de lei (imposto, subsídio)
  - Mercado: agentes compram/vendem, formação de preços
  - Opinião pública: difusão de ideias, polarização
  - Vantagem: testar hipóteses sem custo social
  - Mas: validação é difícil (não há ground truth)
- **Diagrama**: 3 ícones de aplicação
- **Tempo**: 1 min

---

#### Slide 20 — Limites e Críticas
- **Tipo**: Conteúdo
- **Objetivo**: Ser honesto sobre as limitações das simulações sociais
- **Conteúdo**:
  - Agentes são muito coerentes vs humanos (menos ruído)
  - Vieses dos LLMs se amplificam em sociedade
  - Custo computacional (25+ agentes × N interações)
  - Difícil validação (não há ground truth)
  - Pergunta: *Uma simulação social com LLMs pode prever comportamento humano real?*
- **Diagrama**: 4 ícones de limitação
- **Tempo**: 1 min

---

#### Slide 21 — Pergunta: Simulação = Predição?
- **Tipo**: Exercício
- **Objetivo**: Provocar reflexão sobre o valor preditivo de simulações
- **Conteúdo**:
  - "Uma simulação social com LLMs pode prever comportamento humano real?"
  - V/F: "Sociedades de agentes sempre convergem."
  - Discussão aberta rápida (1 min)
- **Diagrama**: Caixa de discussão
- **Tempo**: 0.5 min

---

#### Slide 22 — Exercício Rápido: Cenário de Simulação
- **Tipo**: Exercício
- **Objetivo**: Praticar design de simulação social
- **Conteúdo**:
  - Cenário: "Simular o impacto de uma política de home office em uma empresa"
  - Em duplas: definir 3 tipos de agentes, 2 normas, 1 métrica
  - Qual resultado você espera? Qual pode surpreender?
  - 1 min discussão
- **Diagrama**: Caixa de discussão
- **Tempo**: 0.5 min

---

### SEÇÃO D — Autonomous Research Systems (Slides 23-33 · 12 min)

---

#### Slide 23 — [SEÇÃO] Autonomous Research Systems
- **Tipo**: Seção
- **Objetivo**: Transição para Unidade 3 — Autonomous Research Systems
- **Conteúdo**: Número "3" grande + "Autonomous Research Systems"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 24 — Pipeline de Pesquisa Autônoma
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar o pipeline canônico de pesquisa autônoma
- **Conteúdo**:
  - Pipeline: pergunta → revisão de literatura → hipótese → experimento → análise → relatório
  - Cada etapa pode ser um agente diferente
  - Ou um agente que executa todas as etapas
  - O desafio: manter coerência entre etapas
  - HITL em pontos críticos
- **Diagrama**: Fluxo horizontal de 7 etapas
- **Tempo**: 1 min

---

#### Slide 25 — Diagrama: Research Pipeline
- **Tipo**: Diagrama
- **Objetivo**: Visualizar o pipeline completo de pesquisa autônoma
- **Conteúdo**:
  - Fluxo: pergunta → revisão → hipótese → experimento → execução → análise → escrita
  - HITL no fim: aprovar ou revisar
  - Loop de revisão possível
- **Diagrama**: `12-Diagrams/ETHAGT16/research-pipeline.mmd`
- **Animação**: Etapas aparecem sequencialmente da esquerda para direita
- **Tempo**: 1 min

---

#### Slide 26 — Sakana AI Scientist: Pesquisa ML de Ponta a Ponta
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar o AI Scientist como caso canônico de pesquisa autônoma
- **Conteúdo**:
  - Sakana AI: pesquisa ML do início ao fim
  - Etapas: ideação → literatura → código → experimento → paper
  - Custo: ~$15 por paper
  - Resultado: papers aceitos em workshop ICLR
  - Fonte: Lu et al., arXiv:2408.06292
- **Diagrama**: Fluxo do AI Scientist em 5 etapas
- **Tempo**: 1.5 min

---

#### Slide 27 — Como o AI Scientist Funciona
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar a arquitetura técnica do AI Scientist
- **Conteúdo**:
  - Stage 1: Ideação (LLM gera ideias de pesquisa)
  - Stage 2: Experimentação (LLM escreve código, roda experimentos)
  - Stage 3: Paper writing (LLM escreve paper em LaTeX)
  - Stage 4: Review (LLM revisa como reviewer)
  - Cada stage usa templates e prompts específicos
  - O agente decide: continuar, refinar ou abandonar
- **Diagrama**: Pipeline em 4 stages com feedback loop
- **Tempo**: 1.5 min

---

#### Slide 28 — DeepMind AlphaEvolve: Evolução de Algoritmos
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar AlphaEvolve como fronteira de pesquisa autônoma
- **Conteúdo**:
  - AlphaEvolve: evolução de algoritmos via LLM + avaliação automática
  - LLM propõe mutações em código → avaliador testa → mantém melhores
  - Resultado: descobriu novo algoritmo de multiplicação de matrizes
  - Lição: evolução + avaliação automática = descoberta
- **Diagrama**: Loop evolutivo: LLM → mutação → avaliação → seleção → LLM
- **Tempo**: 1 min

---

#### Slide 29 — Multi-Agent Research Labs
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar a evolução para times de agentes especializados
- **Conteúdo**:
  - Em vez de 1 agente: time de agentes especializados
  - Pesquisador, programador, revisor, escritor
  - Vantagem: especialização + divisão de trabalho
  - Desafio: coordenação, comunicação, overhead
  - Exemplo: AgentVerse colaborativo
- **Diagrama**: Time de 4 agentes com canal de comunicação
- **Tempo**: 1 min

---

#### Slide 30 — DEMO: Mini Sociedade 5 Agentes
- **Tipo**: Código
- **Objetivo**: Demo ao vivo — 5 agentes produzindo um relatório
- **Conteúdo**:
  - 5 agentes: pesquisador, crítico, sintetizador, revisor, editor
  - Tarefa: produzir relatório sobre "impacto de agentes na educação"
  - Mostrar: cada agente contribui, debate, revisa, produz versão final
  - Observar: divergências, consenso, qualidade do resultado
  - Referência: `05-Labs/ETHAGT16/Lab1-Mini-Sociedade`
- **Diagrama**: Code block + terminal side-by-side
- **Animação**: Highlight de linhas chave durante execução
- **Tempo**: 3 min

---

#### Slide 31 — Pergunta da DEMO
- **Tipo**: Exercício
- **Objetivo**: Engajar a turma com uma pergunta sobre a demo
- **Conteúdo**:
  - "Qual papel foi mais crítico para o resultado?"
  - "O que aconteceria se removêssemos o crítico?"
  - "E se o editor tivesse poder de veto?"
  - Discussão em duplas (1 min)
- **Diagrama**: Caixa de discussão
- **Tempo**: 0.5 min

---

#### Slide 32 — Estudo de Caso: AI Scientist — O Que Funcionou
- **Tipo**: Conteúdo
- **Objetivo**: Analisar criticamente os sucessos do AI Scientist
- **Conteúdo**:
  - Papers aceitos em workshop ICLR (peer review real)
  - Custo baixo (~$15/paper) viabiliza exploração
  - Pipeline estruturado garante reprodutibilidade
  - Review automático identifica falhas antes da submissão
  - Lição: estrutura > brilho individual
- **Diagrama**: Checklist de sucessos (etho-success)
- **Tempo**: 0.5 min

---

#### Slide 33 — Estudo de Caso: O Que Falhou
- **Tipo**: Conteúdo
- **Objetivo**: Ser honesto sobre as limitações do AI Scientist
- **Conteúdo**:
  - Experimentos às vezes não convergem (código com bugs)
  - Papers com contribuição marginal (novidade baixa)
  - Alucinação em revisão de literatura
  - Difícil avaliar "qualidade científica" sem humano
  - Lição: autonomia ≠ qualidade
- **Diagrama**: Checklist de falhas (etho-danger)
- **Tempo**: 0.5 min

---

### SEÇÃO E — Emergência e Alinhamento (Slides 34-41 · 8 min)

---

#### Slide 34 — [SEÇÃO] Emergência e Alinhamento
- **Tipo**: Seção
- **Objetivo**: Transição para Unidade 4 — Emergência e alinhamento
- **Conteúdo**: Número "4" grande + "Emergência e Alinhamento"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 35 — Comportamento Emergente: A Soma ≠ Partes
- **Tipo**: Conteúdo
- **Objetivo**: Introduzir o conceito de emergência em sociedades de agentes
- **Conteúdo**:
  - Comportamento emergente: padrões que surgem da interação, não do indivíduo
  - A soma é diferente das partes
  - Exemplos positivos: cooperação espontânea, formação de normas, divisão de trabalho
  - Exemplos negativos: conluio, discriminação, corrida armamentista
  - Pergunta: *Quando a soma é melhor? Quando é pior?*
- **Diagrama**: Agentes individuais → interações → padrões emergentes
- **Tempo**: 1.5 min

---

#### Slide 36 — Diagrama: Emergência
- **Tipo**: Diagrama
- **Objetivo**: Visualizar como comportamento emergente surge
- **Conteúdo**:
  - Agentes individuais seguem regras locais
  - Interações locais produzem padrões emergentes
  - Padrões geram propriedades coletivas: coordenação, polarização, especialização, echo chamber
- **Diagrama**: `12-Diagrams/ETHAGT16/emergence.mmd`
- **Animação**: Fluxo de cima para baixo: agentes → interações → padrões → propriedades
- **Tempo**: 1 min

---

#### Slide 37 — Emergência Desejada vs Indesejada
- **Tipo**: Comparação
- **Objetivo**: Distinguir emergência benéfica de emergência perigosa
- **Conteúdo**:
  - Desejada: cooperação espontânea, divisão de trabalho, inovação
  - Indesejada: conluio (agentes combinam contra objetivo), discriminação, echo chamber, corrida armamentista
  - Fator-chave: alinhamento de valores + supervisão
  - Sem supervisão: emergência tende ao extremo
- **Diagrama**: Duas colunas: verde (desejada) vs vermelho (indesejada)
- **Animação**: Colunas aparecem uma a uma
- **Tempo**: 1.5 min

---

#### Slide 38 — Alinhamento de Valores em Populações
- **Tipo**: Conteúdo
- **Objetivo**: Explicar como alinhar sociedades de agentes
- **Conteúdo**:
  - Alinhamento individual ≠ alinhamento coletivo
  - Constitution para sociedades: regras que governam todas as interações
  - Votação e consenso como mecanismos
  - Tensão: normas rígidas (seguras) vs flexíveis (adaptáveis)
  - Referência: Constitutional AI aplicado a sociedades
- **Diagrama**: Camadas: Valores individuais → Normas sociais → Constitution
- **Tempo**: 1 min

---

#### Slide 39 — Avaliação de Emergência
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar métricas para avaliar comportamento emergente
- **Conteúdo**:
  - Métricas de divergência: quão longe a sociedade está do comportamento esperado
  - Métricas de surpresa: comportamento não previsto pelos designers
  - Métricas de convergência: a sociedade estabiliza ou oscila?
  - Sem métricas: emergência é caixa preta
  - Em produção: monitoramento contínuo de emergência
- **Diagrama**: Dashboard com 3 métricas
- **Tempo**: 1 min

---

#### Slide 40 — Pergunta: Quando Emergência é Indesejada?
- **Tipo**: Exercício
- **Objetivo**: Provocar reflexão sobre limites da autonomia
- **Conteúdo**:
  - "Quando comportamento emergente é indesejado?"
  - 3 cenários rápidos: em qual você interviria?
  - Discussão aberta (1 min)
- **Diagrama**: Caixa de discussão
- **Tempo**: 0.5 min

---

#### Slide 41 — Exercício: Detectando Emergência Indesejada
- **Tipo**: Exercício
- **Objetivo**: Praticar identificação de emergência problemática
- **Conteúdo**:
  - Mostrar trace de uma sociedade de agentes (5 agentes, 10 interações)
  - Em duplas: identificar padrão emergente indesejado
  - Propor 2 correções (norma, supervisão, HITL)
  - 1 min discussão
- **Diagrama**: Trace de interações com padrão destacado
- **Tempo**: 1 min

---

### SEÇÃO F — Fechamento (Slides 42-50 · 10 min)

---

#### Slide 42 — [SEÇÃO] Fronteira e Ética
- **Tipo**: Seção
- **Objetivo**: Transição para Unidade 5 — Fronteira e ética
- **Conteúdo**: Número "5" grande + "Fronteira e Ética"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 43 — Onde a Pesquisa Está Agora
- **Tipo**: Conteúdo
- **Objetivo**: Mapear o estado da arte em sociedades de agentes
- **Conteúdo**:
  - AI Scientist (Sakana, 2024): pesquisa ML automatizada
  - AlphaEvolve (DeepMind, 2024): evolução de algoritmos
  - AutoGen research: framework multi-agente para pesquisa
  - Swarm research: coordenação de grandes populações
  - Tendência: de 1 agente → times → sociedades autônomas
- **Diagrama**: Mapa da fronteira de pesquisa
- **Tempo**: 1 min

---

#### Slide 44 — Questões Éticas: Autoria e Responsible AI
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar dilemas éticos da pesquisa autônoma
- **Conteúdo**:
  - Automação de pesquisa: papers gerados por IA — autoria? revisão?
  - Responsible AI: viés amplificado em sociedades
  - Autopropagação: agente que cria cópias de si mesmo
  - Auto-modificação: agente que altera seu próprio código
  - Discussão: *Onde você traça a linha entre agente útil e perigoso?*
- **Diagrama**: 4 ícones de dilema ético
- **Tempo**: 1.5 min

---

#### Slide 45 — O Que NÃO Fazer
- **Tipo**: Conteúdo
- **Objetivo**: Checklist de práticas perigosas em sistemas autônomos
- **Conteúdo**:
  - Sistemas sem supervisão humana (sem HITL)
  - Auto-modificação irrestrita
  - Deploy sem avaliação de risco
  - Autopropagação sem limites
  - Sociedades sem constitution ou normas
  - Sem métricas de emergência
- **Diagrama**: Checklist vermelho (etho-danger)
- **Tempo**: 1 min

---

#### Slide 46 — Exercício: Avaliar Qualidade de um AI Scientist
- **Tipo**: Exercício
- **Objetivo**: Praticar avaliação crítica de pesquisa autônoma
- **Conteúdo**:
  - Cenário: AI Scientist gerou paper sobre "otimização de prompts"
  - Em grupos: definir 3 critérios para avaliar a qualidade científica
  - Exemplos: reprodutibilidade, novidade, corretude metodológica
  - 2 min discussão, 1 min compartilhar critérios
- **Diagrama**: Caixa de discussão com paper fake
- **Tempo**: 2 min

---

#### Slide 47 — Resumo da Aula
- **Tipo**: Resumo
- **Objetivo**: Sintetizar os pontos-chave
- **Conteúdo**:
  - Sociedades de agentes = papéis + normas + reputação + emergência
  - Smallville = caso canônico de simulação social
  - AI Scientist = fronteira de pesquisa autônoma
  - Emergência pode ser desejada (cooperação) ou indesejada (conluio)
  - Alinhamento coletivo ≠ alinhamento individual
  - Ética: supervisão, avaliação de risco, responsible AI
- **Diagrama**: 6 ícones com os pontos-chave
- **Tempo**: 1 min

---

#### Slide 48 — Quiz: 3 Perguntas Rápidas
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - P1: "Qual pipeline o AI Scientist (Sakana) automatiza?"
    - A) Apenas escrita de papers
    - B) Ideação → experimento → paper → review (resposta B)
    - C) Apenas revisão de literatura
    - D) Apenas análise de dados
  - P2: "O que é comportamento emergente?"
    - A) Comportamento programado explicitamente
    - B) Padrões que surgem da interação, não do indivíduo (resposta B)
    - C) Erro aleatório do modelo
    - D) Comportamento do agente mais influente
  - P3: "V/F: Sociedades de agentes sempre convergem."
    - Falso — sociedades podem polarizar, oscilar ou colapsar
- **Tempo**: 1 min

---

#### Slide 49 — Conexão com Capstone e Referências
- **Tipo**: Referências
- **Objetivo**: Conectar ETHAGT16 com o Capstone e indicar leitura
- **Conteúdo**:
  - ETHAGT90 — Capstone: projeto final integrador
  - O espectro completo: de Augmented LLM (ETHAGT01) a Sociedades de Agentes (ETHAGT16)
  - Leitura obrigatória:
    - Park et al. *Generative Agents* (arXiv:2304.03442)
    - Lu et al. *The AI Scientist* (arXiv:2408.06292)
    - Chen et al. *AgentVerse* (arXiv:2308.10848)
  - Complementar: DeepMind *AlphaEvolve* (2024)
  - Convite: *Onde vocês querem levar isso? Pesquisa, produto, impacto social?*
- **Diagrama**: Mapa da especialização com ETHAGT16 → ETHAGT90
- **Tempo**: 1 min

---

#### Slide 50 — Q&A / Encerramento
- **Tipo**: Capa
- **Objetivo**: Abrir para perguntas e encerrar
- **Conteúdo**:
  - "Perguntas?"
  - Contato do professor
  - "Próximo módulo: ETHAGT90 — Capstone"
  - "Vocês estão na fronteira. Agora é hora de construir."
- **Diagrama**: Logo Etho + fundo etho-dark
- **Tempo**: 1 min

---

## Resumo do Storyboard

| Seção | Slides | Tempo | Conteúdo |
|---|---|---|---|
| A — Abertura | 1-6 | 6 min | Capa, objetivos, competências, agenda, motivação, contexto histórico |
| B — Sociedades de Agentes | 7-15 | 8 min | Do agente à sociedade, papéis, normas, reputação, modelos, diagrama, exercício |
| C — Simulações Sociais | 16-22 | 6 min | Smallville, arquitetura técnica, casos de uso, limites, exercícios |
| D — Autonomous Research Systems | 23-33 | 12 min | Pipeline, AI Scientist, AlphaEvolve, multi-agent labs, DEMO, estudo de caso |
| E — Emergência e Alinhamento | 34-41 | 8 min | Comportamento emergente, desejada vs indesejada, alinhamento, avaliação, exercício |
| F — Fechamento | 42-50 | 10 min | Fronteira, ética, o que não fazer, exercício, resumo, quiz, Capstone, referências, Q&A |
| **Total** | **50** | **50 min** | |

---

## Diagramas Necessários

| # | Slide | Diagrama | Tipo | Fonte |
|---|---|---|---|---|
| D1 | 5 | Escala: 1 agente → sociedade → emergência | Crescimento visual | Novo |
| D2 | 6 | Timeline de marcos (2022-2024) | Timeline | Novo |
| D3 | 8 | Escada de 4 níveis (agente → sociedade) | Escada | Novo |
| D4 | 9 | 5 papéis em círculo | Mind map radial | Novo |
| D5 | 11 | Grafo de confiança (reputação) | Grafo | Novo |
| D6 | 13 | Arquitetura de uma sociedade | Flowchart | `12-Diagrams/ETHAGT16/society.mmd` |
| D7 | 14 | Comparação Grupo vs Instituição vs Sociedade | 3 colunas | Novo |
| D8 | 17 | Mapa de Smallville com agentes | Mapa | Park et al. |
| D9 | 18 | Pipeline Smallville: Memory → Reflection → Action | Flowchart | Novo |
| D10 | 25 | Research pipeline | Flowchart | `12-Diagrams/ETHAGT16/research-pipeline.mmd` |
| D11 | 26 | Fluxo AI Scientist em 5 etapas | Flowchart | Sakana |
| D12 | 27 | Pipeline AI Scientist 4 stages com feedback | Flowchart | Novo |
| D13 | 28 | Loop evolutivo AlphaEvolve | Loop | DeepMind |
| D14 | 29 | Time de 4 agentes com canal de comunicação | Diagrama | Novo |
| D15 | 36 | Comportamento emergente | Flowchart | `12-Diagrams/ETHAGT16/emergence.mmd` |
| D16 | 37 | Emergência desejada vs indesejada | 2 colunas | Novo |
| D17 | 38 | Camadas de alinhamento | Pirâmide | Novo |
| D18 | 43 | Mapa da fronteira de pesquisa | Mind map | Novo |
| D19 | 49 | Mapa da especialização ETHAGT01 → ETHAGT90 | Timeline | Novo |

---

## Pontos de Engajamento

| # | Slide | Tipo | Pergunta / Atividade | Tempo |
|---|---|---|---|---|
| E1 | 5 | Hook | *O que acontece quando 100 agentes interagem sem supervisão humana?* | 0.5 min |
| E2 | 15 | Exercício | Definir 5 papéis para comitê editorial + norma + reputação | 1 min |
| E3 | 20 | Hook | *Uma simulação social com LLMs pode prever comportamento humano real?* | 0.5 min |
| E4 | 21 | Discussão | V/F: "Sociedades de agentes sempre convergem." | 0.5 min |
| E5 | 22 | Exercício | Design de simulação: 3 agentes, 2 normas, 1 métrica (home office) | 0.5 min |
| E6 | 31 | Discussão | *Qual papel foi mais crítico? E sem o crítico?* | 0.5 min |
| E7 | 40 | Hook | *Quando comportamento emergente é indesejado?* | 0.5 min |
| E8 | 41 | Exercício | Detectar emergência indesejada em trace + propor 2 correções | 1 min |
| E9 | 44 | Hook | *Onde você traça a linha entre agente útil e perigoso?* | 0.5 min |
| E10 | 46 | Exercício | Definir 3 critérios para avaliar qualidade científica de AI Scientist | 2 min |
| E11 | 48 | Quiz | 3 perguntas rápidas (pipeline, emergência, convergência) | 1 min |
| E12 | 49 | Reflexão | *Onde vocês querem levar isso? Pesquisa, produto, impacto social?* | 0.5 min |

---

## Pendências de Produção

- [ ] Produzir 16 diagramas novos (D1-D5, D7-D9, D11-D14, D16-D19)
- [ ] Validar 3 diagramas existentes (D6, D10, D15) contra conteúdo dos slides
- [ ] Screenshot do trace da DEMO Mini Sociedade (Slide 30)
- [ ] Screenshot do código com syntax highlighting (Slide 30)
- [ ] Imagem de fundo para capa (Slide 1) — rede de agentes
- [ ] Badge de competências (Slide 3) — radar chart C1-C6
- [ ] Timeline de marcos históricos (Slide 6)
- [ ] Mapa de Smallville estilizado (Slide 17)
- [ ] Trace de interações para exercício de emergência (Slide 41)
- [ ] Paper fake para exercício de avaliação (Slide 46)

---

> **Aguardando aprovação deste storyboard para gerar os slides detalhados com notas do professor.**
