# ETHAGT06 — RAG Agêntico
## Storyboard da Apresentação

> **Universidade Etho · Especialização em Programação Agêntica**
> Fase B — RAG Avançado · 30 h
> Storyboard v1.0 · Julho 2026

---

## Metadados da Apresentação

| Campo | Valor |
|---|---|
| Código | ETHAGT06 |
| Título | RAG Agêntico (Adaptive · Corrective · Self-RAG · Agentic) |
| Duração estimada | 110 min (2 blocos de ~55 min + intervalo) |
| Total de slides | 85 |
| Público | Arquitetos, Engenheiros de Software, Engenheiros de IA, Cientistas de Dados, Tech Leads |
| Pré-requisitos | ETHAGT04 (RAG Systems do Framework Etho recomendado) |
| Competências | C1 (A), C3 (B), C4 (I), C5 (I) |

---

## Mapa Visual da Apresentação

```
BLOCO 1 (~58 min)                            BLOCO 2 (~52 min)
┌──────────────────────────────┐              ┌──────────────────────────────┐
│ SEÇÃO A — Abertura (8 min)   │              │ SEÇÃO F — Agentic RAG (15 m) │
│  Capa · Objetivos · Agenda   │              │  Multi-hop · Multi-source    │
│  Motivação · Contexto        │              │  GraphRAG · DEMO multi-hop   │
├──────────────────────────────┤              ├──────────────────────────────┤
│ SEÇÃO B — RAG Ingênuo (10m)  │              │ SEÇÃO G — Qualidade (15 min) │
│  4 tipos de falha · Mitos    │              │  Chunking · Re-rank · HyDE   │
│  Vector DB resolve tudo?     │              │  Hybrid · Multi-vector       │
├──────────────────────────────┤              ├──────────────────────────────┤
│ SEÇÃO C — Adaptive RAG (12m) │              │ SEÇÃO H — Avaliação (10 min) │
│  Quando recuperar · Routing  │              │  Faithfulness · Ragas ·      │
│  Diagrama adaptive-rag       │              │  Diagrama eval-pipeline      │
├──────────────────────────────┤              ├──────────────────────────────┤
│ SEÇÃO D — CRAG (15 min)      │              │ SEÇÃO I — Fechamento (12 min)│
│  3 caminhos · Fallback web   │              │  Boas práticas · Anti-patterns│
│  Diagrama crag-flow          │              │  Quiz · Projeto · Q&A        │
├──────────────────────────────┤              └──────────────────────────────┘
│ SEÇÃO E — Self-RAG (13 min)  │
│  Tokens de reflexão ·        │
│  Treinado vs prompting       │
└──────────────────────────────┘
```

---

## Storyboard Detalhado

### SEÇÃO A — Abertura (Slides 1-7 · 8 min)

---

#### Slide 1 — Capa
- **Tipo**: Capa
- **Objetivo**: Identificar a aula, professor e contexto
- **Conteúdo**:
  - ETHAGT06 — RAG Agêntico (Adaptive · Corrective · Self-RAG · Agentic)
  - Universidade Etho · Especialização em Programação Agêntica
  - Fase B — RAG Avançado
  - Professor · Data
- **Diagrama**: Logo Etho + imagem de fundo abstrata (base de dados/neural retrieval)
- **Animação**: Fade in do título
- **Tempo**: 1 min

---

#### Slide 2 — Objetivos do Módulo
- **Tipo**: Conteúdo
- **Objetivo**: Deixar claro o que o aluno deve conseguir fazer ao final
- **Conteúdo**:
  - Objetivo geral: Evoluir além do RAG "ingênuo" para RAG agêntico, onde o agente decide *quando*, *o quê* e *como* recuperar
  - 5 objetivos específicos (1 linha cada):
    1. Diagnosticar limites do RAG ingênuo em produção
    2. Implementar Adaptive RAG, CRAG, Self-RAG e Agentic RAG
    3. Aplicar técnicas de qualidade: chunking, re-ranking, query rewriting, hybrid search
    4. Construir pipeline de avaliação de RAG (faithfulness, relevance, context recall/precision)
    5. Produzir um sistema RAG multi-tenant com segurança
  - Diferença RAG fixo vs RAG in-loop
- **Diagrama**: Ícones representando cada objetivo
- **Animação**: Aparecer objetivos um a um (on click)
- **Tempo**: 2 min

---

#### Slide 3 — Competências Desenvolvidas
- **Tipo**: Conteúdo
- **Objetivo**: Conectar a aula ao Framework Etho de competências
- **Conteúdo**:
  - Tabela: 4 competências com nível B/I/A
  - C1 Programação Agêntica → **A** (aprofundamento)
  - C3 MCP & Tool Use → B
  - C4 Agent Memory → **I** (induzido)
  - C5 AgentOps & Avaliação → **I** (induzido)
  - Badge visual por competência
- **Diagrama**: Radar chart dos 4 pilares
- **Animação**: Radar aparece com wipe
- **Tempo**: 1 min

---

#### Slide 4 — Agenda
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar o roteiro da aula com tempos
- **Conteúdo**:
  - Bloco 1: Abertura → RAG Ingênuo Falha → Adaptive RAG → CRAG → Self-RAG
  - Bloco 2: Agentic RAG → Engenharia de Qualidade → Avaliação → Fechamento
  - Tempos estimados por seção
- **Diagrama**: Timeline horizontal com 9 seções
- **Animação**: Timeline cresce da esquerda para direita
- **Tempo**: 1 min

---

#### Slide 5 — Pré-requisitos: ETHAGT04 e o Que Você Já Sabe
- **Tipo**: Conteúdo
- **Objetivo**: Ancorar a aula no conhecimento prévio de RAG
- **Conteúdo**:
  - ETHAGT04 cobriu: RAG básico, vector DBs, embeddings, pipeline retrieve→generate
  - O que você já deveria saber: cosine similarity, top-k retrieval, LangChain básico
  - O que esta aula adiciona: o agente entra no loop de recuperação
  - Você NÃO precisa ter feito ETHAGT04 se já pratica RAG em produção
- **Diagrama**: Ponte ETHAGT04 → ETHAGT06
- **Tempo**: 1 min

---

#### Slide 6 — Motivação: RAG "Funciona" Até Parar de Funcionar
- **Tipo**: Conteúdo
- **Objetivo**: Criar tensão — RAG ingênuo falha silenciosamente em produção
- **Conteúdo**:
  - Cenário real: pergunta "qual a política de férias para estagiários?" — recupera chunks errados, responde com info genérica
  - O usuário não sabe que a resposta está errada — confiança alta, grounding baixo
  - "Vector DB + top-k" parece funcionar na demo e quebra em produção
  - Pergunta: *Quantos de vocês já usaram RAG e obtiveram resposta errada com alta confiança?*
- **Diagrama**: Usuário feliz (demo) → Usuário frustrado (produção)
- **Animação**: Split — lado esquerdo (demo verde), depois lado direito (produção vermelho)
- **Tempo**: 1.5 min

---

#### Slide 7 — Contexto: Do RAG Fixo ao RAG In-Loop
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar a evolução histórica do RAG
- **Conteúdo**:
  - Linha do tempo: 2020 (RAG original, Lewis et al.) → 2023 (Self-RAG, Asai) → 2024 (CRAG, Yan) → 2024 (GraphRAG, Edge) → 2025 (Agentic RAG)
  - RAG fixo: query → retrieve → generate (pipeline rígido)
  - RAG agêntico: agente decide se/quando/o quê/como recuperar, com correção iterativa
  - 4 arquiteturas que veremos: Adaptive → CRAG → Self-RAG → Agentic
- **Diagrama**: Timeline horizontal com marcos (D1)
- **Animação**: Marcos aparecem sequencialmente
- **Tempo**: 0.5 min

---

### SEÇÃO B — Por que o RAG Ingênuo Falha (Slides 8-14 · 10 min)

---

