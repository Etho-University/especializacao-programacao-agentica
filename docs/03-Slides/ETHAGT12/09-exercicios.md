# ETHAGT12 — Exercícios

> Exercícios para aula e para casa.
> Organizados por tipo: em aula, individual, em duplas, projeto.

---

## Exercícios em Aula

### E1 — Identificando Falácias (Votação Rápida)
**Slide**: 14
**Tempo**: 1 min
**Formato**: Individual, votação de mão levantada

**Enunciado**: Para cada afirmação, identifique a falácia:

1. "Testei com 3 exemplos e funcionou, pode ir para produção."
2. "O benchmark mostra 80%, então o agente está bom."
3. "O GPT-4 disse que a resposta está correta."
4. "Ninguém reclamou desde o deploy."

**Gabarito**:
1. **Sample size=1** — sobrevivência de amostra minúscula
2. **Benchmark ≠ produção** — overfitting de benchmark
3. **Self-preference / falta de calibração** — LLM-as-judge sem calibração
4. **Sobrevivência silenciosa** — usuários desistem sem reclamar

---

### E2 — Lendo um Trace (Duplas)
**Slide**: 26
**Tempo**: 3 min
**Formato**: Duplas, 2 min discussão + 1 min compartilhar

**Enunciado**: Analise o seguinte trace:

```
[STEP 0] Thought: "Vou buscar o preço do produto X"
         Action: search_price("Produto X")
         Observation: "Produto X: R$ 99,90"

[STEP 1] Thought: "Vou buscar o preço do produto X"
         Action: search_price("Produto X")
         Observation: "Produto X: R$ 99,90"

[STEP 2] Thought: "Vou buscar o preço do produto X"
         Action: search_price("Produto X")
         Observation: "Produto X: R$ 99,90"

[STEP 3] Thought: "Vou buscar o preço do produto X"
         Action: search_price("Produto X")
         Observation: "Produto X: R$ 99,90"

[STEP 4] Thought: "Vou buscar o preço do produto X"
         Action: search_price("Produto X")
         Observation: "Produto X: R$ 99,90"

[STEP 5] max_steps reached. Abortando.
```

**Perguntas**:
1. Identifique onde o loop acontece e por quê.
2. Proponha 2 correções diferentes.

**Gabarito**:
- **Problema**: Agente repete a mesma action sem processar a Observation. Causas possíveis: (a) prompt não instrui a usar observations anteriores; (b) contexto não inclui observations; (c) modelo fraco.
- **Correção 1 (prompt)**: Adicionar ao system prompt: "Antes de buscar, verifique se você já tem a informação nas observações anteriores."
- **Correção 2 (código)**: Detecção de repetição — se mesma action 3x consecutivas, forçar resposta final.
- **Correção 3 (context)**: Garantir que `messages` inclui todas as observations anteriores.

---

### E3 — Pergunta da DEMO de Traces (Duplas)
**Slide**: 25
**Tempo**: 2 min
**Formato**: Duplas, discussão aberta

**Enunciado**: Após a demo de adicionar observabilidade:

1. O que o trace revelou que logs simples não mostrariam?
2. Qual step do agente é o gargalo de latência?
3. Como você decidiria se vale otimizar esse step?

**Gabarito**:
1. Hierarquia (quem chamou quem), timing cumulativo, custo por step, atributos estruturados.
2. Depende do trace — geralmente a tool call (latência de API).
3. Calcular ROI: quanto economiza em latência vs esforço de otimização. Se tool é 80% da latência, otimize.

---

### E4 — Escrevendo Golden Cases (Duplas)
**Slide**: 42
**Tempo**: 5 min (3 escrita + 2 compartilhar)
**Formato**: Duplas

**Enunciado**: Cenário: agente de reserva de voo. Em duplas, escrevam 2 golden cases com critério mensurável:

1. **Um caso factual**: ex: "reserve um voo direto SP-Rio amanhã"
   - Critério: assertion que a resposta menciona voo direto
