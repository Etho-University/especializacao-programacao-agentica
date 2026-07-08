# ETHAGT08 — Quiz Final

> Quiz individual, sem consulta, 5 perguntas de múltipla escolha + V/F.
> Tempo estimado: 5 min
**Critério**: ≥3 acertos = compreensão básica atingida.

---

## Pergunta 1

Qual é o problema que o MCP resolve?

- A) Falta de modelos grandes o suficiente
- B) A explosão N×M de integrações LLM ↔ sistemas
- C) Ausência de frameworks de agentes
- D) Custo de tokens

<details>
<summary>Resposta</summary>

**B) A explosão N×M de integrações LLM ↔ sistemas**

Antes do MCP, integrar N LLMs a M sistemas exigia N×M integrações custom. Cada provedor tinha seu formato; cada sistema precisava de conector por provedor. MCP padroniza para N+M: cada LLM implementa 1 client; cada sistema implementa 1 server. A está errada (modelos já são grandes). C está errada (há frameworks). D está errada (MCP não resolve custo de tokens).
</details>

---

## Pergunta 2

Qual capability permite que um server peça ao LLM do host para gerar texto?

- A) Tools
- B) Resources
- C) Prompts
- D) Sampling

<details>
<summary>Resposta</summary>

**D) Sampling**

Sampling é a capability que inverte a direção: o server pede ao host para gerar texto via LLM (`sampling/createMessage`). O fluxo é server → client → host → LLM → host → client → server. Tools (A) é host → server (ação). Resources (B) é leitura passiva de dado. Prompts (C) são templates servidos pelo server ao host.
</details>

---

## Pergunta 3

Qual transporte é o canônico para remote servers na spec 2025-11-25?

- A) stdio
- B) HTTP+SSE (deprecated)
- C) Streamable HTTP
- D) WebSocket

<details>
<summary>Resposta</summary>

**C) Streamable HTTP**

Streamable HTTP é o transporte canônico para remote servers desde março/2025, confirmado na spec 2025-11-25. Single endpoint `POST /mcp`, JSON-RPC 2.0, com SSE opcional para streaming. stdio (A) é local (subprocesso). HTTP+SSE (B) está deprecated desde mar/2025. WebSocket (D) não é transporte MCP.
</details>

---

## Pergunta 4

Qual é o maior risco de segurança ao usar resources de fontes não confiáveis?

- A) Rate limiting
- B) Prompt injection
- C) Incompatibilidade de schema
- D) Latência alta

<details>
<summary>Resposta</summary>

**B) Prompt injection**

Resources de fontes não confiáveis (issues do GitHub, emails, páginas web) podem conter texto malicioso que o LLM segue como instrução ("ignore instruções anteriores e..."). Esse é o vetor #1 de ataque em MCP. Mitigação: marcar resources como untrusted, sanitização, HITL para ações sensíveis. A, C, D são problemas operacionais, mas não são o MAIOR risco de segurança.
</details>

---

## Pergunta 5

Verdadeiro ou falso: MCP substitui o tool calling nativo do LLM.

- A) Verdadeiro
- B) Falso — MCP padroniza o protocolo de comunicação, não substitui o tool calling do modelo

<details>
<summary>Resposta</summary>

**B) Falso — MCP padroniza o protocolo de comunicação, não substitui o tool calling do modelo**

MCP é uma camada de padronização do protocolo host↔server. O modelo continua usando tool calling nativo (function calling). MCP padroniza como o host descobre as tools do server, como negocia capabilities, como troca mensagens. Não substitui o mecanismo de tool calling do LLM — o complementa com um protocolo interoperável.

Esta é a pegadinha do quiz — alunos costumam errar achando que MCP é "novo tool calling".
</details>

---

## Pergunta Bônus (não conta para nota)

Qual destas NÃO é uma capability canônica do MCP?

- A) Tools
- B) Resources
- C) Reinforcement Learning
- D) Sampling

<details>
<summary>Resposta</summary>

**C) Reinforcement Learning**

As 4 capabilities canônicas do MCP são: Tools, Resources, Prompts, Sampling. Reinforcement Learning é uma técnica de treinamento de modelos, não uma capability do protocolo MCP. Extras: Roots, Notifications, Subscriptions, Elicitation.
</details>

---

## Resultado

| Acertos | Avaliação |
|---|---|
| 5/5 | Excelente — compreensão completa do MCP |
| 4/5 | Bom — compreensão sólida, revisar 1 ponto |
| 3/5 | Suficiente — revisar 2 pontos (provavelmente sampling e transportes) |
| 2/5 | Insuficiente — reler spec MCP + Anthropic announcement |
| 0-1/5 | Crítico — agendar horário com professor; fazer Lab 1 antes de seguir |

---

## Tópicos para Revisar por Erro

| Errou a pergunta | Revisar |
|---|---|
| 1 (problema N×M) | Slide 5 — motivação; intro.md do 14-MCP |
| 2 (sampling) | Slide 19 — sampling; capabilities.mmd |
| 3 (transportes) | Slide 9-10 — transportes; specification.md do 14-MCP |
| 4 (prompt injection) | Slide 50 — prompt injection via resources |
| 5 (MCP vs tool calling) | Slide 16 — tools; conexão com ETHAGT02 |

---

> **Mantido por**: Universidade Etho · Versão 1.0 · Julho 2026
> **Spec de referência**: MCP Specification 2025-11-25 (modelcontextprotocol.io)
