---
password: Etho-Prof-2026
---
# ETHAGT03 — Gabarito da Prova

> Restrito a mentores. Respostas esperadas e critérios de correção para [`prova.md`](prova.md).

## Parte 1 — Conceitos

**1. (b) Na Parallelization a decomposição é fixa; no Orchestrator-Workers ela é dinâmica.** O Orchestrator-Workers tem um LLM que decompõe a tarefa em tempo de execução (as subtarefas *emergem*), enquanto na Parallelization o particionamento é predefinido em código. Ref.: Capítulo 5 — Orchestrator-Workers, §5.1.

**2. VERDADEIRO.** Routing por dificuldade envia perguntas fáceis para modelo barato (Haiku) e difíceis para modelo potente (Sonnet/Opus). Para 80/20, isso reduz custo 5-7× sem perder qualidade percebida. O trade-off é a qualidade do classificador. Ref.: Capítulo 3 — Routing, §3.3 (Routing por modelo).

**3. (c) Evaluator-Optimizer.** O Evaluator-Optimizer é um loop: um LLM gera, outro avalia e dá feedback, e o gerador refina até satisfazer um critério. Ref.: Capítulo 6 — Evaluator-Optimizer.

**4. FALSO.** Orchestrator-Workers é mais caro (planejamento + síntese) e menos previsível. Para subtarefas *fixas e conhecidas*, Parallelization é mais simples, barato e testável. Orchestrator-Workers só supera quando a decomposição é *dinâmica* (depende do conteúdo). Ref.: Capítulo 5, §5.5 (Trade-off).

## Parte 2 — Aplicação e trade-off

**5.** **Sectioning:** divide a tarefa em subtarefas *independentes* e executa em paralelo. Brilha quando há partes que não dependem umas das outras (ex.: resumir seções de um documento). **Voting:** executa a *mesma tarefa N vezes* (com temperatura/variação) e agrega por maioria. Brilha quando há incerteza e múltiplas amostras aumentam a confiança (ex.: self-consistency em raciocínio matemático). Ref.: Capítulo 4 — Parallelization, §4.2-4.3.

**6.** 1. **Routing:** classifica o ticket (cobrança, técnico, cancelamento) e encaminha ao tratador especializado. 2. **Parallelization:** o tratador resolve, rodando em paralelo com um guardião de segurança (filtra violações de política). 3. **Evaluator-Optimizer:** a resposta é avaliada (política, tom, precisão) e refinada antes de enviar ao cliente. Esta composição é o padrão canônico de produção (Coinbase, Intercom). Ref.: Capítulo 7 — Composições, §7.1.

**7.** O sistema está **forçando workflow em um problema que pede agente**. Sinais: branches crescendo sem parar, `if` sobre `if`, latência explodindo, falha em casos que exigem adaptação. Diagnóstico: o número de caminhos não é previsível — a tarefa pede a flexibilidade de um agente autônomo. Solução: migrar para agente com cercas (tools finitas, critério de sucesso, orçamento de iterações). Ref.: Capítulo 7, §7.3 (Sinais de que você está forçando workflow).

**8. FALSO.** Gates devem ser implementados por **código determinístico** (não LLM), sempre que possível. Um gate que valida "o esboço cobre os tópicos obrigatórios?" deve ser uma função de código que checa, não um LLM subjetivo. Gates de LLM introduzem imprevisibilidade. Ref.: Capítulo 2 — Prompt Chaining, §2.3 (Implementação: "os gates são código, não LLM").

## Parte 3 — Projeto curto

**9.** Três condições de parada: (1) score atinge o limiar (`score >= min_score`); (2) máximo de iterações (`i >= max_iter`); (3) feedback estagnado (delta entre iterações cai abaixo de um threshold — o avaliador não tem mais o que dizer).
```python
def evaluator_optimizer(task, max_iter=5, min_score=0.9):
    output = generate(task)
    for i in range(max_iter):
        score, feedback = evaluate(output, task)
        if score >= min_score or feedback is None:
            return output
        output = refine(output, feedback)
    return output
```
Ref.: Capítulo 6, §6.3 (Critérios e convergência).

**10.** (a) **Parallelization (sectioning):** 3 idiomas são subtarefas independentes; executar em paralelo reduz latência. (b) **Routing:** categorias distintas com tratamentos especializados; classificador encaminha ao tratador certo. (c) **Prompt Chaining:** passos lineares fixos com gates de validação entre etapas. Ref.: Capítulos 2, 3 e 4.

---

## Nota esperada por perfil

- **5,0**: domina os 5 padrões, compõe com critério, diagnostica fronteira workflow/agente.
- **4,0**: diferencia padrões corretamente, com pequenas imprecisões em trade-offs.
- **3,0**: conhece os padrões mas não justifica escolhas com evidência.
- **<3,0**: precisa revisar os 5 workflows.
