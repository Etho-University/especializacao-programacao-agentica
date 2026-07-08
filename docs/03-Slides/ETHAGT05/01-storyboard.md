# ETHAGT05 — Memória de Agentes
## Storyboard da Apresentação

> **Universidade Etho · Especialização em Programação Agêntica**
> Fase B — Memória, Contexto e Persistência · 25 h
> Storyboard v1.0 · Julho 2026

---

## Metadados da Apresentação

| Campo | Valor |
|---|---|
| Código | ETHAGT05 |
| Título | Memória de Agentes (working · episódica · semântica · procedural) |
| Duração estimada | 90 min (2 blocos de 45 min) |
| Total de slides | 70 |
| Público | Arquitetos, Engenheiros de Software, Engenheiros de IA, Cientistas de Dados, Tech Leads |
| Pré-requisitos | ETHAGT04 |
| Competências | C1 (A), C4 (I), C5 (B), C6 (B) |

---

## Mapa Visual da Apresentação

```
BLOCO 1 (45 min)                              BLOCO 2 (45 min)
┌──────────────────────────────┐              ┌──────────────────────────────┐
│ SEÇÃO A — Abertura (8 min)   │              │ SEÇÃO E — Memória Vetorial   │
│  Capa · Objetivos · Agenda   │              │  (12 min)                    │
│  Motivação · Contexto        │              │  Embedding · Recall · Filter │
├──────────────────────────────┤              │  Re-ranking · Pipeline · Lab │
│ SEÇÃO B — Tipos de Memória   │              ├──────────────────────────────┤
│  (12 min)                    │              │ SEÇÃO F — Semântica e Grafos │
│  Working · Episódica         │              │  (8 min)                     │
│  Semântica · Procedural      │              │  Consolidação · KG ·         │
│  4 camadas · MemGPT          │              │  Generative Agents           │
├──────────────────────────────┤              ├──────────────────────────────┤
│ SEÇÃO C — Checkpointer (15m) │              │ SEÇÃO G — Produção (8 min)   │
│  Estado persistente          │              │  Consistência · PII ·        │
│  Postgres/SQLite/Redis       │              │  Direito ao esquecimento ·   │
│  Resume · Replay · Branch    │              │  Custo · Observabilidade     │
│  DEMO: Postgres              │              ├──────────────────────────────┤
├──────────────────────────────┤              │ SEÇÃO H — Fechamento (17 min)│
│ SEÇÃO D — Gerenc. Contexto   │              │  Boas práticas · Anti-patterns│
│  (10 min)                    │              │  Resumo · Quiz · Referências │
│  Custo · Sumarização         │              │  Projeto · Labs · Q&A        │
│  Eviction · Entity memory    │              └──────────────────────────────┘
└──────────────────────────────┘
```

---

## Storyboard Detalhado

### SEÇÃO A — Abertura (Slides 1-6 · 8 min)

---

#### Slide 1 — Capa
- **Tipo**: Capa
- **Objetivo**: Identificar a aula, professor e contexto
- **Conteúdo**:
  - ETHAGT05 — Memória de Agentes (working · episódica · semântica · procedural)
  - Universidade Etho · Especialização em Programação Agêntica
  - Fase B — Memória, Contexto e Persistência
  - Professor · Data
- **Diagrama**: Logo Etho + imagem de fundo abstrata (camadas de memória empilhadas)
- **Animação**: Fade in do título
- **Tempo**: 1 min

---

#### Slide 2 — Objetivos do Módulo
- **Tipo**: Conteúdo
- **Objetivo**: Deixar claro o que o aluno deve conseguir fazer ao final
- **Conteúdo**:
  - Objetivo geral: Arquitetar sistemas de memória que dão a agentes persistência, contexto acumulado e aprendizado — para além da context window
  - 5 objetivos específicos (1 linha cada):
    1. Distinguir tipos de memória e quando cada é necessária
    2. Implementar persistência via checkpointer (Postgres/SQLite/Redis)
    3. Gerenciar a janela de contexto: sumarização, eviction, janela deslizante
    4. Construir memória vetorial para recall episódico
    5. Lidar com consistência, privacidade e custo de memória
- **Diagrama**: Ícones representando cada objetivo
- **Animação**: Aparecer objetivos um a um (on click)
- **Tempo**: 2 min

---

#### Slide 3 — Competências Desenvolvidas
- **Tipo**: Conteúdo
- **Objetivo**: Conectar a aula ao Framework Etho de competências
- **Conteúdo**:
  - Tabela: 4 competências com nível B/I/A
  - C1 Programação Agêntica → A
  - C4 Agent Memory → I
  - C5 AgentOps & Avaliação → B
  - C6 Agent Security → B
  - Badge visual por competência
- **Diagrama**: Radar chart dos 4 pilares
- **Animação**: Radar aparece com wipe
- **Tempo**: 1 min

---

#### Slide 4 — Agenda
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar o roteiro da aula com tempos
- **Conteúdo**:
  - Bloco 1: Abertura → Tipos de Memória → Checkpointer → Gerenciamento de Contexto
  - Bloco 2: Memória Vetorial → Semântica e Grafos → Produção → Fechamento
  - Tempos estimados por seção
- **Diagrama**: Timeline horizontal com 8 seções
- **Animação**: Timeline cresce da esquerda para direita
- **Tempo**: 1 min

---

#### Slide 5 — Motivação: O Agente Amnésico
- **Tipo**: Conteúdo
- **Objetivo**: Criar tensão — agentes sem memória são inúteis em sessões longas
- **Conteúdo**:
  - "Agente sem memória é um hóspede que esquece cada conversa ao fechar a porta"
  - Exemplo: assistente de produtividade — "lembra do projeto X?" — não sabe
  - Exemplo: agente de suporte — pergunta a mesma coisa a cada ticket
  - Sem memória: não aprende, não melhora, não personaliza
  - Pergunta: *Quanto contexto você acha que um assistente pessoal precisa reter?*
- **Diagrama**: Imagem de "amnésia" (agente reiniciando) vs "memória acumulada" (agente evoluindo)
- **Animação**: Split — lado esquerdo (esquece), depois lado direito (lembra)
- **Tempo**: 2 min

---

