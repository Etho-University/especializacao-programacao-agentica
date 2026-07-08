# ETHAGT13 — Quiz Final

> Quiz individual, sem consulta, 5 perguntas de múltipla escolha.
> Tempo estimado: 5 min
**Critério**: ≥3 acertos = compreensão básica atingida.

---

## Pergunta 1

Qual é a diferença fundamental entre injeção direta e indireta?

- A) Direta é mais perigosa que indireta
- B) Indireta vem de fonte externa (RAG, web, MCP); direta vem do próprio usuário
- C) Direta usa SQL; indireta usa prompt
- D) Não há diferença

<details>
<summary>Resposta</summary>

**B) Indireta vem de fonte externa; direta vem do próprio usuário**

Na injeção direta, o atacante é o próprio usuário que digita o prompt malicioso ("ignore suas instruções"). Na indireta, a injeção vem de fonte externa (documento RAG, página web, MCP resource, email) — o usuário é vítima, não atacante. A indireta é geralmente mais perigosa porque é invisível para o usuário e vem por canais que ninguém filtra. A é errada — indireta é mais perigosa. C é errada — ambas usam prompt. D é errada — a diferença é fundamental.
</details>

---

## Pergunta 2

Por que prompt injection é difícil de defender?

- A) Porque os modelos são muito pequenos
- B) Porque não há separação nativa entre instrução e dados em LLMs
- C) Porque não existem ferramentas de defesa
- D) Porque só modelos pagos têm defesa

<details>
<summary>Resposta</summary>

**B) Porque não há separação nativa entre instrução e dados em LLMs**

Em programação tradicional (SQL, HTML), há separação estrutural entre código e dados (prepared statements, escaping). Em LLMs, instruções e dados são a mesma coisa — texto. O modelo não distingue "ignore isto" (dado) de "ignore isto" (instrução). Isto é uma propriedade fundamental da arquitetura transformer, não um bug. A é errada — modelos maiores também são vulneráveis. C é errada — há defesas (delimitadores, classificadores, instruction hierarchy), mas nenhuma é 100%. D é errada — o problema é arquitetural, independe de modelo pago ou gratuito.
</details>

---

## Pergunta 3

O que é defense in depth?

- A) Uma única defesa muito forte
- B) Múltiplas camadas de defesa, nenhuma perfeita sozinha
- C) Usar apenas HITL
- D) Confiar no modelo para se defender

<details>
<summary>Resposta</summary>

**B) Múltiplas camadas de defesa, nenhuma perfeita sozinha**

Defense in depth é o princípio de aplicar múltiplas camadas de defesa em série: input filter, schema estrito, system prompt robusto, tool allowlist, HITL, output filter, auditoria. Nenhuma camada é perfeita, mas juntas tornam o ataque improvável — o atacante precisa atravessar todas para ter impacto. A é errada — "bala de prata" não existe em segurança de LLM. C é errada — HITL é uma camada entre outras. D é errada — confiar no modelo é o oposto de defense in depth.
</details>

---

## Pergunta 4

HITL sozinho é defesa suficiente?

- A) Sim, humano sempre para ataques
- B) Não, HITL é uma camada; precisa de input/output filter, allowlist, auditoria
- C) Sim, se o humano ler tudo
- D) Depende do modelo

<details>
<summary>Resposta</summary>

**B) Não, HITL é uma camada; precisa de input/output filter, allowlist, auditoria**

HITL tem limitações: fatiga de aprovação (humano aprova sem ler após muitas iterações), social engineering (agente justifica ação de forma convincente), latência (nem toda ação pode esperar humano), e humano limitado (não avalia args técnicos obscuros). HITL é uma camada valiosa mas não suficiente — precisa ser combinado com input filter, output filter, allowlist, e auditoria. A é errada — humano é falível. C é errada — fatiga impede leitura total. D é errado — independe do modelo.
</details>

---

## Pergunta 5

O que é policy-as-code?

- A) Código que gera políticas de marketing
- B) Regras de governança em código executável (ex: OPA/Rego), versionável e auditável
- C) Um tipo de prompt para o agente
- D) Documento legal para conformidade

<details>
<summary>Resposta</summary>

**B) Regras de governança em código executável (ex: OPA/Rego), versionável e auditável**

Policy-as-code é a prática de expressar regras de governança em código executável (como Rego, usado pelo OPA), em vez de documentos estáticos. Vantagens: versionável no Git, testável (testes unitários de política), auditável (code review), e automatizável (CI valida políticas). Para agentes: "tool X só pode ser chamada em condição Y" é expressa em Rego e executada pelo OPA como middleware. A é errada — não é marketing. C é errada — policy-as-code é código que valida, não prompt. D é errada — documento legal é estático; policy-as-code é executável e automática.
</details>

---

## Pergunta Bônus (não conta para nota)

Qual destas NÃO é uma das 6 categorias de teste de red team sistematizado?

- A) Exfiltração de dados
- B) Abuso de tools
- C) Otimização de cache
- D) Jailbreak

<details>
<summary>Resposta</summary>

**C) Otimização de cache**

As 6 categorias de teste de red team para agentes são: (1) Exfiltração de dados, (2) Abuso de tools, (3) Jailbreak, (4) Injeção indireta, (5) Escalação de privilégios, (6) DoS. Otimização de cache é preocupação de performance, não de segurança.
</details>

---

## Resultado

| Acertos | Avaliação |
|---|---|
| 5/5 | Excelente — compreensão completa de segurança e governança de agentes |
| 4/5 | Bom — compreensão sólida, revisar 1 ponto |
| 3/5 | Suficiente — revisar 2 pontos |
| 2/5 | Insuficiente — reler OWASP Top 10 + Greshake |
| 0-1/5 | Crítico — agendar horário com professor; refazer Labs 1 e 2 |
