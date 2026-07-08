# ADR-001 — Fundações da Especialização em Programação Agêntica

- **Status**: Accepted
- **Data**: Julho 2026
- **Decisor**: Principal AI Architect — Universidade Etho

## Contexto

A Universidade Etho mantém um catálogo de cursos com códigos estáveis (`ETHDEV`, `ETHFSTK`, `ETHDATA`, `ETHML`, …) organizados em Tronco Comum + trilhas técnicas, com modelo de avaliação de 4 pilares (Técnico 40 / Consultivo 30 / Comportamental 20 / Prático 10) e 5 fases de evolução (Onboarding → Formação → Autonomia → Especialização → Liderança).

O curso `ETHDEV07` — *Introdução à Programação Agêntica* (20 h, Autonomia) já existe no Tronco Comum como porta de entrada. A área de competências "Inteligência Artificial" já cobre LLMs & Prompt Engineering, RAG Systems, MLOps — mas **não cobre** arquitetura de agentes, multi-agentes, MCP, AgentOps ou sistemas autônomos em profundidade.

Cursos existentes no mercado (DeepLearning.AI, HuggingFace, LangGraph, CrewAI, AutoGen, OpenAI Agents SDK, Google ADK, Semantic Kernel, PydanticAI) são **centrados em framework**, superficiais em arquitetura e cobrem mal produção, segurança e fronteira (multi-agentes, pesquisa autônoma).

## Decisão

1. **Criar a Especialização em Programação Agêntica** como trilha de **Especialização (Fase 4)**, com ~440 h e duração 12-18 meses.
2. **Adotar o prefixo `ETHAGT`** para todos os cursos da especialização (mantendo a convenção `ETH<AREA>`).
3. **Estruturar em 4 fases internas (A/B/C/D) + Capstone**, totalizando **16 cursos + 1 capstone**.
4. **Foco em arquitetura, não framework**: o bloco fundamental é o Augmented LLM (Anthropic); SDKs são estudados como instanciação.
5. **Adicionar 6 novas competências** à área "Inteligência Artificial" do Framework: Programação Agêntica, Multi-Agent Systems, MCP & Tool Use, Agent Memory, AgentOps & Avaliação, Agent Security.
6. **Manter o modelo de 4 pilares** com nota de aprovação ≥ 3,0 por módulo e ≥ 4,0 para certificação.
7. **Pré-requisito de entrada**: `ETHDEV07` + `ETHML01` + Python Intermediário.
8. **Capstone obrigatório**: Plataforma de Pesquisa Autônoma (estilo AutoResearch), exercitando todos os módulos.
9. **Ênfase deliberada em multi-agentes e pesquisa autônoma** (diferenciação vs mercado), com equilíbrio entre todas as dimensões.
10. **Carga por módulo**: 15-30 h (Fases A-D); Capstone 60 h.

## Consequências

**Positivas**:
- Formação coerente com o ecossistema Etho (códigos, fases, avaliação, certificação).
- Diferenciação clara vs mercado (profundidade arquitetural + fronteira).
- Rastreabilidade competência → módulo → avaliação preservada.
- Base para futuro crescimento (sociedades de agentes, IA generativa aplicada avançada).

**Negativas / custos**:
- ~440 h é exigente; pode afastar profissionais sem tempo. Mitigação: modularidade (concluir fases A+B já habilita projetos simples).
- Não certifica em framework específico — alguns alunos podem querer "selo LangGraph". Mitigação: eletivos e referências aos frameworks em cada módulo.
- Exige manutenção contínua (estado da arte muda rápido). Mitigação: Research KB viva em `20-Research/`.

## Alternativas consideradas

| Alternativa | Por que rejeitada |
|---|---|
| Trilha "AI Engineer" genérica sem Especialização em agentes | Não cobre a fronteira; perde diferenciação |
| Certificação em LangGraph/CrewAI espec. | Framework-locked; deprecia rápido |
| Especialização sem capstone | Não valida integração; quebra o requisito de certificação Etho (projeto final) |
| Novo prefixo `ETHAI` | Conflitaria com a área "IA" inteira; `ETHAGT` é mais específico |
| Modelo de avaliação diferente dos 4 pilares | Quebraria rastreabilidade e consistência com a Universidade Etho |

## Referências

- Pesquisa de estado da arte (arXiv:2601.12560; Anthropic *Building Effective Agents*; LangGraph examples)
- Convenções da Universidade Etho (espaço `UE` no Confluence): Catálogo de Cursos, Framework de Competências, Avaliações, Processo de Evolução, Template de PDI