#### Slide 6 — Contexto: Por Que Memória Agora
- **Tipo**: Conteúdo
- **Objetivo**: Explicar a confluência que tornou memória de agentes viável e necessária
- **Conteúdo**:
  - Linha do tempo: 2020 (GPT-3, 2k tokens) → 2022 (4k-8k) → 2023 (16k-32k, tool calling) → 2024 (128k-200k, agent frameworks com persistência) → 2025 (MemGPT, Zep, A-MEM)
  - Confluência: context windows maiores + custo menor + frameworks com checkpointer + vector DBs acessíveis
  - Mas: context window maior ≠ memória resolvida (custo, latência, falta de estrutura)
  - Marco: MemGPT (arXiv:2310.08560) — LLMs como sistemas operacionais
- **Diagrama**: Timeline horizontal com marcos
- **Animação**: Marcos aparecem sequencialmente
- **Tempo**: 1 min

---

### SEÇÃO B — Tipos de Memória (Slides 7-16 · 12 min)

---

#### Slide 7 — [SEÇÃO] Tipos de Memória
- **Tipo**: Seção
- **Objetivo**: Transição para o bloco de fundamentos de memória
- **Conteúdo**: Número "1" grande + "Tipos de Memória"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 8 — Working Memory: A Context Window
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar a camada mais básica de memória
- **Conteúdo**:
  - Working memory = context window do LLM (tokens visíveis no prompt)
  - Efêmera: desaparece ao fim da sessão
  - Limitada: 4k a 200k tokens (modelo-dependente)
  - Estratégias: token budget, sliding window, system prompt + últimas N mensagens
  - Custo: cada token no contexto é processado a cada chamada
- **Diagrama**: Caixa "Context Window" com tokens entrando e saindo
- **Animação**: Tokens entram e saem da janela
- **Tempo**: 2 min

---

#### Slide 9 — Limites da Context Window
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar que mesmo context windows grandes não resolvem memória
- **Conteúdo**:
  - "Lost in the middle": LLMs ignoram informação no meio do contexto
  - Custo cresce com o tamanho do contexto (mesmo que não quadraticamente)
  - Latência aumenta com contexto maior
  - 200k tokens ≠ 200k tokens úteis (ruído, redundância, irrelevância)
  - Conclusão: context window é working memory, não memória de longo prazo
- **Diagrama**: Gráfico de "recall accuracy" vs posição no contexto (curva U)
- **Animação**: Curva U aparece com wipe
- **Tempo**: 1.5 min

---

#### Slide 10 — Memória Episódica: Eventos com Timestamp
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar a memória de eventos passados
- **Conteúdo**:
  - Episódica = registro de eventos com timestamp (o que aconteceu, quando)
  - Exemplo: "Usuário perguntou sobre React hooks em 12/mar" → recall por similaridade
  - Armazenamento típico: vector DB (embedding + metadata de tempo)
  - Recall: "o que aconteceu antes que se pareça com X?"
  - Diferença de log: episódica é recuperável por significado, não só por query estruturada
- **Diagrama**: Timeline de eventos com embeddings ao lado
- **Animação**: Eventos aparecem na timeline, embeddings destacados
- **Tempo**: 1.5 min

---

#### Slide 11 — Memória Semântica: Fatos e Conhecimento
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar a memória de fatos consolidados
- **Conteúdo**:
  - Semântica = fatos, conhecimento sobre o mundo/usuário (o que é verdade)
  - Exemplo: "João é desenvolvedor Python" (fato, não evento)
  - Armazenamento típico: KB estruturada, knowledge graph, tabela de perfil
  - Como surge: consolidação da episódica (múltiplos eventos → um fato)
  - Diferença de episódica: semântica não tem "quando", tem "o que é"
- **Diagrama**: Transformação de eventos episódicos em fato semântico
- **Animação**: Eventos convergem para um fato
- **Tempo**: 1.5 min

---

#### Slide 12 — Memória Procedural: Skills Aprendidas
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar a memória de "como fazer"
- **Conteúdo**:
  - Procedural = sequências de actions para objetivos recorrentes (skills)
  - Exemplo: "para deploy: rodar testes → build → push → deploy" (aprendido, não hardcoded)
  - Armazenamento típico: biblioteca de playbooks, prompt templates, tool sequences
  - Como surge: reflexão sobre sucessos/falhas (estilo Reflexion, arXiv:2302.04761)
  - Diferença das outras: procedural é sobre *como agir*, não sobre *o que aconteceu* ou *o que é verdade*
- **Diagrama**: Loop de reflexão → skill extraída → biblioteca procedural
- **Tempo**: 1.5 min

---

#### Slide 13 — As 4 Camadas: Visão Integrada
- **Tipo**: Comparação
- **Objetivo**: Mostrar as 4 camadas lado a lado e quando cada uma é necessária
- **Conteúdo**:
  - Tabela 4×4: Working | Episódica | Semântica | Procedural
  - Eixos: o que armazena, onde armazena, como recupera, quando usar
  - Working: mensagens atuais / context window / no prompt / sempre
  - Episódica: eventos / vector DB / similaridade + metadata / recall de contexto
  - Semântica: fatos / KB ou KG / query estruturada / quando precisa de verdade estável
  - Procedural: skills / playbook library / match de objetivo / quando repete tarefas
- **Diagrama**: Tabela comparativa colorida (4 colunas)
- **Animação**: Colunas aparecem uma a uma
- **Tempo**: 2 min

---

#### Slide 14 — Diagrama: As 4 Camadas de Memória
- **Tipo**: Diagrama
- **Objetivo**: Visualizar a arquitetura integrada de memória
- **Conteúdo**:
  - Agente no centro, conectado às 4 camadas
  - Working (context window, volátil)
  - Episódica (vector DB, recall por similaridade)
  - Semântica (KB/KG, fatos e relações)
  - Procedural (skills, sequências de actions)
  - Checkpointer persistindo o estado do agente
- **Diagrama**: `12-Diagrams/ETHAGT05/memory-layers.mmd`
- **Animação**: Camadas surgem do centro (Agente) para fora
- **Tempo**: 1.5 min

---

#### Slide 15 — Inspiração Cognitiva sem Literalismo
- **Tipo**: Citação
- **Objetivo**: Alertar contra a armadilha de copiar o cérebro literalmente
- **Conteúdo**:
  - "A memória humana é inspiração, não especificação." — Paráfrase didática
  - Working ↔ memória de trabalho (Baddeley)
  - Episódica/Semântica ↔ Tulving (1972)
  - Procedural ↔ memória de habilidades (Squire)
  - Mas: LLMs não consolidam durante o sono, não têm hipocampo, não esquecem por razões biológicas
  - Aprendizado: use a taxonomia como *framework de design*, não como modelo neural
