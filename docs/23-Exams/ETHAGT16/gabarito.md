# ETHAGT16 — Gabarito da Prova
> Restrito a mentores.

## Parte 1 — Conceitos

**1.** **(a)** Correta. Simulação social (Smallville/Generative Agents) modela agentes com comportamento, memória e interação, estudando *emergência*; otimização multi-agente busca maximizar uma função-objetivo coletiva. Não são sinônimos. — *Ref.: Cap. 2 — Simulações sociais (§2.1); Cap. 1 — Sociedades de agentes.*

**2.** **Falso.** Sociedades podem divergir, polarizar, entrar em deadlock ou oscilar. Não há garantia de consenso; a convergência depende de normas, topologia e mecanismos de resolução de conflito. — *Ref.: Cap. 4 — Emergência e alinhamento (§4.5 "Sociedades sempre convergem?").*

**3.** **(a)** Correta. O pipeline canônico: pergunta → revisão de literatura → hipótese → experimento → análise → relatório (AI Scientist e congêneres). — *Ref.: Cap. 3 — Autonomous Research Systems (§3.2 O pipeline de pesquisa).*

**4.** **Verdadeiro.** A emergência surge das interações; agentes individualmente "seguros" podem produzir comportamento coletivo indesejado (polarização, runaways, coordenação para objetivos não-alinhados). — *Ref.: Cap. 4 (§4.1 Comportamento emergente; §4.2 Quando a soma é diferente das partes).*

## Parte 2 — Aplicação e trade-off

**5.** **Simulação social** estuda *como* agentes interagem e o que emerge (ex.: simulação de formação de opinião pública num mercado). **Otimização multi-agente** busca maximizar um objetivo (ex.: fleet de agentes negociando alocação de recursos para maximizar throughput). Diferença: a primeira é descritiva/exploratória; a segunda é normativa/otimizadora. — *Ref.: Cap. 1 — Sociedades; Cap. 2 — Simulações sociais (§2.2 Casos de uso).*

**6.** Causas: (i) o agente hallucina dados sem de fato rodar/validar experimentos; (ii) viés de "narrativa convincente" — o LLM produz texto plausível sem base factual. Mitigações: (a) exigir **execução real** do experimento com logs verificáveis (código que roda e produz artefatos); (b) **HITL** que revisa resultados/claims antes de publicar; (c) checker de consistência citação↔fonte. — *Ref.: Cap. 3 (§3.4 O que funciona e o que falha); Cap. 6 — Casos de estudo (§6.1 AI Scientist).*

**7.** Dificuldades de avaliar qualidade científica do AI Scientist: (i) "qualidade científica" é subjetiva e multidimensional (novidade, validade, relevância) — sem métrica única; (ii) experimentos podem ser hallucinados/não-reproduzíveis; (iii) domínios fora do treino do modelo geram erros factuais sutis difíceis de detectar sem especialista humano. — *Ref.: Cap. 3 (§3.4); Cap. 6 (§6.1).*

**8.** Ética: (i) **autoria/responsabilidade** — quem é responsável por um achado errado? Mitigação: HITL de revisão + atribuição clara de responsabilidade humana. (ii) **automação indevida de pesquisa com consequências públicas** (ex.: pesquisa em áreas sensíveis sem supervisão). Mitigação: escopos permitidos, sandbox, comitê de revisão. (iii) **autopropagação/uso de recursos** — sistemas sem supervisão consomem recursos/escalam sem controle. Mitigação: orçamentos, quotas e kill switches. — *Ref.: Cap. 5 — Fronteira e ética (§5.2 Questões éticas; §5.3 O que NÃO fazer).*

## Parte 3 — Projeto curto

**9.** Sociedade de 5 agentes:
```
pesquisador → coleta fontes/ideias
crítico     → aponta falhas/evidências contrárias
sintetizador→ integra contribuições em rascunho
revisor     → checa coerência/fontes
editor      → finaliza o relatório
```
Fluxo: round-robin com seletor; convergência quando o editor aceita (relatório sem objeções do revisor/crítico) ou ao atingir max_rounds. Critério: relatório coerente com fontes verificáveis. — *Ref.: Cap. 1 — Sociedades de agentes (§1.3 Papéis, normas); Cap. 3 (§3.2 pipeline).*

**10.** O que **NÃO** fazer: (i) permitir **autopropagação** (agentes que criam réplicas de si sem cota/limite); (ii) operar sistemas de pesquisa **sem supervisão humana** em domínios de consequências públicas; (iii) publicar/autoexecutar ações de alto impacto (ex.: code que roda em produção, envio de dados externos) sem HITL e sandbox. — *Ref.: Cap. 5 — Fronteira e ética (§5.3 O que NÃO fazer).*

---

## Erros comuns (parcial/dedução)

- **Q1**: tratar simulação social e otimização como sinônimos → anular.
- **Q2**: crer que sociedades sempre convergem → anular (ignora polarização/deadlock).
- **Q4**: negar emergência indesejada em agentes "seguros" individualmente → anular.
- **Q6**: propor só "melhorar o prompt" sem exigir execução real do experimento + HITL → -50%.
- **Q7**: citar uma métrica única de "qualidade científica" → -40% (deve reconhecer multidimensionalidade).
- **Q9**: sociedade sem critério de convergência/terminação → -40%.
- **Q10**: listas que incluem apenas "ser cuidadoso" sem controles concretos (sandbox/quotas/HITL) → -50%.

Crédito parcial: distinção simulação vs otimização com casos genéricos (não próprios) vale até 60%.

---

## Rubrica por questão (pts)

| Q | Tipo | pts | Aceita parcial |
|---|---|---|---|
| 1 | Múltipla escolha | 10 | 0 |
| 2 | V/F justificado | 10 | 5 |
| 3 | Múltipla escolha | 10 | 0 |
| 4 | V/F justificado | 10 | 5 |
| 5 | Trade-off (distinção + casos) | 10 | 5 distinção + 5 casos próprios |
| 6 | Debug (2 causas + 2 mitigações) | 10 | 2,5 por item (HITL obrigatório) |
| 7 | Análise (3 razões) | 10 | ~3 pts por razão |
| 8 | Trade-off (2 éticas + controle) | 10 | 4 por questão + 1 controle cada |
| 9 | Projeto (sociedade 5) | 10 | 5 papéis/fluxo + 5 critério convergência |
| 10 | Projeto (3 "não fazer") | 10 | ~3 pts por item concreto |

---

## Nota esperada por perfil

- **5,0**: distingue simulação de otimização, identifica emergência indesejada, propõe HITL/controles éticos sólidos.
- **4,0**: descreve pipeline e papéis com pequenas lacunas em alinhamento/emergência.
- **3,0**: conhece AI Scientist/Smallville mas trata sociedades como sempre convergentes.
- **<3,0**: confunde simulação social com otimização ou ignora riscos éticos da pesquisa autônoma.
