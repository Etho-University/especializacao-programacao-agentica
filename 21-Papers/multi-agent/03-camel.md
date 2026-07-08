# CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society

> **Autores**: Guohao Li, Hasan Abed Al Kader Hammoud, Hani Itani, Dmitrii Khizbullin, Bernard Ghanem  
> **Venue/Ano**: NeurIPS 2023 · arXiv:2303.17760  
> **URL**: https://arxiv.org/abs/2303.17760

## TL;DR
CAMEL propõe **Role-Playing** entre agentes (ex.: AI Assistant + AI User) que conversam autonomamente para completar tarefas, usando **inception prompting** para definir papéis.

## Contribuições
- Framework role-playing para cooperação autônoma entre agentes
- Inception prompting: um prompt define o papel, objetivo e restrições de cada agente
- Análise de emergência de comportamentos (escalada, desalinhamento)

## Método
**AI User**: dá instruções (task specifier). **AI Assistant**: executa instruções (tools + reasoning). Loop de conversa: User task → Assistant response → User feedback → ... até critério de parada.

## Resultados
- Geração de datasets sintéticos (instruction tuning)
- Cooperação entre agentes sem intervenção humana
- Demonstra riscos: agentes podem escalar objetivos (misalignment)

## Limitações
- Conversação pode loop sem progresso
- Sem memória de longo prazo
- Role-playing pode perpetuar biases

## Relação com a Especialização
**Referência para ETHAGT09**. CAMEL é precursor de AutoGen e base para comunicação multi-agente bidirecional. Padrão Negotiation Agent (`11-AgentPatterns/22-negotiation-agent.md`) inspirado em CAMEL.
