# Coordinator

> Padrão 3/23 · Categoria A — Orquestração

## Intenção
Mediar comunicação entre agentes sem decidir o conteúdo; gerencia sessão, handoffs, estado compartilhado.

## Estrutura
`coordinator` roteia mensagens, mantém state, não gera conteúdo.

## Quando usar
Muitos agentes precisam coordenar; quer desacoplar remetente/destinatário.

## Anti-patterns
Coordinator virando supervisor (decidindo conteúdo).

## Custo
Baixo (gerenciamento, não geração).

## Referências
- Padrões de middleware
- Actor model
- ETHAGT09 — Comunicação Multi-Agente
