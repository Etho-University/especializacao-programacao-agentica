# ETHAGT12 — Quiz Final

> Quiz individual, sem consulta, 5 perguntas de múltipla escolha.
> Tempo estimado: 5 min
**Critério**: ≥3 acertos = compreensão básica atingida.

---

## Pergunta 1

Qual é a principal limitação do LLM-as-judge?

- A) É muito caro para usar em escala
- B) Não consegue avaliar texto, só código
- C) Tem vieses (positional, sycophancy, verbosity, self-preference, knowledge) que precisam de mitigação
- D) Só funciona com GPT-4 como judge

<details>
<summary>Resposta</summary>

**C) Tem vieses que precisam de mitigação**

LLM-as-judge é barato (centavos por avaliação), consegue avaliar texto, e funciona com vários modelos. A limitação real é ter 5 vieses conhecidos (positional, sycophancy, verbosity, self-preference, knowledge) que exigem mitigação: rubrica clara, calibração com humano, múltiplos judges, cross-model, swap de posição. Sem mitigação, o judge pode estar sistematicamente errado.
</details>

---

## Pergunta 2

O que é um golden case?

- A) Um caso de uso de sucesso usado para marketing
- B) Um par (input, critério de sucesso) usado como teste de regressão para agentes
- C) Um caso que sempre passa no eval (não precisa revisar)
- D) Um benchmark padronizado pela comunidade

<details>
<summary>Resposta</summary>

**B) Um par (input, critério de sucesso) usado como teste de regressão**

Golden case é o teste unitário do mundo de agentes. Estrutura: id, input, expected_behavior, eval_fn, category. Cada bug encontrado vira um novo golden case — assim você garante que nunca mais regredirá nele. Não é marketing (A), não é caso que sempre passa (C — casos podem regredir e precisam de revisão), não é benchmark (D — benchmark é padronizado e público, golden case é seu e específico do seu domínio).
</details>

---

## Pergunta 3

O que o SWE-bench avalia?

- A) Navegação web autônoma em sites simulados
- B) Atendimento ao cliente com APIs e políticas
- C) Resolução de issues reais de GitHub em código Python (com testes como ground truth)
- D) Raciocínio geral multi-step com tools

<details>
<summary>Resposta</summary>

**C) Resolução de issues reais de GitHub (código)**

SWE-bench pega 2.294 issues reais de 12 repositórios Python. O agente gera um patch. Critério: os testes automáticos do repositório passam. Esse é o poder do SWE-bench — código tem ground truth objetivo (testes). SWE-bench Verified (500 casos com validação humana) é o subconjunto canônico. A é WebArena, B é τ-bench, D é GAIA.
</details>

---

## Pergunta 4

Em um pipeline de CI para agentes, o que PRINCIPALMENTE bloqueia o deploy?

- A) Latência acima de 1 segundo por step
- B) Regressão no eval score (golden cases + benchmark subset) acima do threshold
- C) Número de steps diferente da versão anterior
- D) Custo acima de $0.01 por execução

<details>
<summary>Resposta</summary>

**B) Regressão no eval score acima do threshold**

CI gate para agentes é a regressão no eval score. Se o score cair mais que o threshold (0% para casos críticos, 5% para não-críticos), o deploy é bloqueado. Latência (A), número de steps (C), e custo (D) são métricas monitoradas mas não bloqueiam deploy sozinhas — geram alertas. O gate é a regressão porque ela indica que a mudança piorou a qualidade do agente.
</details>

---

## Pergunta 5

Verdadeiro ou Falso: "Bom score em benchmark garante bom desempenho em produção."

- A) Verdadeiro — benchmarks são representativos do mundo real
- B) Falso — benchmark é ambiente controlado; produção é mundo real com variância de ambiente, usuários reais, domínio específico
- C) Depende — só se o benchmark for exatamente do mesmo domínio
- D) Verdadeiro — se passou em SWE-bench, está pronto para qualquer uso

<details>
<summary>Resposta</summary>

**B) Falso**

Benchmark é ambiente controlado — dataset fixo, critério objetivo, condições reproduzíveis. Produção é mundo real — ambiente mutável, usuários reais com inputs imprevisíveis, domínio específico, drift ao longo do tempo. Mesmo benchmark do mesmo domínio (C) não garante — produção tem variância que benchmark não captura. Combine benchmark (comparável com a comunidade) + eval custom (representativo do seu caso de uso). Score de benchmark é necessário mas não suficiente.
</details>

---

## Pergunta Bônus (não conta para nota)

Qual destes NÃO é um viés do LLM-as-judge?

- A) Positional bias (prefere primeira/última opção)
- B) Sycophancy (concorda com o que parece querer humano)
- C) Confirmation bias (só busca evidência a favor)
- D) Verbosity bias (prefere respostas mais longas)

<details>
<summary>Resposta</summary>

**C) Confirmation bias**

Os vieses canônicos do LLM-as-judge são 5: positional, sycophancy, verbosity, self-preference, knowledge bias. Confirmation bias é um viés cognitivo humano (e também aparece em LLMs) mas não está na lista canônica de vieses do judge que cobrimos na aula. Mesmo assim, vale estar atento — o judge pode exibir confirmation bias se o prompt sugerir a resposta esperada (o que se sobrepõe com sycophancy).
</details>

---

## Resultado

| Acertos | Avaliação |
|---|---|
| 5/5 | Excelente — compreensão completa, pronto para o projeto |
| 4/5 | Bom — compreensão sólida, revisar 1 ponto |
| 3/5 | Suficiente — revisar 2 pontos antes do projeto |
| 2/5 | Insuficiente — reler SWE-bench, GAIA, τ-bench + Hamel Husain |
| 0-1/5 | Crítico — agendar horário com professor antes do projeto |
