# ETHAGT01 — Gabarito da Prova

> Restrito a mentores. Respostas esperadas e critérios de correção para [`prova.md`](prova.md).

## Parte 1 — Conceitos

**1. (b) Retrieval · Tools · Memory · Loop de controle.** O Augmented LLM de Anthropic é LLM + retrieval + tools + memory + loop de controle. Ref.: Capítulo 2 — O Augmented LLM: o bloco fundamental, §2.1.

**2. FALSO.** Nem toda aplicação deve ser um agente. Workflows (caminhos predefinidos) oferecem previsibilidade, custo controlado e testabilidade. A recomendação de Anthropic é começar simples e só aumentar complexidade com evidência. Muitas tarefas cabem em uma única chamada ou prompt chaining. Ref.: Capítulo 4 — Workflows vs Agentes, §4.3 (Princípio da complexidade crescente).

**3. (c) Fine-tuning.** As seis componentes são Perception, Brain, Planning, Action, Tool Use, Collaboration. Fine-tuning é técnica de treinamento, não componente arquitetural. Ref.: Capítulo 1 — Do LLM ao Agente, §1.3 (taxonomia unificada).

**4. FALSO.** No Augmented LLM a recuperação é **dinâmica e dirigida pelo modelo** (in-loop): o LLM decide *se*, *o que* e *quantas vezes* recuperar. No RAG ingênuo, a recuperação é estática e externa. Ref.: Capítulo 2, §2.2 (Retrieval in-loop).

## Parte 2 — Aplicação e trade-off

**5.** O colega viola o **Princípio da complexidade crescente** (Anthropic: "find the simplest solution possible — and only increase complexity when demonstrably needed"). Riscos: (i) **imprevisibilidade** — o caminho de execução é não-determinístico, dificultando teste e SLA; (ii) **custo/latência variáveis** — o agente pode consumir muitas iterações sem teto; (iii) **dificuldade de debug** — sem caminho fixo, regressões são difíceis de atribuir. Ref.: Capítulo 4, §4.3-4.4.

**6.** Problema 1: o agente **repete a mesma ação** sem detectar o erro — falta detecção de repetição. Correção: ao ver o mesmo `Action` + `Action Input` N vezes, forçar mudança (re-planejar ou parar). Problema 2: a **ferramenta não existe** no catálogo (`TOOLS`). Correção: a mensagem de erro já lista as opções (boa prática), mas o modelo ignora — pode ser necessário reforçar o prompt ou validar o nome da tool antes de tentar. Ref.: Capítulo 3 — O Agent Loop, §3.3 e §3.5 (Limitações: loops).

**7.** Python puro: **máximo controle e visibilidade** do loop, parsing e estado — essencial para aprender o mecanismo. LangGraph: (i) **checkpointing nativo** (persistência, resume, time-travel, HITL); (ii) **controle de fluxo explícito** como grafo visível e versionável; (iii) streaming/callbacks de infraestrutura. Ref.: Capítulo 5, §5.1-5.3.

**8. FALSO.** O custo é tipicamente **linear** por token de entrada na maioria dos provedores. O que cresce é a **latência** e o risco de degradação de qualidade ("lost in the middle"). Mesmo com contexto longo disponível, não se deve preencher sem critério. Ref.: Capítulo 2, §2.4 e Capítulo 6 (observabilidade).

## Parte 3 — Projeto curto

**9.** Espera-se um esqueleto com os 3 elementos:
```python
def run_agent(llm, pergunta, max_iter=10):
    mensagens = [{"role": "system", "content": SYSTEM_PROMPT},
                 {"role": "user", "content": pergunta}]
    for i in range(max_iter):
        resposta = llm(mensagens)
        mensagens.append({"role": "assistant", "content": resposta})
        if "Final Answer:" in resposta:
            return resposta.split("Final Answer:")[1].strip()
        action = _extrair(resposta, "Action:")
        if action in TOOLS:
            obs = TOOLS[action]["fn"](_extrair(resposta, "Action Input:"))
        else:
            obs = f"Ferramenta '{action}' não existe. Opções: {list(TOOLS)}"
        mensagens.append({"role": "user", "content": f"Observation: {obs}"})
    return "Limite de iterações atingido."
```
Avaliar: (a) `max_iter` como hard cap, (b) fallback com lista de opções, (c) condição `Final Answer`. Ref.: Capítulo 3, §3.3.

**10.** Resposta modelo: (a) **Agente** — research assistant exige número de passos imprevisível e decisões condicionais (refinar queries com base no que encontra). (b) Tools mínimas: `search_local_kb`, `search_web`, `calculate` (se houver dados numéricos). (c) **Custo por execução** (tokens × preço) e **latência ponta-a-ponta** — métricas de primeira classe desde o dia 1. Ref.: Capítulo 4 §4.4 e Capítulo 6 §6.4.

---

## Nota esperada por perfil

- **5,0**: domina o Augmented LLM, implementa ReAct do zero, justifica workflow vs agente com trade-offs.
- **4,0**: entende conceitos e implementa o loop, com algumas imprecisões.
- **3,0**: conhece definições mas não articula trade-offs ou não implementa o loop corretamente.
- **<3,0**: precisa revisar o módulo.
