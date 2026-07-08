# ETHAGT05 — Exercícios

> Exercícios para aula e para casa.
> Organizados por tipo: em aula, individual, em duplas/trios, projeto.

---

## Exercícios em Aula

### E1 — Política de Eviction (Trios)
**Slide**: 39
**Tempo**: 3 min discussão + 1 min compartilhar
**Formato**: Trios, depois compartilhar com a turma

**Enunciado**: Cenário — assistente pessoal com 1 ano de interações diárias (~365 conversas).

Em trios, escrevam uma política de eviction que combine relevância e idade. Considerem:

1. Entidades críticas (pagamentos, prazos, contratos) — devem durar mais?
2. Frequência de recall — eventos acessados frequentemente merecem boost?
3. PII — dados pessoais sensíveis devem ter TTL menor?
4. Custo de storage vs benefício de retenção

**Template**:
```
POLÍTICA DE EVICTION
─────────────────────
score(event) = ____ × relevance + ____ × recency + ____ × access_frequency
threshold = ____
entidades_críticas = [____, ____, ____]
TTL_PII = ____ dias
ação_se_score < threshold = [arquivar / apagar]
```

**Exemplo de resposta**:
```python
score = 0.5 * relevance + 0.3 * recency + 0.2 * access_frequency
threshold = 0.4
if entity in CRITICAL_ENTITIES:
    threshold *= 0.5  # decay lento
if contains_pii(event):
    ttl = 90  # dias
if score < threshold and age > 180:
    archive(event)
```

**Gabarito de discussão**: Não há resposta única. O objetivo é praticar o trade-off entre retenção e custo, e reconhecer que entidades críticas e PII precisam de tratamento especial.

---

### E2 — Embedding ou Metadata? (Discussão Aberta)
**Slide**: 49
**Tempo**: 2 min
**Formato**: Votação + discussão

**Enunciado**: Para cada cenário, vote: **E** (embedding/semantic) ou **M** (metadata/structured) ou **AMBOS**?

1. "Aquela reunião de terça sobre deploy"
2. "Como configurar CI/CD?"
3. "Qual o saldo da minha conta?"
4. "Algo sobre React hooks que conversamos mês passado"
5. "Liste todos os projetos em que usei Python"

**Gabarito**:
1. **AMBOS** — metadata (dia da semana: terça) + vector (tópico: deploy)
2. **E** — semântico (embedding de "CI/CD") + filter por `type="procedural"`
3. **NENHUM** — KB relacional (não é caso para vector DB; saldo é transacional)
4. **AMBOS** — metadata (time range: mês passado) + vector (tópico: React hooks)
5. **M** — relacional/KG (listar por tipo, não por similaridade semântica)

---

### E3 — O Que Acontece Se...? (Duplas)
**Slide**: 29
**Tempo**: 2 min
**Formato**: Duplas, 2 min discussão + 1 min compartilhar

**Enunciado**: Após a DEMO do checkpointer, discutam em duplas:

1. O que acontece se o modelo foi atualizado entre sessão 1 e sessão 2?
2. E se o schema do estado mudou (novo campo adicionado)?
3. Como você testaria que o resume funciona corretamente?

**Gabarito**:
1. Provavelmente funciona, mas o comportamento pode ser ligeiramente diferente (modelo novo pode decidir diferente). Boa prática: gravar a versão do modelo no estado.
2. Sem versionamento, quebra. Com `schema_version` + migração lazy, o estado antigo é convertido no load.
3. Teste de regressão: rodar agente → pausar → retomar → comparar output com execução sem interrupção. Devem ser idênticos (ou muito próximos).

---

## Exercícios Individuais (para casa)

### E4 — 5 Cenários, 4 Camadas
**Tempo estimado**: 15 min
**Formato**: Individual, escrito

**Enunciado**: Para cada um dos 5 cenários abaixo, indique quais tipos de memória são necessários (working, episódica, semântica, procedural) e justifique.

1. Chatbot de suporte técnico que responde perguntas sobre um produto
2. Assistente pessoal de produtividade que acompanha um usuário por anos
3. Agente de IA de RPG (NPC com personalidade)
4. Coding agent que resolve issues de GitHub
5. Agente de análise financeira que monitora portfólio

**Gabarito de exemplo**:

