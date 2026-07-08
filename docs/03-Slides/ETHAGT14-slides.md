# ETHAGT14 — Escalabilidade & Sistemas Distribuídos de Agentes — Slides

> Apresentação para aula síncrona · ~50 min · 13 slides

## Estrutura da aula
- Abertura (5 min): gancho/motivação
- Teoria (25 min): conceitos principais com diagramas de referência
- Demonstração (10 min): código ao vivo ou walkthrough de lab
- Exercício (5 min): questão rápida ou discussão
- Fechamento (5 min): conexão com próximo módulo, leitura recomendada

## Slides

### Slide 1 — Título
- ETHAGT14 — Escalabilidade & Sistemas Distribuídos de Agentes
- Professor, data, Universität Etho
- Pré-requisito: ETHAGT11
- ~1 min

### Slide 2 — Agenda
1. Onde agentes esbarram em escala
2. Caching (exato, semântico, embeddings, tools)
3. Model routing e otimização (complexidade, batching)
4. Distribuição (stateless, sharding, replica)
5. Infraestrutura (Kubernetes, serverless)
6. FinOps de agentes (orçamento, custo)
- ~1 min

### Slide 3 — Gancho / Motivação
- Problema: agente que funciona para 1 usuário custa R$0,50/consulta — para 10.000 usuários, o custo explode
- Exemplo: startup de assistente pessoal → 1.000 usuários simultâneos → latência de 30s, custo mensal de R$50k
- A solução: caching, roteamento, distribuição, FinOps
- Pergunta: *Qual o maior custo oculto que vocês já viram em sistemas de LLM?*
- ~3 min

### Slide 4 — Onde Agentes Esbarram em Escala
- Latência de LLM como gargalo dominante (TTFT, TPOT)
- Custo crescendo com contexto (KV cache, janela grande)
- Concorrência e rate limits (APIs de LLM limitam RPM/TPM)
- Estado distribuído (memória compartilhada entre réplicas)
- Diagrama: `12-Diagrams/ETHAGT14/bottleneck-analysis.mmd`
- ~4 min

### Slide 5 — Caching
- Cache de prompts/exact match (mesmo prompt → mesma resposta)
- Cache semântico (perguntas similares → mesma resposta)
- Cache de embeddings (evita re-embedding)
- Cache de tool results (resultados idempotentes)
- Invalidação e consistência (cache poisoning, TTL)
- Pergunta: *Cache semântico: qual threshold de similaridade? O que acontece com falsos positivos?*
- ~5 min

### Slide 6 — Model Routing e Otimização
- Roteamento por complexidade: Haiku para simples, Sonnet para difícil, Opus para crítico
- Batching de requests (junta N requisições em 1 chamada de API)
- Speculative decoding / prediction (gera rascunho, verifica)
- Streaming para latência percebida (começar a responder antes do fim)
- Distilação e fine-tuning (panorama)
- Pergunta: *Routing por complexidade: como medir a complexidade antes de chamar o modelo?*
- ~4 min

### Slide 7 — DEMO: Cache Semântico
- Código ao vivo: adicionar cache semântico a um agente
- Mostrar: primeira chamada → LLM (lenta, cara); segunda chamada (pergunta similar) → cache hit (rápida, barata)
- Medir redução de custo/latência em 10 perguntas
- Referência: `05-Labs/ETHAGT14/Lab1-Cache-Semantico`
- ~5 min

### Slide 8 — Distribuição
- Stateless vs stateful workers: quando cada
- Sharding por usuário/sessão/domínio (agente A atende usuários 1-1000)
- Replica e balanceamento (round-robin, least-connections)
- Coordenação: consensus (Raft), leader election
- Diagrama: `12-Diagrams/ETHAGT14/sharding.mmd`
- ~4 min

### Slide 9 — Infraestrutura
- Kubernetes para agentes: pods, HPA, service mesh
- Serverless (AWS Lambda) vs dedicado (EC2, GPU)
- GPUs para inferência local (vLLM, TGI) — opcional, alto custo
- Service mesh (Istio, Linkerd) para comunicação entre agentes
- Custo de infra não é só LLM (memória, rede, storage)
- ~4 min

### Slide 10 — FinOps de Agentes
- Orçamento por execução, por usuário, por tenant
- Medição granular de custo (por step, por tool, por token)
- Otimização contínua: dashboards de custo por funcionalidade
- Trade-offs: custo × latência × qualidade (triângulo)
- Pricing para clientes (se aplicável): freemium, tokens, assinatura
- Diagrama: `12-Diagrams/ETHAGT14/finops-flow.mmd`
- Pergunta: *Você cobraria por chamada de API ou assinatura mensal?*
- ~4 min

### Slide 11 — Exercício: Orçamento com Circuit Breaker
- Cenário: sistema multi-tenant com orçamento de R$100/usuário/mês
- Em duplas: escrever lógica de circuit breaker que bloqueia execuções se custo mensal exceder
- Incluir: alerta, log, exceção amigável
- 3 min, compartilhar 2 abordagens
- ~4 min

### Slide 12 — Conexão com Próximo Módulo
- ETHAGT15 — Meta-Agentes: auto-aprendizado contínuo
- ETHAGT90 — Capstone: otimização de custo em sistema real
- Leitura: Kleppmann, M. *Designing Data-Intensive Applications*
- Richards, M. & Ford, N. *Fundamentals of Software Architecture*
- FinOps Foundation *FinOps for ML/AI*
- ~2 min

### Slide 13 — Referências
- Kleppmann, M. *Designing Data-Intensive Applications*
- Richards, M. & Ford, N. *Fundamentals of Software Architecture*
- Cloud provider docs (Anthropic, OpenAI, Bedrock, Vertex)
- Litellm docs (roteamento e custo)
- FinOps Foundation *FinOps for ML/AI*
- vLLM, TGI docs
- ~1 min
