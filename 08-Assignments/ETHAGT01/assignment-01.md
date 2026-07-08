# ETHAGT01 — Avaliação do Módulo

> Curso: Arquitetura Cognitiva de Agentes LLM · Nota mínima de aprovação: 3,0

## Composição da nota (4 pilares)

| Pilar | Peso | Instrumento |
|---|---|---|
| Técnico | 40% | Prova escrita + projeto comparativo (3 versões do agente) |
| Consultivo | 30% | Apresentação de 10 min justificando a arquitetura escolhida |
| Comportamental | 20% | Code review de um colega (repo + traces) |
| Prático | 10% | Demo ao vivo: agente respondendo a 3 perguntas |

**Nota final** = Σ(pilar × peso).

---

## Rubrica — Pilar Técnico (40%)

O projeto exige um agente "research assistant" em 3 versões (Python puro, LangGraph, framework à escolha) que decide entre responder direto, recuperar de base local ou usar tool de busca.

| Critério | Peso | 1 (muito abaixo) | 3 (esperado) | 5 (referência) |
|---|---|---|---|---|
| Correção técnica | 25% | Agente não funciona em nenhuma versão; loop ReAct ausente ou quebrado | 3 versões funcionais com bugs menores; roteamento direto/retrieval/tool operacional | 3 versões completas + casos de borda (sem tool disponível, retrieval vazio, loop infinito tratado) |
| Qualidade arquitetural | 25% | Lógica de decisão e loop acoplados; sem separação de Perception/Brain/Action | Separação razoável entre agent loop, tools e retrieval | Padrões claros (Augmented LLM modular), extensível, escolha de framework justificada em ADR |
| Profundidade | 20% | Implementação superficial; sem entender o agent loop | Cobre ReAct, workflows vs agentes, compara as 3 versões em ≥3 critérios (controle, transparência, esforço) | Discute trade-offs de abstração, identifica o que cada framework esconde, justifica quando reduzir camadas |
| Produção-ready | 15% | Só roda em notebook sem Docker nem README | Roda em ambiente controlado com `docker compose up` e README mínimo | Docker + README comparativo + traces de exemplo + dependências pinadas |
| Avaliação/observabilidade | 15% | Sem logs nem traces; custo não medido | Logging estruturado (thought/action/observation com timestamps) | Traces instrumentados (LangSmith/Phoenix) + custo e latência reportados por versão |

**Prova escrita** (parte do Pilar Técnico): questões sobre taxonomia Perception·Brain·Planning·Action·Tool Use, distinção workflow vs agente, e análise de trace quebrado. Peso: 40% do pilar técnico.

---

## Critérios dos demais pilares

- **Consultivo (30%):** Apresentação de 10 min para banca simulada defendendo a arquitetura escolhida entre as 3 versões.
  - *1:* Não justifica a escolha; lê slides sem clareza.
  - *3:* Justifica com ≥3 critérios coerentes (controle, transparência, esforço); responde a perguntas.
  - *5:* Articula trade-offs com dados reais (custo/latência), antecipa objeções, recomendação acionável.

- **Comportamental (20%):** Code review estruturado do projeto de um colega.
  - *1:* Comentários genéricos ("bom código") ou ausentes.
  - *3:* ≥5 observações específicas sobre correção, legibilidade e ACI das tools.
  - *5:* Review profundo com sugestões de arquitetura, detecção de edge cases e menção a princípios (poka-yoke, grounding).

- **Prático (10%):** Demo ao vivo: agente respondendo a 3 perguntas (1 direta, 1 via retrieval, 1 via tool de busca).
  - *1:* Agente falha em ≥2 perguntas ou não roda.
  - *3:* Responde corretamente as 3 com latência aceitável.
  - *5:* Mostra traces ao vivo, explica decisões do agente em tempo real, lida com pergunta surpresa.

---

## Regras

- Entrega: repositório Git (URL fornecida) até a data limite do calendário acadêmico.
- Formato: repo com README comparativo, código das 3 versões, traces em `./traces/`, ADR em `./docs/adr-001.md`.
- **Integridade acadêmica:** o código deve ser autoral. Uso de LLM para assistência é permitido e deve ser declarado no README. Plágio de colegas ou de repositórios públicos sem atribuição resulta em nota 1,0 e abertura de processo.
- Atraso: -0,5 ponto por dia útil, até 3 dias. Após isso, nota 1,0.
