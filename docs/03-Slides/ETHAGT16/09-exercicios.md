# ETHAGT16 — Exercícios

> Exercícios para aula e para casa.
> Organizados por tipo: em aula, individual, em duplas, projeto.

---

## Exercícios em Aula

### E1 — Definindo Papéis (Votação Rápida)
**Slide**: 15
**Tempo**: 1 min
**Formato**: Duplas, 1 min discussão + share rápido

**Enunciado**: Cenário: "Simular um comitê editorial de revista científica". Em duplas, definam:

1. 5 papéis e suas responsabilidades
2. Qual norma deve ser compartilhada por todos?
3. Como a reputação é acumulada?

**Gabarito**:
- Papéis típicos: editor-chefe, editor associado, revisor 1, revisor 2, autor.
- Norma compartilhada: "toda decisão deve ser justificada por escrito".
- Reputação: número de revisões aceitas, qualidade das revisões (avaliada por outros), tempo de resposta.

---

### E2 — V/F: Sociedades Sempre Convergem?
**Slide**: 21
**Tempo**: 0.5 min
**Formato**: Individual, votação de mão levantada

**Enunciado**: Verdadeiro ou Falso: "Sociedades de agentes sempre convergem para um consenso estável."

**Gabarito**:
- **Falso**. Sociedades podem polarizar (dois polos), oscilar (sem estabilizar) ou colapsar (free-riders dominam). Convergência depende de normas, reputação e alinhamento.

---

### E3 — Design de Simulação: Home Office (Duplas)
**Slide**: 22
**Tempo**: 1 min
**Formato**: Duplas, 1 min discussão

**Enunciado**: Cenário: "Simular o impacto de uma política de home office em uma empresa". Em duplas, definam:

1. 3 tipos de agentes (papéis)
2. 2 normas compartilhadas
3. 1 métrica para acompanhar

**Gabarito**:
- Agentes: gestor, contribuidor sênior, contribuidor júnior.
- Normas: "reuniões síncronas apenas à tarde", "entrega semanal obrigatória".
- Métrica: produtividade média (commits/semana), satisfação (escala 1-5), retenção (%).
- Surpresa possível: juniores sem mentoria presencial podem ter queda de produtividade não prevista pela política.

---

### E4 — Detectando Emergência Indesejada (Duplas)
**Slide**: 41
**Tempo**: 1 min
**Formato**: Duplas, 1 min discussão

**Enunciado**: Analisem o seguinte trace de uma sociedade de 5 agentes (10 interações):

```
[1] Pesquisador: "Vou buscar fontes sobre o tópico X"
[2] Crítico: "Fonte A é fraca"
[3] Pesquisador: "Concordo, vou buscar mais"
[4] Sintetizador: "Fonte A e B dizem a mesma coisa"
[5] Crítico: "B também é fraca"
[6] Pesquisador: "Concordo"
[7] Sintetizador: "Nenhuma fonte é confiável"
[8] Revisor: "Nenhuma fonte é confiável"
[9] Editor: "Não publicamos nada"
[10] Todos: "Concordo, nada é confiável"
```

**Perguntas**:
1. Identifiquem o padrão emergente indesejado.
2. Proponham 2 correções.

**Gabarito**:
- **Padrão**: Echo chamber / paralisia por crítica excessiva. Todos convergem para "nada é confiável" sem produzir saída.
- **Correção 1 (norma)**: Adicionar norma "crítica deve vir acompanhada de alternativa construtiva".
- **Correção 2 (HITL)**: Intervir após 5 rodadas sem saída, forçando síntese parcial.
- **Correção 3 (peso)**: Limitar poder de veto do crítico — ele sinaliza mas não bloqueia.

---

## Exercícios Individuais (para casa)

### E5 — Simulação Social vs Otimização Multi-Agente
**Tempo estimado**: 10 min
**Formato**: Individual, escrito

**Enunciado**: Em 3-4 frases, diferencie simulação social (Smallville-like) de otimização multi-agente (sistemas onde agentes maximizam uma função objetivo).

**Critério de avaliação**:
- Define simulação social como "explorar comportamento emergente sem função objetivo explícita" ✅
- Define otimização multi-agente como "maximizar/minimizar uma função" ✅
- Menciona que simulação social busca **entender**, otimização busca **resolver** ✅
- Exemplo de cada ✅

