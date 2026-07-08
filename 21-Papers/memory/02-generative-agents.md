# Generative Agents: Interactive Simulacra of Human Behavior

> **Autores**: Joon Sung Park, Joseph C. O'Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, Michael S. Bernstein  
> **Venue/Ano**: UIST 2023 · arXiv:2304.03442  
> **URL**: https://arxiv.org/abs/2304.03442

## TL;DR
25 agentes LLM simulam comportamentos humanos realistas em um mundo virtual (Smallville), com memória, reflexão, planejamento e interação social emergente.

## Contribuições
- Arquitetura de memória em 3 camadas: **Memory Stream** (todos eventos), **Reflection** (sumários de alto nível), **Plan** (ações futuras)
- Comportamento social emergente: agentes organizam festa, formam opiniões, convidam outros
- Framework para simulação de sociedades de agentes

## Método
**Memory Stream**: cada evento é armazenado com timestamp, recência, importância e relevância. **Retrieval**: relevância + recência + importância. **Reflection**: quando eventos ultrapassam threshold de importância → LLM sumariza. **Planning**: reflexões + memória → plano diário → ações.

## Resultados
- Comportamentos realistas: agentes acordam, trabalham, socializam, dormem
- Emergência: agente organiza festa sem ser programado
- Memória consistente (agentes lembram de interações passadas)

## Limitações
- Custo alto (cada agente = 1+ LLM calls por passo)
- Simulação lenta (tempo real × 5-10×)
- Validação qualitativa (sem métricas objetivas de "realismo")

## Relação com a Especialização
**Fundamento de ETHAGT05 e ETHAGT16**. Base para o módulo de sociedades de agentes. O Memory Stream inspirou o design de memória da Especialização (recência, relevância, importância). Padrão Generative Memory (`16-Memory/`).
