# ETHAGT05 — Perguntas para Discussão

> Perguntas para estimular debate durante e após a aula.
> Organizadas por profundidade: rápida (1-2 min) → média (3-5 min) → profunda (10+ min).

---

## Perguntas Rápidas (1-2 min)

### Q1 — Quanta Memória é Suficiente?
"Quanto contexto você acha que um assistente pessoal precisa reter? 1 conversa? 1 mês? 1 ano?"
- **Objetivo**: Calibrar expectativas da turma
- **Slide**: 5
- **Resposta esperada**: Depende do caso de uso, mas assistente pessoal de longo prazo precisa de memória cross-sessão (semanas/meses) — não apenas context window.

### Q2 — Lost in the Middle
"Já notaram um agente ou ChatGPT 'esquecendo' algo que estava no início ou meio da conversa longa?"
- **Objetivo**: Conectar fenômeno vivido com o paper "Lost in the Middle"
- **Slide**: 9
- **Resposta esperada**: A maioria vai ter vivido isso. É a prova empírica de que context window maior não resolve tudo.

### Q3 — Backend Favorito
"Se você fosse colocar um agente em produção hoje, qual backend de checkpointer usaria: Postgres, SQLite ou Redis?"
- **Objetivo**: Calibrar experiência prática e aplicar trade-offs
- **Slide**: 22
- **Ação**: Contar mãos levantadas por backend; pedir justificativa rápida

### Q4 — Vector DB na Sua Stack
"Vocês já usaram Qdrant, Chroma, Pinecone ou pgvector em produção?"
- **Objetivo**: Calibrar familiaridade com vector DBs
- **Slide**: 47
- **Ação**: Contar mãos levantadas; se <30%, simplificar a Seção E

---

## Perguntas Médias (3-5 min)

### Q5 — Quando Memória Vetorial é Pior que Relacional
"Sua memória vetorial tem 100k embeddings. O usuário pede 'todos os eventos do usuário X no mês Y'. Por que o vector DB é péssimo para isso?"
- **Objetivo**: Pensar criticamente sobre quando NÃO usar vector search
- **Slide**: 38
- **Resposta esperada**: Vector DB é otimizado para similaridade semântica, não para exact match, ordenação temporal, ou agregação. Este caso é puro SQL: `WHERE user_id = X AND timestamp BETWEEN ...`. Vector search seria lento e impreciso.

### Q6 — Custo do Contexto Maior
"Seu agente usa 200k tokens de contexto a cada chamada. A 10 chamadas por interação, 10k interações/dia, e $0.15/1M tokens input — quanto custa por mês? E se você sumarizar para 20k tokens?"
- **Objetivo**: Praticar cálculo de custo de contexto
- **Slide**: 32
- **Cálculo**: 
  - Sem sumarização: 200k × 10 × 10k = 20B tokens/dia = $3k/dia = $90k/mês
  - Com sumarização (20k): 20k × 10 × 10k = 2B tokens/dia = $300/dia = $9k/mês
  - Economia: 90% de redução

### Q7 — Modelo Atualizado entre Sessões
"O que acontece se o modelo GPT-4-turbo foi atualizado para GPT-4o entre a sessão 1 (pause) e a sessão 2 (resume)?"
- **Objetivo**: Pensar em compatibilidade de estado entre versões
- **Slide**: 29
- **Resposta esperada**: Depende. Se o schema do estado mudou, pode quebrar. Se só o modelo interno mudou, provavelmente funciona, mas o comportamento pode ser ligeiramente diferente. Boa prática: versionar o schema (`schema_version`) e fazer testes de regressão no resume.

### Q8 — Política de Eviction
"Seu assistente pessoal tem 1 ano de interações. Como você decide o que manter, arquivar e apagar?"
- **Objetivo**: Praticar design de política de eviction
- **Slide**: 39
- **Ação**: Em trios, 3 min. Exemplo de resposta: `score = relevance × decay(age)`, entidades críticas (pagamentos, prazos) têm decay lento, recall frequente aumenta score, eventos com > 6 meses e score < 0.5 são arquivados.

---

## Perguntas Profundas (10+ min)

