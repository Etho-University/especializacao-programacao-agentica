# The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery

> **Autores**: Chris Lu, Cong Lu, Robert Tjarko Lange, Jakob Foerster, Jeff Clune, David Ha  
> **Venue/Ano**: Sakana AI, Agosto 2024 · arXiv:2408.06292  
> **URL**: https://arxiv.org/abs/2408.06292

## TL;DR
AI Scientist automatiza o ciclo completo de pesquisa: gerar ideia → escrever código → executar experimentos → escrever paper → revisar. Cada paper custa ~$15.

## Contribuições
- Primeiro sistema que completa o ciclo inteiro de pesquisa científica
- Template de revisão (LLM-as-judge) para avaliar papers gerados
- Demonstra viabilidade (e riscos) de pesquisa autônoma

## Método
**Idea Generation**: LLM propõe ideias baseadas em template. **Experiment**: código é gerado e executado em sandbox. **Paper Writing**: LLM escreve paper LaTeX a partir de resultados. **Review**: LLM-as-judge avalia paper como reviewer.

## Resultados
- Papers gerados que passam em revisão automatizada
- Custo: ~$15 por paper completo
- Gera variações de algoritmos existentes (MLP, transformer)

## Limitações
- Qualidade dos papers é baixa comparada a pesquisadores humanos
- Risco de geração de lixo acadêmico (papers sem contribuição real)
- Código gerado pode conter erros não detectados

## Relação com a Especialização
**Fundamento de ETHAGT15 e ETHAGT16**. AI Scientist é o exemplo máximo de meta-agente e pesquisa autônoma. Capstone ETHAGT90 é inspirado diretamente neste paper. Discussão de riscos e governança em ETHAGT13.