- **Diagrama**: Ícone de "cérebro" com seta para "arquitetura de software"
- **Tempo**: 0.5 min

---

#### Slide 16 — MemGPT: LLMs como Sistemas Operacionais
- **Tipo**: Diagrama
- **Objetivo**: Apresentar a analogia central do MemGPT como referência arquitetural
- **Conteúdo**:
  - MemGPT (Packer et al., arXiv:2310.08560): LLM como SO
  - Context window = RAM (limitada, rápida)
  - Memória persistente = disco (ilimitada, lenta)
  - O modelo gerencia sua própria memória: decide o que page-in / page-out
  - Self-editing memory: o modelo atualiza suas próprias notas/perfil
  - Inspirou: Zep, A-MEM, Letta
- **Diagrama**: Analogia SO: RAM (context window) ↔ Disco (memória persistente)
- **Animação**: Page-in/page-out animado entre RAM e disco
- **Tempo**: 1.5 min

---

### SEÇÃO C — Checkpointer e Estado Persistente (Slides 17-29 · 15 min)

---

#### Slide 17 — [SEÇÃO] Checkpointer e Estado Persistente
- **Tipo**: Seção
- **Objetivo**: Transição para persistência de estado
- **Conteúdo**: "2 — Checkpointer e Estado Persistente"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 18 — O Problema: Estados Efêmeros
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar por que precisamos de persistência de estado
- **Conteúdo**:
  - Sem checkpointer: agente perde todo estado ao reiniciar
  - Casos que quebram:
    - Servidor reinicia → conversa perdida
    - HITL demora dias → contexto evaporou
    - Debug: não dá para reproduzir execução passada
    - A/B testing: não dá para voltar no tempo
  - Solução: serializar estado em storage durável
- **Diagrama**: Agente "morre" (estado perdido) vs agente "hiberna" (estado persistido)
- **Tempo**: 1.5 min

---

#### Slide 19 — LangGraph Checkpointer: Conceito
- **Tipo**: Conteúdo
- **Objetivo**: Introduzir o modelo de checkpointer do LangGraph
- **Conteúdo**:
  - Checkpointer = camada que serializa o estado do grafo a cada step
  - Estado = qualquer objeto serializável (TypedDict, Pydantic, dataclass)
  - Cada node execution → checkpoint gravado
  - thread_id identifica a conversa/sessão
  - checkpoint_id identifica o momento (versionado)
  - Profundidade em ETHAGT03 (StateGraph)
- **Diagrama**: Grafo com checkpoints em cada node
- **Tempo**: 1.5 min

---

#### Slide 20 — Estado Serializável
- **Tipo**: Código
- **Objetivo**: Mostrar como modelar estado serializável
- **Conteúdo**:
  - Estado deve ser JSON-serializable (ou com serializer custom)
  - Padrão: TypedDict com messages, intermediate results, metadata
  - Snippet de código: definição de State + Graph com checkpointer
  - Pegadinha: objetos não-serializáveis (conexões DB, file handles, closures)
  - Solução: separar estado serializável de recursos efêmeros
- **Diagrama**: Code block com State definition
- **Tempo**: 2 min

---

#### Slide 21 — Backends: Postgres, SQLite, Redis
- **Tipo**: Comparação
- **Objetivo**: Apresentar as implementações de checkpointer disponíveis
- **Conteúdo**:
  - Postgres: produção, multi-tenant, ACID, escalável
  - SQLite: desenvolvimento local, single-node, zero-config
  - Redis: baixa latência, TTL automático, ideal para sessões curtas
  - Outros: MongoDB, DynamoDB (comunidade)
  - Critério: durabilidade vs latência vs escala
- **Diagrama**: 3 colunas com prós/contras
- **Tempo**: 1.5 min

---

#### Slide 22 — Comparação de Backends
- **Tipo**: Comparação
- **Objetivo**: Sistematizar trade-offs dos backends de checkpointer
- **Conteúdo**:
  - Tabela: Postgres vs SQLite vs Redis
  - Eixos: durabilidade, latência, multi-tenant, custo, operação, TTL, ACID
  - Postgres: durabilidade alta, latência média, multi-tenant sim
  - SQLite: durabilidade alta (disco local), latência baixa, multi-tenant não
  - Redis: durabilidade média (persistência config), latência baixíssima, TTL nativo
  - Regra: comece com SQLite (dev), vá para Postgres (prod), use Redis para cache de sessão
- **Diagrama**: Tabela comparativa colorida
- **Tempo**: 1.5 min

---

#### Slide 23 — Resume: Retomando Execução
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar como retomar uma execução interrompida
- **Conteúdo**:
  - Resume: carregar estado do último checkpoint e continuar
  - Casos: HITL demora, servidor reinicia, usuário volta dias depois
  - Código: `graph.invoke(None, config={"configurable": {"thread_id": "xyz"}})`
  - O agente retoma exatamente de onde parou (mensagens, contexto, steps)
  - Pegadinha: modelo pode ter mudado (versão diferente) → estado pode ser incompatível
- **Diagrama**: Fluxo: execução → interrupção → dias depois → resume
- **Tempo**: 1.5 min

---

#### Slide 24 — Diagrama: Checkpointer Resume
- **Tipo**: Diagrama
- **Objetivo**: Visualizar o fluxo de pause/resume com checkpointer
- **Conteúdo**:
  - Agente em execução (sessão 1) → estado serializado → Checkpointer (Postgres)
  - Checkpointer → thread_id → Agente retoma (dias depois, sessão 2)
  - Mesmo thread_id → Agente retoma (semana depois, sessão 3)
  - HITL: humano aprova → resume
- **Diagrama**: `12-Diagrams/ETHAGT05/checkpointer-resume.mmd`
- **Animação**: Fluxo step-by-step (sessão 1 → pause → sessão 2)
- **Tempo**: 1.5 min

---

#### Slide 25 — Replay: Debugando o Passado
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar como reproduzir execução passada para debug
- **Conteúdo**:
  - Replay: carregar checkpoint de um momento específico e re-executar
  - Casos: "por que o agente tomou decisão X?" → replay a partir do checkpoint anterior
  - Diferença de resume: replay re-executa, resume continua
  - Útil para: debugging, A/B testing de prompts, regressão
  - Ferramentas: LangSmith + checkpointer = replay visual
- **Diagrama**: Timeline de checkpoints com cursor de replay
- **Tempo**: 1 min

---

