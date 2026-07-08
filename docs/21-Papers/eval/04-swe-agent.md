# SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

> **Autores**: John Yang, Carlos E. Jimenez, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan  
> **Venue/Ano**: NeurIPS 2024 · arXiv:2405.15793  
> **URL**: https://arxiv.org/abs/2405.15793

## TL;DR
SWE-agent introduz o conceito de **Agent-Computer Interface (ACI)**: a interface entre o agente e o ambiente (terminal, editor) precisa ser desenhada com tanto cuidado quanto HCI.

## Contribuições
- Conceito de ACI: a interface agente-ferramenta merece design dedicado
- SWE-agent: agente que navega repositórios, edita arquivos e executa testes
- Demonstra que design de ACI impacta mais que o modelo base

## Método
**ACI Design**: comandos especializados (view, edit, search, run) com feedback rico. **Agent Loop**: ReAct com ACI otimizada. Ambiente: container Docker com repositório + ferramentas de linha de comando.

## Resultados
- SWE-bench: 12.5% (GPT-4) → ~30% (com ACI otimizada) → 49% (Claude + ACI)
- Princípio ACI generalizável para outros domínios
- Código aberto (MIT)

## Limitações
- ACI é específica para software engineering
- Não aborda segurança (agente executa comandos arbitrários)
- Avaliação só em SWE-bench

## Relação com a Especialização
**Referência para ETHAGT02 e ETHAGT08**. O conceito de ACI é central para design de tools e MCP. Guia MCP (`14-MCP/04-building-servers.md`) detalha princípios ACI para design de tools. Lab 2 de ETHAGT02 projeta ACI.
