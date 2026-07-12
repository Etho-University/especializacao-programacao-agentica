# ETHAGT15 — Gabarito

> Restrito a mentores. Cada resposta justificada com referência à apostila.

## Múltipla escolha

1. **b)** — Um meta-agente é um agente que opera sobre outros agentes — criando, configurando, otimizando ou evoluindo agentes especializados para tarefas específicas (Capítulo 1 — O que é meta-agência).

2. **b)** — DSPy compila chamadas declarativas de LLM em pipelines otimizados, ajustando prompts automaticamente com base em um benchmark, sem reescrita manual (Capítulo 3.1 — Otimização de prompts, DSPy).

3. **b)** — Goal drift é o desvio dos objetivos originais do agente ao longo do tempo, causado por auto-modificação, aprendizado de padrões errados ou feedback mal calibrado (Capítulo 5.2 — Drift de objetivos).

4. **b)** — O meta-governor supervisiona e pode vetar ações de meta-agentes que sejam perigosas, garantindo que a auto-modificação não fuja do controle (Capítulo 5.3 — Segurança: meta-governor pattern).

## Verdadeiro ou Falso (justificado)

1. **Falso.** Auto-aprendizado contínuo pode levar a goal drift, overfitting ao feedback disponível, aprendizado de padrões errados e degradação ao longo do tempo. Sem supervisão e mecanismos de "esquecimento" seletivo, pode piorar (Capítulo 4.4 e exercícios do syllabus).

2. **Verdadeiro.** Otimização automatizada (DSPy) precisa de um benchmark automatizado para medir melhoria. Com benchmark claro, ela explora o espaço de prompts mais sistematicamente que um humano. Sem benchmark, otimização manual é preferível (Capítulo 3.1).

3. **Verdadeiro.** Meta-agentes que se auto-modificam podem entrar em recursão descontrolada — cada geração modifica a anterior sem convergência. Fences de segurança (limite de profundidade, vetos, sandbox) são essenciais (Capítulo 5.1 — Recursão e loops).

4. **Verdadeiro.** Agentes gerados automaticamente não têm garantia de qualidade ou segurança. Devem passar por eval (benchmark) e teste de segurança antes de deploy em produção (Capítulo 2.3 — Validação do agente gerado).

## Código curto

1. **Meta-agente que gera e avalia agente especializado:**
```python
def meta_agent(task, benchmark):
    prompt = llm(f"Crie um prompt de agente especializado para: {task}")
    score = evaluate_agent(prompt, benchmark)
    if score > threshold:
        return deploy(prompt)
    return iterate(prompt, score)
```
Referência: Capítulo 2 (Geração de agentes).

2. **Veto de meta-governor:**
```python
def meta_governor_check(generated_agent):
    if "modify" in generated_agent.instructions and "self" in generated_agent.instructions:
        raise VetoError("Self-modification not allowed")
    return True
```
Referência: Capítulo 5.3 (Meta-governor pattern, vetos).

3. **Strategy evolver:**
```python
def evolve(strategies, benchmark, top_k=3):
    scored = [(s, evaluate(s, benchmark)) for s in strategies]
    scored.sort(key=lambda x: x[1], reverse=True)
    survivors = [s for s, _ in scored[:top_k]]
    return survivors + mutate(survivors)  # próxima geração
```
Referência: Capítulo 4.3 (Estratégia evolutiva).

## Análise de trade-off

1. **Manual vs. automatizada:** Manual é preferível quando o problema é novo, não há benchmark claro, ou a interpretabilidade do prompt importa (humano precisa entender). Automatizada (DSPy) é preferível quando há benchmark automatizado, muitas variações a testar, e o objetivo é performance bruta (Capítulo 3.1).

2. **Contínuo vs. supervisionado periódico:** Contínuo adapta-se em tempo real mas tem risco de drift, instabilidade e feedback loops. Supervisionado periódico é mais estável e controlável mas menos responsivo. O risco do contínuo é goal drift e degradação silenciosa (Capítulo 4.4).

3. **Confiança incremental:** Sempre que o meta-agente gera agentes que serão usados em produção com acesso a tools reais. Sandbox permite testar sem risco; produção gradual (canary) limita o impacto de falhas. Agentes gerados têm comportamento não garantido (Capítulo 5.4).

## Debug / diagnóstico

1. **Diagnóstico:** Overfitting ao benchmark — o DSPy otimizou o prompt para o benchmark específico, que não representa fielmente a distribuição de produção. A "melhoria" é ilusória. **Correção:** usar um conjunto de validação separado do de otimização, e um holdout de produção para avaliar generalização (Capítulo 3.1 e princípios de eval do ETHAGT12).

2. **Diagnóstico:** O meta-agente está explorando complexidade sem seleção efetiva — adiciona elementos sem que eles melhorem o score. Pode ser função de avaliação não discriminativa ou falta de pressão seletiva. **Correção:** revisar a função de avaliação, adicionar penalidade por complexidade (parsimony), e limitar a profundidade de modificação (Capítulo 3.2 e 5).
