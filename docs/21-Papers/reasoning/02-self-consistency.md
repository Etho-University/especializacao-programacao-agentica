# Self-Consistency Improves Chain of Thought Reasoning in Language Models

> **Autores**: Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V. Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, Denny Zhou  
> **Venue/Ano**: ICLR 2023 · arXiv:2203.11171  
> **URL**: https://arxiv.org/abs/2203.11171

## TL;DR
Self-Consistency amostra múltiplas cadeias de CoT para a mesma pergunta e seleciona a resposta mais frequente (majority voting), melhorando robustez.

## Contribuições
- Técnica simples que melhora CoT sem treinamento adicional
- Voting sobre múltiplos caminhos de raciocínio
- Demonstra que caminhos diferentes podem levar à mesma resposta correta

## Método
Gerar N cadeias CoT (com temperature > 0) → extrair respostas finais → majority voting (ou weighted by log-prob). Pode ser combinado com outras técnicas.

## Resultados
- GSM8K: 74% (CoT) → 84% (SC) com GPT-3
- Melhora consistente em 8+ datasets de raciocínio
- Efetivo mesmo com temperature zero (amostragem via diferentes prompts)

## Limitações
- Custo N× maior que CoT simples
- Não funciona quando a maioria erra consistentemente
- Voting cego (não pondera qualidade do raciocínio)

## Relação com a Especialização
**Referência para ETHAGT04**. Self-Consistency é técnica de ensemble aplicada a reasoning. Usada como baseline nos labs de ETHAGT04. Princípio de "múltiplos caminhos" reaparece em ToT e LATS.
