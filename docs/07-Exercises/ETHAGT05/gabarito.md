---
password: Etho-Prof-2026
---
# ETHAGT05 — Gabarito

> Restrito a mentores. Cada resposta justificada com referência à apostila.

## Múltipla escolha

1. **c)** — Memória procedural armazena "como fazer" — skills, procedimentos, conhecimentos operacionais sobre como executar tarefas (Capítulo 1 — Tipos de memória).

2. **b)** — O checkpointer persiste o estado serializável do agente (ex.: em Postgres, SQLite, Redis), permitindo resume (retomar), replay e branching (time travel) (Capítulo 2 — Checkpointer e estado persistente).

3. **b)** — Sumarização em cascata condensa o histórico antigo quando a conversa cresce, preservando informação essencial e mantendo o contexto dentro dos limites da janela (Capítulo 3 — Gerenciamento de contexto).

4. **b)** — Em entity-centric memory, a informação é organizada em torno de entidades (pessoas, lugares, conceitos) com seus atributos e relações, permitindo recuperação estruturada (Capítulo 3.4 — Entity-centric memory, estilo MemGPT).

## Verdadeiro ou Falso (justificado)

1. **Falso.** Memória vetorial é excelente para recall por similaridade semântica, mas é pior que relacional quando é necessário query estruturado (ex.: "todos os pedidos do usuário X em janeiro"), joins, ou integridade transacional. Cada tipo brilha em cenários diferentes (Capítulo 4).

2. **Geralmente verdadeiro.** Eviction por relevância preserva informação útil independentemente da idade, enquanto eviction por tempo pode descartar informação crítica que ainda é relevante. A combinação de ambos é ideal (Capítulo 3.3).

3. **Verdadeiro.** PII em memória de longo prazo exige redação (mascarar dados sensíveis), política de retenção (quanto tempo guardar) e direito ao esquecimento (LGPD/GDPR) (Capítulo 6.2 — PII em memória).

4. **Falso.** Para a maioria dos provedores, o custo financeiro é **linear** por token de entrada. A confusão comum vem do fato de que a *atenção* (computo) em transformers padrão é O(n²), mas isso se reflete em latência e requisitos de memória, não necessariamente no preço cobrado por token. A latência cresce e a qualidade pode degradar em contextos longos ("lost in the middle") (Capítulo 3.1).

## Código curto

1. **Eviction por relevância + idade:**
```python
def evict(memory_items, max_items=100):
    scored = []
    for item in memory_items:
        age_score = 1.0 / (1 + (now() - item.timestamp).days)
        priority = item.relevance * 0.7 + age_score * 0.3
        scored.append((item, priority))
    scored.sort(key=lambda x: x[1], reverse=True)
    return [item for item, _ in scored[:max_items]]
```
Referência: Capítulo 3.3 (Eviction por relevância ou tempo).

2. **Recall episódico:**
```python
def recall_episodic(query, user_id, k=5):
    query_emb = embed(query)
    results = vector_db.search(
        query_emb, top_k=k,
        filter={"user_id": user_id}  # metadata filtering
    )
    return [r.payload for r in results]
```
Referência: Capítulo 4 (Memória vetorial para recall).

3. **Sumarização em cascata:**
```python
def maybe_summarize(messages, threshold=20):
    if len(messages) <= threshold:
        return messages
    old = messages[:threshold // 2]
    recent = messages[threshold // 2:]
    summary = llm(f"Summarize: {old}")
    return [{"role": "system", "content": f"Resumo: {summary}"}] + recent
```
Referência: Capítulo 3.2 (Sumarização em cascata).

## Análise de trade-off

1. **Vetorial vs. relacional:** Vetorial é melhor para recall semântico ("encontre conversas sobre problemas similares"). Relacional é melhor para queries estruturados ("pedidos do usuário X em data Y") e integridade. Um agente de suporte se beneficia de ambos: relacional para dados transacionais, vetorial para histórico de conversas (Capítulo 4 e 5).

2. **Working memory vs. persistente:** Working memory (context window) basta para interações curtas e sem necessidade de continuidade cross-sessão. Memória persistente é necessária quando o agente precisa recordar interações anteriores, sobreviver a restarts, ou manter estado de longo prazo (Capítulo 2 e 3).

3. **Camadas necessárias para assistente pessoal:**
   - **Working:** para a conversa atual.
   - **Episódica:** para recordar interações anteriores relevantes.
   - **Semântica:** para fatos sobre o usuário (preferências, informações pessoais).
   - **Procedural:** opcional, para skills aprendidas (ex.: fluxos que o usuário repete).
   Referência: Capítulo 1 e projeto do módulo.

## Debug / diagnóstico

1. **Causas prováveis de perda de contexto:**
   - **thread_id incorreto:** O resume usa um thread_id diferente do original, carregando estado errado. Correção: garantir consistência do thread_id.
   - **Schema de estado mudou:** O estado serializado não é compatível com a versão atual do agente. Correção: versionamento de schema de estado (Capítulo 2.4).

2. **Diagnóstico:** Filtro de metadata não está sendo aplicado — a busca vetorial retorna eventos de qualquer usuário. **Correção:** adicionar `filter={"user_id": current_user_id}` na query ao vector DB (Capítulo 4.3 — Metadata filtering).
