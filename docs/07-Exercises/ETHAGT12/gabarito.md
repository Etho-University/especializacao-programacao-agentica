# ETHAGT12 — Gabarito

> Restrito a mentores. Cada resposta justificada com referência à apostila.

## Múltipla escolha

1. **b)** — Um span é uma unidade de trabalho dentro de um trace — ex.: uma chamada de LLM, uma tool execution, um step do agente. Spans compõem um trace completo (Capítulo 2 — Observabilidade).

2. **d)** — Todos são vieses possíveis do LLM-as-judge: verbosity bias (preferir respostas longas), position bias (preferir a primeira/última opção), self-preference (preferir respostas do mesmo modelo) (Capítulo 3.1 — LLM-as-judge: vieses).

3. **b)** — τ-bench (tau-bench) avalia tool-agent-user interaction em domínios específicos como airline e retail, medindo a capacidade do agente de usar tools e interagir com usuários simulados (Capítulo 4 — Benchmarks canônicos).

4. **b)** — Golden cases são casos de teste com resposta/critério esperado conhecido, usados em conjunto de regressão para detectar quando mudanças (prompt, modelo, tool) degradam o desempenho (Capítulo 3.2 — Golden cases).

## Verdadeiro ou Falso (justificado)

1. **Falso.** Benchmarks são proxies — não representam fielmente a distribuição de produção. Contaminação, overfitting ao benchmark e diferenças de ambiente levam a scores inflados que não se traduzem em performance real (Capítulo 4.5 — Limites e contaminação).

2. **Verdadeiro.** Se os dados do benchmark estão no treinamento do modelo, ele memoriza as respostas e seu score é artificialmente alto, sem refletir capacidade de generalização (Capítulo 4.5).

3. **Verdadeiro.** LLM-as-judge tem vieses conhecidos e pode discordar de humanos em casos difíceis. Calibração (human agreement rate) é necessária para estabelecer confiabilidade antes de usar em produção (Capítulo 3.1).

4. **Verdadeiro.** Traces detalhados, logs estruturados e métricas customizadas consomem armazenamento, processamento e até tokens extras. O custo de observabilidade deve ser orçado (Capítulo 2.5 — Custo de observabilidade).

## Código curto

1. **Golden case:**
```json
{
  "id": "gc-001",
  "input": "Qual a capital da França?",
  "expected": "Paris",
  "criteria": {
    "exact_match": false,
    "contains": ["Paris"],
    "faithfulness": true
  },
  "category": "factual"
}
```
Referência: Capítulo 3.2 (Golden cases).

2. **Pipeline de avaliação:**
```python
def eval_pipeline(agent, golden_cases, baseline_rate):
    successes = sum(1 for c in golden_cases if agent_passes(agent, c))
    rate = successes / len(golden_cases)
    if rate < baseline_rate:
        print(f"REGRESSION: {rate} < {baseline_rate}")
    return rate
```
Referência: Capítulo 3 (Avaliação automatizada) e 5 (CI para agentes).

3. **LLM-as-judge:**
```python
def llm_judge(output, criteria):
    prompt = f"Avalie este output segundo os critérios: {criteria}\nOutput: {output}\nRetorne JSON: {{'score': 0.0-1.0, 'reason': '...'}}"
    return llm(prompt)
```
Referência: Capítulo 3.1 (LLM-as-judge).

## Análise de trade-off

1. **SWE-bench vs. custom:** SWE-bench é padronizado e comparável entre sistemas, mas pode não refletir o domínio da sua aplicação. Custom benchmark reflete seu domínio mas não é comparável e exige esforço de construção. Use SWE-bench para posicionamento geral; custom para regressão interna (Capítulo 4).

2. **Traces vs. logs simples:** Logs estruturados são leves e suficientes para sistemas simples. Traces (LangSmith/Phoenix) valem o overhead quando há múltiplos steps, calls aninhados e necessidade de visualizar causalidade, latência por step e debug temporal (Capítulo 2).

3. **Success rate vs. partial credit:** Success rate binário é simples mas perde informação (uma resposta 90% certa conta como falha). Partial credit é mais informativo para tarefas complexas onde há graus de sucesso — mas é mais caro de avaliar (Capítulo 3.3).

## Debug / diagnóstico

1. **Investigação de regressão:** Executar os golden cases que falharam após a mudança e comparar com os traces das versões anterior e nova. Categorizar as falhas (ex.: alucinação, tool misuse, formato errado) para identificar o padrão de regressão causado pelo novo prompt (Capítulo 5 e 6).

2. **Diagnóstico:** O LLM-as-judge não tem capacidade de julgar casos difíceis (nuance, ambiguidade) — concorda com humanos no óbvio mas falha no complexo. **Correção:** usar human evaluation para casos difíceis, ou calibrar o judge com rubricas mais detalhadas e exemplos de casos difíceis anotados (Capítulo 3.1).
