---
password: Etho-Prof-2026
---
# ETHAGT16 — Avaliação do Módulo

> Curso: Sociedades de Agentes & Autonomous Research Systems · Nota mínima de aprovação: 3,0

## Composição da nota (4 pilares)

| Pilar | Peso | Instrumento |
|---|---|---|
| Técnico | 40% | Protótipo (sistema de pesquisa autônoma) + paper review |
| Consultivo | 30% | Defesa crítica |
| Comportamental | 20% | Ética em discussão |
| Prático | 10% | Demo: relatório gerado |

**Nota final** = Σ(pilar × peso).

---

## Rubrica — Pilar Técnico (40%)

O projeto exige projetar um protótipo de sistema de pesquisa autônoma que, dada uma pergunta técnica, produz um relatório com fontes (esboço do Capstone). Meta: relatório coerente em ≥60% dos casos; análise honesta do que funcionou e falhou.

| Critério | Peso | 1 (muito abaixo) | 3 (esperado) | 5 (referência) |
|---|---|---|---|---|
| Correção técnica | 25% | Sistema não produz relatório; sem papéis definidos | Protótipo funcional com papéis (pesquisador, crítico, sintetizador, etc.); relatório coerente em ≥60% dos casos | ≥60% + casos de borda (fontes conflitantes, pergunta ambígua, comportamento emergente indesejado) tratados |
| Qualidade arquitetural | 25% | Sociedade monolítica; sem separação de papéis/normas | Separação razoável (papéis, normas, instituições); pipeline de pesquisa estruturado | Padrões claros (papéis/normas/reputação modelados), pipeline pergunta→hipótese→experimento→relatório modular, ADR |
| Profundidade | 20% | Superficial; não entende sociedades vs otimização | Diferencia simulação social de otimização multi-agente; justifica escolha de papéis | Discute trade-offs (emergência vs controle, AI Scientist vs AlphaEvolve), analisa convergência, avalia qualidade científica |
| Produção-ready | 15% | Só roda em notebook | Docker; pipeline reproduzível; análise crítica honesta | Docker + ambiente de simulação + pipeline reproduzível + análise crítica estruturada + ADR de topologia social |
| Avaliação/observabilidade | 15% | Sem avaliação de qualidade do relatório | Avaliação de coerência em ≥10 perguntas; análise do que funcionou/falhou | Avaliação de qualidade científica (fontes, coerência, originalidade), detecção de comportamento emergente, logs de convergência |

**Paper review** (parte do Pilar Técnico): revisão crítica de ≥1 paper canônico (Generative Agents, AI Scientist, AgentVerse) analisando método, resultados, limites e aplicabilidade ao protótipo. Peso: 40% do pilar técnico.

---

## Critérios dos demais pilares

- **Consultivo (30%):** Defesa crítica do protótipo para banca, discutindo o que funcionou, o que falhou e limitações.
  - *1:* Apresenta sem análise crítica nem limites.
  - *3:* Discute resultados honestamente, identifica ≥3 limitações, propõe melhorias.
  - *5:* Articula trade-offs de emergência vs controle, avalia fronteira do estado da arte, propõe direções de pesquisa.

- **Comportamental (20%):** Ética em discussão — participação em debate estruturado sobre riscos de pesquisa autônoma.
  - *1:* Não participa do debate ou posicionamento ético ausente.
  - *3:* Contribui com ≥3 argumentos éticos coerentes (autoria, responsible AI, autopropagação).
  - *5:* Articula dilemas éticos profundos, propõe salvaguardas, distingue pesquisa responsável de não-responsável.

- **Prático (10%):** Demo: relatório gerado pelo sistema de pesquisa autônoma ao vivo.
  - *1:* Sistema não produz relatório na demo.
  - *3:* Sistema produz relatório coerente com fontes em tempo aceitável.
  - *5:* Mostra papéis interagindo, fontes citadas, análise crítica do resultado em tempo real.

---

## Regras

- Entrega: repositório Git com protótipo, paper review (`./docs/paper-review.md`), análise crítica e ADR.
- **Integridade acadêmica:** a análise crítica deve ser honesta (não inflacionar resultados). Paper review deve ser autoral; resumo direto de LLM sem análise resulta em dedução. Plágio resulta em nota 1,0.
- Atraso: -0,5 ponto por dia útil, até 3 dias.