2. **Um caso subjetivo**: ex: "quais opções de viagem para o RJ?"
   - Critério: rubrica para LLM-as-judge avaliar clareza e utilidade

**Estrutura**:
```python
{
    "id": "GC-XXX",
    "input": "...",
    "expected_behavior": "...",
    "eval_fn": "...",
    "category": "..."
}
```

**Gabarito (exemplo)**:
```python
# Caso factual
{
    "id": "GC-001",
    "input": "Reserve um voo direto de São Paulo para Rio de Janeiro amanhã de manhã.",
    "expected_behavior": "Agente deve propor voo direto (sem escalas) com horário matutino.",
    "eval_fn": "assert 'direto' in response.lower() and any(h in response for h in ['manhã', 'matutino', '06', '07', '08', '09', '10', '11'])",
    "category": "factual"
}

# Caso subjetivo
{
    "id": "GC-002",
    "input": "Quais opções de viagem para o RJ você recomenda?",
    "expected_behavior": "Resposta útil: menciona pelo menos 2 opções de transporte (voo, ônibus, carro), com prós/contras ou contexto.",
    "eval_fn": "LLM-as-judge com rubrica: (1) menciona 2+ opções, (2) dá contexto útil, (3) é claro",
    "category": "subjective"
}
```

**Critério de avaliação**:
- Critério é operacionalizável (não "resposta boa") ✅
- Tem id rastreável ✅
- Categoria apropriada ✅

---

### E5 — V/F: LLM-as-Judge É Sempre Confiável
**Slide**: 43
**Tempo**: 1 min
**Formato**: Individual, votação

**Enunciado**: Verdadeiro ou Falso: "LLM-as-judge é sempre confiável."

**Gabarito**: **Falso**. LLM-as-judge tem 5 vieses (positional, sycophancy, verbosity, self-preference, knowledge). Sem mitigação (rubrica, calibração, múltiplos judges, cross-model), pode estar sistematicamente errado.

---

### E6 — Escolhendo um Benchmark (Votação)
**Slide**: 53
**Tempo**: 1 min
**Formato**: Individual, votação

**Enunciado**: Para cada cenário, escolha o benchmark:

1. "Agente de coding que resolve issues de GitHub" → ?
2. "Assistente de pesquisa geral multi-step" → ?
3. "Agente de atendimento ao cliente com APIs e políticas" → ?
4. "Bot que navega e-commerce e completa compras" → ?

**Gabarito**:
1. **SWE-bench** — código verificável
2. **GAIA** — raciocínio geral multi-step
3. **τ-bench** — tool use com policy
4. **WebArena** — navegação web

---

### E7 — Detectando Regressão (Grupos)
**Slide**: 64
**Tempo**: 5 min (3 discussão + 2 compartilhar)
**Formato**: Grupos de 3-4

**Enunciado**: Cenário: o time mudou o prompt do agente e o eval score caiu de 85% para 72%. Em grupos, discutam:

1. É regressão real ou viés do judge? Como distinguir?
2. Quais casos regrediram — tem padrão?
3. Próximos passos: A/B test? Reverter prompt? Revisar casos?

**Gabarito (orientação)**:
1. **Distinguir**: olhar caso por caso. Se falhas fazem sentido (realmente pioraram) → regressão real. Se não fazem sentido → viés do judge. Confirmar com humano.
2. **Padrão**: agrupar casos que falharam por categoria (factual, tool-use, etc.). Se uma categoria concentra falhas, é regressão direcionada.
3. **Próximos passos**:
   - Se regressão real e concentrada: corrigir prompt na área problemática
   - Se difusa: reverter prompt
   - Se ambígua: A/B test com mais casos
   - Sempre: rever casos que falharam para validar critério

---

## Exercícios Individuais (para casa)

### E8 — Definindo Observabilidade vs Eval vs Monitoring
**Tempo estimado**: 10 min
**Formato**: Individual, escrito

**Enunciado**: Em suas palavras, defina e diferencie:

1. Observabilidade
2. Avaliação (eval)
3. Monitoring

