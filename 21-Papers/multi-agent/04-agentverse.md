# AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors

> **Autores**: Weize Chen, Yusheng Su, Jingwei Zuo, Cheng Yang, Chenfei Yuan, Chi-Min Chan, Heyang Yu, Yuxia Lu, Yi-Hsin Hung, Chen Qian, Yujia Qin, Xin Cong, Ruobing Xie, Zhiyuan Liu, Maosong Sun  
> **Venue/Ano**: ICLR 2024 · arXiv:2308.10848  
> **URL**: https://arxiv.org/abs/2308.10848

## TL;DR
AgentVerse propõe um framework para **orquestração dinâmica** de agentes, onde um "manager" recruta agentes especializados para cada tarefa e coordena sua colaboração.

## Contribuições
- Framework dinâmico: manager recruta agentes conforme a tarefa
- Suporte a múltiplos modos de comunicação (transmissão, rodízio, debate)
- Observatório para monitorar comportamentos emergentes

## Método
**Manager**: analisa tarefa → recruta especialistas → define modo de comunicação. **Specialists**: agentes especializados que colaboram via modo definido. **Observer**: monitora interações para emergência.

## Resultados
- Demonstra que manager dinâmico melhora qualidade vs equipe fixa
- Comportamentos emergentes: competição, cooperação, especialização
- Aplicações em debug de código, QA, debate

## Limitações
- Manager pode não recrutar especialistas ótimos
- Modos de comunicação fixos (não adaptativos)
- Escalabilidade limitada (manager central)

## Relação com a Especialização
**Referência para ETHAGT09, ETHAGT10 e ETHAGT16**. AgentVerse é exemplo de topologia dinâmica (manager recruta ad-hoc). Conceito de emergência é base para ETHAGT16 (Sociedades de Agentes).
