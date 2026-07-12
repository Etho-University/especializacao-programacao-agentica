# ETHAGT90 — Guia de Defesa

> Como se preparar para os 45 minutos que decidem sua certificação (25 min apresentação + 20 min Q&A).

## Princípio

A defesa não é apresentar um produto — é **demonstrar domínio**. O painel avalia se você é um **arquiteto** (sabe justificar) ou um **montador** (só colou exemplos). Cada slide, cada decisão, cada métrica deve sobreviver a perguntas.

## Estrutura da apresentação (25 min)

| Tempo | Seção | Conteúdo |
|---|---|---|
| 0-3 min | Contexto e objetivo | qual problema, por que este cenário, não-objetivos |
| 3-8 min | Arquitetura | diagrama C4 + topologia + por que essa |
| 8-12 min | Decisões técnicas (ADRs) | 2-3 ADRs principais com trade-offs |
| 12-16 min | Segurança e governança | threat model + HITL + red team results |
| 16-20 min | Avaliação | eval report + métricas + análise de falhas |
| 20-23 min | Demo ao vivo | 1 pergunta executada na hora |
| 23-25 min | Lições e riscos residuais | o que aprendeu, o que faria diferente |

## Q&A (20 min) — perguntas esperadas

Prepare respostas para:

### Arquitetura
- Por que essa topologia e não [alternativa]?
- Onde está o ponto único de falha?
- Como escala para 100x o volume?

### Decisões técnicas
- Por que [tool X] e não [tool Y]?
- Qual trade-off mais doloroso você aceitou?
- Se refizesse do zero, o que mudaria?

### Segurança
- Como você defenderia contra [ataque específico]?
- O red team encontrou X — como mitiga?
- HITL é suficiente para [cenário]?

### Avaliação
- Seu eval é confiável? Por quê?
- A métrica de sucesso mede o que importa?
- Onde o sistema falha sistematicamente?

### Fronteira
- Como seu sistema se compara a [AI Scientist / Deep Research]?
- O que falta para pesquisa realmente autônoma?
- Questões éticas do seu design?

### Profundidade (pegadinhas)
- Explique o que o framework faz sob o capô (não a API).
- Mostre o prompt efetivo que chega ao modelo.
- O que acontece se [componente] falhar?

## Como se preparar

1. **Ensaiar cronometrado** — 25 min é pouco; practice até caber.
2. **Simular Q&A** com colega/mentor fazendo perguntas difíceis.
3. **Conhecer traces** — painel pode pedir para abrir um trace e explicar.
4. **Conhecer números** — não decorar tudo, mas saber onde achar.
5. **Honestidade** — se não sabe, diga "não sei, mas investigaria assim". Melhor que inventar.

## Critérios de aprovação (Consultivo, 30%)

| Nota | O que o painel observa |
|---|---|
| **1-2** | Não consegue explicar decisões; copiou sem entender; métricas infladas |
| **3** | Explica razoavelmente; algumas decisões sem justificativa forte |
| **4** | Justifica com clareza; discute trade-offs; honesto sobre limites |
| **5** | Domínio profundo; pensa como arquiteto sênior; surpreende com insights |

## O que reprova (consultivo)

- Não conseguir explicar o que o código faz.
- Inflar métricas (painel percebe).
- Falta de HITL ou eval (requisitos do enunciado).
- Não conhecer riscos do próprio sistema.
- Copiar sem atribuir.

## Demo ao vivo (10 min, Prático)

- 3 perguntas **novas** (não ensaiadas) que o painel escolhe.
- Sistema deve responder em tempo razoável (≤5 min cada).
- Trace visível para o painel acompanhar.
- Se falhar: explicar por que (não esconder) — painel respeita honestidade.

## Checklist pré-defesa (5 dias antes)

- [ ] Código + docs entregues ao painel.
- [ ] Apresentação ensaiada cronometrada.
- [ ] Q&A simulado com mentor.
- [ ] Sistema rodando estavelmente.
- [ ] Plano B se demo falhar (vídeo de backup).
- [ ] Sono na noite anterior.

---

*Princípio: o painel quer que você passe. Mostre domínio, honestidade e maturidade — não perfeição.*