#### Slide 8 — [SEÇÃO] Por que o RAG Ingênuo Falha
- **Tipo**: Seção
- **Objetivo**: Transição para o diagnóstico de falhas
- **Conteúdo**: Número "1" grande + "Por que o RAG Ingênuo Falha"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 9 — O Pipeline do RAG Ingênuo
- **Tipo**: Diagrama
- **Objetivo**: Mostrar o pipeline canônico e onde ele quebra
- **Conteúdo**:
  - Pipeline: query → embed → vector search (top-k) → stuff into prompt → generate
  - Cada etapa tem pontos de falha:
    - Embed: sinônimos não capturados
    - Search: top-k traz irrelevante junto com relevante
    - Stuff: contexto quebrado, janela estourada
    - Generate: alucinação sobre docs ruins
  - Fonte: arXiv:2005.11401 (RAG original, Lewis et al.)
- **Diagrama**: `12-Diagrams/ETHAGT06/` — pipeline com pontos de falha destacados (D2)
- **Animação**: Cada etapa acende, depois pontos de falha aparecem em vermelho
- **Tempo**: 2 min

---

#### Slide 10 — Falha 1: Chunking Quebra Contexto
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar que o chunking ingênuo (tamanho fixo) destrói semântica
- **Conteúdo**:
  - Chunking por tamanho fixo (ex.: 512 tokens) corta no meio de uma ideia
  - Exemplo: política de férias dividida entre dois chunks — nenhum faz sentido sozinho
  - Sobreposição (overlap) ajuda mas não resolve
  - Consequência: embedding captura fragmento sem contexto → recuperação irrelevante
  - Preview da solução: chunking semântico, hierárquico, late-chunking (Seção G)
- **Diagrama**: Documento cortado ao meio com contexto perdido (D3)
- **Tempo**: 1.5 min

---

#### Slide 11 — Falha 2: Embedding Não Captura Semântica
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar que embeddings têm limites semânticos
- **Conteúdo**:
  - Embedding captura similaridade lexical, não raciocínio
  - Exemplo: "férias de estagiário" vs "licença de aprendiz" — semanticamente equivalentes, lexicalmente diferentes
  - Multilingual: mesma ideia em PT vs EN pode ter embeddings distantes
  - Dados tabulares: embeddings de texto não captura estrutura de tabela
  - Preview da solução: query rewriting, HyDE, hybrid search (Seção G)
- **Diagrama**: Dois pontos no espaço vetorial distantes mas semanticamente iguais (D3)
- **Tempo**: 1.5 min

---

#### Slide 12 — Falha 3: Sem Re-Rank, Top-k Traz Lixo
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar que top-k puro mistura relevante com irrelevante
- **Conteúdo**:
  - Top-k retorna os k mais similares — nem todos são relevantes
  - Sem re-rank: o chunk #1 pode ser irrelevante e "afogar" os bons
  - LLM recebe contexto poluído → alucinação ou confusão
  - Exemplo: top-5 traz 1 chunk bom e 4 irrelevantes
  - Preview da solução: re-ranking com Cohere, bge, Jina (Seção G)
- **Diagrama**: Top-5 resultados com 1 verde e 4 vermelhos (D3)
- **Tempo**: 1.5 min

---

#### Slide 13 — Falha 4: Sem Avaliação, Você Está Cego
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar que sem métricas não há como saber se o RAG está bom
- **Conteúdo**:
  - "Funciona na minha máquina" ≠ funciona em produção
  - Sem métricas: melhoria é adivinhação
  - Métricas que importam: faithfulness, answer relevance, context precision/recall
  - Sem dataset de holdout: não há como detectar regressão
  - Preview da solução: Ragas, TruLens, DeepEval (Seção H)
- **Diagrama**: Pessoa vendada tentando melhorar RAG (D3)
- **Tempo**: 1.5 min

---

#### Slide 14 — O Mito "Vector DB Resolve Tudo" + Casos Problemáticos
- **Tipo**: Comparação
- **Objetivo**: Desconstruir o mito e mostrar casos onde RAG ingênuo falha
- **Conteúdo**:
  - O mito: "só joga no vector DB e funciona"
  - A realidade: vector DB é uma peça, não a solução
  - Casos problemáticos:
    - Dados tabulares: embeddings não capturam estrutura de tabela
    - Multilingual: mesma ideia em idiomas diferentes → distância vetorial alta
    - Multi-modal: texto + imagem + tabela exigem estratégias diferentes
  - Pergunta: *Qual o pior tipo de falha — não responder ou responder errado com confiança?*
- **Diagrama**: 3 casos problemáticos em grid (D4)
- **Animação**: Casos aparecem um a um
- **Tempo**: 1.5 min

---

### SEÇÃO C — Adaptive RAG (Slides 15-23 · 12 min)

---

#### Slide 15 — [SEÇÃO] Adaptive RAG
- **Tipo**: Seção
- **Objetivo**: Transição para a primeira evolução do RAG
- **Conteúdo**: "2 — Adaptive RAG: Decidir Quando Recuperar"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 16 — A Ideia: Decidir Quando Recuperar
- **Tipo**: Comparação
- **Objetivo**: Mostrar que nem toda pergunta precisa de retrieval
- **Conteúdo**:
  - RAG ingênuo: SEMPRE recupera, mesmo para "Quem é o presidente do Brasil?"
  - Adaptive RAG: classificador decide se precisa recuperar
  - Três caminhos:
    - Não precisa → responder direto (LLM puro)
    - Pergunta simples → recuperar top-3
    - Pergunta complexa → recuperar + query rewrite
  - Benefício: menos latência e custo em perguntas triviais
- **Diagrama**: Comparação "sempre recupera" vs "decide se recupera"
- **Tempo**: 1.5 min

---

#### Slide 17 — Decidir Quanto Recuperar
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar que a quantidade de chunks deve ser dinâmica
- **Conteúdo**:
  - Top-k fixo (ex.: sempre 5) é subótimo
  - Pergunta factual: 1-2 chunks bastam
  - Pergunta analítica: 5-10 chunks podem ser necessários
  - Estratégia: classificar complexidade → ajustar k dinamicamente
  - Trade-off: mais chunks = mais contexto = mais custo + mais ruído
- **Diagrama**: Sliding scale de k (1 → 10) com tipos de pergunta
- **Tempo**: 1.5 min

---

#### Slide 18 — Estratégias de Routing por Complexidade
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar estratégias de classificação de perguntas
- **Conteúdo**:
  - Routing por regras: keywords, comprimento da pergunta
  - Routing por LLM: classificador zero-shot ("esta pergunta precisa de retrieval?")
  - Routing por complexidade: simples / média / complexa
  - Routing por fonte: base local vs web vs KG
  - LangGraph: `RouteQuery` node com conditional edges
- **Diagrama**: Árvore de decisão de routing
- **Tempo**: 1.5 min

---

#### Slide 19 — Diagrama: Adaptive RAG
- **Tipo**: Diagrama
- **Objetivo**: Visualizar o fluxo completo do Adaptive RAG
- **Conteúdo**:
  - Fluxo: pergunta → classificador → (direto | simples | complexa) → gerar → resposta
  - Classificador decide: responder direto, retrieve top-3, ou retrieve + query rewrite
  - Fonte: LangGraph examples — `adaptive_rag`
- **Diagrama**: `12-Diagrams/ETHAGT06/adaptive-rag.mmd` (D5)
- **Animação**: Caminhos acendem um a um a partir do classificador
- **Tempo**: 2 min

---

#### Slide 20 — Exemplo Prático: Quando Responder Direto
- **Tipo**: Comparação
- **Objetivo**: Concretizar a decisão com exemplos reais
- **Conteúdo**:
  - "Quem é o presidente do Brasil?" → responder direto (conhecimento paramétrico)
  - "Qual a política de férias para estagiários?" → recuperar (conhecimento específico)
  - "Compare a política de férias de 2023 com a de 2024" → recuperar + query rewrite
  - O classificador pode errar — por isso CRAG existe (próxima seção)
- **Diagrama**: 3 cards com exemplos e decisões
- **Tempo**: 1.5 min

---