### Q9 — Context Window de 10M Tokens Resolveria?
"Se a context window crescesse para 10 milhões de tokens, ainda precisaríamos de memória persistente e vector DB?"
- **Objetivo**: Pensar sobre limites fundamentais da memória
- **Slide**: 9, 31
- **Resposta esperada**: Sim, ainda precisamos. Razões:
  1. Custo cresce linearmente com contexto (mesmo que não quadraticamente)
  2. Qualidade degrada com muito contexto (Lost in the Middle)
  3. Latência aumenta
  4. Memória persistente é entre sessões; context window é dentro de uma
  5. Sem estrutura (vector + metadata + KG), 10M tokens de conversa é ruído, não memória

### Q10 — Direito ao Esquecimento em Vector DB
"LGPD/GDPR exigem 'direito ao esquecimento'. Como você implementa isso em uma memória vetorial com 10M embeddings e sumários consolidados?"
- **Objetivo**: Pensar sobre privacidade em sistemas de memória
- **Slide**: 61
- **Resposta esperada**: Três estratégias:
  1. Delete por metadata (`WHERE user_id = X`) — rápido, mas não cobre sumários consolidados que já incorporaram a informação
  2. Re-embed: remover eventos do usuário e re-gerar sumários — caro mas consistente
  3. Cryptographic erasure: encriptar por usuário, destruir chave — instantâneo e criptograficamente seguro
  - Discussão: nenhuma é perfeita; combinar depende do caso.

### Q11 — Memória é Identidade?
"Park et al. dizem que 'a arquitetura de memória é a identidade do agente'. O que isso significa? Um agente com outra memória seria outro agente?"
- **Objetivo**: Pensar sobre memória e identidade
- **Slide**: 56
- **Resposta esperada**: Sim — em Generative Agents, cada agente tem memória única (observações, experiências), o que molda suas decisões, planos e socialização. Trocar a memória = trocar a identidade. Análogo a humanos: nossas experiências nos definem. Implicação prática: a memória não é só storage — é parte do "cérebro" do agente.

### Q12 — Multi-Agente com Memória Compartilhada
"3 agentes compartilham uma memória vetorial. Agente A lê um fato, B o atualiza, A usa o fato desatualizado. Como resolver?"
- **Objetivo**: Pensar em consistência em sistemas multi-agente
- **Slide**: 59
- **Resposta esperada**:
  - Strong consistency: locks / transações (caro, lento)
  - Eventual consistency: aceitar defasagem (mais simples, padrão)
  - Event sourcing: log de mudanças (auditável, replay)
  - Padrão: cada agente tem memória local + memória compartilhada via message bus
  - Profundidade em ETHAGT09 (Multi-Agent) e ETHAGT14 (Escalabilidade)

---

## Perguntas Bônus (para alunos avançados)

### Q13 — Generative Agents em Produção
"A fórmula de recall de Generative Agents é `score = α·recency + β·importance + γ·relevance`. Quais valores de α, β, γ você usaria para um assistente de produtividade vs um NPC de jogo?"
- **Objetivo**: Discutir calibração de trade-offs
- **Resposta**: 
  - Assistente de produtividade: alta relevance (γ alto) — precisa de recall preciso
  - NPC de jogo: alta recency (α alto) — reage ao contexto imediato
  - Importance (β): alto para ambos, mas mais para NPCs (decisões dramáticas)

### Q14 — Sumarização Perde Informação Crítica?
"Sumarização em cascata comprime mensagens. E se o sumário perder exatamente o detalhe que importa em uma sessão futura?"
- **Objetivo**: Pensar sobre perda de informação em sumarização
- **Resposta**: Sim, é um risco real. Estratégias de mitigação:
  1. Manter eventos originais no vector DB (episódica) mesmo após sumarização
  2. Sumário multi-nível (L1, L2, L3) com fallback para nível inferior
  3. Eviction por relevância em vez de sumarização cega
  4. Human-in-the-loop para confirmar que detalhes críticos foram preservados

### Q15 — Quando NÃO Memorizar
"Cite 3 casos em que é melhor o agente NÃO memorizar uma interação."
- **Objetivo**: Pensar sobre minimização de dados
- **Resposta**: 
  1. Informação efêmera ("qual a temperatura agora?") — sempre recalculável
  2. Dados sensíveis sem consentimento explícito do usuário
  3. Informação volátil ("saldo atual", "status da tarefa") — muda rápido demais para consolidar
  4. Conteúdo duplicado / redundante (já existe na memória)
  5. Eventos sem valor futuro (boilerplate de conversa)