#### Slide 26 — Branching: Time Travel
- **Tipo**: Diagrama
- **Objetivo**: Mostrar como criar ramos alternativos a partir de um checkpoint
- **Conteúdo**:
  - Branching: partir de um checkpoint e seguir caminho diferente
  - Casos: "e se o agente tivesse usado tool Y em vez de X?"
  - Como: fork do checkpoint_id → nova execução com parâmetros diferentes
  - Análogo a `git checkout` + `git checkout -b`
  - Pergunta: *Time travel: ferramenta de debug ou risco de segurança?*
- **Diagrama**: Árvore de checkpoints com ramos (estilo git graph)
- **Tempo**: 1.5 min

---

#### Slide 27 — Versionamento de Schema de Estado
- **Tipo**: Conteúdo
- **Objetivo**: Lidar com evolução do schema de estado ao longo do tempo
- **Conteúdo**:
  - Problema: estado v1 (sem campo "priority") vs estado v2 (com "priority")
  - Checkpoints antigos têm schema diferente → quebra ao retomar
  - Estratégias:
    - Migração lazy: converter no load
    - Version field no estado: `schema_version: 2`
    - Backward compatibility: campos novos com default
  - Analogia: migração de DB, mas para estado de agente
- **Diagrama**: Estado v1 → migração → Estado v2
- **Tempo**: 1.5 min

---

#### Slide 28 — DEMO: Checkpointer em Postgres
- **Tipo**: Código
- **Objetivo**: Demo ao vivo — agente interrompido e retomado
- **Conteúdo**:
  - Código do `05-Labs/ETHAGT05/Lab1-Checkpointer-Postgres`
  - Passo 1: agente inicia tarefa (thread_id = "demo-001")
  - Passo 2: agente é interrompido (kill do processo)
  - Passo 3: dias depois, retoma com mesmo thread_id
  - Mostrar estado preservado (mensagens, contexto, steps)
  - Replay de execução anterior para debug
- **Diagrama**: Code block + terminal side-by-side
- **Animação**: Highlight de linhas chave (thread_id, resume)
- **Tempo**: 2 min

---

#### Slide 29 — Pergunta da DEMO
- **Tipo**: Exercício
- **Objetivo**: Engajar a turma com uma pergunta sobre a demo
- **Conteúdo**:
  - "O que acontece se o modelo foi atualizado entre sessão 1 e sessão 2?"
  - "E se o schema do estado mudou?"
  - "Como você testaria que o resume funciona corretamente?"
  - Discussão em duplas (2 min)
- **Diagrama**: Caixa de discussão
- **Tempo**: 1.5 min

---

### SEÇÃO D — Gerenciamento de Contexto (Slides 30-40 · 10 min)

---

#### Slide 30 — [SEÇÃO] Gerenciamento de Contexto
- **Tipo**: Seção
- **Objetivo**: Transição para o problema de janela de contexto finita
- **Conteúdo**: "3 — Gerenciamento de Contexto"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 31 — O Problema: Context Window é Finita
- **Tipo**: Conteúdo
- **Objetivo**: Estabelecer a tensão fundamental de gerenciamento de contexto
- **Conteúdo**:
  - Mesmo com 200k tokens, a context window enche
  - Conversas longas + tools + retrieval → estouro de contexto
  - Sintomas: agente "esquece" início da conversa, respostas degradam, erro 400
  - Tensão: mais contexto = mais informação, mas também mais custo, latência e ruído
  - Solução: estratégias ativas de gerenciamento (não apenas "encher até estourar")
- **Diagrama**: Balde enchendo de tokens até transbordar
- **Tempo**: 1 min

---

#### Slide 32 — Custo: Quadrático ou Linear? Visão Crítica
- **Tipo**: Conteúdo
- **Objetivo**: Desmistificar a afirmação "custo cresce quadraticamente"
- **Conteúdo**:
  - Mito: "attention é O(n²)" → custo quadraticamente
  - Realidade: attention é O(n²) em *computação*, mas:
    - KV cache: tokens já processados não são recomputados
    - Sliding window attention: só atende a uma janela local
    - Custo de API é *linear* em tokens (preço por token in/out)
  - Mas: latência sim cresce, e qualidade degrada com contexto longo
  - Conclusão: o problema não é só custo — é *qualidade* e *latência*
- **Diagrama**: Gráfico: custo (linear) vs latência (sub-linear) vs qualidade (curva U invertida)
- **Tempo**: 1.5 min

---

#### Slide 33 — Estratégia 1: Janela Deslizante
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar a estratégia mais simples de gerenciamento de contexto
- **Conteúdo**:
  - Manter apenas as últimas N mensagens no contexto
  - Simples, previsível, barato
  - Mas: perde contexto antigo ("do que estávamos falando?")
  - Variação: system prompt + últimas N mensagens (preserva instrução)
  - Quando usar: chatbots simples, conversas curtas, não críticas
- **Diagrama**: Janela deslizante sobre uma sequência de mensagens
- **Tempo**: 1 min

---

#### Slide 34 — Estratégia 2: Sumarização em Cascata
- **Tipo**: Diagrama
- **Objetivo**: Mostrar como sumarizar contexto progressivamente
- **Conteúdo**:
  - Quando contexto enche: sumarizar mensagens antigas → substituir por sumário
  - Sumarização em cascata: sumário de sumários (níveis de compressão)
  - Cada nível: menos detalhe, mais abstração
  - Pegadinha: sumário pode perder informação crítica
  - Quando usar: conversas longas, agentes de suporte, reuniões
- **Diagrama**: Pirâmide invertida: mensagens → sumário L1 → sumário L2 → sumário L3
- **Animação**: Níveis de sumário aparecem de baixo para cima
- **Tempo**: 1 min

---

#### Slide 35 — Estratégia 3: Eviction por Relevância
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar eviction inteligente (não só por tempo)
- **Conteúdo**:
  - Nem tudo no contexto é igualmente relevante
  - Eviction por relevância: score = f(recência, importância, frequência de acesso)
  - Manter: system prompt, últimas mensagens, entidades ativas, fatos críticos
  - Evitar: mensagens antigas de baixa importância, tool outputs verbosos, redundâncias
  - Análogo a LRU cache, mas com score semântico
- **Diagrama**: Matriz relevância × idade com zonas (manter / arquivar / apagar)
- **Tempo**: 1 min

---

#### Slide 36 — Diagrama: Eviction Flow
- **Tipo**: Diagrama
- **Objetivo**: Visualizar o fluxo de decisão de eviction
- **Conteúdo**:
  - Novo evento → score = relevance × decay(age)
  - Score > threshold? → manter na memória
  - Entidade crítica? (ex.: pagamento) → decay lento, manter mais tempo
  - Recall frequente? → aumenta score (reforço)
  - Caso contrário → arquivar / apagar
