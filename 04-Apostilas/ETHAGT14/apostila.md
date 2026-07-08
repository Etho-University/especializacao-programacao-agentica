# ETHAGT14 — Escalabilidade & Sistemas Distribuídos de Agentes

> **Apostila do curso** · Especialização em Programação Agêntica · Universidade Etho
> Fase D — Produção, Governança e Fronteira · Carga 30 h · Versão 1.0 · Julho 2026
> *Material de referência duradouro (nível pós-graduação lato sensu). Os slides são auxiliares.*

---

## Sumário

- **Capítulo 1** — Onde agentes esbarram em escala
- **Capítulo 2** — Caching
- **Capítulo 3** — Model routing e otimização
- **Capítulo 4** — Distribuição
- **Capítulo 5** — Infraestrutura
- **Capítulo 6** — FinOps de agentes
- **Capítulo 7** — Casos de estudo
- **Capítulo 8** — Referências e leituras

---

## Capítulo 1 — Onde agentes esbarram em escala

### 1.1 Do protótipo à escala

Um agente que funciona para 10 usuários em protótipo frequentemente *quebra* em escala: fica lento, caro, sobrecarregado. Este módulo trata a **escala de produção** — levar sistemas de agentes a milhares de usuários/tarefas mantendo custo, latência e qualidade controlados. É a engenharia que separa uma demo de um produto.

### 1.2 O gargalo dominante: o LLM

Em sistemas agentes, o **gargalo dominante é quase sempre o LLM** — sua latência (segundos por chamada) e custo (centavos por chamada, multiplicados por N iterações). As demais componentes (tools, memória, rede) são tipicamente ordens de magnitude mais rápidas e baratas. A consequência: **otimizar o LLM é onde o maior retorno está.** Antes de micro-otimizar infraestrutura, pergunte: quantas chamadas LLM estou fazendo, e posso fazer menos?

> **Diagrama de referência:** [`12-Diagrams/ETHAGT14/bottleneck-analysis.mmd`](../../12-Diagrams/ETHAGT14/bottleneck-analysis.mmd).

### 1.3 Custo crescendo com contexto

O custo de uma chamada LLM cresce com o *tamanho do contexto* (mais tokens de entrada). Em agentes, o contexto cresce com a conversação, as observações de tools e a memória recuperada — então o custo *por iteração* cresce ao longo de uma tarefa. Sem gestão de contexto (ETHAGT05 §3), o custo explode. A escala agrava: mil tarefas longas custam muito mais que mil tarefas curtas.

### 1.4 Concorrência e rate limits

Provedores de LLM impõem **rate limits** (requests por minuto, tokens por minuto). Em escala, múltiplas tarefas concorrem por esses limites — e o sistema fica limitado pelo teto do provedor, não pela sua infraestrutura. Gerenciar rate limits (filas, backoff, múltiplos provedores) é parte essencial da escala.

### 1.5 Estado distribuído

Em multi-agente distribuído (ETHAGT11), o *estado* (memória, contexto de workflow) vive em múltiplos nós. Manter consistência, sobreviver a falhas e escalar esse estado é o problema clássico de sistemas distribuídos (Kleppmann, *Designing Data-Intensive Applications*).

---

## Capítulo 2 — Caching

### 2.1 A alavanca de maior retorno

Depois de "fazer menos chamadas" (reduzir iterações), a maior alavanca de custo/latência é o **caching**: se a mesma computação já foi feita, reutilizar o resultado em vez de refazer. Em agentes, há múltiplas camadas de cache a explorar.

### 2.2 Cache de prompts (exact match)

A forma mais simples: se uma chamada LLM idêntica (mesmo modelo, prompt, parâmetros) já foi feita, retornar a resposta cacheada. Útil para casos repetitivos. Provedores oferecem *prompt caching* nativo (Anthropic, OpenAI) que cacheia o prefixo do prompt — reduzindo custo de contextos longos repetidos.

