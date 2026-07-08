# ETHAGT14 — Perguntas para Discussão

> Perguntas para estimular debate durante e após a aula.
> Organizadas por profundidade: rápida (1-2 min) → média (3-5 min) → profunda (10+ min).

---

## Perguntas Rápidas (1-2 min)

### Q1 — Maior Custo Oculto
"Qual o maior custo oculto que vocês já viram em sistemas de LLM?"
- **Objetivo**: Calibrar a turma e revelar custos invisíveis
- **Slide**: 5, 14
- **Resposta esperada**: Varia — contexto crescente, retries silenciosos, tools/APIs externas, logs, observabilidade. Lição: custo de LLM é só 60-70% do total.

### Q2 — Latência p95 do Sistema
"Qual a latência p95 do agente mais crítico de vocês hoje?"
- **Objetivo**: Fazer alunos medirem latência real (não média)
- **Slide**: 8, 13
- **Resposta esperada**: Surpreendentemente alta (frequentemente >10s). Revela urgência de otimização.

### Q3 — Experiência com Caching
"Vocês já implementaram cache semântico em produção? Hit rate?"
- **Objetivo**: Calibrar experiência prática
- **Slide**: 18
- **Ação**: Contar mãos levantadas

### Q4 — Rate Limit em Produção
"Quem aqui já tomou 429 em produção?"
- **Objetivo**: Mostrar que rate limit é problema universal
- **Slide**: 10
- **Resposta esperada**: A maioria que já operou LLM em produção.

### Q5 — Orçamento Configurado
"Vocês têm orçamento (por execução/usuário/tenant) configurado hoje?"
- **Objetivo**: Revelar lacuna comum em FinOps
- **Slide**: 55
- **Resposta esperada**: <30% tem orçamento granular configurado. Motivar a seção de FinOps.

---

## Perguntas Médias (3-5 min)

### Q6 — Threshold do Cache Semântico
"Em que tipo de sistema você usaria threshold baixo (0.80)? E alto (0.95)?"
- **Objetivo**: Praticar escolha de threshold por domínio
- **Slide**: 20
- **Resposta esperada**: Baixo (0.80) para FAQs gerais, conhecimento estável. Alto (0.95) para dados numéricos/sensíveis (preço, dados pessoais).

### Q7 — Por Onde Começar a Otimizar
"Se você tivesse 1 semana para otimizar um agente em produção, por onde começaria?"
- **Objetivo**: Priorização de otimizações
- **Slide**: 37
- **Resposta esperada**: Caching primeiro (maior ROI, menor esforço). Depois routing. Depois batching. Speculative e fine-tuning exigem mais tempo.

### Q8 — Sharding por Qual Chave
"Em qual chave vocês fariam sharding no sistema de vocês (tenant, user, região, domínio)?"
- **Objetivo**: Aplicar sharding ao caso real deles
- **Slide**: 42
- **Dica**: Depende do padrão de acesso. Multi-tenant → tenant_id. Global → região. Multi-domínio → categoria.

### Q9 — Cálculo de Custo em Escala
"Seu agente custa R$0,05 por execução, faz 5 steps, atende 1.000 usuários/dia com 10 consultas cada. Quanto custa por mês?"
- **Objetivo**: Praticar cálculo de custo real
- **Slide**: 9, 27
- **Cálculo**: R$0,05 × 5 steps × 1.000 usuários × 10 consultas × 30 dias = R$75.000/mês. Sem otimização. Com 60% de redução (caching + routing): R$30.000/mês.

### Q10 — Pricing para Clientes
"Vocês cobrariam por chamada de API ou assinatura mensal?"
- **Objetivo**: Discutir modelos de pricing
- **Slide**: 60
- **Dica**: Assinatura com limite + excedente é geralmente mais previsível para cliente e sustentável para você.

---

## Perguntas Profundas (10+ min)

### Q11 — Cache Semântico Perigoso
"Em que cenário cache semântico é mais perigoso que útil?"
- **Objetivo**: Pensamento crítico sobre limitações do caching
- **Slide**: 72
- **Resposta esperada**: Em domínios sensíveis a tempo/contexto (preço de ações, notícia, dados pessoais). Falso positivo serve resposta errada como certa. Para esses, use TTL curto ou não cacheie.

