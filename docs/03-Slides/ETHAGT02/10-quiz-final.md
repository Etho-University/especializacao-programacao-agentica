# ETHAGT02 — Quiz Final

> Quiz individual, sem consulta, 5 perguntas de múltipla escolha.
> Tempo estimado: 5 min
**Critério**: ≥3 acertos = compreensão básica atingida.

---

## Pergunta 1

O que é "poka-yoke" no contexto de Agent-Computer Interface (ACI)?

- A) Uma técnica de prompt engineering para reduzir alucinações
- B) Um design de tool que torna o erro impossível de cometer
- C) Um tipo de structured output que força JSON válido
- D) Um framework para versionamento de tools

<details>
<summary>Resposta</summary>

**B) Um design de tool que torna o erro impossível de cometer**

Poka-yoke (do japonês, "prevenção de erros") em ACI significa projetar a tool de forma que o modelo NÃO POSSA errar — ex.: exigir path absoluto com regex em vez de aceitar path relativo e torcer para o modelo lembrar. A Anthropic mudou `view_file` para exigir paths absolutos no SWE-bench: o erro desapareceu sem mexer no prompt.
</details>

---

## Pergunta 2

Qual é a analogia central que a Anthropic usa para justificar o investimento em design de tools?

- A) Tools são como funções de biblioteca — quanto mais reutilizáveis, melhor
- B) ACI (Agent-Computer Interface) merece tanto esforço quanto HCI (Human-Computer Interface)
- C) Tools são como APIs REST — siga o contrato e está resolvido
- D) Tools são como prompts — o contexto é tudo

<details>
<summary>Resposta</summary>

**B) ACI merece tanto esforço quanto HCI**

A Anthropic é explícita: invista em ACI (Agent-Computer Interface) com o mesmo rigor que investe em HCI (Human-Computer Interface). O "usuário" da tool é o modelo — e assim como um humano confunde uma UI mal desenhada, o modelo confunde uma tool mal descrita. A diferença: o modelo não pode "perguntar de novo".
</details>

---

## Pergunta 3

Quando o Human-in-the-Loop (HITL) é OBRIGATÓRIO?

- A) Para toda tool que retorna dados do banco
- B) Para toda tool que aceita parâmetros do usuário
- C) Para toda tool irreversível E de alto impacto (ex.: delete_account, deploy)
- D) Para toda tool que pode demorar mais de 5 segundos

<details>
<summary>Resposta</summary>

**C) Para toda tool irreversível E de alto impacto**

A matriz de risco classifica tools por reversibilidade × impacto. HITL é obrigatório no quadrante "irreversível + alto impacto" (ex.: delete_account, deploy_to_production, send_email, transfer_money). Tools de leitura (get_order) não precisam. Tools reversíveis de baixo impacto (log_event) não precisam. O critério é o dano potencial, não a complexidade.
</details>

---

## Pergunta 4

Qual é a forma CORRETA de tratar um erro quando uma tool falha?

- A) Propagar a exceção para o framework tratar
- B) Retornar o traceback de Python cru como observation
- C) Capturar o erro e retornar uma mensagem estruturada útil ao modelo
- D) Abortar o agente imediatamente

<details>
<summary>Resposta</summary>

**C) Capturar o erro e retornar uma mensagem estruturada útil ao modelo**

O ideal é retornar algo como `{"error": "division by zero", "suggestion": "try with b != 0"}`. Traceback cru confunde o modelo (ele não sabe o que fazer com 20 linhas de stack Python). Propagar a exceção quebra o loop. Abortar perde todo o trabalho. A mensagem estruturada permite que o modelo decida: tentar de novo com args diferentes, usar outra tool, ou informar o usuário.
</details>

---

## Pergunta 5

Qual é a "regra de ouro" da Anthropic sobre onde investir tempo ao melhorar um agente?

- A) Otimize o prompt do sistema antes de tudo
- B) Troque para um modelo maior quando a acurácia estagnar
- C) Passe mais tempo otimizando as tools do que o prompt principal
- D) Adicione mais tools para dar mais opções ao modelo

<details>
<summary>Resposta</summary>

**C) Passe mais tempo otimizando as tools do que o prompt principal**

Citação direta da Anthropic (caso SWE-bench): "We spent more time optimizing our tools than the overall prompt." A lição: quando o agente falha sistematicamente, o instinto é melhorar o prompt. Mas a maioria das falhas sistêmicas vem de tools mal desenhadas — descrição vaga, schema frouxo, falta de poka-yoke. Corrigir a tool resolve para sempre; corrigir o prompt é remendo temporário.
</details>

---

## Pergunta Bônus (não conta para nota)

Qual destes NÃO é um dos 4 tipos de tools na tipologia de risco desta aula?

- A) Leitura (read)
- B) Escrita (write)
- C) Destrutiva (destructive)
- D) Otimização (optimization)
- E) External side-effect

<details>
<summary>Resposta</summary>

**D) Otimização (optimization)**

Os 4 tipos são: Leitura (search, get — seguro), Escrita (update, create — reversível), Destrutiva (delete, drop — irreversível), External side-effect (email, deploy, transfer — afeta mundo externo). "Otimização" não é um tipo de tool — é um objetivo de engenharia.
</details>

---

## Resultado

| Acertos | Avaliação |
|---|---|
| 5/5 | Excelente — compreensão completa de ACI |
| 4/5 | Bom — compreensão sólida, revisar 1 ponto |
| 3/5 | Suficiente — revisar 2 pontos (provavelmente HITL ou erro tratado) |
| 2/5 | Insuficiente — reler Anthropic Appendix 2 + fazer Lab 1 |
| 0-1/5 | Crítico — agendar horário com professor; reforço de JSON Schema recomendado |
