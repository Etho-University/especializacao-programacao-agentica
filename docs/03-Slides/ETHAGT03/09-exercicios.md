# ETHAGT03 — Exercícios

> Exercícios para aula e para casa.
> Organizados por tipo: em aula, individual, em duplas, projeto.

---

## Exercícios em Aula

### E1 — Gate em Tradução (Discussão em Duplas)
**Slide**: 16
**Tempo**: 2 min
**Formato**: Duplas, 2 min discussão + 1 min compartilhar

**Enunciado**: Cenário: prompt chaining para tradução técnica (EN → PT-BR). Descreva um gate programático útil entre o step de tradução e o step de revisão.

**Dica**: pense em verificação estrutural, não semântica. Gates são código puro.

**Gabarito** (exemplos aceitáveis):
- Contagem de parágrafos: o nº de parágrafos na tradução deve ser igual ao original
- Glossário: termos técnicos do glossário foram preservados (regex sobre lista de termos)
- Variáveis preservadas: tokens entre `{chaves}` ou `<tags>` não foram traduzidos
- Contagem de tokens: a tradução está dentro de ±20% do tamanho do original
- URLs e emails preservados (regex)

**Gabarito** (NÃO aceitável — é evaluator, não gate):
- "Verificar se a tradução é fiel" (semântica → evaluator)
- "Avaliar a qualidade da tradução" (subjetivo → evaluator)

---

### E2 — Avaliando o Router (Discussão em Duplas)
**Slide**: 23
**Tempo**: 2 min
**Formato**: Duplas, 2 min discussão + 1 min compartilhar

**Enunciado**: Discutam:
1. Como saber se o roteador está errando? O que medir?
2. Qual métrica é mais importante: precision ou recall? Depende do quê?
3. Se o router envia 10% dos fáceis para o path difícil, isso é problema?

**Gabarito**:
1. Logs de classificação vs ground truth → matriz de confusão → precision/recall por categoria.
2. Depende do custo do erro. Recall importa mais quando o path errado (difícil→fácil) gera resposta ruim. Precision importa mais quando o path errado é caro (fácil→difícil desperdiça Sonnet). Em routing por modelo, recall é geralmente mais importante (erro difícil→fácil é o mais caro).
3. Não é problema grave — manda para Sonnet, custa mais mas resolve. O problema real é o oposto: difíceis indo para Haiku.

---

### E3 — Voting vs Sectioning (Votação Rápida)
**Slide**: 32
**Tempo**: 1.5 min
**Formato**: Individual, votação de mão levantada

**Enunciado**: Para cada cenário, vote: Sectioning (S) ou Voting (V)?

1. Traduzir 3 páginas independentes
2. Decidir se um email é phishing
3. Gerar 3 alternativas de copy para anúncio

**Gabarito**:
1. **S** — cada página é uma subtarefa diferente (sectioning)
2. **V** — mesma pergunta, múltiplas perspectivas para robustez (voting)
3. **S** para gerar (cada alternativa é diferente) MAS **V** para escolher a melhor (ou um judge)

---

### E4 — V/F "Orchestrator-Workers É Sempre Melhor"
**Slide**: 39
**Tempo**: 1 min
**Formato**: Individual, votação + explicação

**Enunciado**: Verdadeiro ou Falso: *"Orchestrator-workers é sempre melhor que parallelization."*

**Gabarito**: **Falso**. Se as subtarefas são fixas e conhecidas, parallelization é mais simples, barato e previsível. Orchestrator-workers adiciona custo (LLM de planejamento) e latência (step extra). Só use quando as subtarefas são genuinamente dinâmicas.

---

### E5 — Condição de Parada para Tradução Literária (Duplas)
**Slide**: 46
**Tempo**: 2 min
**Formato**: Duplas, 2 min discussão + 1 min compartilhar

**Enunciado**: Cenário: evaluator-optimizer para tradução de um poema (EN → PT-BR). Escreva a condição de parada:
- Quais critérios?
- Qual threshold?
- Quantas iterações máximas?

**Dica**: tradução literária é subjetiva — como evitar loop infinito?

