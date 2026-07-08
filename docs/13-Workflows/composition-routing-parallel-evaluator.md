# Composição: Routing + Parallelization + Evaluator-Optimizer

## Intenção
Padrão típico de suporte ao cliente em produção (Coinbase, Intercom, Thomson Reuters). Combina os 3 workflows para tratar tickets heterogêneos com qualidade.

## Estrutura
```
ticket ─► [Routing: classificar]
            │
            ├── geral ─► [Parallelization: responder + filtrar (guardrails)]
            │
            ├── reembolso ─► [Prompt Chaining + HITL]
            │
            └── técnico ─► [Orchestrator-Workers: diagnóstico + sub-queries]
                              │
                              ▼
                       [Evaluator-Optimizer: refinar resposta]
                              │
                              ▼
                          resposta
```

## Quando usar
- Tickets heterogêneos com perfis diferentes.
- Precisa de guardrails + qualidade.
- Volume que justifica arquitetura composta.

## Lições
1. Raramente há **um** padrão. Há **composição**.
2. HITL nos lugares certos (ações destrutivas).
3. Sucesso mensurável ("resolvido?") orienta o design.

## Referências
- Anthropic *Building Effective Agents*, Appendix 1 (2024).