#### Slide 21 — Implementação: Classificador com LangGraph
- **Tipo**: Código
- **Objetivo**: Mostrar como implementar o Adaptive RAG
- **Conteúdo**:
  - LangGraph StateGraph com nós: `route_query`, `retrieve`, `generate`
  - Edge condicional: `route_query` → `generate` (direto) ou `retrieve` (precisa retrieval)
  - Snippet: `structured_output` com Pydantic para classificar
  - Query rewrite node para perguntas complexas
  - Referência: LangGraph `adaptive_rag` example
- **Diagrama**: `12-Diagrams/ETHAGT06/adaptive-rag.mmd` sobreposto ao código (D6)
- **Tempo**: 2 min

---

#### Slide 22 — Limitações do Adaptive RAG
- **Tipo**: Conteúdo
- **Objetivo**: Ser honesto sobre os trade-offs
- **Conteúdo**:
  - O classificador pode errar (falso negativo: não recupera quando deveria)
  - Não avalia a qualidade dos docs recuperados — confia cegamente
  - Não tem fallback se a base local não tem a resposta
  - Não corrige: se recuperou lixo, gera com lixo
  - → Motivação para CRAG (próxima seção)
- **Diagrama**: Lista de limitações com ícones de alerta
- **Tempo**: 1 min

---

#### Slide 23 — Exercício Rápido: Responder Direto ou Recuperar?
- **Tipo**: Exercício
- **Objetivo**: Praticar a decisão de routing
- **Conteúdo**:
  - 5 perguntas rápidas — votar: "direto" ou "recuperar":
    1. "O que é Python?" → direto
    2. "Qual a política de home office da Etho?" → recuperar
    3. "Quem escreveu Dom Casmurro?" → direto
    4. "Compare as APIs de dois produtos internos" → recuperar + rewrite
    5. "Qual a temperatura de ebulição da água?" → direto
  - Votação rápida (mãos levantadas)
- **Diagrama**: 5 cards com perguntas
- **Tempo**: 0.5 min

---

### SEÇÃO D — Corrective RAG / CRAG (Slides 24-34 · 15 min)

---

#### Slide 24 — [SEÇÃO] Corrective RAG (CRAG)
- **Tipo**: Seção
- **Objetivo**: Transição para a correção de recuperação
- **Conteúdo**: "3 — Corrective RAG (CRAG): Avaliar Antes de Confiar"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 25 — A Ideia: Avaliar Antes de Confiar
- **Tipo**: Comparação
- **Objetivo**: Mostrar que CRAG adiciona um avaliador de relevância
- **Conteúdo**:
  - Adaptive RAG: decide SE recuperar, mas confia nos docs recuperados
  - CRAG: recupera, AVALIA a relevância dos docs, e corrige se necessário
  - Três caminhos após avaliação:
    1. Docs relevantes → usar e gerar
    2. Docs parcialmente relevantes → refinar (knowledge refinement)
    3. Docs irrelevantes → buscar na web (fallback)
  - Fonte: Yan et al., arXiv:2401.15884
- **Diagrama**: Adaptive (confia) vs CRAG (avalia) (D7)
- **Tempo**: 1.5 min

---

#### Slide 26 — O Retrieval Evaluator (Grau de Relevância)
- **Tipo**: Conteúdo
- **Objetivo**: Explicar como o avaliador classifica os docs
- **Conteúdo**:
  - Avaliador: LLM ou modelo leve que classifica cada doc recuperado
  - Três classes de relevância: `correto` / `ambíguo` / `incorreto`
  - Score de relevância agregado decide o caminho:
    - Maioria correta → usar
    - Mistura → refinar
    - Maioria incorreta → web search
  - Implementação: prompt estruturado ou modelo fine-tuned
- **Diagrama**: Avaliador classificando docs em 3 buckets
- **Tempo**: 2 min

---

#### Slide 27 — Três Caminhos: Usar / Corrigir / Web
- **Tipo**: Diagrama
- **Objetivo**: Visualizar os três caminhos do CRAG
- **Conteúdo**:
  - Caminho 1 (relevante): usar docs diretamente → gerar resposta
  - Caminho 2 (ambíguo): knowledge refinement — extrair apenas partes relevantes
  - Caminho 3 (irrelevante): web search como fallback → gerar com web results
  - Trigger de fallback: quando a base local não tem a resposta
- **Diagrama**: Fluxograma com 3 ramificações (D7)
- **Animação**: Ramificações aparecem uma a uma
- **Tempo**: 1.5 min

---

#### Slide 28 — Diagrama: CRAG Flow
- **Tipo**: Diagrama
- **Objetivo**: Visualizar o fluxo completo do CRAG
- **Conteúdo**:
  - Fluxo: query → retrieve (KB local) → avaliador → (sim/ambíguo/não) → gerar → resposta
  - O avaliador é o coração do CRAG
  - Web search só é acionado quando docs locais são irrelevantes
  - Fonte: arXiv:2401.15884; LangGraph example `crag`
- **Diagrama**: `12-Diagrams/ETHAGT06/crag-flow.mmd` (D7)
- **Animação**: Caminhos acendem um a um a partir do avaliador
- **Tempo**: 2 min

---

#### Slide 29 — Caminho 1: Usar (Docs Relevantes)
- **Tipo**: Conteúdo
- **Objetivo**: Detalhar o caminho "feliz" do CRAG
- **Conteúdo**:
  - Avaliador classifica como `correto` → docs vão direto para geração
  - Equivale ao RAG ingênuo, mas com confirmação de qualidade
  - É o caminho mais comum quando a base é boa e a pergunta é clara
  - Latência: mínima (só o overhead do avaliador)
- **Diagrama**: Caminho verde no fluxograma
- **Tempo**: 1 min

---

#### Slide 30 — Caminho 2: Corrigir (Docs Parciais) — Knowledge Refinement
- **Tipo**: Conteúdo
- **Objetivo**: Detalhar o caminho de correção
- **Conteúdo**:
  - Avaliador classifica como `ambíguo` → docs têm partes relevantes e irrelevantes
  - Knowledge refinement: extrair apenas as partes relevantes de cada doc
  - Técnicas: decompose em sentenças, re-avaliar, filtrar
  - Resultado: contexto limpo para o gerador
  - Trade-off: mais um step de LLM = mais latência e custo
- **Diagrama**: Doc bruto → filtro → doc limpo
- **Tempo**: 1.5 min

---

#### Slide 31 — Caminho 3: Web Search (Docs Irrelevantes) — Fallback
- **Tipo**: Conteúdo
- **Objetivo**: Detalhar o fallback para web
- **Conteúdo**:
  - Avaliador classifica como `incorreto` → base local não tem a resposta
  - Web search: usar Tavily, SerpAPI, ou busca nativa do modelo
  - Combinar web results com qualquer fragmento útil dos docs locais
  - Quando ativa: base desatualizada, pergunta sobre evento recente, gap de cobertura
  - Pergunta: *Quando CRAG decide buscar na web? Quando o avaliador diz "incorreto"*
- **Diagrama**: Base local (vazia) → Web search → resposta
- **Tempo**: 1.5 min

---

#### Slide 32 — Implementação: O Avaliador em Código
- **Tipo**: Código
- **Objetivo**: Mostrar como implementar o retrieval evaluator
- **Conteúdo**:
  - Snippet: função `grade_documents(state)` que classifica cada doc
  - Pydantic model: `GradeDocuments` com `binary_score: "yes" | "no"`
  - LangGraph node: `grade_documents` → conditional edge → `generate` | `web_search`
  - Referência: LangGraph `crag` example
- **Diagrama**: Code block com highlight no avaliador
- **Tempo**: 2 min

---

#### Slide 33 — Comparação: RAG Ingênuo vs CRAG
- **Tipo**: Comparação
- **Objetivo**: Sistematizar os ganhos do CRAG
- **Conteúdo**:
  - Tabela comparativa:
    - RAG ingênuo: confia cegamente, sem fallback, sem avaliação
    - CRAG: avalia relevância, refina se parcial, web se irrelevante
  - Custo: CRAG adiciona 1-2 chamadas de LLM (avaliador + possível refinement)
  - Ganho: respostas com grounding muito maior
  - Quando NÃO usar CRAG: latência crítica e base de alta qualidade