**Gabarito** (exemplo aceitável):
- **Rubric**: 4 dimensões (fidelidade, fluência, ritmo, tom), cada uma 1-5
- **Threshold**: média ≥ 4.0 (NÃO 5.0 — perfeição é inatingível em literário)
- **Max iters**: 3-4 (literário não melhora indefinidamente; modelo trava após ~3)
- **Delta estagnado**: se média não melhora por 1 iteração, parar
- **Combinação**: parar se (média ≥ 4.0) OU (iter ≥ 3) OU (delta < 0.1)

---

### E6 — Escolha o Workflow (5 Cenários)
**Slide**: 60
**Tempo**: 5 min
**Formato**: Grupos de 3-4, 3 min discussão + 2 min compartilhar

**Enunciado**: Para cada cenário, indique o workflow mais adequado e justifique:

1. Tradução com revisão de qualidade
2. Análise de sentimentos de 10.000 tweets
3. Geração de relatório com múltiplas fontes
4. Chatbot de FAQ simples
5. Correção de redação com feedback

**Gabarito**:
1. **Prompt Chaining + Evaluator-Optimizer** — traduz (LLM 1) → gate (estrutura) → revisa (LLM 2) → refina até rubric. Linear com loop de qualidade.
2. **Routing + Parallelization (sectioning)** — routing por idioma → cada tweet analisado em paralelo. 10k tweets = sectioning massivo.
3. **Orchestrator-Workers** — fontes são dinâmicas (orquestrador decide quantas e quais). Workers pesquisam, reducer sintetiza.
4. **Routing** — classifica a pergunta (categoria de FAQ) → despacha para handler com a resposta. Simples e barato.
5. **Evaluator-Optimizer** — gera correção → avalia contra rubric (gramática, coesão, clareza) → refina com feedback. Loop de qualidade.

**Critério de avaliação**: a JUSTIFICATIVA deve citar restrições do problema (linearidade, categorias, paralelismo, dinamicidade, refinamento).

---

## Exercícios Individuais (para casa)

### E7 — Gate Útil em Prompt Chaining de Tradução
**Tempo estimado**: 10 min
**Formato**: Individual, escrito

**Enunciado**: Descreva pelo menos 3 gates programáticos úteis em um prompt chaining de tradução técnica (EN → PT-BR). Para cada gate, indique: o que verifica, como (código), e o que fazer se falhar.

**Critério de avaliação**:
- Cada gate é código (não LLM) ✅
- Cada gate é verificável estruturalmente ✅
- Ação ao falhar é específica (retry/fallback/escalada) ✅

---

### E8 — Verdadeiro/Falso Justificado
**Tempo estimado**: 10 min
**Formato**: Individual, escrito

**Enunciado**: Responda V ou F e justifique em 2-3 frases:

1. "Gates em prompt chaining devem ser implementados com LLM para máxima flexibilidade."
2. "Voting corrige viés sistemático do modelo."
3. "Orchestrator-workers é sempre melhor que parallelization porque é mais flexível."
4. "Paralelismo reduz custo porque compartilha contexto."
5. "Evaluator-optimizer só converge se o evaluator for melhor que o generator."

**Gabarito**:
1. **F** — Gates são CÓDIGO (determinístico), não LLM. Se fosse LLM, seria evaluator-optimizer. Determinismo é o ponto do gate.
2. **F** — Voting corrige VARIÂNCIA (aleatoriedade), não viés (erro sistemático). Se todos os modelos têm o mesmo viés, a maioria reforça o erro.
3. **F** — Se as subtarefas são fixas e conhecidas, parallelization é mais simples, barato e previsível. Orchestrator adiciona custo e latência desnecessários.
4. **F** — Paralelismo NÃO reduz custo. Você paga todas as chamadas. Só reduz LATÊNCIA (max em vez de sum).
5. **V** — Se o evaluator é mais fraco que o generator, o feedback é pior que a saída. O loop diverge — cada iteração piora.

---

### E9 — Matriz de Confusão do Router
**Tempo estimado**: 15 min
**Formato**: Individual, análise

