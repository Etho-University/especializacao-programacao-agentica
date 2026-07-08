# MetaGPT: Meta Programming for Multi-Agent Systems

> **Autores**: Sirui Hong, Mingchen Zhuge, Jonathan Chen, Xiawu Zheng, Yuheng Cheng, Ceyao Zhang, Jinlin Wang, Zili Wang, Steven Ka Shing Yau, Zijuan Lin, Liyang Zhou, Chenyu Ran, Lingfeng Xiao, Chenglin Wu, Jürgen Schmidhuber  
> **Venue/Ano**: ICLR 2024 · arXiv:2308.00352  
> **URL**: https://arxiv.org/abs/2308.00352

## TL;DR
MetaGPT atribui **papéis humanos** a agentes (PM, Arquiteto, Engenheiro, QA) e usa **SOPs** (Standard Operating Procedures) com artefatos estruturados (PRD, design, código) para coordenação.

## Contribuições
- Framework multi-agente com papéis baseados em personas de engenharia de software
- SOPs formais: cada papel gera artefatos específicos (documentos, código)
- Hierarquia de informação: PRD → Design → Tasks → Código → Review

## Método
**CEO** → **PM** (PRD) → **Architect** (design) → **Project Manager** (tasks) → **Engineers** (código) → **QA** (testes). Cada papel tem system prompt especializado e ferramentas específicas. Artefatos intermediários são validados antes de passar para o próximo papel.

## Resultados
- Geração de código (HumanEval): competitive com modelos 10× maiores
- Geração de software completo (ex.: jogo Snake) do zero
- Demonstra que papéis especializados melhoram qualidade

## Limitações
- Rígido: sequência fixa de papéis
- Alto custo (8+ LLM calls por iteração)
- Só funciona para domínios com SOPs bem definidos

## Relação com a Especialização
**Referência para ETHAGT09 e ETHAGT10**. MetaGPT é o exemplo mais conhecido de topologia Hierarchical com papéis especializados. Laboratório de ETHAGT10 implementa versão simplificada.