- **Diagrama**: Tabela comparativa colorida
- **Tempo**: 0.5 min

---

#### Slide 34 — Quando CRAG Brilha e Quando Falha
- **Tipo**: Conteúdo
- **Objetivo**: Dar critérios práticos de uso
- **Conteúdo**:
  - Brilha: base com cobertura parcial, perguntas diversas, dados que envelhecem
  - Falha: avaliador erra (falso positivo de relevância), web search retorna lixo
  - Melhoria: combinar CRAG com re-ranking (Seção G)
  - Limitação: não reflete sobre a PRÓPRIA resposta — isso é Self-RAG (próxima seção)
- **Diagrama**: Prós e contras em duas colunas
- **Tempo**: 0.5 min

---

### SEÇÃO E — Self-RAG (Slides 35-44 · 13 min)

---

#### Slide 35 — [SEÇÃO] Self-RAG
- **Tipo**: Seção
- **Objetivo**: Transição para Self-RAG
- **Conteúdo**: "4 — Self-RAG: Modelo que Reflete sobre Recuperação"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 36 — A Ideia: Modelo que Reflete sobre Recuperação
- **Tipo**: Comparação
- **Objetivo**: Mostrar que Self-RAG vai além de avaliar docs — avalia a si mesmo
- **Conteúdo**:
  - CRAG: avalia os docs recuperados (antes de gerar)
  - Self-RAG: o modelo reflete sobre TODO o processo — antes, durante e depois de gerar
  - Modelo treinado para emitir tokens de reflexão que controlam o fluxo
  - Fonte: Asai et al., arXiv:2310.11511
  - Diferença chave: Self-RAG julga se a resposta é suportada pelos docs
- **Diagrama**: CRAG (avalia docs) vs Self-RAG (avalia docs + resposta) (D8)
- **Tempo**: 1.5 min

---

#### Slide 37 — Tokens de Reflexão
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar os tokens de reflexão do Self-RAG
- **Conteúdo**:
  - `[Retrieve]` — decidir se precisa recuperar
  - `[Retrieve(target)]` — decidir qual fonte recuperar
  - `[Relevant]` / `[Irrelevant]` — julgar relevância do doc
  - `[Fully supported]` / `[Partly supported]` / `[No support]` — julgar se a resposta é suportada
  - `[Utility]` — julgar utilidade da resposta final
  - Cada token controla uma decisão no pipeline
- **Diagrama**: Lista de tokens com ícones e descrição
- **Tempo**: 2 min

---

#### Slide 38 — O Fluxo do Self-RAG
- **Tipo**: Diagrama
- **Objetivo**: Visualizar o fluxo completo com tokens de reflexão
- **Conteúdo**:
  - Fluxo: pergunta → [Retrieve?] → se sim: recuperar → [Relevant?] → [Fully supported?] → resposta
  - Se [No support]: regenerar ou recuperar mais
  - O modelo decide em cada etapa via tokens de reflexão
  - Fonte: arXiv:2310.11511
- **Diagrama**: Fluxograma com tokens de reflexão nos edges (D8)
- **Animação**: Tokens aparecem nos decision points
- **Tempo**: 2 min

---

#### Slide 39 — Modelo Treinado: Como Funciona
- **Tipo**: Conteúdo
- **Objetivo**: Explicar a versão original (modelo fine-tuned)
- **Conteúdo**:
  - Self-RAG original: LLM fine-tuned para emitir tokens de reflexão
  - Treinamento: dados com anotações de reflexão (relevância, suporte, utilidade)
  - Vantagem: reflexão embutida no modelo, sem prompts extras
  - Desvantagem: requer modelo específico — não funciona com GPT-4, Claude, etc.
  - Por isso: adaptação para modelos não-treinados via prompting
- **Diagrama**: Pipeline de treinamento do Self-RAG
- **Tempo**: 1.5 min

---

#### Slide 40 — Adaptação para Modelos Não-Treinados: Prompting
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar como aplicar Self-RAG sem modelo treinado
- **Conteúdo**:
  - Ideia: replicar os tokens de reflexão via prompting estruturado
  - Prompt pede ao LLM para:
    1. Decidir se precisa recuperar
    2. Avaliar relevância de cada doc
    3. Avaliar se a resposta é suportada
    4. Regenerar se não suportada
  - Custo: múltiplas chamadas de LLM
  - Benefício: funciona com qualquer modelo (GPT-4, Claude, Llama)
- **Diagrama**: Mapeamento token → prompt
- **Tempo**: 1.5 min

---

#### Slide 41 — Implementação: Self-RAG via Prompt
- **Tipo**: Código
- **Objetivo**: Mostrar código prático de Self-RAG via prompting
- **Conteúdo**:
  - Snippet: prompt estruturado que pede reflexão
  - Pydantic models: `GradeDocuments`, `GradeHallucinations`, `GradeAnswer`
  - LangGraph nodes: `grade_documents` → `generate` → `grade_hallucination` → `grade_answer` | `regenerate`
  - Loop de regeneração com max_retries
  - Referência: LangGraph `self_rag` example
- **Diagrama**: Code block + grafo LangGraph lado a lado
- **Tempo**: 2 min

---

#### Slide 42 — Comparação: Adaptive vs CRAG vs Self-RAG
- **Tipo**: Comparação
- **Objetivo**: Sistematizar as três arquiteturas
- **Conteúdo**:
  - Tabela comparativa:
    - Adaptive: decide SE recuperar | não avalia docs | não avalia resposta
    - CRAG: recupera sempre | avalia docs | não avalia resposta
    - Self-RAG: decide SE recuperar | avalia docs | avalia resposta (hallucination check)
  - Complexidade crescente: Adaptive < CRAG < Self-RAG
  - Custo crescente: Adaptive < CRAG < Self-RAG
  - Próximo passo: Agentic RAG (agente dirige tudo)
- **Diagrama**: Tabela 3-colunas com checkpoints destacados (D9)
- **Tempo**: 1 min

---

#### Slide 43 — Quando Usar Self-RAG
- **Tipo**: Conteúdo
- **Objetivo**: Dar critérios práticos de uso
- **Conteúdo**:
  - Use Self-RAG quando:
    - Alucinação é inaceitável (jurídico, médico, financeiro)
    - Você pode pagar o custo de múltiplas chamadas
    - Precisa de garantia de que a resposta é suportada
  - Não use quando:
    - Latência é crítica
    - Base é pequena e confiável
    - Caso de uso tolera imprecisão
- **Diagrama**: Árvore de decisão
- **Tempo**: 0.5 min

---

#### Slide 44 — Exercício: Self-RAG via Prompting
- **Tipo**: Exercício
- **Objetivo**: Praticar a adaptação de Self-RAG
- **Conteúdo**:
  - Cenário: sistema de FAQ jurídico com 10.000 documentos
  - Em duplas: quando usar Adaptive RAG vs Self-RAG?
  - Critérios: tipo de pergunta, custo, qualidade esperada
  - Escrever o prompt de reflexão para um doc recuperado
  - 3 min discussão, 2 min compartilhar
- **Diagrama**: Caixa de discussão
- **Tempo**: 0.5 min

---

### SEÇÃO F — Agentic RAG (Slides 45-55 · 15 min)

---

#### Slide 45 — [SEÇÃO] Agentic RAG
- **Tipo**: Seção
- **Objetivo**: Transição para o paradigma mais avançado
- **Conteúdo**: "5 — Agentic RAG: O Agente Dirige Todo o Processo"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 46 — A Ideia: Agente Dirige Todo o Processo
- **Tipo**: Comparação
- **Objetivo**: Mostrar a diferença fundamental do Agentic RAG
- **Conteúdo**:
  - Adaptive/CRAG/Self-RAG: pipeline fixo com gates de decisão
  - Agentic RAG: o AGENTE decide tudo — planeja, busca, refina, decide parar
  - O agente tem tools de busca (web, interno, KG) e as chama como qualquer tool
  - Não há pipeline predefinido — o loop do agente É o pipeline
  - Conexão com ETHAGT01: é o Augmented LLM com retrieval in-loop
