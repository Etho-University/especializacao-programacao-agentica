# ETHAGT10 — Exercícios

> Exercícios para aula e para casa.
> Organizados por tipo: em aula, individual, em duplas, projeto.

---

## Exercícios em Aula

### E1 — Matching Cenário → Topologia (Votação Rápida)
**Slide**: 16
**Tempo**: 2 min
**Formato**: Individual, votação de mão levantada

**Enunciado**: Para cada cenário abaixo, vote na topologia mais adequada:

1. "Chatbot de suporte com escalonamento"
2. "Revisão de PR com 3 especialistas"
3. "Relatório financeiro em etapas"
4. "Simulação de mercado"
5. "Assistente pessoal multi-função"
6. "Pesquisa autônoma com exploração"

**Gabarito**:
1. Supervisor (escalonamento = roteamento) ou Swarm (handoffs)
2. Supervisor (síntese de 3 revisões) ou Swarm (se independentes)
3. Pipeline (etapas fixas e predefinidas)
4. Actor Model / Mesh (agentes autônomos em paralelo)
5. Swarm (multi-função com handoffs)
6. Tree (exploração de múltiplos caminhos)

---

### E2 — Hierarchical ou Flat? (Votação)
**Slide**: 28
**Tempo**: 2 min
**Formato**: Individual, votação

**Enunciado**: Para cada cenário, vote: Flat (1 supervisor), 2 níveis, ou 3 níveis?

1. "Sistema com 3 domínios distintos (code, security, docs)"
2. "Chatbot simples com 3 ferramentas"
3. "Software house simulado com 6 papéis"
4. "Assistente de viagem com 4 sub-tarefas"

**Gabarito**:
1. 2 níveis (3 domínios distintos justificam sub-supervisores)
2. Flat (3 ferramentas = 1 supervisor resolve)
3. 2-3 níveis (MetaGPT: PM → Architect → Engineer → QA)
4. Flat (4 sub-tarefas em um domínio)

---

### E3 — Pipeline ou Agente? (Justificativa)
**Slide**: 40
**Tempo**: 2 min
**Formato**: Individual, votação + justificativa em 1 frase

**Enunciado**: Para cada cenário, vote Pipeline (P) ou Agente orquestrador (A) e justifique:

1. "Geração de relatório financeiro trimestral"
2. "Investigação de incidente de segurança"
3. "Processamento de pedidos de e-commerce"

**Gabarito**:
1. **P** — etapas fixas: coletar → analisar → redigir → revisar → publicar
2. **A** — passos imprevisíveis: depende do incidente, ordem varia
3. **P** — processamento padronizado: validar → pagar → enviar → confirmar

---

### E4 — 6 Cenários + Esqueleto de ADR (Grupos)
**Slide**: 58
**Tempo**: 5 min (3 min discussão + 2 min compartilhar)
**Formato**: Grupos de 3-4

**Enunciado**: Para cada um dos 6 cenários abaixo, em grupos:
1. Propor a topologia mais adequada
2. Escrever o esqueleto de ADR (Contexto, Decision, Consequências)

**Cenários**:
1. "Chatbot de suporte com escalonamento humano"
2. "Sistema de revisão de código com 3 especialistas"
3. "Pipeline de geração de relatório financeiro"
4. "Simulação de mercado com múltiplos agentes"
5. "Assistente pessoal multi-função"
6. "Sistema de pesquisa autônoma com exploração"

**Critério de avaliação do ADR**:
- **Contexto**: problema, requisitos, restrições estão claros?
- **Decision**: topologia + justificativa conectada aos requisitos?
- **Consequências**: trade-offs aceitos e sinais de evolução identificados?

**Exemplo de ADR (Cenário 2 — Revisão de Código)**:
```
# ADR-001: Topologia para Revisão de Código Multi-Agente

## Contexto
Sistema de revisão automatizada de PRs com 3 especialistas:
code quality, security, documentation. Requisitos:
- Latência < 30s por PR (não crítico, mas desejável)
- Síntese das 3 revisões em relatório unificado
- Custo controlado (< $0.50 por PR)

## Decision
Supervisor com 3 workers (code, security, docs).
Justificativa: síntese de 3 revisões é requisito;
supervisor orquestra e agrega naturalmente.

## Consequências
- Trade-off: supervisor adiciona ~1 hop de latência (aceitável)
- Risco: supervisor gargalo se volume de PRs crescer
- Sinal de evolução: se P95 > 30s, avaliar swarm paralelo
```

---

## Exercícios Individuais (para casa)

### E5 — Esqueleto de ADR para Seu Sistema
**Tempo estimado**: 20 min
**Formato**: Individual, escrito

**Enunciado**: Escolha um sistema multi-agente (real ou hipotético) e escreva um ADR completo:
1. **Contexto**: problema, requisitos (latência, custo, consistência), restrições
2. **Decision**: topologia escolhida + justificativa conectada aos requisitos
3. **Consequências**: trade-offs aceitos, riscos, sinais de evolução

