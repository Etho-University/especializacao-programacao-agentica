# Caso de Estudo — Suporte ao cliente em produção (Coinbase / Intercom / Thomson Reuters)

> ETHAGT03 · Os 5 padrões aplicados em arquitetura real.

## Contexto

Vários casos documentados (Anthropic *Building Effective Agents*, Appendix 1) mostram empresas usando workflows agênticos para suporte ao cliente. O suporte é um caso especialmente bom para agentes porque:

- Combina **conversação** + **ação**.
- Integração com **dados externos** (pedidos, contas).
- Ações programáticas (reembolsar, atualizar) são bem definidas.
- **Sucesso é mensurável** (resolvido? cliente satisfeito?).
- Empresas cobram por **resolução** (não por token) — alinhamento de incentivos.

## Arquitetura típica (síntese de casos públicos)

```
ticket do cliente
   │
   ▼
[Routing] classifica em: geral / reembolso / técnico / escala
   │
   ├── geral ───────► [Parallelization: responder + filtrar (guardrails)]
   │
   ├── reembolso ───► [Prompt Chaining: validar elegibilidade → aprovar (HITL) → executar]
   │
   ├── técnico ─────► [Orchestrator-Workers: diagnóstico + sub-queries em docs/histórico]
   │                       │
   │                       ▼
   │                 [Evaluator-Optimizer: refinar resposta antes de enviar]
   │
   └── escala ──────► Humano
```

## Padrões identificados

| Padrão | Onde | Por quê |
|---|---|---|
| Routing | Topo | Categorias distintas têm tratamentos próprios |
| Parallelization | Respostas gerais | Responder + filtrar em paralelo melhora ambos |
| Prompt Chaining | Reembolsos | Etapas fixas com gates (validação, HITL) |
| Orchestrator-Workers | Casos técnicos | Subtarefas dependem do problema específico |
| Evaluator-Optimizer | Antes de enviar | Garantir qualidade antes do cliente ver |

## Lições

1. **Raramente há um padrão único**. Arquiteturas reais **compoêm** padrões.
2. **HITL nos lugares certos** — não em tudo, mas sim em ações destrutivas (reembolso).
3. **Medida de sucesso externa** — "resolvido?" orienta o design inteiro.
4. **Modelos de cobrança por resolução** alinham incentivos: a empresa só paga se o agente resolveu, o que força qualidade.
5. **Guardrails em paralelo** (não embutidos no responder) — lição direta do padrão parallelization.

## Diferenciação da Especialização

Cursos de mercado geralmente param em "aqui está um exemplo de agente de suporte". Nós decompomos a arquitetura nos 5 padrões, mostrando **onde cada um vive** e **por quê**. Esse olhar é o que permite ao aluno projetar (não só copiar).

## Referências

- Anthropic. *Building Effective Agents*, Appendix 1: "Customer support". dez/2024.
- Relatos públicos: Coinbase, Intercom, Thomson Reuters (casos citados pela Anthropic).