---

### E6 — 3 Questões Éticas de Pesquisa Autônoma
**Tempo estimado**: 15 min
**Formato**: Individual, escrito

**Enunciado**: Liste 3 questões éticas levantadas pelo AI Scientist (Sakana) operando sem supervisão. Para cada uma, proponha 1 mitigação.

**Exemplo de resposta**:

1. **Questão**: Autoria — quem é autor de um paper gerado por IA?
   **Mitigação**: Rotular claramente como "gerado por AI Scientist v1"; reivindicar autoria apenas para o desenho do sistema.

2. **Questão**: Qualidade — papers plausíveis mas errados podem poluir a literatura.
   **Mitigação**: Review humano obrigatório antes de submissão; registro público de papers gerados por IA.

3. **Questão**: Recursos — autopropagação sem supervisão pode consumir recursos indefinidamente.
   **Mitigação**: Limites rígidos de custo, iterações e taxa de submissão; HITL em decisões de "continuar x abandonar".

---

### E7 — Verdadeiro/Falso Justificado
**Tempo estimado**: 10 min
**Formato**: Individual, escrito

**Enunciado**: Responda V ou F e justifique em 2-3 frases:

1. "Sociedades de agentes sempre convergem."
2. "AI Scientist produz papers de qualidade consistentemente sem supervisão humana."
3. "Comportamento emergente é sempre benéfico porque surge da cooperação."
4. "Smallville (Generative Agents) prova que LLMs simulam humanos perfeitamente."
5. "Alinhamento individual de cada agente é suficiente para alinhar uma sociedade."

**Gabarito**:
1. **F** — Sociedades podem polarizar, oscilar ou colapsar. Convergência depende de normas, reputação e alinhamento.
2. **F** — AI Scientist produz papers com contribuição marginal, bugs de código, alucinação em literatura. Autonomia ≠ qualidade.
3. **F** — Emergência pode ser cooperação (desejada) ou conluio, discriminação, echo chamber (indesejada).
4. **F** — Smallville mostra emergência impressionante mas com limites: agentes são muito coerentes, vieses amplificados, difícil validação.
5. **F** — Alinhamento individual não garante alinhamento coletivo. Interações produzem propriedades emergentes que podem violar valores individuais.

---

### E8 — Avaliar Qualidade de um AI Scientist
**Tempo estimado**: 15 min
**Formato**: Individual, escrito

**Enunciado**: Cenário: AI Scientist gerou um paper sobre "otimização de prompts". Defina 3 critérios objetivos para avaliar a qualidade científica do paper.

**Exemplo de resposta**:

1. **Reprodutibilidade**: o código e os dados estão disponíveis e um humano consegue reproduzir os resultados?
2. **Novidade**: o paper propõe algo que não está trivialmente na literatura existente (comparar com survey recente)?
3. **Corretude metodológica**: o desenho experimental controla variáveis relevantes? Há baseline adequado? Significância estatística?

**Bônus**: validade estatística, ética (consentimento de dados), clareza da escrita.

---

## Projeto do Módulo

### P1 — Protótipo de Sistema de Pesquisa Autônoma
**Prazo**: 2 semanas
**Formato**: Individual ou em duplas
**Carga**: ~10h

**Descrição**: Projetar um protótipo de sistema de pesquisa autônoma que, dada uma pergunta técnica, produz um relatório com fontes (esboço do Capstone).

**Pipeline mínimo**: pergunta → revisão de literatura → hipótese → análise → relatório com fontes.

**Entrega**: protótipo funcional + análise crítica (o que funcionou, o que falhou).

**Entregáveis**:
- Repositório Git com o protótipo
- Relatório gerado pelo sistema (mínimo 2 perguntas-teste)
- README com análise crítica honesta
- Traces de execução

**Critério de sucesso**:
- Relatório coerente em ≥60% dos casos
- Análise honesta do que funcionou e do que falhou

**Avaliação** (rubrica de 4 pilares):

| Pilar | Peso | Critério |
|---|---|---|
| Técnico | 40% | Protótipo funcional, paper review |
| Consultivo | 30% | Defesa crítica da análise |
| Comportamental | 20% | Ética em discussão |
| Prático | 10% | Demo: relatório gerado |

**Nota mínima de aprovação**: 3.0