- **Diagrama**: `12-Diagrams/ETHAGT05/eviction-flow.mmd`
- **Animação**: Fluxo step-by-step (evento → score → decisão)
- **Tempo**: 1 min

---

#### Slide 37 — Estratégia 4: Entity-Centric Memory (MemGPT, Zep)
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar a abordagem de memória centrada em entidades
- **Conteúdo**:
  - Em vez de uma lista de mensagens, organizar memória por *entidade*
  - Cada entidade (usuário, projeto, tarefa) tem seu próprio "perfil" de memória
  - O modelo decide quando page-in (carregar) e page-out (descarregar) entidades
  - MemGPT: self-editing memory — o modelo atualiza suas próprias notas
  - Zep: memória de longo prazo com graph + vector
  - Vantagem: contexto sempre relevante à entidade ativa
- **Diagrama**: Entidades como "pastas" de memória com page-in/page-out
- **Tempo**: 1 min

---

#### Slide 38 — Quando Memória Vetorial é Pior que Relacional
- **Tipo**: Comparação
- **Objetivo**: Ser crítico — nem tudo deve ser vector DB
- **Conteúdo**:
  - Vector DB é ótimo para: recall por significado, fuzzy matching, "mais ou menos"
  - Vector DB é péssimo para: exact match, ordenação temporal, agregação, joins
  - Exemplos onde relacional ganha:
    - "Todos os eventos do usuário X no mês Y" → SQL (WHERE + ORDER BY)
    - "Qual o saldo atual?" → KB relacional (não embedding)
    - "Listar entidades do tipo 'projeto'" → tabela (não similaridade)
  - Regra: vector para recall semântico, relacional para fatos estruturados, KG para relações
- **Diagrama**: 3 colunas: Vector DB | Relacional | Knowledge Graph — com casos de uso
- **Tempo**: 1 min

---

#### Slide 39 — Exercício: Política de Eviction
- **Tipo**: Exercício
- **Objetivo**: Praticar o design de uma política de eviction
- **Conteúdo**:
  - Cenário: assistente pessoal com 1 ano de interações
  - Em trios: escrever política de eviction combinando relevância e idade
  - Exemplo: "eventos com > 6 meses e score < 0.5 são arquivados"
  - Considerar: entidades críticas (pagamentos, prazos), frequência de recall, PII
  - 3 min discussão, 1 min compartilhar
- **Diagrama**: Template de política de eviction
- **Tempo**: 1.5 min

---

#### Slide 40 — [Transição] De Contexto para Recall
- **Tipo**: Seção
- **Objetivo**: Transição da gestão de contexto para memória vetorial
- **Conteúdo**: "Gestão de contexto resolve o curto prazo. E o longo prazo?"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

### SEÇÃO E — Memória Vetorial para Recall (Slides 41-50 · 12 min)

---

#### Slide 41 — [SEÇÃO] Memória Vetorial para Recall
- **Tipo**: Seção
- **Objetivo**: Transição para memória episódica via embeddings
- **Conteúdo**: "4 — Memória Vetorial para Recall"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 42 — Embedding de Eventos
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar como converter eventos em embeddings
- **Conteúdo**:
  - Cada evento (mensagem, ação, observação) → texto → embedding
  - Embedding = vetor de N dimensões (384, 768, 1536, 3072)
  - Modelos: OpenAI text-embedding-3-small/large, Cohere, BGE, E5
  - Armazenar: vector DB (Qdrant, Chroma, Pinecone, pgvector)
  - Metadata: timestamp, user_id, session_id, type, entities
  - Snippet de código: embed_event(event) → (vector, metadata)
- **Diagrama**: Evento → texto → embedding → vector DB
- **Tempo**: 1.5 min

---

#### Slide 43 — Recall por Similaridade Semântica
- **Tipo**: Conteúdo
- **Objetivo**: Explicar como recuperar memórias relevantes
- **Conteúdo**:
  - Query: converter pergunta atual em embedding
  - Buscar: top-K eventos mais similares (cosine similarity)
  - Reinsertir: colocar eventos recuperados no contexto do agente
  - Exemplo: usuário pergunta "como resolveu aquele bug de autenticação?" → recall de evento passado similar
  - Pós-recuperação: nem sempre o mais similar é o mais útil → re-ranking
- **Diagrama**: Query embedding → busca no vector DB → top-K → contexto
- **Tempo**: 1.5 min

---

#### Slide 44 — Metadata Filtering
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar como filtrar recall por metadata estruturada
- **Conteúdo**:
  - Vector search sozinho é insuficiente: "aquela reunião de terça"
  - Metadata filter: `session_id = X AND timestamp > Y AND type = "meeting"`
  - Combinação: filter por metadata + rank por similaridade
  - Padrão: pre-filter (filtra antes da busca) vs post-filter (filtra depois)
  - Vector DBs modernas suportam hybrid search (vector + structured)
- **Diagrama**: Pipeline: metadata filter → vector search → resultado filtrado
- **Tempo**: 1.5 min

---

#### Slide 45 — Pós-Recuperação: Re-ranking
- **Tipo**: Conteúdo
- **Objetivo**: Explicar por que o top-K do vector DB não é suficiente
- **Conteúdo**:
  - Vector search é rápido mas impreciso (aproximação)
  - Re-ranking: modelo separado re-avuala os top-K resultados
  - Modelos: Cohere Rerank, BGE Reranker, cross-encoder
  - Pipeline: vector search (top 20) → re-ranker (top 5) → contexto
  - Trade-off: re-ranking adiciona latência mas melhora precisão
- **Diagrama**: Funil: 1000 candidatos → 20 (vector) → 5 (re-rank) → contexto
- **Tempo**: 1 min

---

#### Slide 46 — Pipeline Completo de Recall
- **Tipo**: Diagrama
- **Objetivo**: Visualizar o pipeline end-to-end de recall episódico
- **Conteúdo**:
  - 1. Query atual → embedding
  - 2. Metadata filter (user, session, time range)
  - 3. Vector search (top-K candidatos)
  - 4. Re-ranking (top-N final)
  - 5. Inserção no contexto do agente
  - 6. Agente responde com memória recuperada
- **Diagrama**: Pipeline horizontal com 6 etapas
- **Animação**: Etapas aparecem sequencialmente
- **Tempo**: 1.5 min

