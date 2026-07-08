# ETHAGT15 — Exercícios

> Exercícios para aula e para casa.
> Organizados por tipo: em aula, individual, em duplas, projeto.

---

## Exercícios em Aula

### E1 — É Meta-Agência ou Não? (Votação Rápida)
**Slide**: 14
**Tempo**: 1.5 min
**Formato**: Individual, votação de mão levantada

**Enunciado**: Para cada cenário abaixo, vote: Meta-Agência (M) ou Agência Comum (C)?

1. Agente que escreve código Python
2. Agente que gera prompt para outro agente
3. Agente que ajusta sua própria temperatura
4. Agente que busca na web

**Gabarito**:
1. C (age sobre ambiente — código)
2. M (synthesis — gera config de outro agente)
3. M (optimization — ajusta config de agente, mesmo que a própria)
4. C (age sobre ambiente — web)

---

### E2 — Perguntas da DEMO (Discussão em Duplas)
**Slide**: 22
**Tempo**: 2 min
**Formato**: Duplas, 2 min discussão

**Enunciado**: Após a demo do meta-agente gerando um classificador de tickets, discutam:

1. O agente gerado é pior que um escrito manualmente?
2. Como sabemos que o eval cobre casos suficientes?
3. E se o meta-agente gerar config que funciona no eval mas falha em produção?

**Gabarito**:
1. Depende — benchmark comparativo é o árbitro.
2. Nunca se sabe com certeza — por isso confiança incremental.
3. Overfitting ao eval — solução: holdout set + shadow run + monitoramento.

---

### E3 — Critérios de Qualidade (Duplas)
**Slide**: 23
**Tempo**: 3 min
**Formato**: Duplas, 2 min listar + 1 min compartilhar

**Enunciado**: Listem 5 critérios de qualidade para um agente gerado por meta-agente. Bônus: como detectar overfitting ao eval?

**Gabarito** (exemplos aceitáveis):
- Success rate (acertou?)
- Latência (quão rápido?)
- Custo por execução
- Safety (não violou políticas?)
- Robustez a edge cases
- Consistência (comportamento previsível?)
- Auditabilidade (dá para entender?)
- Overfitting: holdout set, shadow run, distribuição diferente de inputs.

---

### E4 — Detectar Drift (Duplas)
**Slide**: 43
**Tempo**: 3 min
**Formato**: Duplas, 2 min propor + 1 min compartilhar

**Enunciado**: Cenário: agente de suporte com 6 meses de memória. Success rate caiu de 92% → 78% em 30 dias. Proponham 3 estratégias para detectar e mitigar drift.

**Gabarito** (exemplos):
1. Comparar distribuição de queries atuais vs históricas (mudou o tipo de pergunta?)
2. TTL agressivo — descartar memória >30 dias e medir se melhora
3. Re-treinar/otimizar com dados recentes apenas
4. Entrevistar usuários (o que mudou no produto?)
5. Monitorar tópicos emergentes (novas perguntas não cobertas)

---

### E5 — Projetar um Meta-Governor (Trios)
**Slide**: 53
**Tempo**: 5 min
**Formato**: Trios, 3 min design + 2 min compartilhar

**Enunciado**: Cenário: meta-agente quer modificar o próprio system prompt. Em trios, projetem um meta-governor:

1. Quais regras de veto vocês implementariam? (mínimo 3)
2. Qual o pipeline de gates? (sandbox → shadow → canary)
3. Quando HITL é obrigatório?
4. Qual o critério de rollback?

**Bônus**: O que acontece se o meta-governor também for um agente?

**Gabarito** (exemplos de veto):
- "NUNCA remover safety constraints do system prompt"
- "NUNCA aumentar custo por execução >10%"
- "NUNCA remover tools de auditoria/logging"
- "NUNCA mudar para modelo não-aprovado"
- "Mudança >20% no prompt requer HITL"

**Bônus**: Se o governor for LLM, regressão infinita. Solução: governors críticos devem ser determinísticos (policy-as-code).

---

### E6 — Auto-Aprendizado Sempre Melhora? (V/F)
**Slide**: 44
**Tempo**: 1 min
**Formato**: Individual, votação

**Enunciado**: V/F: "Auto-aprendizado contínuo sempre melhora."

**Gabarito**: **FALSO**. Razões: overfitting, drift não detectado, loop de feedback positivo (jogar a métrica), catastrophic forgetting. Precisa de monitoramento, validação e reset.

---

## Exercícios Individuais (para casa)

### E7 — Defina Meta-Agência
**Tempo estimado**: 10 min
**Formato**: Individual, escrito

**Enunciado**: Em suas palavras, defina meta-agência e distinga das 3 estratégias (synthesis, evolution, optimization) em 2-3 frases cada. Use um exemplo de cada.