| Cenário | Working | Episódica | Semântica | Procedural | Justificativa |
|---|---|---|---|---|---|
| 1. Suporte técnico | ✅ | ⚠️ (opcional) | ✅ (FAQ) | ✅ (playbooks) | Working para conversa atual; semântica para FAQs; procedural para playbooks de resolução. Episódica só se quiser contexto de tickets anteriores. |
| 2. Assistente pessoal | ✅ | ✅ | ✅ | ✅ | Todas as 4: working (sessão), episódica (eventos passados), semântica (perfil do usuário), procedural (rotinas aprendidas). |
| 3. NPC de RPG | ✅ | ✅ | ⚠️ | ✅ | Working (conversa atual), episódica (eventos do mundo), procedural (comportamentos). Semântica: opcional (conhecimento do mundo via prompt). |
| 4. Coding agent | ✅ | ✅ | ⚠️ | ✅ | Working (sessão), episódica (estado do repo, arquivos vistos), procedural (estratégias de debug). Semântica: conhecimento da linguagem vem do modelo. |
| 5. Análise financeira | ✅ | ✅ | ✅ | ✅ | Todas: working (sessão), episódica (histórico de mercado), semântica (perfil do cliente, regras), procedural (estratégias de análise). |

**Critério de avaliação**:
- Justifica cada camada com motivo concreto ✅
- Reconhece quando uma camada é opcional ✅
- Diferencia episódica (eventos) de semântica (fatos) ✅

---

### E5 — Vector DB vs Relacional vs KG
**Tempo estimado**: 15 min
**Formato**: Individual, escrito

**Enunciado**: Para cada query abaixo, indique qual sistema de memória é mais apropriado (Vector DB, Relacional, Knowledge Graph) e justifique.

1. "Todos os eventos do usuário X no mês Y"
2. "Algo sobre deploy que conversamos semana passada"
3. "Quem trabalha com Python e está livre na semana 20?"
4. "Qual o saldo atual da conta do usuário X?"
5. "Documentação sobre a API de pagamento"

**Gabarito**:

1. **Relacional** — `WHERE user_id = X AND timestamp BETWEEN ...`. Filtro estruturado, ordenação temporal.
2. **Vector DB + metadata** — metadata (time range: semana passada) + vector (tópico: deploy). Hybrid.
3. **Knowledge Graph** — query multi-hop (pessoa → skill → Python; pessoa → disponibilidade → semana 20). Cypher/SPARQL.
4. **Relacional** — `SELECT saldo FROM contas WHERE user_id = X`. Transacional, não é recall semântico.
5. **Vector DB** — recall por similaridade semântica. O usuário não sabe o título exato; busca por significado.

---

### E6 — Política de Eviction em Pseudocódigo
**Tempo estimado**: 20 min
**Formato**: Individual, pseudocódigo

**Enunciado**: Escreva uma política de eviction que combine relevância, idade e frequência de acesso. Considere:

- Eventos têm `relevance_score` (0-1), `timestamp`, `access_count`, `entities`, `contains_pii`
- Entidades críticas (ex.: pagamento, contrato) devem ter decay lento
- PII deve ter TTL máximo (ex.: 90 dias)
- Eventos com baixo score e alta idade devem ser arquivados (não apagados)
- Eventos com recall frequente devem ter score boost

**Exemplo de resposta**:
```python
def eviction_policy(event, now):
    age_days = (now - event.timestamp).days

    if event.contains_pii and age_days > 90:
        return "delete_pii"

    relevance = event.relevance_score
    recency = decay(age_days, half_life=180)
    frequency = min(event.access_count / 10, 1.0)

    score = 0.5 * relevance + 0.3 * recency + 0.2 * frequency

    if any(e in CRITICAL_ENTITIES for e in event.entities):
        score *= 1.5

    if score < 0.3 and age_days > 180:
        return "archive"
    elif score < 0.1 and age_days > 365:
        return "delete"

    return "keep"

def decay(age_days, half_life):
    return 0.5 ** (age_days / half_life)
```

**Critério de avaliação**:
- Combina os 3 fatores (relevância, idade, frequência) ✅
- Trata entidades críticas ✅
- Trata PII com TTL ✅
- Diferencia arquivar de apagar ✅

---

### E7 — Verdadeiro/Falso Justificado
**Tempo estimado**: 10 min
**Formato**: Individual, escrito

**Enunciado**: Responda V ou F e justifique em 2-3 frases:

