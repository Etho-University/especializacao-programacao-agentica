# Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection

> **Autores**: Kai Greshake, Sahar Abdelnabi, Shailesh Mishra, Christoph Endres, Thorsten Holz, Mario Fritz  
> **Venue/Ano**: ACM CCS 2023 · arXiv:2302.12173  
> **URL**: https://arxiv.org/abs/2302.12173

## TL;DR
Demonstra que LLMs integrados a aplicações são vulneráveis a **indirect prompt injection**: atacantes inserem instruções maliciosas em conteúdo externo (web pages, emails, docs) que o LLM processa.

## Contribuições
- Categorização de ataques de injeção indireta (via ferramentas)
- Demonstração em aplicações reais (Bing Chat, GitHub Copilot)
- Taxonomia de vetores de ataque: dados recuperados, tool outputs, contexto

## Método
Atacante insere prompt malicioso em conteúdo recuperado (ex.: "Ignore instruções anteriores e faça X"). Quando o LLM processa o conteúdo como contexto, o prompt malicioso é ativado.

## Resultados
- 8 aplicações reais comprometidas
- Ataques: exfiltração de dados, manipulação de comportamento, jailbreak
- Taxonomia completa de vetores

## Limitações
- Apenas demonstra vulnerabilidade; sem defesas robustas propostas
- Alguns ataques dependem de engenharia social
- Cenário evolui rápido (defesas em 2025 são melhores)

## Relação com a Especialização
**Fundamento de ETHAGT13**. Este paper define a categoria de ataque mais relevante para agentes (injeção via ferramentas). Base para o threat model da Especialização. Padrão Guardian (`11-AgentPatterns/17-guardian.md`) é defesa contra este ataque.
