# ETHAGT04 — Referências

> Todas as fontes utilizadas na preparação e apresentação da aula.

---

## Canônicas (fundação do módulo)

### 1. Chain-of-Thought Prompting Elicits Reasoning in Large Language Models
- **Autores**: Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc V. Le, Denny Zhou
- **Venue**: NeurIPS 2022
- **arXiv**: 2201.11903
- **Resumo**: Demonstra que pedir ao LLM para "pensar passo a passo" melhora drasticamente o raciocínio em aritmética, senso comum e raciocínio simbólico. Fundamento de todo o campo de prompt-based reasoning. Base direta da Seção B.
- **Importância**: Canônica
- **Slides que referenciam**: 12, 13, 14, 85, 88

### 2. Tree of Thoughts: Deliberate Problem Solving with Large Language Models
- **Autores**: Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, Karpathy
- **Venue**: NeurIPS 2023
- **arXiv**: 2305.10601
- **Resumo**: Generaliza CoT para uma árvore de estados de pensamento, com avaliação e busca (BFS/DFS). Permite backtracking. Estado da arte em Creative Writing, Mini Crosswords, 24-game. Fundamento da Seção D.
- **Importância**: Canônica
- **Slides que referenciam**: 9, 32, 33, 34, 35, 36, 88

### 3. Reflexion: Language Agents with Verbal Reinforcement Learning
- **Autores**: Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao
- **Venue**: NeurIPS 2023
- **arXiv**: 2303.11366
- **Resumo**: Adiciona auto-crítica verbal e memória episódica de reflexões ao loop do agente. Atinge SOTA em HumanEval, AlfWorld, HotpotQA sem fine-tuning. "Reinforcement learning verbal". Base da Seção E.
- **Importância**: Canônica
- **Slides que referenciam**: 46, 47, 48, 49, 50, 51, 52, 88

### 4. Language Agent Tree Search Unifies Reasoning, Acting and Planning in Language Models
- **Autores**: Andy Zhou, Kai Yan, Michal Shlapentokh-Rothman, Haohan Wang, Yu-Xiong Wang
- **Venue**: NeurIPS 2024
- **arXiv**: 2310.01757
- **Resumo**: Combina MCTS (Monte Carlo Tree Search) com LLM como política, valor e recompensa. Integra Reflexion como memória. SOTA em HotpotQA, BlocksWorld, WebShop. Base da Seção D (LATS).
- **Importância**: Canônica
- **Slides que referenciam**: 36, 37, 38, 39, 40, 41, 88

### 5. Self-Consistency Improves Chain of Thought Reasoning in Language Models
- **Autores**: Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V. Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, Denny Zhou
- **Venue**: ICLR 2023
- **arXiv**: 2203.11171
- **Resumo**: Amostra múltiplas cadeias de pensamento e escolhe a resposta majoritária. Melhora CoT sem custo de prompt engineering. Base do Slide 15.
- **Importância**: Canônica
- **Slides que referenciam**: 14, 15, 88

---

## Importantes (complementam e aprofundam)

### 6. Self-Discover: Large Language Models Self-Compose Reasoning Structures
- **Autores**: Pei Zhou, Jay Pujara, Xiang Ren, Xinyun Chen, Heng-Tze Cheng, Quoc V. Le, Ed Chi, Denny Zhou, Swaroop Mishra, Huaixiu Steven Zheng
- **Venue**: ICML 2024
- **arXiv**: 2402.03620
- **Resumo**: O LLM descobre e compõe sua própria estrutura de raciocínio a partir de primitivas (CoT, decomposição, pensamento crítico). Transfere entre modelos. Base da Seção F.
- **Importância**: Importante
- **Slides que referenciam**: 56, 57, 58, 59, 60, 61, 88

### 7. ReWOO: Reasoning with Outlines Improves LLM-Based Multi-Agent Systems
- **Autores**: Binfeng Xu, Zhiyuan Peng, Bowen Lei, Subhabrata Mukherjee, Yuchen Liu, Di Xu
- **arXiv**: 2305.18323
- **Resumo**: Separa planejamento (plano com variáveis de evidência) de execução. Reduz chamadas de LLM e tokens. Fundamento da Seção C (ReWOO).
- **Importância**: Importante
- **Slides que referenciam**: 22, 23, 24, 25, 26, 88

