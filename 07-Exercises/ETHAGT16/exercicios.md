# ETHAGT16 — Lista de Exercícios

> Curso: Sociedades de Agentes & Autonomous Research Systems. Fixação de conceitos. Use a apostila `04-Apostilas/ETHAGT16/apostila.md` como referência.

## Múltipla escolha

**1. Na simulação de Smallville (Generative Agents), os agentes exibem:**

a) Apenas respostas a comandos
b) Comportamento social emergente (rotinas, relacionamentos, memória) a partir de agentes com memória e reflexão
c) Otimização matemática
d) Navegação web

**2. Um "Autonomous Research System" (ex.: AI Scientist da Sakana) segue qual pipeline?**

a) Prompt → resposta
b) Pergunta → revisão de literatura → hipótese → experimento → análise → relatório
c) Treinamento → inferência
d) Indexação → busca

**3. "Comportamento emergente" em sociedades de agentes significa que:**

a) O comportamento é programado explicitamente
b) O comportamento do sistema como um todo não é trivialmente previsível a partir dos agentes individuais
c) Os agentes param de funcionar
d) O sistema fica mais simples

**4. AlphaEvolve (DeepMind) é um sistema que:**

a) Simula sociedades humanas
b) Usa evolução automatizada de código/algoritmos via LLMs para descobrir soluções novas
c) É um vector database
d) É um protocolo A2A

## Verdadeiro ou Falso (justificado)

**1.** "Sociedades de agentes sempre convergem para um consenso." — Justifique.

**2.** "Comportamento emergente pode ser indesejado — nem toda emergência é benéfica." — Justifique.

**3.** "Automação de pesquisa científica por IA levanta questões éticas sobre autoria e responsabilidade." — Justifique.

**4.** "Avaliar a 'qualidade científica' de um AI Scientist é trivial e bem definido." — Justifique.

## Código curto

**1.** Escreva o pseudocódigo de uma "mini sociedade" de 3 agentes (pesquisador, crítico, sintetizador) que colaboram para produzir um relatório via blackboard.

**2.** Escreva o pseudocódigo de um pipeline de autonomous research: pergunta → literatura → hipótese → experimento (simulado) → relatório.

**3.** Escreva o pseudocódigo de uma detecção de não-convergência em uma sociedade de agentes (após N turnos sem acordo, declarar impasse).

## Análise de trade-off

**1.** Compare simulação social (Smallville-like) vs. otimização multi-agente. Quando cada é apropriado?

**2.** Compare um AI Scientist totalmente autônomo vs. um sistema de assistência à pesquisa (human-in-the-loop). Riscos de cada?

**3.** Para avaliar a "qualidade científica" de um relatório gerado por AI, quais 3 critérios você usaria?

## Debug / diagnóstico

**1.** Uma sociedade de 5 agentes produz um relatório, mas o relatório tem contradições internas — um agente afirma X e outro afirma não-X, e o sintetizador não resolve. Diagnóstico e correção.

**2.** Um AI Scientist gera hipóteses plausíveis mas os "experimentos" são inválidos (não reproduzíveis, dados fabricados). Diagnóstico e 2 mitigações.
