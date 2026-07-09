---
password: Etho-Prof-2026
---
# Checklist — Code Review de Agente

> Use ao revisar código de agentes (em projetos, labs ou pull requests). Complementa o code review tradicional com itens específicos de Agentic AI.

## Estrutura e arquitetura
- [ ] Separação clara: prompts / tools / loop / memory / eval
- [ ] Não há lógica de negócio embutida em prompts (prompts são dados)
- [ ] Padrão arquitetural identificável (supervisor, ReAct, workflow, …)
- [ ] ADR para decisões não-triviais (em `10-Architecture/adr/`)

## Prompts
- [ ] Prompts versionados (não in-line hardcoded)
- [ ] Templates com variáveis explícitas (sem f-string ambígua)
- [ ] Sem segredos no prompt
- [ ] Few-shot examples validados
- [ ] Idioma e tom consistentes

## Tools
- [ ] Schemas claros (Pydantic / TypedDict / JSON schema)
- [ ] Descrições ricas (princípio ACI: exemplos, edge cases, poka-yoke)
- [ ] Tratamento de erro em cada tool (timeout, exceção, retry)
- [ ] Idempotência onde aplicável
- [ ] Tools destrutivas marcadas como tal

## Loop e controle
- [ ] Limite de iterações explícito
- [ ] Timeout por chamada e total
- [ ] Tratamento de loops (detecção de repetição)
- [ ] Recuperação de falhas (retry policy, fallback)

## Memória e estado
- [ ] Estado serializável (checkpointer compatível)
- [ ] Janela de contexto gerenciada (sumarização / eviction)
- [ ] PII não persistida sem necessidade
- [ ] Migrações de schema consideradas

## Avaliação
- [ ] Testes unitários para tools
- [ ] Testes de integração para o agente (golden cases)
- [ ] Eval automatizado (LLM-as-judge ou similar)
- [ ] Dataset de regressão
- [ ] Medição de custo/latência

## Segurança
- [ ] Passou pelo `checklist-security-agente.md`
- [ ] Inputs não confiáveis tratados
- [ ] HITL nas ações críticas

## Produção
- [ ] Observabilidade (traces para LangSmith/Phoenix/Langfuse)
- [ ] Logs estruturados (não print)
- [ ] Métricas exportadas (Prometheus / equivalente)
- [ ] Dockerfile / ambiente reproduzível
- [ ] Variáveis de ambiente documentadas (.env.example)
- [ ] Sem chaves no código (secret scanning passou)

## Documentação
- [ ] README do projeto/runnable
- [ ] Como rodar, testar, avaliar
- [ ] Limitações conhecidas
- [ ] Diagrama de arquitetura

## Revisão pedagógica (se for material didático)
- [ ] Está alinhado ao syllabus do módulo
- [ ] Códigos `ETHAGT` referenciados corretamente
- [ ] Convenções de nomenclatura seguidas
- [ ] Comentários explicam o **porquê**, não o **o quê**

---

**Aprovação**: requer 1 revisor para labs/exemplos; 2 revisores para material didático oficial ou mudanças em `01-Curriculum/` ou `00-Governanca/`.