**Critério de avaliação**:
- Define meta-agente como "agente cujo ambiente é outro agente" ✅
- Distingue as 3 estratégias corretamente ✅
- Exemplos são realistas ✅

---

### E8 — Assinatura DSPy
**Tempo estimado**: 15 min
**Formato**: Individual, código

**Enunciado**: Escreva uma assinatura DSPy para um agente que classifica tickets de suporte em: bug, feature request, dúvida, elogio. Inclua:
- Assinatura declarativa
- Métrica de avaliação
- Descrição do que o teleprompter otimizaria

**Exemplo de resposta**:
```python
import dspy

class ClassifyTicket(dspy.Signature):
    """Classifica um ticket de suporte em uma de 4 categorias."""
    ticket_text: str = dspy.InputField(desc="Texto do ticket do usuário")
    category: str = dspy.OutputField(desc="Uma de: bug, feature_request, duvida, elogio")

# Métrica: exatidão da categoria vs label humano
def metric(example, pred, trace=None):
    return 1.0 if example.category.lower() == pred.category.lower() else 0.0

# Teleprompter otimizaria: few-shot examples, instruções de classificação, formato de output
```

---

### E9 — Regra de Veto em Policy-as-Code
**Tempo estimado**: 15 min
**Formato**: Individual, código

**Enunciado**: Escreva 3 regras de veto em pseudocódigo policy-as-code (estilo Rego/CEL) para um meta-governor. As regras devem ser binárias (bloqueia ou não) e cobrir: safety constraints, custo e modelo.

**Exemplo de resposta**:
```
veto(change) if change.removes_safety_constraint == true
veto(change) if change.cost_increase > 0.10
veto(change) if change.new_model not in APPROVED_MODELS
```

**Critério**: regras são binárias, não têm "exceto se", cobrem os 3 eixos.

---

### E10 — Verdadeiro/Falso Justificado
**Tempo estimado**: 10 min
**Formato**: Individual, escrito

**Enunciado**: Responda V ou F e justifique em 2-3 frases:

1. "Meta-agente precisa ser mais inteligente que os agentes que cria."
2. "DSPy substitui a necessidade de escrever prompts manualmente."
3. "Goal drift só acontece com métricas ruins."
4. "Voyager poderia ser aplicado diretamente em um sistema de suporte ao cliente."
5. "Auto-aprendizado contínuo sem HITL é sempre seguro se o eval for bom."

**Gabarito**:
1. **F** — Meta-agente não precisa ser mais inteligente; precisa ter acesso a primitivas e eval. É composição, não inteligência superior.
2. **F** — DSPy otimiza prompts a partir de assinaturas, mas você ainda escreve a assinatura (intenção). Substitui a otimização manual, não o design.
3. **F** — Toda métrica é proxy imperfeito. Goal drift acontece até com métricas boas, se o ambiente mudar ou o agente encontrar atalhos.
4. **F** — Voyager funciona porque Minecraft é sandboxed, determinístico e sem consequências. Suporte ao cliente é o oposto — precisa adaptar extensivamente.
5. **F** — Eval bom é necessário mas não suficiente. Sem HITL, overfitting ao eval e drift não detectados passam despercebidos. HITL é o último guardrail.

---

## Projeto do Módulo

### P1 — Otimização Automática com DSPy
**Prazo**: 2 semanas
**Formato**: Individual
**Carga**: ~10h

**Descrição**: Implementar um sistema onde prompts e/ou tools são otimizados automaticamente usando DSPy (ou Promptbreeder, ou OPRO) e medir o ganho em um benchmark.

**Entrega**:
1. **Sistema**: pipeline com otimização automática funcional
2. **Eval comparativo**: antes vs depois da otimização, em benchmark definido
3. **Análise crítica**: o que melhorou? O que piorou? Por quê?
4. **Safety**: meta-governor com pelo menos 2 regras de veto implementadas

**Entregáveis**:
- Repositório Git com código e README
- Benchmark com ≥20 casos de teste
- Relatório comparativo (métricas: success rate, latência, custo)
- Config versionada (antes vs depois)
- Meta-governor com vetos (policy-as-code ou equivalente)

**Critério de sucesso**:
- Otimização funcional e reproduzível
- Ganho mensurável (mesmo que pequeno) no benchmark
- Meta-governor implementado e testado
- Análise crítica honesta (incluindo regressões)

**Avaliação** (rubrica de 4 pilares):

| Pilar | Peso | Critério |
|---|---|---|
| Técnico | 40% | Otimização funcional, benchmark, qualidade da implementação |
| Consultivo | 30% | Análise crítica — clareza dos trade-offs observados |
| Comportamental | 20% | Meta-governor com vetos — governance implementada |
| Prático | 10% | Demo ao vivo: antes vs depois da otimização |

**Nota mínima de aprovação**: 3.0
