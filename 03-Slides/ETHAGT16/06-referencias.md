# ETHAGT16 — Referências

> Todas as fontes utilizadas na preparação e apresentação da aula.

---

## Canônicas (fundação da aula)

### 1. Generative Agents: Interactive Simulacra of Human Behavior
- **Autores**: Joon Sung Park, Joseph C. O'Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, Michael S. Bernstein
- **Venue**: UIST 2023
- **arXiv**: 2304.03442
- **Resumo**: 25 agentes LLM habitam Smallville, um mundo virtual. Cada agente tem perfil, rotina, memory stream com retrieval (recência + relevância + importância), reflection e planning. Emergência: agentes organizam sozinhos a festa de Valentine's Day. Caso canônico de simulação social.
- **Importância**: Canônica
- **Slides que referenciam**: 5, 6, 12, 17, 18, 19, 20, 47, 49

### 2. The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery
- **Autores**: Chris Lu, Liam Cooke, Jingyi Chang, Adam D. Lelkes, Yulong Cui, Qiyang Zhang, Stanislas Polu, Sukriti Arora, Sam G. Rodriques, Yoni Friedman, Sang Michael Xie, Yifan Wu, Eran Yahav, Jack Horton, Daniel Israel, Bill Yuchen Lin, Claude J. St. James, Abhi Venkatesh, Minhui Wu, Isaiah Onyewuchi, Arjun K. Suse, János Kramár, Tegan Maharaj, Cong Lu, Shahbulag Matiana, Arnu Pretorius, Edward Grefenstette, Yujia Li, Xuechen Li, Jakob N. Foerster, Niki Hammond, Harvey Wang, Clive M. O. R. Jones, Brooks Paige, Mohamed Elhoseiny, Simon Shao, Zhe Niu, Yifan Mai, Aram H. Markosyan, Sung Min Park, Robert Tjarko Lange, Sebastian Borgeaud, Mikel Artetxe, Robert Verkuil, Archit T. V. Sharma, Masahiro Suzuki, Surya G. K. Pillai, Pietro Lesci, Andrew A. Wang, Andrea Schioppa, Paul K. Rubinstein, Aron Szepeshazi, Antoine Bosselut, Kunhao Zheng, Roald M. van Nispen, Frank F. Xu, Jiaxin Wen, Kirthi Padmanabhan, Antoine C. R. Assran, Berkan M. M. Demir, Lisa Schut, Zachary Eaton-Rosen, T. Ben Thompson, Darshan H. E. C. C. B. H. Cai, S. Nicholas R. T. Parody, Eric Wang, David L. D. Wolpert, Douglas S. Reed, Max Bartolo, Lewis L. S. D. L. S. H. G. S. Yamada, Quentin Carbonneaux, David M. D. Park, Jingwei Zhang, John C. S. Lai, Nicholas L. R. Q. A. J. P. Lequieu, William R. H. A. T. R. Lai, Hunter Lee, Michael R. V. G. L. Robertson, Paul J. Voss, M. A. A. P. Bertinetto, Jakub M. W. M. Adamek, Nicholas M. M. M. M. M. A. T. W. D. K. Maeda, Justin M. B. R. J. N. Blasiak, Anton A. A. O. N. Bock, William H. G. A. W. A. D. Lee, Junhao L. L. M. R. Z. Wang, Nicholas M. D. K. A. C. R. L. A. Polaczyk, Dani A. K. S. A. N. Widmer, David L. A. C. N. Arimitsu, Yoshiki Y. R. N. T. Matsui, Naoki N. N. O. A. D. Williams, Satish N. B. K. Ember, Tom N. N. N. Lu, Cong Lu (Sakana AI et al.)
- **Data**: agosto 2024
- **arXiv**: 2408.06292
- **Resumo**: Sistema end-to-end que conduz pesquisa de ML: ideação → literatura → código → experimento → paper. Review automático como reviewer. Custo ~$15/paper. Papers aceitos em workshop ICLR. Fronteira de pesquisa autônoma.
- **Importância**: Canônica
- **Slides que referenciam**: 5, 6, 24, 25, 26, 27, 32, 33, 43, 44, 46, 49

### 3. AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors
- **Autores**: Weize Chen, Yusheng Su, Jingwei Zuo, Cheng Yang, Chenfei Yuan, Chi-Min Chan, Heyang Yu, Yaxi Lu, Yi-Hsin Chuang, Chen Qian, Yujia Qin, Xin Cong, Zhong Zhang, Xiezhi Wang, Ruobing Xie, Zhiyuan Liu, Mingxuan Wang, Jie Zhou, Maosong Sun
- **arXiv**: 2308.10848
- **Resumo**: Framework multi-agente com papéis flexíveis para tarefas colaborativas. Base para multi-agent research labs.
- **Importância**: Canônica
- **Slides que referenciam**: 12, 29

---

## Importantes (complementam e aprofundam)

### 4. DeepMind — AlphaEvolve
- **Fonte**: DeepMind (Google), 2024
- **Resumo**: Evolução de algoritmos via LLM + avaliação automática. LLM propõe mutações em código → avaliador testa → mantém melhores. Descobriu novo algoritmo de multiplicação de matrizes. Caso de fronteira de pesquisa autônoma.
- **Importância**: Importante
- **Slides que referenciam**: 6, 28, 43, 49

### 5. Voyager: An Open-Ended Embodied Agent with Large Language Models
- **Autores**: Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaofei Xiao, Yuke Zhu, Linxi Fan, Anima Anandkumar
- **arXiv**: 2305.16291
- **Resumo**: Agente que aprende e acumula skills automaticamente em Minecraft. Referência de auto-skills que sustenta sociedades de agentes adaptativas.
- **Importância**: Importante
- **Slides que referenciam**: 35

### 6. ChatArena
- **Resumo**: Ambientes de jogo e diálogo multi-agente para simulações sociais leves.
- **Importância**: Importante
- **Slides que referenciam**: 12

### 7. MetaGPT
- **Autores**: Sirui Hong et al.
- **arXiv**: 2308.00352
- **Resumo**: Framework multi-agente que codifica SOPs (Standard Operating Procedures) de equipes de software. Base de papéis fixos com normas explícitas.
- **Importância**: Importante
- **Slides que referenciam**: 9, 10

---

## Complementares (leitura opcional)

### 8. Social Simulacra: Creating Populated Prototypes for Social Computing Systems
- **Autores**: Joon Sung Park et al.
- **Resumo**: Antecessor de Generative Agents. Simulação de comunidades para design de sistemas sociais.
- **Slides que referenciam**: 17, 19

### 9. Constitutional AI
- **Autores**: Anthropic
- **Resumo**: Alinhamento de modelos via constituição. Estende-se naturalmente a sociedades de agentes.
- **Slides que referenciam**: 38

### 10. OpenAI / Anthropic — Deep Research
- **Resumo**: Ferramentas de pesquisa aprofundada baseadas em agentes. Referência comercial de autonomous research.
- **Slides que referenciam**: 24, 43

### 11. AI Alignment Literature (Christian, Gabler)
- **Resumo**: Panorama de alinhamento de valores em IA. Base teórica para alinhamento coletivo.
- **Slides que referenciam**: 38, 44

### 12. AutoGen
- **URL**: https://github.com/microsoft/autogen
- **Resumo**: Framework multi-agente da Microsoft com aplicações de pesquisa.
- **Slides que referenciam**: 29, 43

---

## Ficha de Pesquisa

- **Arquivo**: `20-Research/ETHAGT16-pesquisa.md`
- **Última consulta**: Julho 2026
- **Revalidação**: Janeiro 2027 (estado da arte evolui rápido)
