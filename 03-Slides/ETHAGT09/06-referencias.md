# ETHAGT09 — Referências

> Todas as fontes utilizadas na preparação e apresentação da aula.

---

## Canônicas (fundação do módulo)

### 1. AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation
- **Autores**: Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu, Beibin Li, Erkang Zhu, Li Jiang, Xiaoyun Zhang, Shaokun Zhang, Jiale Liu, Ahmed Hassan Awadallah, Ryen W. White, Doug Burger, Chi Wang
- **Data**: outubro 2023
- **arXiv**: 2308.08155
- **Resumo**: Apresenta AutoGen — framework multi-agente baseado em conversação. Introduz GroupChat, conversational agents, selector e round-robin. Base direta da Seção C (slides 20-21) e do Lab 1.
- **Importância**: Canônica
- **Slides que referenciam**: 6, 17, 20, 21, 25, 43, 65, 71

### 2. CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society
- **Autores**: Guohao Li, Hasan Abed Al Kader Hammoud, Hani Itani, Dmitrii Khizbullin, Bernard Ghanem
- **Data**: março 2023
- **arXiv**: 2303.17760
- **Resumo**: Introduz role-playing entre dois agentes (assistente e usuário simulado) com inception prompting para manter papéis. Base do padrão two-agent dialogue (Slides 18-19).
- **Importância**: Canônica
- **Slides que referenciam**: 6, 17, 18, 19, 25, 65, 71

### 3. Hewitt — Actor Model
- **Autor**: Carl Hewitt, Peter Bishop, Richard Steiger
- **Data**: 1973
- **Venue**: AI Memo 332, MIT
- **Resumo**: Clássico que define o actor model — atores encapsulam estado, comunicam-se apenas por mensagens, processam uma por vez. Base da Seção E (slides 34-42).
- **Importância**: Canônica
- **Slides que referenciam**: 35, 36, 37, 38, 40, 65, 71

### 4. OpenAI Swarm
- **Autor**: OpenAI
- **Data**: 2024
- **URL**: https://github.com/openai/swarm
- **Resumo**: Framework experimental leve que introduz handoffs — agentes transferem controle sem orquestrador central. Base do padrão handoff (Slides 22-23) e do Lab 2.
- **Importância**: Canônica
- **Slides que referenciam**: 6, 17, 22, 23, 25, 65, 71

---

## Importantes (complementam e aprofundam)

### 5. MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework
- **Autores**: Sirui Hong, Mingchen Zhuge, Jonathan Chen, Xiawu Zheng, Yuheng Cheng, Ceyao Zhang, Jinlin Wang, Zili Wang, Steven Ka Shing Yau, Zijuan Lin, Liyang Zhou, Chenyu Ran, Lingfeng Xiao, Chenglin Wu, Jürgen Schmidhuber
- **Venue**: ICLR 2024
- **arXiv**: 2308.00352
- **Resumo**: Framework multi-agente para desenvolvimento de software usando SOPs (Standard Operating Procedures). Cada papel (PM, Architect, Engineer, QA) tem entradas, processo e saídas definidos. Base do caso de estudo (Slide 63) e do Slide 24.
- **Importância**: Importante
- **Slides que referenciam**: 6, 24, 63, 65

### 6. AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors
- **Autores**: Weize Chen, Suozhi Wang, Chenfei Yuan, Ziyan Chen, Ganqu Cui, Yujia Qin, Yusheng Su, Xin Cheng, Zhiyuan Liu, Ming Ding, Jingren Zhou, Jie Tang
- **arXiv**: 2308.10848
- **Resumo**: Framework multi-agente que facilita colaboração e explora comportamentos emergentes. Suporta recruitment dinâmico de agentes e comunicação estruturada.
- **Importância**: Importante
- **Slides que referenciam**: 6, 25

### 7. Google — A2A Protocol (Agent-to-Agent)
- **Autor**: Google
- **Data**: 2024
- **URL**: https://google.github.io/A2A/
- **Resumo**: Protocolo aberto para comunicação entre agentes de diferentes frameworks. Define Agent Card (manifesto de capacidades) e Tasks (unidade de trabalho delegável). Base da Seção G (slides 54-55, 59).
- **Importância**: Importante
- **Slides que referenciam**: 6, 54, 55, 56, 59, 71

### 8. LLM-based Multi-Agents: A Survey
- **Autores**: Taicheng Guo et al.
- **Data**: fevereiro 2024
- **arXiv**: 2402.01680
- **Resumo**: Survey sobre sistemas multi-agente baseados em LLM. Panorama de arquiteturas, proficiência, comunicação e mecanismos. Citado na contextualização.
- **Importância**: Importante
- **Slides que referenciam**: 6

### 9. Survey on LLM-based Multi-Agent Systems
- **arXiv**: 2308.00352
- **Resumo**: Survey canônico que aparece no syllabus. Panorama acadêmico de comunicação e coordenação.
- **Importância**: Importante
- **Slides que referenciam**: 6

---

## Complementares (leitura opcional)

### 10. FIPA — Foundation for Intelligent Physical Agents
- **URL**: http://www.fipa.org/
- **Resumo**: Padrões clássicos de comunicação multi-agente (FIPA-ACL, performatives). Contexto histórico para entender que LLM agents redescobrem conceitos antigos.
- **Slides que referenciam**: 58, 59

### 11. Erlang/OTP Documentation
- **URL**: https://www.erlang.org/docs
- **Resumo**: Pioneiro em actor model com tolerância a falha (supervisores). Referência para o Slide 40.
- **Slides que referenciam**: 40

### 12. Akka Documentation
- **URL**: https://doc.akka.io/
- **Resumo**: Actor system para JVM (Scala/Java). Referência para o Slide 40.
- **Slides que referenciam**: 40

### 13. LangGraph Multi-Agent Examples
- **URL**: https://github.com/langchain-ai/langgraph
- **Resumo**: Exemplos `multi_agent/` — hierarchical_agent_teams, multi-agent-collaboration. Implementação prática de supervisor, delegação e handoff.
- **Slides que referenciam**: 23, 43

### 14. CrewAI Documentation
- **URL**: https://docs.crewai.com/
- **Resumo**: Framework role-based para multi-agente. Comparação com AutoGen.
- **Slides que referenciam**: 25

---

## Ficha de Pesquisa

- **Arquivo**: `20-Research/ETHAGT09-pesquisa.md`
- **Última consulta**: Julho 2026
- **Revalidação**: Janeiro 2027 (estado da arte evolui rápido — A2A Protocol ainda é emerging spec)