**Critério de avaliação**:
- Contexto tem requisitos quantificáveis (não "rápido", mas "P95 < 5s") ✅
- Decision justifica com base nos requisitos ✅
- Consequências incluem sinais de evolução mensuráveis ✅
- Considerou ao menos 1 topologia alternativa ✅

---

### E6 — Implementar Supervisor em LangGraph
**Tempo estimado**: 1h
**Formato**: Individual, código

**Enunciado**: Implemente um supervisor com 3 workers em LangGraph:
- Worker A: pesquisador (usa uma tool de busca simulada)
- Worker B: escritor (usa uma tool de escrita)
- Worker C: revisor (usa uma tool de validação)
- Supervisor: roteia usando tool calls

**Entregáveis**:
- Código funcional em Python
- Trace de execução mostrando o supervisor roteando
- Teste com 3 perguntas que exercitem diferentes workers

**Critério de sucesso**:
- Supervisor roteia corretamente para o worker certo ✅
- Cada worker executa e retorna resultado ✅
- Supervisor sintetiza a resposta final ✅
- Trace mostra claramente cada nível ✅

---

### E7 — Comparar Swarm vs Supervisor (Mesma Tarefa)
**Tempo estimado**: 2h
**Formato**: Individual, código + relatório

**Enunciado**: Implemente a MESMA tarefa em duas topologias:
- **Versão Supervisor**: 3 workers com supervisor roteando
- **Versão Swarm**: 3 agentes com handoffs

**Tarefa**: "Revisão de PR com 3 especialistas (code, security, docs)"

**Medir e comparar**:
1. Latência (tempo total de execução)
2. Custo (número de LLM calls / tokens)
3. Qualidade (subjetiva: a saída faz sentido?)

**Entregáveis**:
- Código das duas versões
- Tabela comparativa com as 3 métricas
- Análise: qual topologia ganhou em cada eixo? Por quê?

**Exemplo de tabela comparativa**:

| Métrica | Supervisor | Swarm |
|---|---|---|
| Latência | ~12s (5 LLM calls) | ~8s (3-4 LLM calls) |
| Custo (tokens) | ~3500 | ~2000 |
| Qualidade | Alta (síntese) | Média (sem síntese) |

---

### E8 — Verdadeiro/Falso Justificado
**Tempo estimado**: 15 min
**Formato**: Individual, escrito

**Enunciado**: Responda V ou F e justifique em 2-3 frases:

1. "Mesh é sempre a topologia mais escalável."
2. "Supervisor é melhor que swarm quando se precisa de síntese."
3. "Recursive é sempre anti-pattern."
4. "Pipeline dinâmico é a mesma coisa que supervisor."
5. "Em produção, quase todo sistema é hybrid."

**Gabarito**:
1. **F** — Mesh escala em agentes autônomos, mas conexões crescem O(N²). Hierarchical é O(N). Para muitos agentes, hierarchical escala melhor.
2. **V** — Supervisor tem síntese nativa (agrega resultados). Swarm transfere controle, não sintetiza. Se síntese é requisito, supervisor.
3. **F** — Recursive é anti-pattern sem guardrails (max_depth, orçamento). Com guardrails e decomposição natural, é adaptativo e útil.
4. **F** — Pipeline dinâmico decide o próximo step em runtime, mas a estrutura ainda é sequencial. Supervisor roteia para workers arbitrários em ordem qualquer. Pipeline dinâmico é mais estruturado que supervisor.
5. **V** — Sistemas reais combinam topologias: pipeline no macro, hierarchical/swarm no micro, event-driven para integração. Hybrid é a regra em produção madura.

---

## Projeto do Módulo

### P1 — Topologia para Revisão de PR + ADR + Benchmark
**Prazo**: 2 semanas
**Formato**: Individual
**Carga**: ~10h

**Descrição**: Dada a tarefa de revisão de PR com especialistas (code, security, docs):
1. Projetar a topologia mais adequada, justificada em ADR
2. Implementar a topologia escolhida
3. Implementar ao menos 1 topologia alternativa
4. Fazer benchmark comparativo (latência, custo, qualidade)

**Entregáveis**:
- Repositório Git com as implementações
- ADR completo (Contexto, Decision, Consequências)
- Benchmark comparativo (tabela + análise)
- Demo ao vivo da topologia escolhida

**Critério de sucesso**:
- ADR coerente e justificado com requisitos quantificáveis
- Implementação funcional das topologias
- Medições reais (não estimativas)
- Topologia justificada com base nas medições

**Avaliação** (rubrica de 4 pilares):

| Pilar | Peso | Critério |
|---|---|---|
| Técnico | 40% | Código funcional, traces, benchmark |
| Consultivo | 30% | ADR — clareza da justificativa e defesa |
| Comportamental | 20% | Code review de um colega |
| Prático | 10% | Demo ao vivo: topologia rodando |

**Nota mínima de aprovação**: 3.0
