# ETHAGT16 — Projeto do Módulo: Protótipo de Sistema de Pesquisa Autônoma

> Curso: Sociedades de Agentes & Autonomous Research Systems · Pilar: Técnico 40% + Prático 10% · Equipe: individual ou dupla

## Contexto / Cenário

Um instituto de pesquisa em tecnologia quer explorar o estado da arte de *autonomous research systems*: sistemas de agentes que, dada uma pergunta técnica aberta, conduzem autonomamente o ciclo de pesquisa — revisão de literatura, formulação de hipótese, coleta de evidências, análise crítica, síntese e relatório com fontes verificáveis. Este protótipo serve como esboço do Capstone da especialização (ETHAGT90). O instituto é ciente dos riscos éticos (autoria, alucinação de fontes, responsabilidade) e exige uma análise crítica honesta: o que funciona, o que falha, e onde a supervisão humana é insubstituível. O sistema deve usar uma *sociedade* de agentes com papéis distintos (pesquisador, crítico, sintetizador, revisor, editor).

## Objetivo

Projetar um protótipo de sistema de pesquisa autônoma que, dada uma pergunta técnica, produz um relatório estruturado com fontes verificáveis. Implementar a sociedade de ≥5 agentes com papéis definidos (pesquisador, crítico, sintetizador, revisor, editor). Entregar o protótipo funcional e uma análise crítica honesta do que funcionou, do que falhou, e das questões éticas levantadas — este é o esboço do Capstone.

## Requisitos

### Funcionais

1. Sociedade de ≥5 agentes com papéis distintos:
   - Pesquisador: busca e coleta fontes relevantes (web, arXiv, documentos).
   - Crítico: avalia qualidade e relevância das fontes; rejeita fontes fracas.
   - Sintetizador: integra evidências em narrativa coerente.
   - Revisor: verifica consistência interna, citações e contradições.
   - Editor: formata relatório final com estrutura acadêmica.
2. Pipeline de pesquisa: pergunta → revisão de literatura → hipótese/síntese → análise crítica → relatório.
3. Relatório com ≥1.000 palavras, seções estruturadas (introdução, achados, discussão, conclusão, referências).
4. Fontes verificáveis: cada afirmação substantiva citada com URL/DOI; falsificação de fontes detectada e reportada.
5. Normas de colaboração: agentes seguem regras (ex.: revisor pode rejeitar e pedir reescrita; crítico tem veto sobre fontes).

### Não-funcionais

- Latência total do relatório ≤ 10 minutos.
- Custo por relatório documentado.
- Fontes verificadas: ≥80% das URLs/DOIs citadas são acessíveis e suportam a afirmação (validação automatizada).
- Reprodutível: mesma pergunta com mesma seed produz relatório comparável em estrutura.
- Observabilidade: traces de cada agente e interação entre eles.

## Entregáveis

- Protótipo (repositório com sociedade de agentes, pipeline de pesquisa, validação de fontes).
- ≥3 relatórios gerados em perguntas técnicas distintas (para análise comparativa).
- Análise crítica honesta (o que funcionou, o que falhou, limitações, questões éticas, onde supervisão humana é necessária).
- Paper review: análise crítica de ≥1 paper canônico (AI Scientist ou Generative Agents) contextualizando o protótipo.

## Critérios de sucesso (mensuráveis)

- Relatório coerente e utilizável em ≥60% dos casos (≥3 perguntas avaliadas por humano com rubrica).
- ≥80% das fontes citadas são verificáveis (URL/DOI acessível e suporta a afirmação).
- Sociedade de ≥5 agentes demonstra colaboração estruturada (papéis distintos, normas seguidas, vetos respeitados).
- Análise crítica identifica ≥3 limitações concretas do sistema (ex.: alucinação de fontes, superficialidade, viés de síntese).
- Paper review contextualiza o protótipo frente ao estado da arte com profundidade técnica.

## Competências avaliadas

- C1 Programação Agêntica — nível **A** (sociedade de agentes funcional).
- C2 Multi-Agent Systems — nível **A** (papéis, normas, instituições, coordenação).
- C3 MCP & Tool Use — nível **B** (tools de busca e validação de fontes).
- C4 Agent Memory — nível **A** (estado compartilhado da pesquisa, memória entre agentes).
- C5 AgentOps & Avaliação — nível **I** (validação de fontes, avaliação de coerência, traces).
- C6 Agent Security — nível **I** (questões éticas, supervisão humana, responsible AI).

## Referências

- Apostila: `04-Apostilas/ETHAGT16/apostila.md`
- Rubrica técnica: `08-Assignments/ETHAGT16/assignment-01.md`