Dê um exemplo concreto de cada no contexto de um agente de atendimento.

**Critério de avaliação**:
- Define observabilidade como "capacidade de ver o que acontece internamente (traces)" ✅
- Define eval como "medir qualidade em conjunto controlado com critério" ✅
- Define monitoring como "observar métricas em produção em tempo real" ✅
- Exemplos são realistas e distintos ✅

---

### E9 — Calculando Custo de Eval
**Tempo estimado**: 15 min
**Formato**: Individual, cálculo

**Enunciado**: Você tem um agente com as seguintes características:
- 25 chamadas de LLM por tarefa em média
- Cada chamada: ~1500 tokens de entrada, ~400 de saída
- Modelo: GPT-4o ($2.50/1M input, $10/1M output)
- Conjunto de eval: 200 casos × 3 runs (para variância)

**Perguntas**:
1. Custo por tarefa?
2. Custo total do eval?
3. Se você rodar eval a cada PR (5 PRs/dia), quanto por mês?
4. Estratégia para reduzir custo em 80%?

**Gabarito**:
1. Tokens por tarefa: 25 × (1500 in + 400 out) = 37500 in + 10000 out. Custo: $2.50 × 0.0375 + $10 × 0.01 = $0.094 + $0.10 = **$0.194/tarefa**
2. Total: 200 × 3 × $0.194 = **$116.40 por eval**
3. Por mês: $116.40 × 5 × 22 = **$12.804/mês**
4. **Estratégias**:
   - Subconjunto (50 casos vs 200) → 75% redução
   - Modelo mais barato para casos fáceis (GPT-4o-mini para string match)
   - 1 run para casos críticos, 3 para novos
   - Combinar: subconjunto de 50 casos com 1 run = ~$10 por eval = **~95% redução**

---

### E10 — Escrevendo 5 Golden Cases
**Tempo estimado**: 30 min
**Formato**: Individual, código

**Enunciado**: Escolha um domínio (atendimento, coding assistant, research assistant). Escreva 5 golden cases com:

- 1 caso factual (critério exato)
- 1 caso de tool-use (a tool certa foi chamada)
- 1 caso subjetivo (LLM-as-judge com rubrica)
- 1 caso de edge case (input malformado, ambíguo)
- 1 caso de error-handling (recuperação de falha)

Cada caso deve ter: id, input, expected_behavior, eval_fn, category.

**Critério de avaliação**:
- 5 casos cobrem as 5 categorias ✅
- Critérios são operacionalizáveis ✅
- Casos são realistas para o domínio ✅
- Estrutura completa (id, input, eval_fn, category) ✅

---

### E11 — Verdadeiro/Falso Justificado
**Tempo estimado**: 15 min
**Formato**: Individual, escrito

**Enunciado**: Responda V ou F e justifique em 2-3 frases:

1. "LLM-as-judge é sempre confiável se você usar GPT-4."
2. "Bom score em SWE-bench garante bom desempenho em produção."
3. "Observabilidade é custo desnecessário se você tem bons testes."
4. "Tail sampling é sempre melhor que head sampling."
5. "Benchmark padronizado substitui eval custom."

**Gabarito**:
1. **F** — GPT-4 como judge tem vieses (self-preference, verbosity). Sem mitigação (rubrica, calibração), pode estar sistematicamente errado.
2. **F** — SWE-bench é ambiente controlado. Produção tem variância de ambiente, usuários reais, domínio específico. Combine com eval custom.
3. **F** — Observabilidade é investimento. Sem traces, você não consegue debugar em produção, detectar regressão silenciosa, ou otimizar com dados.
4. **F** — Tail sampling é melhor para priorizar erros mas é mais caro (precisa completar o trace). Head sampling é mais barato e suficiente em muitos casos.
5. **F** — Benchmark é comparável mas não representativo do seu caso de uso. Eval custom cobre seu domínio específico. Combinar ambos.

---

### E12 — Análise de Eval Report
**Tempo estimado**: 20 min
**Formato**: Individual, análise