- **Diagrama**: Pipeline fixo (gates) vs Loop de agente (D10)
- **Tempo**: 1.5 min

---

#### Slide 47 — Planeja Busca, Refina Queries, Decide Parar
- **Tipo**: Conteúdo
- **Objetivo**: Detalhar as capacidades do agente
- **Conteúdo**:
  - Planeja: "Preciso buscar X, depois Y, depois combinar"
  - Refina queries: "A busca por X retornou pouco — vou reformular"
  - Decide parar: "Tenho informação suficiente para responder" ou "Preciso de mais um hop"
  - max_steps como guardrail (lição de ETHAGT01)
  - O agente raciocina sobre o QUE recuperou e o QUE ainda falta
- **Diagrama**: Loop do agente com planejamento
- **Tempo**: 1.5 min

---

#### Slide 48 — Multi-Hop: Cadeias de Recuperação
- **Tipo**: Conteúdo
- **Objetivo**: Introduzir o conceito de multi-hop retrieval
- **Conteúdo**:
  - Single-hop: uma busca → resposta
  - Multi-hop: múltiplas buscas encadeadas, cada uma dependendo da anterior
  - Exemplo: "Quem fundou a empresa que criou o ChatGPT?"
    - Hop 1: buscar "quem criou o ChatGPT?" → OpenAI
    - Hop 2: buscar "quem fundou a OpenAI?" → Sam Altman, Elon Musk, etc.
    - Resposta: sintetizar
  - Sem agente: difícil de orquestrar
- **Diagrama: Multi-hop retrieval** (D10)
- **Animação**: Hops aparecem em sequência
- **Tempo**: 1.5 min

---

#### Slide 49 — Exemplo Multi-Hop Detalhado
- **Tipo**: Diagrama
- **Objetivo**: Concretizar multi-hop com um trace real
- **Conteúdo**:
  - Pergunta: "Qual a diferença entre a política de férias da Etho e a legislação brasileira?"
  - Trace do agente:
    - Thought: "Preciso de duas fontes"
    - Action: search_etho_docs("política de férias")
    - Observation: "30 dias após 1 ano..."
    - Action: search_web("CLT férias Brasil")
    - Observation: "30 dias corridos após 12 meses..."
    - Thought: "Agora posso comparar"
    - Answer: "A Etho segue a CLT, com diferença em..."
- **Diagrama**: Trace de console estilizado
- **Animação**: Linhas aparecem sequencialmente (simulando execução)
- **Tempo**: 1.5 min

---

#### Slide 50 — Tools de Busca como Ferramentas do Agente
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar que busca é uma tool como outra qualquer
- **Conteúdo**:
  - O agente tem tools: `search_internal(query)`, `search_web(query)`, `search_kg(query)`
  - ACI importa: tool bem documentada > prompt melhor (lição de ETHAGT01/ETHAGT02)
  - O agente escolhe qual tool usar baseado na pergunta
  - Exemplo: "Qual a política interna?" → `search_internal`; "Notícia de hoje?" → `search_web`
  - Tool return format: lista de docs com score, não texto bruto
- **Diagrama**: Agente com 3 tools de busca
- **Tempo**: 1.5 min

---

#### Slide 51 — Múltiplas Fontes: Web, Interno, Knowledge Graph
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar a diversidade de fontes
- **Conteúdo**:
  - Web search: Tavily, SerpAPI, Brave Search — para dados externos e recentes
  - Interno: vector DB (Qdrant, Milvus), SQL DB — para dados proprietários
  - Knowledge Graph: Neo4j, GraphRAG — para dados relacionais estruturados
  - O agente combina fontes: web para contexto + interno para detalhe
  - O agente decide quando uma fonte é insuficiente e precisa de outra
- **Diagrama**: 3 fontes convergindo para o agente
- **Tempo**: 1.5 min

---

#### Slide 52 — GraphRAG: Do Local ao Global
- **Tipo**: Conteúdo
- **Objetivo**: Introduzir GraphRAG como padrão avançado
- **Conteúdo**:
  - RAG tradicional: recupera chunks locais (vizinhança no espaço vetorial)
  - GraphRAG: constrói grafo de conhecimento do corpus e recupera subgrafos
  - Vantagem: responde perguntas globais ("quais os temas principais deste corpus?")
  - Pipeline: extrair entidades/relações → agrupar em comunidades → sumarizar → recuperar
  - Fonte: Edge et al., Microsoft, arXiv:2404.16130
  - No Agentic RAG: o agente pode usar GraphRAG como uma tool
- **Diagrama**: Grafo de conhecimento com comunidades (D11)
- **Tempo**: 1.5 min

---

#### Slide 53 — DEMO: Agentic RAG Multi-Hop
- **Tipo**: Código
- **Objetivo**: Demo ao vivo — agente que refina queries e combina fontes
- **Conteúdo**:
  - Código do `05-Labs/ETHAGT06/Lab2-Agentic-RAG-Multi-Hop`
  - Agente com tools: `search_internal`, `search_web`
  - Pergunta multi-hop: "Compare a política de férias da Etho com a CLT"
  - Mostrar trace: planejamento → busca interna → busca web → síntese
  - Mostrar max_steps guardrail em ação
- **Diagrama**: Code block + terminal side-by-side
- **Animação**: Highlight de linhas chave no trace
- **Tempo**: 2 min

---

#### Slide 54 — Pergunta da DEMO
- **Tipo**: Exercício
- **Objetivo**: Engajar a turma com uma pergunta sobre a demo
- **Conteúdo**:
  - "O que acontece se o agente não encontrar nada na busca interna?"
  - "Como o agente decide que tem informação suficiente para parar?"
  - "E se o max_steps for muito baixo?"
  - Discussão em duplas (2 min)
- **Diagrama**: Caixa de discussão
- **Tempo**: 0.5 min

---

#### Slide 55 — A Escalada: Adaptive → CRAG → Self-RAG → Agentic
- **Tipo**: Diagrama
- **Objetivo**: Sistematizar a evolução das 4 arquiteturas
- **Conteúdo**:
  - Adaptive: decide SE recuperar
  - CRAG: avalia docs recuperados
  - Self-RAG: avalia docs + resposta
  - Agentic: agente dirige todo o processo (planeja, busca, refina, para)
  - Cada nível adiciona reflexão e controle
  - Trade-off: mais controle = mais custo e complexidade
  - Regra: comece com Adaptive, só suba com evidência de insuficiência
- **Diagrama**: Escada/pirâmide de complexidade (D12)
- **Animação**: Níveis aparecem de baixo para cima
- **Tempo**: 0.5 min

---

### SEÇÃO G — Engenharia de Qualidade (Slides 56-66 · 15 min)

---

#### Slide 56 — [SEÇÃO] Engenharia de Qualidade
- **Tipo**: Seção
- **Objetivo**: Transição para técnicas de qualidade
- **Conteúdo**: "6 — Engenharia de Qualidade: O RAG é Tão Bom Quanto Seus Chunks"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 57 — Chunking: O Fundamento Esquecido
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar que chunking é a decisão mais impactante
- **Conteúdo**:
  - "Garbage in, garbage out" — chunking ruim contamina todo o pipeline
  - Chunking fixo (512 tokens): simples, mas quebra contexto
  - Chunking por sentença/parágrafo: preserva semântica
  - Chunking semântico: agrupa por tópicos
  - O chunk é o átomo do RAG — tudo depende dele
- **Diagrama**: Documento → diferentes estratégias de chunk (D13)
- **Tempo**: 1.5 min

---

#### Slide 58 — Chunking Semântico e Hierárquico
- **Tipo**: Comparação
- **Objetivo**: Detalhar duas estratégias avançadas
- **Conteúdo**:
  - Chunking semântico:
    - Detectar mudanças de tópico (embeddings de sentença → clustering)
    - Agrupar sentenças relacionadas em um chunk
  - Chunking hierárquico:
    - Múltiplos níveis: seção → parágrafo → sentença
    - Recuperar no nível apropriado pergunta
    - Parent-child: recuperar filho, retornar pai para contexto
  - Quando cada brilha: semântico para docs densos, hierárquico para docs estruturados
