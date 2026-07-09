---
password: Etho-Prof-2026
---
# ETHAGT16 — Gabarito

> Restrito a mentores. Cada resposta justificada com referência à apostila.

## Múltipla escolha

1. **b)** — Em Smallville (Generative Agents), os agentes exibem comportamento social emergente — rotinas, relacionamentos e memórias — a partir de agentes equipados com memória episódica e capacidade de reflexão, sem comportamento explicitamente scriptado (Capítulo 2 — Simulações sociais).

2. **b)** — O AI Scientist segue o pipeline: pergunta → revisão de literatura → hipótese → experimento → análise → relatório, espelhando o método científico (Capítulo 3 — Autonomous Research Systems).

3. **b)** — Comportamento emergente significa que o comportamento do sistema como um todo não é trivialmente previsível a partir do comportamento dos agentes individuais — a soma é diferente das partes (Capítulo 4 — Emergência e alinhamento).

4. **b)** — AlphaEvolve (DeepMind) usa evolução automatizada de código/algoritmos via LLMs para descobrir soluções novas em problemas matemáticos e de algoritmos (Capítulo 3 — Sistemas de referência).

## Verdadeiro ou Falso (justificado)

1. **Falso.** Sociedades de agentes podem não convergir — agentes com objetivos parcialmente conflitantes podem entrar em deadlock, polarização ou oscilação sem consenso. A convergência depende da arquitetura de coordenação (voting, mediator, norms) (Capítulo 4 e exercícios do syllabus).

2. **Verdadeiro.** Emergência pode produzir comportamentos prejudiciais — polarização, echo chambers, discriminação, manipulação. Nem toda emergência é benéfica; é necessário avaliar e mitigar (Capítulo 4.2 — Quando a soma é diferente das partes).

3. **Verdadeiro.** Automação de pesquisa levanta questões sobre autoria (quem é autor?), responsabilidade (quem responde por erros?), integridade (os resultados são reproduzíveis?), e impacto na comunidade científica (Capítulo 5.2 — Questões éticas).

4. **Falso.** Avaliar qualidade científica é notoriamente difícil — envolve novidade, validade metodológica, reprodutibilidade, relevância e impacto, muitos dos quais são subjetivos e só verificáveis a longo prazo. Não há métrica trivial (Capítulo 4.4 e exercícios do syllabus).

## Código curto

1. **Mini sociedade via blackboard:**
```python
def mini_society(topic):
    bb = Blackboard(topic)  # espaço compartilhado
    bb.write(pesquisador.explore(topic))
    bb.write(critico.critique(bb.read_all()))
    report = sintetizador.synthesize(bb.read_all())
    return report
```
Referência: Capítulo 1 (Sociedades de agentes) e Lab 1.

2. **Pipeline de autonomous research:**
```python
def autonomous_research(question):
    lit = literature_review(question)
    hypothesis = generate_hypothesis(question, lit)
    results = run_experiment(hypothesis)  # simulado
    analysis = analyze(results)
    return write_report(question, lit, hypothesis, analysis)
```
Referência: Capítulo 3 (Autonomous Research Systems).

3. **Detecção de não-convergência:**
```python
def check_convergence(turns, max_turns=20):
    if len(turns) >= max_turns:
        positions = [t.position for t in turns[-5:]]
        if not agree(positions):
            return "IMPASSE: no convergence after max turns"
    return None
```
Referência: Capítulo 4 (Emergência e alinhamento).

## Análise de trade-off

1. **Simulação social vs. otimização multi-agente:** Simulação social explora comportamento emergente em ambientes com agentes heterogêneos (policy simulation, opinião pública). Otimização multi-agente busca otimizar uma função objetivo (escalonamento, alocação). Simulação para entender fenômenos sociais; otimização para resolver problemas (Capítulo 2 e 1).

2. **Totalmente autônomo vs. assistência (HITL):** Autônomo tem risco de produzir pesquisa inválida, fabricar dados, ou chegar a conclusões erradas sem supervisão. Assistência (HITL) mantém o humano no controle das decisões críticas (validação de hipótese, interpretação de resultados), reduzindo risco. O risco do autônomo é responsabilidade e integridade (Capítulo 5).

3. **Critérios para avaliar qualidade científica de relatório de AI:**
   - **Reprodutibilidade:** Os experimentos podem ser replicados?
   - **Validade metodológica:** A metodologia é correta e apropriada?
   - **Novidade/relevância:** A contribuição é nova e significativa?
   Referência: Capítulo 4.4 e 5.

## Debug / diagnóstico

1. **Diagnóstico:** O sintetizador não tem mecanismo de resolução de conflito — aceita todas as contribuições sem reconciliar contradições. **Correção:** adicionar uma etapa de resolução de conflito onde o sintetizador identifica afirmações contraditórias, solicita evidências aos agentes, e escolhe a posição melhor suportada ou marca a contradição como não resolvida (Capítulo 4 e Lab 1).

2. **Diagnóstico:** O AI Scientist fabrica dados de experimentos porque o "experimento" é puramente textual (LLM gera resultados sem execução real). **Mitigações:** (1) Conectar o experimento a código executável real (rodar experimento de verdade); (2) Adicionar verificação de reprodutibilidade (re-executar e comparar) e flag para dados não-reproduzíveis (Capítulo 3 e 5).
