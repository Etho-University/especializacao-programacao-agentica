---
password: Etho-Prof-2026
---
# ETHAGT04 — Gabarito da Prova

> Restrito a mentores. Respostas esperadas e critérios de correção para [`prova.md`](prova.md).

## Parte 1 — Conceitos

**1. (b) CoT = linear sem reflexão; Plan-and-Execute = linear sem reflexão; Reflexion = adiciona auto-correção.** No mapa tridimensional (momento × estrutura × auto-correção): CoT é linear, raciocínio-durante, sem reflexão. Plan-and-Execute é linear, raciocínio-antes, sem reflexão. Reflexion adiciona a quarta dimensão: auto-correção após falha. Ref.: Capítulo 1 — Tipologia, §1.2.

**2. FALSO.** CoT ajuda em tarefas que *genuinamente requerem* raciocínio multi-step (matemática, lógica). Em recuperação factual simples ("qual a capital da França?"), CoT *adiciona custo sem benefício* e às vezes introduz erros. Regra: aplique CoT onde há raciocínio, não onde há fato. Ref.: Capítulo 2 — CoT, §2.2.

**3. (b) O planner gera o plano inteiro de uma vez ("cego"), sem re-raciocinar entre passos, e executa em paralelo.** ReWOO (Xu et al., arXiv:2305.18323) gera o plano completo sem ver evidências intermediárias, inclui variáveis para saídas futuras, e resolve as chamadas em paralelo — reduzindo drasticamente as chamadas ao LLM. Ref.: Capítulo 3 — Plan-and-Execute e ReWOO, §3.3.

**4. FALSO.** Com um reasoning model nativo, o modelo *já raciocina internamente*. Adicionar "pense passo a passo" é redundante ou até prejudicial. O design muda: não force CoT promptado; mais foco em tools; calibre o orçamento de thinking tokens. Ref.: Capítulo 7 — Inference-Time Reasoning, §7.2.

## Parte 2 — Aplicação e trade-off

**5.**
| | Latência | Custo (tokens) | Robustez a planos errados |
|---|---|---|---|
| ReAct | média | alto (re-raciocina a cada passo; contexto cresce) | média (adapta via observação) |
| Plan-and-Execute | média (1 planner + execução sequencial, mas sem re-raciocínio por passo) | médio | alta (re-planner corrige) |
| ReWOO | baixa (execução em paralelo) | baixo | baixa (rígido, plano cego) |

Ref.: Capítulo 3, §3.2-3.3.

**6.** Dois critérios: (i) o problema tem **múltiplos caminhos possíveis com qualidade variável** (espaço de busca explorável); (ii) há um **avaliador confiável** para podar ramos (sem avaliação, a árvore não sabe para onde ir). Adicional: o orçamento permite (o problema é valioso o suficiente). ToT é "artilharia pesada" — reserve para onde CoT/ReAct já falharam. Ref.: Capítulo 4 — ToT e LATS, §4.3.

**7.** Defesas canônica: (i) **limite de tentativas** (`max_attempts`) — hard cap que força o agente a parar; (ii) **detecção de repetição** — se o mesmo erro/lição aparece N vezes, force mudança; (iii) **orçamento de tokens/passos** — pare quando o gasto excede o orçamento; (iv) re-planejamento supervisionado (HITL se o agente está perdido). Ref.: Capítulo 5 — Reflexion, §5.4 e Capítulo 8 — Falhas, §8.1.

**8. FALSO.** Self-Discover é adequado para problemas *novos ou heterogêneos* onde não há padrão pronto. Para problemas bem-known (matemática padrão), CoT/ToT são mais previsíveis. Self-Discover adiciona custo inicial (fase de descoberta) que só vale em tarefas complexas. Ref.: Capítulo 6 — Self-Discover, §6.3.

## Parte 3 — Projeto curto

**9.** Espera-se os 3 atores com memória:
```python
def reflexion(task, max_attempts=3):
    memoria = []
    for attempt in range(max_attempts):
        trace = actor(task, memoria)           # Actor age, alimentado pela memória
        if evaluator(trace) == "sucesso":      # Evaluator avalia
            return trace
        licao = self_reflect(trace, task)       # Self-Reflection produz lição
        memoria.append(licao)                   # "na próxima, verifique X antes de Y"
    return trace
```
Avaliar: loop com `max_attempts`, memória acumulada entre tentativas, 3 papéis distintos. Ref.: Capítulo 5, §5.2.

**10.** (a) **Self-Consistency (voting sobre CoT):** raciocínio matemático beneficia-se de múltiplas amostras votadas — cadeias erradas divergem, a correta converge. (b) **ReAct:** depuração tem número de passos imprevisível e exige observar o resultado de cada ação antes de decidir o próximo passo. (c) **Self-Discover:** problema tão novo que não há padrão pronto — o agente compõe sua própria estratégia. Ref.: Capítulos 2, 1, 6.

---

## Nota esperada por perfil

- **5,0**: posiciona estratégias no mapa, implementa Reflexion, justifica escolhas com trade-offs explícitos.
- **4,0**: diferencia estratégias, com pequenas imprecisões em custo/robustez.
- **3,0**: conhece as estratégias mas não justifica quando usar cada uma.
- **<3,0**: precisa revisar raciocínio e planejamento.
