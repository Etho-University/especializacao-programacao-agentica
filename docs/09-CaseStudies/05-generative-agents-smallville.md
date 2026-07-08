# Caso de Estudo — Generative Agents (Smallville)

> ETHAGT05 · Memória de longo prazo em agentes com personalidade.

## Contexto

Park et al. (arXiv:2304.03442, Stanford, 2023) criaram "Smallville": uma simulação com 25 agentes LLM vivendo num vilarejo virtual, cada um com memória própria e personalidade persistente. Os agentes demonstraram comportamentos emergentes (organizaram uma festa de Halloween sozinhos).

## Arquitetura de memória

Cada agente tinha:

1. **Memory stream**: lista cronológica de observações (eventos), cada uma com:
   - Timestamp.
   - Descrição textual.
   - **Recency** (quão recente).
   - **Importance** (score atribuído na criação).
   - **Relevance** (similaridade com contexto atual).

2. **Recall**: score combinado `α·recency + β·importance + γ·relevance`. Top-k recuperado.

3. **Reflection**: periodicamente, o agente consolida observações em **insights** de alto nível (ex.: "Klaus Mueller está lendo muito sobre pesquisa eleitoral" → "Klaus quer pesquisar eleições").

## Lições

1. **Recency + Importance + Relevance** é uma fórmula eficaz para recall de memória.
2. **Reflection** (consolidação episódica → semântica) é poderosa: o agente "pensa" sobre seu passado.
3. Comportamento emergente surge com memória persistente + personalidade.

## Aplicação prática

A fórmula de Smallville é diretamente aplicável em agentes Etho:
- Memória episódica de interações com cliente.
- Recency/Importance/Relevance para recall.
- Reflection periódica para consolidar perfil do cliente.

## Referências

- Park, J.S. et al. *Generative Agents: Interactive Simulacra of Human Behavior*. arXiv:2304.03442. UIST 2023.
