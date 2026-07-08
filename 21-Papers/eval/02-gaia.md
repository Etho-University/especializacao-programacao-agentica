# GAIA: A Benchmark for General AI Assistants

> **Autores**: Grégoire Mialon, Clémentine Fourrier, Craig Swift, Thomas Wolf, Yann LeCun, et al.  
> **Venue/Ano**: ICLR 2024 · arXiv:2311.12983  
> **URL**: https://arxiv.org/abs/2311.12983

## TL;DR
GAIA propõe 466 perguntas que exigem **raciocínio multi-passo** com **ferramentas variadas** (web search, código, processamento de arquivos). Questões são triviais para humanos mas desafiadoras para agentes.

## Contribuições
- Benchmark de nível "humano": perguntas que humanos resolvem facilmente
- Requer composição de múltiplas ferramentas e passos
- 3 níveis de dificuldade (L1: 1 ferramenta, L2: 2+, L3: 3+)

## Método
466 perguntas (166 L1, 165 L2, 135 L3). Cada pergunta: enunciado + lista de ferramentas necessárias. Avaliação: resposta exata (string match) ou LLM-as-judge para respostas abertas.

## Resultados
- Humanos: 92% (L1), 85% (L2), 69% (L3) — média ~80%
- GPT-4 com plugins: ~30%
- Agentes com tool use: ~15-45% (dependendo do setup)
- Lacuna: agentes ainda distantes de humanos

## Limitações
- Apenas 466 questões (pode overfittar)
- Algumas questões dependem de conhecimento temporal (datas)
- Avaliação exata pode ser injusta

## Relação com a Especialização
**Benchmark principal de ETHAGT12**. GAIA testa composição de ferramentas, raciocínio multi-passo e planejamento — competências centrais da Especialização. Usado nos labs de ETHAGT12 para avaliação.