---

#### Slide 47 — Qdrant/Chroma/Pinecone: Comparação
- **Tipo**: Comparação
- **Objetivo**: Comparar as principais opções de vector DB
- **Conteúdo**:
  - Qdrant: Rust, open-source, self-hosted ou cloud, alta performance
  - Chroma: Python, easy setup, ideal para protótipos
  - Pinecone: managed, serverless, escala automática
  - pgvector: extensão PostgreSQL, unifica relacional + vetorial
  - Critério: managed vs self-hosted, escala, custo, latência, hybrid search
- **Diagrama**: Tabela comparativa
- **Tempo**: 1.5 min

---

#### Slide 48 — Lab 2: Memória Episódica
- **Tipo**: Código
- **Objetivo**: Apresentar o laboratório de memória episódica
- **Conteúdo**:
  - Lab 2 (5h): "Memória episódica"
  - Agente recorda interações anteriores relevantes via recall vetorial
  - Comparar agente com e sem memória em sessões espaçadas
  - Stack: LangGraph + Qdrant + OpenAI embeddings
  - Referência: `05-Labs/ETHAGT05/Lab2-Memoria-Episodica`
- **Diagrama**: Arquitetura do lab
- **Tempo**: 1 min

---

#### Slide 49 — Pergunta: Embedding ou Metadata?
- **Tipo**: Exercício
- **Objetivo**: Praticar a escolha entre recall semântico e filtro estruturado
- **Conteúdo**:
  - "Se o usuário pergunta 'aquela reunião de terça' — embedding ou metadata?"
  - Resposta: ambos! Metadata filter (dia da semana) + vector search (tópico)
  - "E se pergunta 'como configurar deploy?' — embedding ou metadata?"
  - Resposta: embedding (semântico) + filter por type="procedural"
  - "E se pergunta 'qual o saldo da conta?' — embedding ou metadata?"
  - Resposta: nenhum! KB relacional, não vector DB
  - Discussão aberta (2 min)
- **Tempo**: 2 min

---

#### Slide 50 — [Transição] De Episódica para Semântica
- **Tipo**: Seção
- **Objetivo**: Transição de memória episódica para consolidação semântica
- **Conteúdo**: "Eventos acumulados viram conhecimento?"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

### SEÇÃO F — Memória Semântica e Grafos (Slides 51-57 · 8 min)

---

#### Slide 51 — [SEÇÃO] Memória Semântica e Grafos
- **Tipo**: Seção
- **Objetivo**: Transição para consolidação e knowledge graphs
- **Conteúdo**: "5 — Memória Semântica e Grafos"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 52 — Consolidação: Episódica → Semântica
- **Tipo**: Diagrama
- **Objetivo**: Mostrar como eventos episódicos viram fatos semânticos
- **Conteúdo**:
  - Consolidação: processo de extrair fatos de eventos acumulados
  - Analogia biológica: consolidação da memória durante o sono
  - Em agentes: processo offline ou em batch que:
    1. Agrupa eventos relacionados
    2. Extrai fatos consolidados
    3. Remove redundância
    4. Promove para KB semântica
  - Exemplo: 5 eventos "João perguntou sobre Python" → fato "João é desenvolvedor Python"
- **Diagrama**: Eventos episódicos → processo de consolidação → fatos semânticos
- **Animação**: Eventos convergem para fatos
- **Tempo**: 1.5 min

---

#### Slide 53 — Quando Promover uma Memória?
- **Tipo**: Conteúdo
- **Objetivo**: Definir critérios para consolidação
- **Conteúdo**:
  - Nem todo evento vira fato — critérios de promoção:
    - Frequência: evento recorrente (múltiplas ocorrências)
    - Confiança: fonte confiável ou confirmado múltiplas vezes
    - Estabilidade: fato não muda frequentemente
    - Utilidade: fato será relevante em sessões futuras
  - Quando NÃO promover:
    - Eventos únicos e sem valor futuro
    - Fatos voláteis (saldo bancário, status de tarefa)
    - Informação sensível (PII desnecessária)
- **Diagrama**: Checklist de critérios de promoção
- **Tempo**: 1 min

---

#### Slide 54 — Knowledge Graph como Memória
- **Tipo**: Diagrama
- **Objetivo**: Apresentar KG como camada de memória estruturada
- **Conteúdo**:
  - KG = grafo de entidades + relações + atributos
  - Exemplo: (João) --[trabalha_em]--> (Projeto X) --[usa]--> (Python)
  - Vantagens: consulta estruturada, raciocínio multi-hop, explicitação de relações
  - Integração com LLM: GraphRAG, Cypher + LLM, text-to-graph
  - Profundidade em ETHAGT07 — Knowledge Graphs para Agentes
- **Diagrama**: Mini knowledge graph com 5 nós e relações
- **Tempo**: 1.5 min

---

#### Slide 55 — Exemplo: De Evento para Fato
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar um exemplo concreto de consolidação
- **Conteúdo**:
  - Eventos episódicos (vector DB):
    - "João perguntou sobre decorators em Python" (12/jan)
    - "João pediu ajuda com asyncio" (25/jan)
    - "João compartilhou repositório de FastAPI" (03/fev)
  - Consolidação → Fato semântico (KB):
    - "João é desenvolvedor Python (nível intermediário-avançado)"
    - Interesses: decorators, asyncio, FastAPI
  - Ação: agente agora *sabe* quem é João sem precisar recordar cada evento
- **Diagrama**: 3 eventos → seta de consolidação → 1 perfil semântico
- **Tempo**: 1 min

---

#### Slide 56 — Generative Agents: Memória de Smallville
- **Tipo**: Citação
- **Objetivo**: Mostrar o caso canônico de memória em agentes
- **Conteúdo**:
  - Park et al. (arXiv:2304.03442): 25 agentes em Smallville
  - Cada agente tem:
    - Memory stream: log de observações com timestamp
    - Retrieval: por recência + importância + relevância
    - Reflection: consolida eventos em insights de alto nível
  - Resultado: agentes "lembram", planejam, socializam de forma emergente
  - Lição: a arquitetura de memória *é* a identidade do agente
- **Diagrama**: Memory stream de um agente de Smallville
- **Tempo**: 1 min

---

