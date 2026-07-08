# Actor Model

> Topologia 5/12 · ETHAGT09, ETHAGT11

## Descrição
Agentes modelados como **atores** com estado privado, mailboxes e comunicação assíncrona via mensagens. Cada ator processa uma mensagem por vez, podendo criar outros atores.

## Estrutura
```
[Actor A] ──msg──► [Actor B]
    │                    │
    │ create             │ create
    ▼                    ▼
[Actor C]          [Actor D]
```
- **Estado privado**: só o ator modifica
- **Mailbox**: fila de mensagens
- **Comunicação**: assíncrona, fire-and-forget

## Quando usar
- Sistemas distribuídos com alta concorrência
- Tolerância a falhas (cada ator é isolado)
- Muitos agentes (dezenas a centenas)

## Quando evitar
- Poucos agentes locais (overkill)
- Baixa latência crítica (assincronia adiciona overhead)
- Raciocínio sequencial síncrono

## Trade-offs
| Prós | Contras |
|------|---------|
| Escala horizontalmente | Complexidade de raciocínio |
| Isolamento forte | Overhead de mensagens |
| Resiliência | Debug distribuído difícil |

## Referências
- ETHAGT09 — Comunicação Multi-Agente
- ETHAGT11 — Event-Driven & Orquestração
- Hewitt 1973 — *A Universal Modular Actor Formalism*
- Akka, Erlang/OTP
