# Guardian

> Padrão 17/23 · Categoria E — Governança e Segurança

## Intenção
Aplicar guardrails e exercer veto sobre ações perigosas.

## Estrutura
`guardian(proposed_action)` → aprova/rejeita/edita.

## Quando usar
Ações destrutivas; ambientes adversariais.

## Anti-patterns
- Guardian leniente
- Sem log de veto

## Custo
1 chamada por ação sensível.

## Referências
- Constitutional AI
- NeMo Guardrails
- ETHAGT13 — Segurança