1. "Context window de 1M tokens elimina a necessidade de memória vetorial."
2. "Vector DB é sempre melhor que relacional para memória de agentes."
3. "Sumarização em cascata é lossless — nenhum dado é perdido."
4. "Cryptographic erasure é a estratégia mais rápida para direito ao esquecimento."
5. "Checkpointer deve ser adicionado apenas em produção, não em desenvolvimento."

**Gabarito**:
1. **F** — Custo cresce linearmente, qualidade cai (Lost in the Middle), latência aumenta, e memória vetorial é entre sessões. Context maior reduz, mas não elimina.
2. **F** — Vector DB é péssimo para exact match, ordenação temporal, agregação e joins. Use vector para recall semântico, relacional para fatos estruturados, KG para relações.
3. **F** — Sumarização é lossy por definição. Compressão implica perda de detalhe. Mitigação: manter eventos originais no vector DB e usar sumário multi-nível com fallback.
4. **V** — Destruição da chave é instantânea e criptograficamente segura. Mas requer planejamento: encriptar por usuário desde o início.
5. **F** — Checkpointer deve ser usado desde o dia 1. Em dev, permite resume/replay para debugging. Modelar estado serializável desde o início evita refatoração dolorosa depois.

---

## Projeto do Módulo

### P1 — Memória de Agente Pessoal de Longo Prazo
**Prazo**: 2 semanas
**Formato**: Individual
**Carga**: ~10h

**Descrição**: Projetar a memória de um agente pessoal de produtividade (assistente que acompanha um usuário por meses/anos) com as 4 camadas (working, episódica, semântica, procedural). Justificar trade-offs arquiteturais.

**Entregáveis**:
1. **Implementação** do agente com:
   - Checkpointer (Postgres ou SQLite)
   - Memória episódica (Qdrant ou Chroma)
   - Memória semântica (KB simples: JSON ou SQLite)
   - Política de eviction implementada
2. **ADR de Memória** (Architecture Decision Record) documentando:
   - Por que essas 4 camadas
   - Quais backends e por quê
   - Política de eviction
   - Trade-offs (custo vs benefício, latência vs precisão)
3. **Política de Privacidade/Evicção** em texto:
   - Quais dados são memorizados
   - TTL por tipo de dado
   - Estratégia de direito ao esquecimento
   - Tratamento de PII
4. **Demo** mostrando memória útil em sessões espaçadas:
   - Sessão 1: usuário compartilha preferências
   - Sessão 2 (dias depois): agente lembra das preferências sem re-perguntar

**Stack sugerida**:
- LangGraph (StateGraph + checkpointer)
- Postgres ou SQLite (checkpointer)
- Qdrant ou Chroma (vector DB)
- OpenAI ou Anthropic (LLM + embeddings)

**Critério de sucesso**:
- Agente demonstra memória útil em sessões espaçadas ✅
- 4 camadas implementadas e justificadas ✅
- ADR documenta trade-offs de forma clara ✅
- Política de privacidade/eviction é coerente ✅

**Avaliação** (rubrica de 4 pilares):

| Pilar | Peso | Critério |
|---|---|---|
| Técnico | 40% | Implementação funcional, 4 camadas, demo de memória cross-sessão |
| Consultivo | 30% | ADR de memória — clareza dos trade-offs arquiteturais |
| Comportamental | 20% | Code review de um colega (foco na política de eviction) |
| Prático | 10% | Demo ao vivo: agente lembrando entre sessões |

**Nota mínima de aprovação**: 3.0

---

## Laboratórios

### Lab 1 — Checkpointer em Postgres (4h)
**Referência**: `05-Labs/ETHAGT05/Lab1-Checkpointer-Postgres/`

**Objetivo**: Implementar um agente interrompido e retomado dias depois, preservando estado.

**Entregáveis**:
- Agente LangGraph com `PostgresSaver`
- Script que: inicia tarefa → `Ctrl+C` → retoma com mesmo `thread_id`
- Log mostrando estado preservado (mensagens, contexto, steps)
- Replay de execução anterior para debug

### Lab 2 — Memória Episódica (5h)
**Referência**: `05-Labs/ETHAGT05/Lab2-Memoria-Episodica/`

**Objetivo**: Agente que recorda interações anteriores relevantes via recall vetorial.

**Entregáveis**:
- Agente LangGraph + Qdrant
- Pipeline de recall: embed → metadata filter → vector search → re-rank → contexto
- Comparação A/B: agente com memória vs sem memória (qualidade das respostas)
- Métricas: hit rate do recall, latência, custo extra por interação
