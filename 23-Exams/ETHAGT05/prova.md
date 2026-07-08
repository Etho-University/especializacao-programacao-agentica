# ETHAGT05 — Prova do Módulo: Memória de Agentes

> Universidade Etho · Versão 1.0 · Julho 2026
> Duração: ~60 min · 10 questões · closed book · Pilar Técnico (40%)

Esta prova avalia arquitetura de memória para agentes: tipos (working, episódica, semântica, procedural), checkpointer, gerenciamento de contexto, memória vetorial e produção.

---

## Parte 1 — Conceitos (Q1-4)

**1. (Múltipla escolha)** Quais são as quatro camadas de memória canônicas?
- (a) Cache · buffer · disco · nuvem
- (b) Working · Episódica · Semântica · Procedural
- (c) Curto prazo · longo prazo · permanente · temporária
- (d) Vector · graph · relacional · key-value

**2. (V/F justificado)** "A working memory (janela de contexto) é efêmera: some ao fim da sessão, enquanto a persistent memory sobrevive entre sessões."

**3. (Múltipla escolha)** Qual implementação é tipicamente usada para memória **episódica** (eventos passados com timestamp)?
- (a) Apenas a janela de contexto
- (b) Vector store + metadados
- (c) Variáveis globais em Python
- (d) Arquivos de log de console

**4. (V/F justificado)** "Todo agente precisa das quatro camadas de memória, por padrão."

---

## Parte 2 — Aplicação e trade-off (Q5-8)

**5. (Trade-off)** Por que o checkpointer é necessário para HITL (Human-in-the-Loop)? Sem ele, o que falha?

**6. (Análise de evicção)** Descreva a fórmula de scoring de eviction dos Generative Agents (Park et al.) combinando três fatores.

**7. (Debug de memória)** Um agente tem a fato semântico "o usuário mora em São Paulo", mas o usuário mudou-se para o Rio. Quais são 3 estratégias para lidar com fatos que mudam ao longo do tempo?

**8. (V/F justificado)** "Para consultas exatas por chave estruturada ('qual o CPF do usuário?'), uma memória vetorial é superior a uma base relacional."

---

## Parte 3 — Projeto curto (Q9-10)

**9. (Projeto curto)** Escreva o esqueleto de uma função `gerenciar_contexto(mensagens, max_tokens)` que faz sumarização em cascata das mensagens mais antigas quando o contexto excede o limite.

**10. (Projeto curto)** Para um agente pessoal de longo prazo (assistente de produtividade), justifique as 4 camadas de memória com um exemplo concreto de cada: working, episódica, semântica, procedural.

---

## Critérios de correção (resumo)

| Conceito | Questões | Peso |
|---|---|---|
| Tipos de memória | 1, 2, 4 | 20% |
| Checkpointer & HITL | 5 | 15% |
| Gerenciamento de contexto | 6, 9 | 25% |
| Memória semântica & factual | 7, 8 | 20% |
| Arquitetura de memória | 3, 10 | 20% |

**Conversão**: cada questão vale 10 pts; total 100 pts. Nota 1-5.
- 90+ pts: 5,0
- 75-89: 4,0
- 60-74: 3,0 (mínimo aprovação)
- <60: reprovação.

Gabarito comentado em [`gabarito.md`](gabarito.md).
