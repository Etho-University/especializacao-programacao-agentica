---
password: Etho-Prof-2026
---
# Blueprint do Exame de Certificação

> Especialização em Programação Agêntica · Universidade Etho
> Versão 1.0 · Julho 2026

Este blueprint define a estrutura do exame de certificação "Especialista em Programação Agêntica".

## Visão geral

| Aspecto | Valor |
|---|---|
| **Duração** | 3 horas |
| **Formato** | escrito + prático (com código) |
| **Questões** | 40 (30 conceituais + 10 práticas) |
| **Material permitido** | closed book para conceituais; open repo para práticas |
| **Nota mínima** | 4,0 (escala 1-5) |
| **Frequência** | semestral (oferecido ao fim de cada turma) |

## Distribuição por competência

| Competência | Peso | # Questões | Foco |
|---|---|---|---|
| C1 Programação Agêntica | 25% | 10 | fundamentos, agent loop, workflows |
| C2 Multi-Agent Systems | 20% | 8 | topologias, A2A, coordenação |
| C3 MCP & Tool Use | 15% | 6 | ACI, MCP, governança de tools |
| C4 Agent Memory | 10% | 4 | tipos de memória, checkpointer |
| C5 AgentOps & Avaliação | 15% | 6 | traces, eval, benchmarks |
| C6 Agent Security | 15% | 6 | prompt injection, guardrails, HITL |

## Distribuição por nível cognitivo (Bloom)

| Nível | Peso | O que mede |
|---|---|---|
| **Recordar/Compreender** | 20% | definições, taxonomias, vocabulário |
| **Aplicar** | 30% | usar conceitos em cenários novos |
| **Analisar** | 25% | decompor sistemas, identificar trade-offs |
| **Avaliar** | 15% | julgar arquiteturas, recomendar abordagens |
| **Criar** | 10% | projetar soluções para problemas abertos |

## Tipos de questão

### Conceituais (30 questões)
- **Múltipla escolha** (15): 4 alternativas, 1 correta.
- **Verdadeiro/falso justificado** (8): V/F + 2-3 linhas de justificativa.
- **Análise de trade-off** (5): dado cenário, comparar 2-3 abordagens.
- **Análise de arquitetura** (2): dado diagrama, criticar e sugerir melhorias.

### Práticas (10 questões, com código/repo)
- **Debug de agente** (3): dado trace com problema, identificar e corrigir.
- **Design de tool/ACI** (2): escrever schema + descrição para tool específica.
- **Design de prompt** (2): escrever prompt para padrão específico.
- **Eval design** (2): dado cenário, projetar pipeline de avaliação.
- **ADR writing** (1): dado requisito, escrever ADR justificando decisão.

## Exemplos (no exame modelo)

Ver [`exame-v1.md`](exame-v1.md) para um exame completo de exemplo com gabarito.

## Pré-requisitos para o exame

- Todos os 16 módulos aprovados (≥3,0).
- Capstone aprovado (≥4,0 em todos os pilares).
- ≥8 sessões de mentoria realizadas.

> **Nota**: o exame é **complementar** ao Capstone. O Capstone valida integração prática; o exame valida profundidade conceitual individual.

## Processo

1. **Inscrição**: via RH (Fluxo 06 — Certificação).
2. **Sistema** valida pré-requisitos automaticamente.
3. **Exame aplicado** presencialmente ou via plataforma (com proctoring).
4. **Correção**: gabarito + rubrica; dupla correção para questões abertas.
5. **Resultado**: em até 10 dias úteis.
6. **Recurso**: aluno pode revisar prova e contestar até 5 dias depois.

## Recertificação (validade 2 anos)

Ver [`recertificacao.md`](recertificacao.md).
