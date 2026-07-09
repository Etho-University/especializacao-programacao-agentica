---
password: Etho-Prof-2026
---
# Checklist — Segurança de Agente

> Aplicar **antes** de levar qualquer agente/sistema para avaliação, laboratório de produção, ou entrega a cliente. Baseado em OWASP LLM Top-10, princípios de Anthropic, e boas práticas de `ETHAGT13`.

## Princípios fundamentais
- [ ] **Princípio do menor privilégio**: o agente tem só as tools/escopos estritamente necessários
- [ ] **Sandbox**: execução isolada (container, VM, workspace descartável)
- [ ] **Defense in depth**: múltiplas camadas (input filter + schema + output filter + HITL)

## Entradas (input)
- [ ] Schema estrito nos inputs (structured outputs / JSON schema)
- [ ] Filtro/classificador de prompt injection na entrada
- [ ] Limite de tamanho de input
- [ ] Sanitização de dados não confiáveis (especialmente em RAG)
- [ ] Rate limiting por usuário/sessão

## Ferramentas (tools)
- [ ] Allowlist explícita de tools (não dinâmica)
- [ ] Cada tool tem escopo mínimo (credenciais separadas, IAM restrito)
- [ ] Tools destrutivas (delete, deploy, transfer) exigem **HITL obrigatório**
- [ ] Tools com side-effects externos têm confirmação e log de auditoria
- [ ] MCP servers auditados (supply chain: código, dependências, origem)

## LLM / prompts
- [ ] System prompt trata explicitamente instruções não confiáveis
- [ ] Dados de usuário são separados de instruções de sistema (delimitadores claros)
- [ ] Temperature e parâmetros calibrados para a tarefa (não mais altos que necessário)
- [ ] Não há segredos no prompt (chaves, PII, dados sensíveis)

## Saídas (output)
- [ ] Validação de output (schema, formato)
- [ ] Filtro de conteúdo (PII, conteúdo proibido, dados sensíveis)
- [ ] Verificação de "tool call" antes de executar (especialmente ações externas)

## Execução e controle
- [ ] **Limite de iterações** (max steps) para evitar loops infinitos
- [ ] **Timeout** total por tarefa
- [ ] **Orçamento** (max tokens / max custo) por execução
- [ ] **Circuit breaker**: pausa o agente se detectar padrão anômalo
- [ ] Checkpoints de HITL para decisões críticas

## Observabilidade e auditoria
- [ ] Todos os passos (thought/action/observation) logados
- [ ] Tool calls com args + resultado + timestamp
- [ ] Traces preservados por política de retenção
- [ ] Alertas para: falhas repetidas, custo acima do esperado, tool não-prevista

## Avaliação adversarial (red team)
- [ ] Testes de prompt injection direto e indireto (via documentos em RAG)
- [ ] Testes de jailbreak
- [ ] Testes de exfiltração de dados
- [ ] Testes de abuso de tools
- [ ] Cobertura de casos de borda (inputs malformados, Unicode, escaping)

## Governança
- [ ] Responsável pelo agente definido (DRI)
- [ ] Política de incident-response (plano se algo der errado)
- [ ] Conformidade regulatória verificada (LGPD/GDPR se aplicável)
- [ ] Documentação ADR para decisões de risco assumidas

## Específico para multi-agente
- [ ] Cada agente com escopo próprio (não credencial compartilhada)
- [ ] Validação de mensagens entre agentes (A2A)
- [ ] Supervisor tem poder de veto sobre workers
- [ ] Logs consolidados de toda a topologia

---

**Princípio norteador (Anthropic)**: agentes são ideais para escalar em **ambientes confiáveis**. Em ambientes adversariais, preferir workflows ou manter HITL forte.