### 2.3 Cache semântico

O cache *exact match* perde o caso onde a pergunta é *ligeiramente diferente* mas pede a mesma coisa. O **cache semântico** usa embeddings: embeda a pergunta, busca no cache por perguntas *semanticamente similares*; se encontrar acima de um limiar, retorna a resposta cacheada. Captura muito mais acertos que o exact match.

```python
def cached_llm(prompt):
    q = embed(prompt)
    hit = semantic_cache.search(q, threshold=0.92)
    if hit:
        return hit.response
    resp = llm(prompt)
    semantic_cache.add(q, resp)
    return resp
```

### 2.4 Cache de embeddings e tool results

- **Embeddings:** se o mesmo texto é embedado repetidamente, cacheie o embedding (computação não-trivial).
- **Tool results:** se uma tool retorna o mesmo dado para os mesmos args (ex.: `get_weather`), cacheie o resultado — mas atenção ao *frescor* (previsão do tempo muda).

### 2.5 Invalidação e consistência

Cache introduce o problema da **invalidação**: quando o resultado cacheado deixa de ser válido? Previsão do tempo expira; dados que mudam precisam ser invalidados. Políticas: TTL (expira após N tempo), invalidação explícita (quando a fonte muda), e versionamento (cache por versão dos dados). Cache *stale* (desatualizado) é um bug silencioso.

> **Princípio.** Quando o cache semântico falha? Quando perguntas semanticamente similares pedem *respostas diferentes* (ex.: "saldo da conta A" vs "saldo da conta B" são semânticamente próximas mas a resposta depende do contexto). Use cache semântico só onde a similaridade implica resposta compartilhada.

---

## Capítulo 3 — Model routing e otimização

### 3.1 Roteamento por complexidade

Nem toda tarefa precisa do modelo mais caro. O **model routing** (ETHAGT03 §3.3) envia tarefas fáceis para modelos rápidos/baratos e difíceis para modelos potentes/caros. Em escala, isso reduz custo drasticamente mantendo qualidade — a maior parte das tarefas é "fácil". O desafio é medir a complexidade confiavelmente: um classificador de complexidade, calibrado contra o conjunto golden (ETHAGT12).

### 3.2 Batching de requests

Provedores oferecem **batch APIs**: envie N requests, receba N respostas, com desconto (ex.: 50% mais barato) e latência maior (processamento assíncrono). Para tarefas *não*-interativas (processamento em massa, offline), o batching é uma economia enorme. Para interativas (usuário esperando), a latência extra não compensa.

### 3.3 Speculative decoding e streaming

- **Speculative decoding:** um modelo pequeno "adivinha" tokens que um modelo grande confirma — reduzindo latência sem perder qualidade. Relevante para quem serve modelos próprios (vLLM, TGI).
- **Streaming:** retornar tokens *à medida que são gerados* reduz a *latência percebida* (o usuário vê progresso). **Atenção:** streaming *não* reduz a latência total — o tempo até o último token é o mesmo. Mas melhora a experiência percebida.

### 3.4 Distilação e fine-tuning (panorama)

Para tarefas muito específicas e de alto volume, **fine-tuning** (ajustar um modelo ao domínio) ou **distilação** (treinar um modelo pequeno a imitar um grande) podem reduzir custo e melhorar qualidade. É uma otimização avançada — não é trivial e tem custo inicial. Reservada para quando o volume justifica.

---

## Capítulo 4 — Distribuição

### 4.1 Stateless vs stateful workers

Para escalar, distribua o processamento por múltiplos *workers*:

- **Stateless:** workers não mantêm estado entre requests; qualquer worker pode tratar qualquer request. Fácil de escalar (adicione workers), mas exige externalizar estado (memória em Redis/DB). Ideal para a *maioria* do processamento.
- **Stateful:** workers mantêm estado (ex.: uma sessão longa). Mais complexo de escalar (afinidade), mas necessário para workflows duráveis (ETHAGT11).