**Enunciado**: Dada a seguinte matriz de confusão de um router de tickets (linhas = real, colunas = predito):

| | técnico | billing | geral |
|---|---|---|---|
| **técnico** | 80 | 5 | 15 |
| **billing** | 3 | 90 | 7 |
| **geral** | 10 | 2 | 88 |

1. Calcule precision e recall para cada categoria.
2. Qual categoria tem o pior recall? O que isso significa em routing por modelo?
3. Proponha uma mitigação.

**Gabarito**:
1. **Precision** (dos classificados como X, quantos eram X):
   - técnico: 80/(80+3+10) = 80/93 = 86%
   - billing: 90/(5+90+2) = 90/97 = 93%
   - geral: 88/(15+7+88) = 88/110 = 80%
2. **Recall** (dos que eram X, quantos o router pegou):
   - técnico: 80/(80+5+15) = 80/100 = 80%
   - billing: 90/(3+90+7) = 90/100 = 90%
   - geral: 88/(10+2+88) = 88/100 = 88%
   - Pior recall: **técnico (80%)** — 20% dos tickets técnicos são classificados como billing ou geral. Em routing por modelo, isso significa tickets técnicos difíceis indo para Haiku (resposta ruim).
3. **Mitigação**: Quando o router está incerto entre técnico e outra categoria, despachar para o path técnico (Sonnet) por segurança. Ou retreinar o router com mais exemplos de técnicos confundidos.

---

### E10 — Trade-offs de Custo em Composição
**Tempo estimado**: 15 min
**Formato**: Individual, cálculo

**Enunciado**: Você tem uma composição routing → parallelization (3 workers) → evaluator-optimizer (média 2 iters). Cada chamada LLM custa $0.01. Você tem 5.000 execuções/dia.

1. Quantas chamadas LLM por execução (pior caso)?
2. Custo por dia? Por mês?
3. Se você cortar voting de 3 para 2 workers, quanto economiza por mês?
4. Se o evaluator-optimizer convergir em 1 iter (em vez de 2), quanto economiza?

**Gabarito**:
1. **Pior caso**: 1 (router) + 3 (workers) + 1 (reducer) + 2×(generator + evaluator) = 1 + 3 + 1 + 4 = 9 chamadas
2. **Custo**: 9 × $0.01 × 5.000 = $450/dia = $13.500/mês
3. **Cortar voting para 2 workers**: 1 + 2 + 1 + 4 = 8 chamadas → $400/dia → $12.000/mês. Economia: $1.500/mês (11%).
4. **Evaluator em 1 iter**: 1 + 3 + 1 + 1×2 = 7 chamadas → $350/dia → $10.500/mês. Economia: $3.000/mês (22%).

---

## Projeto do Módulo

### P1 — Síntese de Relatório com Workflow Composto
**Prazo**: 2 semanas
**Formato**: Individual
**Carga**: ~10h

**Descrição**: Dada uma tarefa de síntese de relatório a partir de múltiplas fontes, projetar e implementar o workflow composto mais adequado. Comparar 2 abordagens (ex.: prompt chaining vs orchestrator-workers) em qualidade, custo e latência.

**Entregáveis**:
- Repositório Git com as 2 implementações
- Benchmark com ≥20 casos (medições de custo, latência, qualidade)
- ADR (Architecture Decision Record) justificando a escolha
- Traces de execução mostrando o workflow em ação

**Critério de sucesso**:
- Ambas as implementações funcionais
- Benchmark com ≥20 casos reais (não sintéticos)
- ADR coerente com trade-offs mensurados
- Traces demonstram o workflow

**Avaliação** (rubrica de 4 pilares):

| Pilar | Peso | Critério |
|---|---|---|
| Técnico | 40% | Código funcional, medições reais, qualidade das implementações |
| Consultivo | 30% | ADR — clareza da justificativa, defesa para "cliente" |
| Comportamental | 20% | Code review de um colega (em duplas) |
| Prático | 10% | Demo ao vivo: workflow escolhido rodando |

**Nota mínima de aprovação**: 3.0