### 8. OpenAI — Learning to Reason with LLMs (o1 launch)
- **Data**: setembro 2024
- **URL**: https://openai.com/index/learning-to-reason-with-llms/
- **Resumo**: Introduz modelos o1 treinados com RL para raciocínio interno (chain-of-thought oculto). Redefine quando usar reasoning promptado vs nativo. Base da Seção G.
- **Importância**: Importante
- **Slides que referenciam**: 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 88

### 9. Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models
- **Autores**: Lei Wang, Jiacheng Ye, Yuning Jiang, Siheng Yan, Barlas Oguz, Yashar Mehdad, Wen-tau Yih, Xin Eric Wang
- **Venue**: ACL 2023
- **arXiv**: 2305.04091
- **Resumo**: Generaliza CoT pedindo ao modelo para primeiro formular um plano e depois executá-lo. Conexão entre CoT e Plan-and-Execute. Base do Slide 19-20.
- **Importância**: Importante
- **Slides que referenciam**: 19, 20, 21, 88

### 10. LLMCompiler: An Open Compiler for LLMs
- **Autores**: Sehoon Kim, Suhong Moon, Ryan Tabrizi, Nicholas Lee, Michael W. Mahoney, Kurt Keutzer, Amir Gholami
- **arXiv**: 2312.04511
- **Resumo**: Paraleliza chamadas de ferramentas independentes, reduzindo latência e custo. Inspirador para ReWOO e execução paralela. Base do Slide 26.
- **Importância**: Importante
- **Slides que referenciam**: 26, 27, 88

### 11. ReAct: Synergizing Reasoning and Acting in Language Models
- **Autores**: Shunyu Yao et al.
- **Venue**: ICLR 2023
- **arXiv**: 2210.03629
- **Resumo**: Padrão Thought/Action/Observation em loop. Fundamento de ETHAGT01 e base para comparação em ETHAGT04.
- **Importância**: Importante (pré-requisito)
- **Slides que referenciam**: 8, 17, 18, 46

### 12. SWE-agent: Agent-Computer Interactions Enable Software Engineering
- **Autores**: John Yang, Carlos Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press
- **arXiv**: 2405.15793
- **Resumo**: Agente que resolve issues reais do GitHub usando LATS/Reflexion com ACI otimizada. Caso de estudo.
- **Importância**: Importante
- **Slides que referenciam**: 42, 83

---

## Complementares (leitura opcional)

### 13. LangGraph — Examples
- **URL**: https://github.com/langchain-ai/langgraph
- **Resumo**: Implementações de referência: `plan-and-execute.ipynb`, `lats/lats.ipynb`, `reflexion/reflexion.ipynb`, `self-discover/`, `rewoo/`.
- **Slides que referenciam**: 21, 38, 48, 58

### 14. Karpathy, A. — "Thinking clearly"
- **Resumo**: Palestra sobre como modelos raciocinam e os limites do CoT promptado.
- **Slides que referenciam**: 14, 72

### 15. Anthropic — Extended Thinking (Claude)
- **URL**: https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking
- **Resumo**: Documentação de extended thinking nativo no Claude. Base da Seção G.
- **Slides que referenciam**: 65, 66, 72

### 16. Anthropic — Interpretability of Reasoning
- **Resumo**: Pesquisa sobre como entender o raciocínio interno de modelos. Fronteira.
- **Slides que referenciam**: 72, 88

### 17. GAIA: A Benchmark for General AI Assistants
- **Autores**: Grégoire Mialon et al.
- **arXiv**: 2311.12983
- **Resumo**: Benchmark de assistentes gerais multi-step. Base do projeto do módulo.
- **Slides que referenciam**: 87

---

## Ficha de Pesquisa

- **Arquivo**: `20-Research/ETHAGT04-pesquisa.md`
- **Última consulta**: Julho 2026
- **Revalidação**: Janeiro 2027 (estado da arte evolui rápido, especialmente em reasoning models nativos)