### Q12 — Stateless é Sempre Preferível
"Stateless é sempre preferível? Justifique com um contra-exemplo."
- **Objetivo**: Nuance sobre o trade-off stateless/stateful
- **Slide**: 72
- **Resposta esperada**: Falso. Stateful é necessário para sessões longas com contexto acumulado, WebSockets/streaming, caches em memória para baixa latência. Solução híbrida: stateless-friendly com checkpoint externo.

### Q13 — Convencendo o CTO sobre FinOps
"Como você convenceria um CTO a investir em FinOps ANTES de escalar?"
- **Objetivo**: Estruturar argumento executivo
- **Slide**: 72
- **Resposta esperada**: Argumentos: (1) "Sem FinOps, um bug ou pico de uso pode gerar $50k em uma noite — FinOps é seguro contra desastre financeiro"; (2) "ROI é imediato — circuit breaker evita perda, dashboards revelam otimizações"; (3) "FinOps é mais barato que o estrago que previne".

### Q14 — Maior Risco de Autoscaling por CPU
"Qual o maior risco de autoscaling baseado apenas em CPU?"
- **Objetivo**: Pensar sobre limitações de métricas de escala
- **Slide**: 72
- **Resposta esperada**: Autoscaling por CPU não captura gargalos I/O-bound. Uma fila pode estar crescendo com CPU baixa (agente esperando API externa). Sempre use métricas de negócio (tamanho de fila, latência p95, taxa de erro) complementarmente.

### Q15 — Escolhendo Eixo do Trade-off
"No triângulo custo × latência × qualidade, qual eixo é prioritário no sistema de vocês? Por quê?"
- **Objetivo**: Aplicar trade-off ao caso real
- **Slide**: 57
- **Ação**: Deixar 3-4 alunos compartilharem justificativas. Não há resposta certa — depende do caso de uso (saúde = qualidade; suporte = custo; chat ao vivo = latência).

---

## Perguntas Bônus (para alunos avançados)

### Q16 — KV Cache do Provider vs Cache Semântico Próprio
"Qual a diferença entre o KV cache do provider (Anthropic/OpenAI) e o cache semântico que você implementa?"
- **Objetivo**: Distinguir camadas de cache
- **Resposta**: KV cache do provider cacheia o prefixo do prompt no lado deles — reduz custo de processamento mas você ainda paga pelos tokens (com desconto). Cache semântico próprio intercepta a query ANTES de chamar o provider — custo zero, latência zero. São complementares (L3 e L2 respectivamente).

### Q17 — Multi-Provider como Estratégia de Rate Limit
"Como usar múltiplos providers (Anthropic + OpenAI + Bedrock) para contornar rate limits?"
- **Objetivo**: Estratégia avançada de rate limit handling
- **Resposta**: Failover automático. Request tenta Anthropic primeiro; se 429, vai para OpenAI; se 429, vai para Bedrock. LiteLLM implementa isto nativamente. Cuidado: modelos têm capacidades diferentes — fallback pode reduzir qualidade.

### Q18 — When Does Fine-Tuning Beat Routing
"Em que cenário fine-tuning de um modelo pequeno é melhor que routing para modelo grande?"
- **Objetivo**: Profundizar a decisão fine-tuning vs routing
- **Resposta**: Quando o domínio é específico e estável, e volume é alto (>100k requests/mês). Exemplo: classificação de tickets de suporte em uma empresa específica — fine-tune de Haiku no domínio da empresa pode superar Sonnet genérico, a 10x menos custo.

### Q19 — Cache Poisoning em Sistema Multi-Tenant
"Como um tenant malicioso poderia envenenar o cache compartilhado? Como mitigar?"
- **Objetivo**: Profundizar segurança de caching
- **Resposta**: Cenário: tenant envia query esperada com contexto manipulado, LLM gera resposta errada, é cacheada, outros tenants recebem a resposta errada. Mitigação: (1) separar cache por tenant; (2) não cachear respostas de tiers não confiáveis; (3) validar respostas antes de cachear (eval automático).

### Q20 — TCO de Self-Hosting vs API
"Em que ponto (volume/mês) self-hosting de LLM se torna mais barato que API?"
- **Objetivo**: Decisão de make-or-buy para inferência
- **Resposta**: Depende do modelo e da GPU. Regra prática: para volumes > 1M tokens/dia com modelo open-source que atende ao caso (e.g., Llama 70B), self-hosted geralmente vence. Abaixo disso, API é mais barato (sem custo de ops). Calcule TCO: GPU/hora × 24 × 30 + ops (engenheiro dedicado) vs API/token × volume.