#### Slide 57 — Integração com KG (Preview ETHAGT07)
- **Tipo**: Conteúdo
- **Objetivo**: Conectar com o próximo módulo de Knowledge Graphs
- **Conteúdo**:
  - ETHAGT07 aprofunda: GraphRAG, ontologias, raciocínio multi-hop
  - Memória semântica + KG = raciocínio estruturado de longo prazo
  - Exemplo: "Quem trabalha com Python e está livre na semana 20?" → query no KG
  - Padrão: vector DB para recall + KG para raciocínio + relacional para fatos transacionais
- **Diagrama**: 3 camadas: Vector DB | Knowledge Graph | Relacional
- **Tempo**: 0.5 min

---

### SEÇÃO G — Produção: Consistência, Privacidade, Custo (Slides 58-63 · 8 min)

---

#### Slide 58 — [SEÇÃO] Produção: Consistência, Privacidade, Custo
- **Tipo**: Seção
- **Objetivo**: Transição para os desafios de produção
- **Conteúdo**: "6 — Produção: Consistência, Privacidade, Custo"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 59 — Consistência em Multi-Agente
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar os desafios de memória compartilhada entre agentes
- **Conteúdo**:
  - Múltiplos agentes compartilham memória → problemas de concorrência
  - Race condition: agente A lê fato, agente B atualiza, A usa fato desatualizado
  - Estratégias:
    - Eventual consistency: aceitar defasagem (mais simples)
    - Strong consistency: locks / transações (mais caro)
    - Event sourcing: log de mudanças (auditável)
  - Padrão: cada agente tem memória local + memória compartilhada via message bus
- **Diagrama**: 3 agentes + memória compartilhada com locks
- **Tempo**: 1.5 min

---

#### Slide 60 — PII em Memória: Redação e Retenção
- **Tipo**: Conteúdo
- **Objetivo**: Lidar com dados pessoais em memória de longo prazo
- **Conteúdo**:
  - Memória acumula PII: nomes, emails, preferências, histórico
  - Riscos: vazamento, profiling, inferência indevida
  - Redação: mascarar PII antes de armazenar (NER + replacement)
  - Retenção: definir TTL por tipo de dado (ex.: conversas = 90 dias, perfil = até consentimento)
  - Compliance: LGPD/GDPR exigem minimização de dados
- **Diagrama**: Pipeline: evento → NER → redação → armazenamento seguro
- **Tempo**: 1.5 min

---

#### Slide 61 — Direito ao Esquecimento em Memória Vetorial
- **Tipo**: Conteúdo
- **Objetivo**: Discutir como implementar "esquecer" em vector DB
- **Conteúdo**:
  - Desafio: "esquecer tudo sobre o usuário X" em vector DB
  - Problema: embeddings não são reversíveis — não dá para "apagar" um fato de um embedding
  - Estratégias:
    - Delete por metadata: `WHERE user_id = X` (se metadata foi armazenada)
    - Re-embed: remover evento e re-gerar sumários consolidados
    - Cryptographic erasure: encriptar por usuário, destruir chave
  - Pergunta: *Como implementar direito ao esquecimento em memória vetorial?*
- **Diagrama**: 3 estratégias lado a lado
- **Tempo**: 1.5 min

---

#### Slide 62 — Custo de Memória vs Benefício
- **Tipo**: Conteúdo
- **Objetivo**: Critério para decidir quando NÃO memorizar
- **Conteúdo**:
  - Memória não é grátis: storage, embedding, recall, contexto adicional
  - Pergunta-chave: "esta memória vai melhorar uma decisão futura?"
  - Quando NÃO memorizar:
    - Eventos sem valor futuro ("qual a temperatura agora?")
    - Informação facilmente recalculável ("saldo atual")
    - Dados que mudam rápido demais para consolidar
    - Conteúdo sem consentimento do usuário
  - Regra: melhor memória mínima e útil que memória máxima e ruidosa
- **Diagrama**: Matriz custo × benefício de memória
- **Tempo**: 1 min

---

#### Slide 63 — Observabilidade de Memória
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar que memória precisa de observabilidade própria
- **Conteúdo**:
  - Memória é um sistema — precisa de monitoring:
    - Quem acessou qual memória, quando?
    - Hit rate do recall (quantos recalls retornam algo útil?)
    - Latência do recall
    - Custo de storage vs custo de recall
    - Drift: a memória está desatualizada?
  - Ferramentas: LangSmith (memory traces), dashboards custom, audit logs
  - Profundidade em ETHAGT12 — AgentOps
- **Diagrama**: Dashboard de memória com métricas
- **Tempo**: 1 min

---

### SEÇÃO H — Fechamento (Slides 64-70 · 17 min)

---

#### Slide 64 — Boas Práticas (DO)
- **Tipo**: Conteúdo
- **Objetivo**: Checklist de boas práticas de memória
- **Conteúdo**:
  - Comece com working memory + checkpointer (antes de vector DB)
  - Modele estado serializável desde o dia 1
  - Use thread_id consistente (conversa = thread)
  - Versione o schema de estado (`schema_version`)
  - Combine vector + metadata (não use só similaridade)
  - Defina política de eviction desde o início
  - Redação de PII antes de armazenar
  - Observe a memória (hit rate, latência, drift)
- **Diagrama**: Checklist verde (etho-success)
- **Tempo**: 2 min

---

#### Slide 65 — Anti-Patterns (DON'T)
- **Tipo**: Conteúdo
- **Objetivo**: Checklist do que NÃO fazer em memória
- **Conteúdo**:
  - Encher context window até estourar (sem gestão ativa)
  - Usar vector DB para tudo (quando relacional bastava)
  - Não versionar schema de estado (quebra no resume)
  - Armazenar PII sem redação
  - Sem política de eviction (memória cresce infinitamente)
  - Confiar cegamente no recall (sem re-ranking)
  - Misturar memória de usuários diferentes (cross-contamination)
  - Sem observabilidade de memória ("caixa preta" de longo prazo)
  - Promover tudo para semântica (sem critério de consolidação)
- **Diagrama**: Checklist vermelho (etho-danger)
- **Tempo**: 2 min

---

#### Slide 66 — Resumo da Aula
- **Tipo**: Resumo
- **Objetivo**: Sintetizar os pontos-chave
- **Conteúdo**:
  - 4 camadas de memória: working (context window), episódica (vector DB), semântica (KB/KG), procedural (skills)
  - Checkpointer = persistência de estado (Postgres/SQLite/Redis) → resume, replay, branching
  - Gerenciamento de contexto: janela deslizante, sumarização em cascata, eviction por relevância, entity-centric
  - Memória vetorial: embedding + metadata filter + re-ranking = recall episódico
  - Consolidação: episódica → semântica (com critérios de promoção)
  - Produção: consistência, PII, direito ao esquecimento, custo vs benefício, observabilidade
  - MemGPT e Generative Agents como referências canônicas