**Enunciado**: Você recebe o seguinte eval report parcial:

```
Agente: Assistente de Reserva de Hotel
Dataset: 150 golden cases (3 runs cada)
Versão: v2.1 (novo prompt)

Resultados:
- Success rate: 78% (vs 85% na v2.0)
- Latência P50: 4.2s (vs 3.8s)
- Latência P95: 12s (vs 9s)
- Custo por execução: $0.21 (vs $0.18)
- Steps médios: 8 (vs 6)

Análise de falhas (33 casos que falharam):
- 18 (55%): "Tool errada — agente usou search_hotels quando deveria usar get_availability"
- 8 (24%): "Incompleto — agente parou antes de confirmar reserva"
- 4 (12%): "Alucinação — agente inventou nome de hotel"
- 3 (9%): "Não entendeu tarefa — interpretou reserva como busca"
```

**Perguntas**:
1. Houve regressão? Em quais métricas?
2. Qual é a causa mais provável? O que corrigir primeiro?
3. Vale fazer deploy da v2.1? Justifique.
4. Proponha 2 próximas ações.

**Gabarito**:
1. **Regressão**: success rate (-7pp), latência P50 (+0.4s), P95 (+3s), custo (+$0.03), steps (+2). Todas as métricas pioraram.
2. **Causa mais provável**: 55% das falhas são "tool errada". Provavelmente o novo prompt confunde as tools (search_hotels vs get_availability). **Corrigir primeiro**: ACI — melhorar descrição das tools ou prompt que diferencia quando usar cada uma.
3. **Não fazer deploy**. Regressão em todas as métricas + causa concentrada em ACI. Reverter prompt ou corrigir ACI antes.
4. **Próximas ações**:
   - Revisar descrição de `search_hotels` vs `get_availability` — tornar distinção clara
   - A/B test com prompt corrigido vs v2.0 (baseline)
   - Adicionar golden cases específicos de confusão de tool (viram regressão test)

---

## Projeto do Módulo

### P1 — Avaliar um Agente em τ-bench ou GAIA
**Prazo**: 4 semanas
**Formato**: Individual ou duplas
**Carga**: ~15h

**Descrição**: Avalie um agente (construído em módulos anteriores) em um subconjunto de τ-bench ou GAIA. Produza um eval report completo.

**Entregáveis**:
1. **Eval report** completo usando o template `24-Templates/template-eval-report.md`
2. **Dataset**: subconjunto de 30-50 casos do benchmark (com justificativa da seleção)
3. **Código de rerun**: outro engenheiro consegue reproduzir os resultados
4. **Análise de falhas**: ≥3 categorias de falha documentadas com correção proposta

**Critério de sucesso**:
- Eval é reproduzível (código roda, resultados batem)
- ≥3 categorias de falha documentadas
- Cada categoria tem correção proposta (não só diagnóstico)
- Eval report segue o template
- Comparações incluem baseline

**Avaliação** (rubrica de 4 pilares):

| Pilar | Peso | Critério |
|---|---|---|
| Técnico | 40% | Eval report + pipeline (rigor, reprodutibilidade) |
| Consultivo | 30% | Apresentação dos resultados para "diretoria" |
| Comportamental | 20% | Code review de um colega |
| Prático | 10% | Demo: regressão detectada |

**Nota mínima de aprovação**: 3.0

---

## Labs (paralelos ao projeto)

### Lab 1 — Traces Everywhere (5h)
**Descrição**: Adicionar observabilidade (LangSmith ou Phoenix) a um agente ReAct existente. Criar dashboard com 6 painéis. Identificar gargalo de latência.
**Entrega**: agente instrumentado + screenshot do trace + dashboard.

### Lab 2 — Eval Automatizado (5h)
**Descrição**: Construir pipeline de eval com LLM-as-judge + 10 golden cases. Mudar prompt do agente e detectar regressão. Produzir mini-eval report.
**Entrega**: pipeline + golden cases + eval report mostrando regressão detectada.
