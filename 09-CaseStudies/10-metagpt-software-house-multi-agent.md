# Caso de Estudo — MetaGPT: software house multi-agente

> ETHAGT09 · Sociedade de agentes simulando uma equipe de desenvolvimento.

## Contexto

Hong et al. (arXiv:2308.00352) criaram o **MetaGPT**, um framework multi-agente que simula uma software house: agentes com papéis (Product Manager, Architect, Engineer, QA) colaboram para produzir software a partir de uma especificação.

## Arquitetura

```
[Product Manager] ─► spec
       │
       ▼
[Architect] ─► design técnico
       │
       ▼
[Engineer] ─► código
       │
       ▼
[QA Engineer] ─► testes + feedback
       │
       ▼ (se falhar, volta para Engineer)
   software final
```

## Padrões de comunicação usados

- **Sequência estruturada**: papéis bem definidos, fluxo previsível.
- **Documentos compartilhados**: cada agente publica seu output (spec, design) num formato estruturado que outros consomem (estilo SOP — Standard Operating Procedure).
- **Feedback loop**: QA → Engineer quando há bug.

## Lições

1. **SOPs (procedimentos operacionais padrão)** melhoram qualidade multi-agente — agentas seguem "processo" como humanos em empresa madura.
2. **Papéis claros reduzem ambiguidade** de quem faz o quê.
3. **Documentos estruturados** como interface entre agentes é mais robusto que conversa livre.
4. A estrutura reduz loops infinitos e melhora convergência.

## Aplicação prática

O padrão MetaGPT é aplicável a qualquer "empresa virtual":

- Pesquisa (pesquisador + revisor + editor).
- Marketing (estrategista + copywriter + designer).
- Operações (triager + executor + auditor).

## Referências

- Hong, S. et al. *MetaGPT: Meta Programming for Multi-Agent Collaborative Framework*. arXiv:2308.00352. ICLR 2024.
- Chen, W. et al. *AgentVerse*. arXiv:2308.10848.
