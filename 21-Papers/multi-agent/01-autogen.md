# AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation

> **Autores**: Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu, Beibin Li, Erkang Zhu, Li Jiang, Xiaoyun Zhang, Shaokun Zhang, Jiale Liu, Ahmed Awadallah, Ryen W. White, Doug Burger, Jianfeng Gao, Chi Wang  
> **Venue/Ano**: Microsoft Research, Agosto 2023 · arXiv:2308.08155  
> **URL**: https://arxiv.org/abs/2308.08155

## TL;DR
AutoGen é um framework multi-agente onde agentes conversam entre si (e com humanos) via mensagens. O desenvolvedor define papéis, ferramentas e protocolos de conversação.

## Contribuições
- Framework de agentes conversacionais assíncronos
- Suporte a HITL (human-in-the-loop) natural
- Topologias flexíveis (sequencial, group chat, hierárquico)

## Método
**Agent**: entidade que envia/recebe mensagens e executa ações (LLM, tool, human). **Conversation**: sequência de mensagens entre 2+ agentes. **GroupChat**: broadcast manager que roteia mensagens. O desenvolvedor define *assistant agent* (LLM) e *user proxy* (humano ou código).

## Resultados
- Aplicações: QA, coding, decisão, entretenimento
- Flexibilidade: mesmo framework para chatbots simples e sistemas multi-agente complexos
- Código aberto, adoção ampla (20K+ stars)

## Limitações
- Conversação pode ser ineficiente (mensagens demais)
- Sem governança de memória de longo prazo nativa
- Debugging de conversas multi-agente é difícil

## Relação com a Especialização
**Framework principal de ETHAGT09** (comunicação multi-agente). AutoGen é referência para topologias de conversação. Contrastado com topologias mais estruturadas (hierarchical, event-driven) em ETHAGT10.