> **Diagrama de referência:** [`12-Diagrams/ETHAGT14/sharding.mmd`](../../12-Diagrams/ETHAGT14/sharding.mmd).

### 4.2 Sharding por usuário/sessão/domínio

Para manter o estado coeso, **shardeie** por uma chave (usuário, sessão, tenant): todo o processamento de uma entidade vai ao mesmo worker. Isso mantém o estado local (rápido) e isola (multi-tenancy). O erro: sharding mal escolhido causa *hotspots* (um shard sobrecarregado).

### 4.3 Replica e balanceamento

Replicar workers (múltiplas cópias) com um *load balancer* distribui carga e provê redundância (se um cai, outros assumem). Combine com health checks e auto-scaling (adicionar workers sob carga).

### 4.4 Coordenação: consensus e leader election

Em sistemas distribuídos com estado, surge a necessidade de *coordenação*: qual worker é o "líder" para uma tarefa? Como evitar que dois workers processem a mesma tarefa (duplicação)? Padrões de *consensus* (Paxos, Raft) e *leader election* resolvem isso — frequentemente via um serviço (etcd, ZooKeeper, ou o próprio Temporal).

### 4.5 "Stateless é sempre preferível?"

Quase sempre — pela simplicidade de escala. Mas workflows de longa duração com estado rico (ETHAGT11) precisam de stateful. A regra: **stateless por padrão; stateful só quando o estado é intrínseco à tarefa.** Externalize o máximo de estado possível.

---

## Capítulo 5 — Infraestrutura

### 5.1 Kubernetes para agentes

O **Kubernetes** é a plataforma de fato para orquestrar workers distribuídos: auto-scaling, health checks, rolling updates, service discovery. Para agentes em escala, K8s gerencia o *compute* (workers), enquanto ferramentas como Temporal gerenciam o *workflow*. Eles se complementam.

### 5.2 Serverless vs dedicado

- **Serverless** (Lambda, Cloud Run): escala a zero, paga por execução. Bom para cargas *esparsas* ou *intermitentes*. Limite: cold starts (latência na primeira invocação) e timeouts (muitos serverless limitam a minutos — inadequado para workflows longos).
- **Dedicado** (containers/servidores sempre no ar): baixa latência, sem limites de duração. Bom para cargas *contínuas*. Custa mesmo sem tráfego.

A escolha depende do padrão de carga.

### 5.3 GPUs para inferência local

Para quem quer controlar custo e privacidade, servir modelos próprios em **GPUs** (com vLLM, TGI) é uma alternativa às APIs. Vantagem: custo previsível (capex), privacidade total. Desvantagem: complexidade operacional, necessidade de expertise em ML infra, e o modelo fica atrás do estado da arte dos provedores. Reservado para casos específicos.

### 5.4 Service mesh e custo de infra

Em microserviços, um **service mesh** (Istio, Linkerd) gerencia comunicação, segurança e observabilidade entre serviços. Adiciona capacidades mas também complexidade e overhead. O custo de infra (computação, rede, armazenamento) deve ser monitorado — em escala, otimizações de infra somam.

---

## Capítulo 6 — FinOps de agentes

### 6.1 Custo como métrica de primeira classe

Em ETHAGT01 (§6.4) estabelecemos custo e latência como métricas de primeira classe. Em escala, isso vira **FinOps**: a prática de gerenciar e otimizar o custo financeiro do sistema como uma disciplina contínua. Agentes são particularmente vulneráveis a custo descontrolado (chamadas LLM multiplicam-se), então FinOps é crítica.

> **Diagrama de referência:** [`12-Diagrams/ETHAGT14/finops-flow.mmd`](../../12-Diagrams/ETHAGT14/finops-flow.mmd).

### 6.2 Orçamento por execução, usuário, tenant