- **Diagrama**: 7 ícones com os pontos-chave
- **Tempo**: 2 min

---

#### Slide 67 — Quiz: Pergunta 1
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "Qual tipo de memória é mais apropriado para 'o usuário prefere respostas em português'?"
  - A) Working memory (context window)
  - B) Memória episódica (vector DB)
  - C) Memória semântica (KB / perfil)
  - D) Memória procedural (skills)
  - Resposta: C — é um fato estável sobre o usuário, não um evento
- **Tempo**: 1 min

---

#### Slide 68 — Quiz: Pergunta 2
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "O que acontece se o schema de estado mudar e um checkpoint antigo for carregado?"
  - A) Erro 500 e crash do agente
  - B) O agente ignora campos novos e continua
  - C) Depende — sem versionamento, quebra; com migração lazy, funciona
  - D) O checkpointer reescreve o estado automaticamente
  - Resposta: C — sem versionamento, campos novos podem causar erro; com migração lazy, o estado é convertido no load
- **Tempo**: 1 min

---

#### Slide 69 — Quiz: Pergunta 3
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "Usuário pede: 'lembra daquela conversa sobre deploy na semana passada?' Qual estratégia de recall usar?"
  - A) Apenas vector search (similaridade semântica com "deploy")
  - B) Apenas metadata filter (timestamp da semana passada)
  - C) Metadata filter (tempo) + vector search (tópico) + re-ranking
  - D) Sumarização em cascata
  - Resposta: C — combinar filtro temporal com busca semântica e re-ranking para precisão
- **Tempo**: 1 min

---

#### Slide 70 — Conexão, Projeto e Q&A
- **Tipo**: Capa
- **Objetivo**: Conectar com próximos módulos, apresentar projeto e encerrar
- **Conteúdo**:
  - Próximos módulos:
    - ETHAGT06 — RAG Agêntico (memória + recuperação combinados)
    - ETHAGT07 — Knowledge Graphs (memória semântica aprofundada)
    - ETHAGT14 — Escalabilidade (memória em produção multi-tenant)
  - Projeto do módulo: projetar memória de agente pessoal de longo prazo (4 camadas + ADR + política de privacidade/evicção)
  - Labs: Lab 1 (Checkpointer em Postgres, 4h) · Lab 2 (Memória Episódica, 5h)
  - Leitura: Packer et al. *MemGPT* (arXiv:2310.08560)
  - "Perguntas?"
  - Contato do professor
- **Diagrama**: Logo Etho + fundo etho-dark
- **Tempo**: 4 min

---

## Resumo do Storyboard

| Seção | Slides | Tempo | Conteúdo |
|---|---|---|---|
| A — Abertura | 1-6 | 8 min | Capa, objetivos, competências, agenda, motivação, contexto |
| B — Tipos de Memória | 7-16 | 12 min | Working, episódica, semântica, procedural, 4 camadas, MemGPT |
| C — Checkpointer | 17-29 | 15 min | Estado persistente, backends, resume, replay, branching, DEMO |
| D — Gerenciamento de Contexto | 30-40 | 10 min | Custo, sumarização, eviction, entity-centric memory, exercício |
| E — Memória Vetorial | 41-50 | 12 min | Embedding, recall, metadata filtering, re-ranking, pipeline, lab |
| F — Semântica e Grafos | 51-57 | 8 min | Consolidação, KG, Generative Agents, Smallville |
| G — Produção | 58-63 | 8 min | Consistência, PII, direito ao esquecimento, custo, observabilidade |
| H — Fechamento | 64-70 | 17 min | Boas práticas, anti-patterns, resumo, quiz, conexão, projeto, Q&A |
| **Total** | **70** | **90 min** | |

---

## Diagramas Necessários

| # | Slide | Diagrama | Tipo | Fonte |
|---|---|---|---|---|
| D1 | 9 | Recall accuracy vs posição no contexto (curva U) | Gráfico | "Lost in the Middle" (arXiv:2307.03172) |
| D2 | 13 | Comparação 4 camadas de memória | Tabela comparativa | Novo |
| D3 | 14 | As 4 camadas de memória (integrado) | Flowchart | `12-Diagrams/ETHAGT05/memory-layers.mmd` |
| D4 | 16 | MemGPT: analogia SO (RAM vs disco) | Analogia visual | arXiv:2310.08560 |
| D5 | 22 | Comparação de backends (Postgres/SQLite/Redis) | Tabela comparativa | Novo |
| D6 | 24 | Checkpointer resume (pause/retomar) | Flowchart | `12-Diagrams/ETHAGT05/checkpointer-resume.mmd` |
| D7 | 26 | Branching: árvore de checkpoints | Git graph | Novo |
| D8 | 34 | Sumarização em cascata | Pirâmide invertida | Novo |
| D9 | 36 | Eviction flow (relevância × idade) | Flowchart | `12-Diagrams/ETHAGT05/eviction-flow.mmd` |
| D10 | 37 | Entity-centric memory (page-in/page-out) | Diagrama de entidades | MemGPT / Zep |
| D11 | 46 | Pipeline completo de recall vetorial | Pipeline horizontal | Novo |
| D12 | 52 | Consolidação: episódica → semântica | Transformação | Novo |
| D13 | 54 | Knowledge graph como memória | Grafo de entidades | Novo (preview ETHAGT07) |
| D14 | 56 | Memory stream de Generative Agents | Timeline | arXiv:2304.03442 |
| D15 | 59 | Consistência em multi-agente | Diagrama de concorrência | Novo |
| D16 | 61 | Direito ao esquecimento (3 estratégias) | Comparação | Novo |

---

## Pendências de Produção

- [ ] Produzir 11 diagramas novos (D1, D2, D4, D5, D7, D8, D10, D11, D12, D13, D14, D15, D16)
- [ ] Screenshot do demo de checkpointer em Postgres (Slide 28)
- [ ] Screenshot do código com syntax highlighting (Slides 20, 28, 48)
- [ ] Imagem de fundo para capa (Slide 1)
- [ ] Badge de competências (Slide 3)
- [ ] Timeline de marcos históricos de memória (Slide 6)
- [ ] Gráfico "Lost in the Middle" — curva U (Slide 9)
- [ ] Dashboard de observabilidade de memória (Slide 63)

---

> **Aguardando aprovação deste storyboard para gerar os slides detalhados com notas do professor.**