- **Diagrama**: Estrutura hierárquica de chunks (D13)
- **Tempo**: 1.5 min

---

#### Slide 59 — Late Chunking (Contextual Retrieval)
- **Tipo**: Conteúdo
- **Objetivo**: Introduzir a técnica mais recente de chunking
- **Conteúdo**:
  - Problema: chunk isolado perde contexto do documento
  - Late chunking (Anthropic Contextual Retrieval, 2024):
    - Processar o documento inteiro no modelo ANTES de chunkar
    - Cada chunk recebe contexto do documento
    - Embeddings capturam contexto, não só fragmento
  - Implementação: passar documento completo, depois chunkar, depois embedar
  - Reduz falhas de recuperação em 30-50% (Anthropic)
- **Diagrama**: Chunk isolado vs chunk com contexto (D13)
- **Tempo**: 1.5 min

---

#### Slide 60 — Re-Ranking: Por Que e Como
- **Tipo**: Conteúdo
- **Objetivo**: Explicar o porquê do re-ranking
- **Conteúdo**:
  - Recuperação (BM25/densa): rápida, barata, mas imprecisa
  - Re-ranking: lento, caro, mas preciso
  - Pipeline: retrieve top-50 → re-rank → top-5 para o LLM
  - O re-ranker avalia relevância query-doc, não só similaridade
  - Reduz ruído no contexto do LLM
- **Diagrama**: Funil: top-50 → re-rank → top-5
- **Tempo**: 1.5 min

---

#### Slide 61 — Re-Rankers: Cohere, bge, Jina
- **Tipo**: Comparação
- **Objetivo**: Comparar os re-rankers disponíveis
- **Conteúdo**:
  - Cohere Rerank: API comercial, alta qualidade, paga por requisição
  - bge-reranker (BAAI): open-source, roda local, bom custo-benefício
  - Jina Reranker: API e self-hosted, foco em multilingual
  - Critério de escolha: latência, custo, qualidade, privacidade
  - Trade-off: re-ranker cross-encoder é mais preciso mas mais lento
- **Diagrama**: Tabela comparativa de re-rankers
- **Tempo**: 1.5 min

---

#### Slide 62 — Query Rewriting e HyDE
- **Tipo**: Conteúdo
- **Objetivo**: Introduzir query transformation
- **Conteúdo**:
  - Query rewriting: LLM reescreve a pergunta do usuário para melhorar recuperação
    - "férias estagiário" → "política de licença para aprendizes e estagiários"
  - HyDE (Hypothetical Document Embeddings):
    - Gerar resposta HIPOTÉTICA à pergunta
    - Embedar a resposta hipotética (não a pergunta)
    - Buscar por similaridade com a resposta hipotética
  - Por que funciona: resposta hipotética é mais próxima dos docs relevantes que a pergunta
  - Pergunta: *Query rewriting: o agente deve reescrever a pergunta do usuário? Quando?*
- **Diagrama**: Fluxo HyDE: pergunta → resposta hipotética → embed → search (D14)
- **Tempo**: 1.5 min

---

#### Slide 63 — Hybrid Search: BM25 + Densa
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar que combinar busca lexical e densa é melhor
- **Conteúdo**:
  - BM25 (lexical): captura keywords exatas, termos técnicos, nomes próprios
  - Densa (embedding): captura semântica, sinônimos, paráfrase
  - Hybrid: combinar scores de ambos com reciprocal rank fusion (RRF)
  - Resultado: melhor recall que qualquer método isolado
  - Implementação: Qdrant e Milvus suportam hybrid nativamente
- **Diagrama**: Dois ramos (BM25 + densa) → fusão → top-k (D15)
- **Tempo**: 1.5 min

---

#### Slide 64 — Multi-Vector: ColBERT
- **Tipo**: Conteúdo
- **Objetivo**: Introduzir representações multi-vetoriais
- **Conteúdo**:
  - Embedding tradicional: 1 vetor por documento (sentence embedding)
  - ColBERT: 1 vetor POR TOKEN do documento
  - Recuperação: max-similarity entre tokens da query e tokens do doc
  - Vantagem: granularidade muito maior, captura match a nível de token
  - Desvantagem: armazenamento e computação muito maiores
  - Quando usar: corpora técnicos com terminologia específica
- **Diagrama**: 1 vetor/doc vs N vetores/doc
- **Tempo**: 1.5 min

---

#### Slide 65 — Multimodal RAG: Texto, Imagem, Tabela
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar que RAG vai além de texto
- **Conteúdo**:
  - Texto: embedding de texto (padrão)
  - Imagem: CLIP, vision embeddings — buscar por descrição ou imagem
  - Tabela: converter para texto estruturado ou embedar como dado tabular
  - Multimodal: combinar texto + imagem + tabela no mesmo espaço
  - Modelos: GPT-4V, Claude Vision, LLaVA para geração multimodal
  - Desafio: chunking de imagem (regiões), alinhamento modal
- **Diagrama**: 3 modalidades → espaço compartilhado
- **Tempo**: 1 min

---

#### Slide 66 — Exercício: Escolhendo a Estratégia
- **Tipo**: Exercício
- **Objetivo**: Praticar a escolha de técnicas de qualidade
- **Conteúdo**:
  - 3 cenários — em duplas, escolher estratégia:
    1. Documentação técnica em inglês (10k páginas) → hybrid + re-rank
    2. FAQ jurídico em português (5k docs) → query rewriting + semantic chunking
    3. Catálogo de produtos com imagens (50k items) → multimodal + ColBERT
  - Justificar com 2 critérios cada
  - 2 min discussão
- **Diagrama**: 3 cards com cenários
- **Tempo**: 0.5 min

---

### SEÇÃO H — Avaliação de RAG (Slides 67-73 · 10 min)

---

#### Slide 67 — [SEÇÃO] Avaliação de RAG
- **Tipo**: Seção
- **Objetivo**: Transição para avaliação
- **Conteúdo**: "7 — Avaliação de RAG: Sem Métricas, Você Está Cego"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 68 — Por Que Avaliar RAG é Diferente
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar que RAG tem componentes que falham independentemente
- **Conteúdo**:
  - Avaliação de LLM puro: a resposta está certa ou errada
  - Avaliação de RAG: 3 componentes independentes:
    1. Retrieval: os docs recuperados são relevantes?
    2. Generation: a resposta é fiel aos docs?
    3. End-to-end: a resposta responde à pergunta?
  - Cada componente precisa de métricas próprias
  - Sem isso: não sabe se o problema é retrieval ou generation
- **Diagrama**: 3 componentes com métricas separadas
- **Tempo**: 1.5 min

---

#### Slide 69 — Métricas: Faithfulness e Answer Relevance
- **Tipo**: Conteúdo
- **Objetivo**: Detalhar as métricas de geração
- **Conteúdo**:
  - Faithfulness: a resposta é fiel aos docs recuperados? (sem alucinação)
    - Decompor resposta em claims → verificar cada claim contra os docs
    - Score = claims suportadas / total de claims
  - Answer relevance: a resposta responde à pergunta?
    - Gerar perguntas a partir da resposta → comparar com pergunta original
    - Score = similaridade semântica
  - Tensão: alta faithfulness pode baixar relevance (responde só com o que está nos docs)
- **Diagrama**: Fórmula visual de faithfulness
- **Tempo**: 1.5 min

---

#### Slide 70 — Métricas: Context Precision e Context Recall
- **Tipo**: Conteúdo
- **Objetivo**: Detalhar as métricas de retrieval
- **Conteúdo**:
  - Context precision: dos docs recuperados, quantos são relevantes?
    - Score = relevantes no top-k / k
    - Penaliza ruído (docs irrelevantes que "afogam" os bons)
  - Context recall: dos docs necessários, quantos foram recuperados?
    - Score = recuperados / necessários
    - Penaliza gaps (docs que faltam)
  - Tensão: mais docs recuperados → mais recall, menos precision
  - Re-ranking melhora precision sem sacrificar recall
