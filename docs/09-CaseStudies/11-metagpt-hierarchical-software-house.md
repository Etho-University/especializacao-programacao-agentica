# Caso de Estudo — MetaGPT em software house multi-agente

> ETHAGT10 · Topologia hierarchical aplicada a desenvolvimento de software.

## Contexto

O **MetaGPT** (Hong et al., arXiv:2308.00352) é a aplicação canônica de topologia hierarchical em agentes: simula uma software house com papéis de Product Manager, Architect, Engineer, QA.

## Topologia

```
              [Stakeholder input]
                     │
                     ▼
            [Product Manager] ─► PRD (spec)
                     │
                     ▼
              [Architect] ─► design técnico
                     │
                     ▼
        ┌────────────┴────────────┐
        ▼                         ▼
   [Engineer]                [QA Engineer]
        │                         │
        ▼                         ▼
     código ─◄─── feedback ─── testes
        │
        ▼
   software final
```

## Padrões observados

1. **Hierarchical com papéis**: cada agente tem especialização clara.
2. **Documentos estruturados como interface**: PRD, design, código — formatos padronizados que outros consomem (SOPs).
3. **Feedback loops**: QA → Engineer quando há bug.

## Resultados

MetaGPT atingiu state-of-the-art em benchmarks de geração de software multi-arquivo. A topologia hierarchical (com papéis e SOPs) é creditada como diferencial.

## Lições

1. **Topologia + papéis claros** superam agentes "genéricos".
2. **SOPs (procedimentos operacionais padrão)** trazem disciplina de empresa humana para sociedade de agentes.
3. **Documentos estruturados** são interface mais robusta que conversa livre.
4. Hierarchical escala bem para sistemas com complexidade gerenciável.

## Referências

- Hong, S. et al. *MetaGPT*. arXiv:2308.00352. ICLR 2024.
- Chen, W. et al. *AgentVerse*. arXiv:2308.10848.