Defina **orçamentos** em múltiplos níveis: por execução (esta tarefa deve custar < $0,50), por usuário (mês), por tenant. Quando o orçamento estoura, o sistema age — alerta, degrada (modelo mais barato), ou bloqueia. Um circuit breaker de custo impede que um único usuário ou bug drenem o orçamento.

### 6.3 Medição granular

Meça custo *granularmente*: por step, por tool, por tipo de tarefa, por modelo. Sem granularidade, você não sabe *onde* o custo está — e não pode otimizar. Ferramentas como **LiteLLM** roteiam e medem custo através de múltiplos provedores de forma unificada.

### 6.4 Otimização contínua e trade-offs

FinOps é contínuo: monitore, identifique os maiores gastadores, otimize, meça novamente. O trade-off fundamental é **custo × latência × qualidade** — raramente melhora-se os três simultaneamente. A otimização consciente escolhe qual dimensão sacrificar (ex.: aceitar +5% de latência por -30% de custo).

### 6.5 Pricing para clientes

Se você cobra pelo serviço, o custo internal precisa casar com o pricing. Modelos de pricing: por uso (pay-per-task), assinatura, ou híbrido. Entender o *custo unitário real* (com margem de segurança para variância) é pré-requisito para pricing sustentável.

---

## Capítulo 7 — Casos de estudo

### 7.1 Assistentes enterprise em escala

Os casos de escala em produção (assistentes enterprise com milhares de usuários) mostram um padrão: a combinação de *model routing* (fáceis→barato), *caching semântico* (acertos repetidos) e *orçamentos por tenant* é o que torna o custo viável. Sem essas três, a unidade econômica não fecha.

> **Leitura.** [`09-CaseStudies/`](../../09-CaseStudies/) e Research KB ([`20-Research/`](../../20-Research/)).

### 7.2 Lições transversais

1. **O LLM é o gargalo.** Otimize chamadas antes de infra.
2. **Cache é a maior alavanca de custo.** Especialmente o semântico.
3. **FinOps é contínua.** Orçamentos, medição granular, otimização iterativa.
4. **Stateless por padrão.** Externalize estado.

---

## Capítulo 8 — Referências e leituras

### 8.1 Bibliografia fundamental

- **Kleppmann, M.** *Designing Data-Intensive Applications.*
- **Richards, M. & Ford, N.** *Fundamentals of Software Architecture.*
- **Cloud provider docs:** Anthropic, OpenAI, Bedrock, Vertex.

### 8.2 Bibliografia complementar

- **FinOps Foundation.** *FinOps for ML/AI.*
- **LiteLLM** docs — roteamento e custo unificado.
- **Leviathan, Y. et al.** *Speculative Decoding.* arXiv:2211.17192.

### 8.3 Recursos práticos

- **Serving:** vLLM, TGI (HuggingFace).
- **Infra:** Kubernetes, Redis, OpenTelemetry, Grafana, LiteLLM.

### 8.4 Ficha de pesquisa

Fontes em [`20-Research/ETHAGT14-pesquisa.md`](../../20-Research/ETHAGT14-pesquisa.md). Última consulta: Julho 2026.

---

## Síntese do módulo

Ao concluir ETHAGT14, você deve ser capaz de:

1. **Identificar** gargalos em sistemas multi-agente (LLM dominante) e priorizar otimização.
2. **Aplicar** caching (semântico, de prompts, de embeddings, de tools) com invalidação correta.
3. **Distribuir** agentes (stateless/sharding/replica/consensus) com consciência de trade-offs.
4. **Otimizar** custo e latência (model routing, batching, streaming) e operar infraestrutura.
5. **Operar** FinOps de agentes (orçamentos, medição granular, pricing).

Próximos passos: ETHAGT90 (Capstone) exige um sistema escalável e um FinOps dashboard.

---

*Mantido por: Escola de Tecnologia — Universidade Etho · Área de Inteligência Artificial · Versão 1.0 · Julho 2026*