- **Diagrama**: Matriz precision × recall
- **Tempo**: 1.5 min

---

#### Slide 71 — Frameworks: Ragas, TruLens, DeepEval
- **Tipo**: Comparação
- **Objetivo**: Comparar os frameworks de avaliação
- **Conteúdo**:
  - Ragas: foco em RAG, métricas padronizadas, open-source, integração LangChain
  - TruLens: tracing + avaliação, dashboard interativo, foco em produção
  - DeepEval: testes unitários para LLM, integra CI/CD, pytest-style
  - Critério de escolha: stack existente, necessidade de tracing, CI/CD
  - Todos usam LLM-as-judge internamente
- **Diagrama**: Tabela comparativa de frameworks
- **Tempo**: 1.5 min

---

#### Slide 72 — Diagrama: Eval Pipeline
- **Tipo**: Diagrama
- **Objetivo**: Visualizar o pipeline de avaliação
- **Conteúdo**:
  - Pipeline: pergunta → retrieve → generate → resposta
  - Eval coleta: pergunta, docs recuperados, resposta gerada
  - Métricas computadas: faithfulness, answer_relevance, context_precision, context_recall
  - Dataset de holdout: perguntas + ground truth (docs e respostas esperadas)
  - Execução: batch eval em CI/CD para detectar regressão
- **Diagrama**: `12-Diagrams/ETHAGT06/eval-pipeline.mmd` (D16)
- **Animação**: Métricas aparecem uma a uma
- **Tempo**: 2 min

---

#### Slide 73 — LLM-as-Judge e Dataset de Holdout
- **Tipo**: Conteúdo
- **Objetivo**: Detalhar LLM-as-judge e a importância do holdout
- **Conteúdo**:
  - LLM-as-judge: usar um LLM (GPT-4, Claude) para avaliar respostas
  - Vieses a mitigar:
    - Position bias (prefere primeira opção) → randomizar ordem
    - Self-preference (prefere próprio estilo) → usar modelo diferente do gerador
    - Length bias (prefere respostas longas) → normalizar
  - Dataset de holdout: perguntas curadas com ground truth
  - Regressão: se faithfulness cai de 0.90 para 0.82 após mudança → bloquear deploy
  - Critério do projeto: faithfulness ≥ 0.85, context recall ≥ 0.80
- **Diagrama**: Pipeline CI/CD com gate de qualidade
- **Tempo**: 1.5 min

---

### SEÇÃO I — Fechamento (Slides 74-85 · 12 min)

---

#### Slide 74 — [SEÇÃO] Fechamento
- **Tipo**: Seção
- **Objetivo**: Transição para o fechamento
- **Conteúdo**: "8 — Boas Práticas, Anti-Patterns e Próximos Passos"
- **Diagrama**: Fundo etho-primary
- **Tempo**: 0.5 min

---

#### Slide 75 — Boas Práticas (DO)
- **Tipo**: Conteúdo
- **Objetivo**: Checklist de boas práticas
- **Conteúdo**:
  - Comece com Adaptive RAG antes de pular para Agentic
  - Avalie docs recuperados antes de gerar (CRAG)
  - Use re-ranking sempre que possível
  - Chunking semântico > chunking fixo
  - Avaliação automatizada desde o dia 1 (Ragas)
  - Dataset de holdout para regressão
  - Hybrid search (BM25 + densa) como padrão
  - max_steps em agentes RAG (guardrail)
- **Diagrama**: Checklist verde (etho-success)
- **Tempo**: 1.5 min

---

#### Slide 76 — Anti-Patterns (DON'T)
- **Tipo**: Conteúdo
- **Objetivo**: Checklist do que NÃO fazer
- **Conteúdo**:
  - Começar com Agentic RAG sem entender Adaptive/CRAG
  - Chunking fixo sem pensar no conteúdo
  - Confiar cegamente no top-k sem re-rank
  - Sem avaliação — "funciona na demo"
  - Sem fallback web quando a base local é insuficiente
  - Adicionar mais docs sem re-rank (mais contexto ≠ melhor)
  - Sem dataset de holdout — sem como detectar regressão
  - Query rewriting automático sem validação
- **Diagrama**: Checklist vermelho (etho-danger)
- **Tempo**: 1.5 min

---

#### Slide 77 — Resumo da Aula
- **Tipo**: Resumo
- **Objetivo**: Sintetizar os pontos-chave
- **Conteúdo**:
  - RAG ingênuo falha silenciosamente — 4 tipos de falha sistemáticos
  - Adaptive RAG: decide QUANDO recuperar
  - CRAG: AVALIA docs antes de usar, com fallback web
  - Self-RAG: reflete sobre docs E resposta (hallucination check)
  - Agentic RAG: agente dirige todo o processo (multi-hop, multi-source)
  - Qualidade: chunking + re-rank + hybrid + query rewriting
  - Avaliação: faithfulness, relevance, context precision/recall com Ragas
  - Escalada: Adaptive → CRAG → Self-RAG → Agentic (comece simples)
- **Diagrama**: 8 ícones com os pontos-chave
- **Tempo**: 1.5 min

---

#### Slide 78 — Checklist da Aula
- **Tipo**: Resumo
- **Objetivo**: Confirmar que todos os tópicos foram cobertos
- **Conteúdo**:
  - [ ] Diagnosticou 4 tipos de falha do RAG ingênuo
  - [ ] Explicou Adaptive RAG (decidir quando recuperar)
  - [ ] Implementou CRAG (avaliar + 3 caminhos)
  - [ ] Diferenciou Self-RAG (reflexão sobre resposta)
  - [ ] Descreveu Agentic RAG (agente dirige, multi-hop)
  - [ ] Listou 3+ técnicas de qualidade (chunking, re-rank, hybrid)
  - [ ] Definiu 4 métricas de avaliação (faithfulness, relevance, precision, recall)
- **Diagrama**: Checklist visual
- **Tempo**: 1 min

---

#### Slide 79 — Quiz: Pergunta 1
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "Qual é a diferença fundamental entre Adaptive RAG e Self-RAG?"
  - A) Adaptive usa vector DB, Self-RAG usa grafo
  - B) Adaptive decide quando recuperar, Self-RAG também avalia a resposta
  - C) Adaptive é mais caro que Self-RAG
  - D) Não há diferença significativa
  - Resposta: B
- **Tempo**: 1 min

---

#### Slide 80 — Quiz: Pergunta 2
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "Em CRAG, quando o sistema decide buscar na web?"
  - A) Sempre, como primeiro passo
  - B) Quando o avaliador classifica os docs como irrelevantes
  - C) Quando a resposta é muito curta
  - D) Quando o usuário pede explicitamente
  - Resposta: B
- **Tempo**: 1 min

---

#### Slide 81 — Quiz: Pergunta 3
- **Tipo**: Exercício
- **Objetivo**: Verificar compreensão
- **Conteúdo**:
  - "Qual métrica mede se a resposta é fiel aos documentos recuperados?"
  - A) Context precision
  - B) Answer relevance
  - C) Faithfulness
  - D) Context recall
  - Resposta: C
- **Tempo**: 1 min

---

#### Slide 82 — Conexão com Próximos Módulos
- **Tipo**: Conteúdo
- **Objetivo**: Mostrar como ETHAGT06 conecta com o resto da especialização
- **Conteúdo**:
  - ETHAGT07 — Knowledge Graphs & Vector DBs: além do RAG plano (GraphRAG em profundidade)
  - ETHAGT90 — Projeto final (aplicar Agentic RAG)
  - Conexão com ETHAGT01: Agentic RAG = Augmented LLM com retrieval in-loop
  - Conexão com ETHAGT05: memória do agente RAG (estado entre hops)
  - Conexão com ETHAGT12: AgentOps — traces de agentes RAG
- **Diagrama**: Mapa da especialização com ETHAGT06 destacado
- **Tempo**: 1 min

---

#### Slide 83 — Referências Completas
- **Tipo**: Referências
- **Objetivo**: Listar todas as fontes
- **Conteúdo**:
  1. Lewis, P. et al. *Retrieval-Augmented Generation*. arXiv:2005.11401, 2020
  2. Asai, A. et al. *Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection*. arXiv:2310.11511, 2023
  3. Yan, S. et al. *Corrective Retrieval Augmented Generation (CRAG)*. arXiv:2401.15884, 2024
  4. Edge, D. et al. *GraphRAG: From Local to Global*. Microsoft, arXiv:2404.16130, 2024
  5. Anthropic. *Contextual Retrieval*. 2024
  6. LangGraph examples: `adaptive_rag`, `crag`, `self_rag`, `agentic_rag`
  7. Cohere. *Rerank Documentation*
  8. Ragas: *Evaluation framework for RAG*
- **Tempo**: 0.5 min

---

#### Slide 84 — Projeto do Módulo + Labs
- **Tipo**: Conteúdo
- **Objetivo**: Apresentar o projeto e laboratórios
- **Conteúdo**:
  - Projeto: construir sistema RAG de produção sobre corpus técnico
    - Pipeline agêntico (Adaptive/CRAG/Agentic)
    - Eval automatizado com Ragas
    - Entrega: sistema + eval report + ADR
    - Critério: faithfulness ≥ 0.85 e context recall ≥ 0.80
  - Lab 1 (4h): "Diagnosticando falhas" — RAG ingênuo em corpus problemático
  - Lab 2 (5h): "Agentic RAG multi-hop" — agente que refina queries e combina fontes
- **Tempo**: 1 min

---

#### Slide 85 — Q&A / Encerramento
- **Tipo**: Capa
- **Objetivo**: Abrir para perguntas e encerrar
- **Conteúdo**:
  - "Perguntas?"
  - Contato do professor
  - "Na próxima aula: ETHAGT07 — Knowledge Graphs & Vector DBs"
  - Leitura: Asai et al. *Self-RAG* (arXiv:2310.11511) antes da próxima aula
- **Diagrama**: Logo Etho + fundo etho-dark
- **Tempo**: 1 min

---

## Resumo do Storyboard

| Seção | Slides | Tempo | Conteúdo |
|---|---|---|---|
| A — Abertura | 1-7 | 8 min | Capa, objetivos, competências, agenda, pré-requisitos, motivação, contexto |
| B — RAG Ingênuo Falha | 8-14 | 10 min | Pipeline ingênuo, 4 tipos de falha, mito vector DB, casos problemáticos |
| C — Adaptive RAG | 15-23 | 12 min | Quando recuperar, routing, diagrama, implementação, exercício |
| D — CRAG | 24-34 | 15 min | Avaliador de relevância, 3 caminhos, knowledge refinement, web fallback, código |
| E — Self-RAG | 35-44 | 13 min | Tokens de reflexão, modelo treinado vs prompting, comparação, exercício |
| F — Agentic RAG | 45-55 | 15 min | Agente dirige, multi-hop, GraphRAG, multi-source, DEMO, escalada |
| G — Engenharia de Qualidade | 56-66 | 15 min | Chunking, late-chunking, re-ranking, HyDE, hybrid, ColBERT, multimodal |
| H — Avaliação de RAG | 67-73 | 10 min | Faithfulness, relevance, context precision/recall, Ragas, eval pipeline |
| I — Fechamento | 74-85 | 12 min | Boas práticas, anti-patterns, resumo, quiz, conexão, referências, projeto, Q&A |
| **Total** | **85** | **110 min** | |

---

## Diagramas Necessários

| # | Slide | Diagrama | Tipo | Fonte |
|---|---|---|---|---|
| D1 | 7 | Evolução RAG fixo → RAG agêntico | Timeline | Novo |
| D2 | 9 | Pipeline do RAG ingênuo com pontos de falha | Flowchart | Novo |
| D3 | 10-13 | 4 tipos de falha do RAG (grid) | Grid 2x2 | Novo |
| D4 | 14 | Casos problemáticos (tabular, multilingual, multimodal) | Comparação | Novo |
| D5 | 19 | Adaptive RAG | Flowchart | `12-Diagrams/ETHAGT06/adaptive-rag.mmd` |
| D6 | 21 | Implementação Adaptive RAG (LangGraph) | Flowchart | LangGraph `adaptive_rag` |
| D7 | 28 | CRAG Flow | Flowchart | `12-Diagrams/ETHAGT06/crag-flow.mmd` |
| D8 | 38 | Self-RAG flow (tokens de reflexão) | Flowchart | arXiv:2310.11511 |
| D9 | 42 | Comparação Adaptive vs CRAG vs Self-RAG | Tabela | Novo |
| D10 | 48 | Multi-hop retrieval | Sequência | Novo |
| D11 | 52 | GraphRAG (local to global) | Flowchart | arXiv:2404.16130 |
| D12 | 55 | Escalada Adaptive → CRAG → Self-RAG → Agentic | Escada | Novo |
| D13 | 57-59 | Estratégias de chunking (fixo, semântico, hierárquico, late) | Comparação | Novo |
| D14 | 62 | HyDE flow | Sequência | Novo |
| D15 | 63 | Hybrid search (BM25 + densa) | Flowchart | Novo |
| D16 | 72 | Eval pipeline | Flowchart | `12-Diagrams/ETHAGT06/eval-pipeline.mmd` |
| D17 | 73 | Métricas de RAG (matriz) | Matriz | Ragas |

---

## Pontos de Engajamento

| # | Slide | Tipo | Descrição | Duração |
|---|---|---|---|---|
| E1 | 6 | Pergunta | "Quantos já usaram RAG e obtiveram resposta errada com alta confiança?" | 1 min |
| E2 | 14 | Pergunta | "Qual o pior tipo de falha — não responder ou responder errado com confiança?" | 1 min |
| E3 | 23 | Exercício rápido | "Responder direto ou recuperar?" — 5 perguntas, votação | 0.5 min |
| E4 | 44 | Exercício | "Adaptive vs Self-RAG" — FAQ jurídico, discussão em duplas | 5 min |
| E5 | 53 | DEMO | "Agentic RAG Multi-Hop" — código ao vivo com trace | 2 min |
| E6 | 54 | Pergunta da DEMO | "Como o agente decide parar em multi-hop?" — discussão em duplas | 0.5 min |
| E7 | 66 | Exercício | "Escolhendo a estratégia de qualidade" — 3 cenários em duplas | 0.5 min |
| E8 | 79 | Quiz | "Diferença entre Adaptive RAG e Self-RAG?" | 1 min |
| E9 | 80 | Quiz | "Quando CRAG decide buscar na web?" | 1 min |
| E10 | 81 | Quiz | "Qual métrica mede fidelidade aos docs?" | 1 min |
| E11 | 85 | Q&A | Perguntas abertas e encerramento | 1 min |

---

## Pendências de Produção

- [ ] Produzir 14 diagramas novos (D1, D2, D3, D4, D6, D8, D9, D10, D11, D12, D13, D14, D15, D17)
- [ ] Validar 3 diagramas existentes (D5, D7, D16) — `adaptive-rag.mmd`, `crag-flow.mmd`, `eval-pipeline.mmd`
- [ ] Screenshot do trace multi-hop do Lab 2 (Slide 49, 53)
- [ ] Screenshot do código com syntax highlighting (Slides 21, 32, 41)
- [ ] Imagem de fundo para capa (Slide 1)
- [ ] Badge de competências (Slide 3)
- [ ] Timeline de evolução do RAG (Slide 7)
- [ ] Grid de tipos de falha (Slides 10-13)
- [ ] Tabela comparativa Adaptive vs CRAG vs Self-RAG (Slide 42)
- [ ] Mapa da especialização com ETHAGT06 destacado (Slide 82)
- [ ] Dataset de holdout de exemplo para demo de avaliação (Slide 72)

---

> **Aguardando aprovação deste storyboard para gerar os slides detalhados com notas do professor.**
