# Caso de Estudo — Voyager e AI Scientist: a fronteira da meta-agência

> ETHAGT15 · Os dois casos canônicos de sistemas autoaprendentes.

## Voyager (Wang et al., NVIDIA, arXiv:2305.16291)

Agente que aprende skills no **Minecraft** automaticamente:

1. **Explora** ambiente (via código).
2. **Descobre** sequências úteis de ações.
3. **Codifica** como skills reutilizáveis (em código Python).
4. **Acumula** biblioteca crescente.
5. **Compõe** skills complexos a partir de simples.

**Resultado**: sem intervenção humana, atinge milestones do jogo. Demonstração de **auto-skilling** em ambiente estruturado.

## AI Scientist (Sakana AI, Lu et al., arXiv:2408.06292)

Sistema que conduz pesquisa científica automaticamente:

1. **Lê** papers da área.
2. **Gera** hipóteses.
3. **Escreve** código para testar.
4. **Roda** experimentos.
5. **Escreve** paper completo (com revisão humana).

**Resultado**: alguns papers com qualidade aceitável (com caveats sobre originalidade). Demonstração de meta-agência em pesquisa científica.

## Lições para a Especialização

1. **Auto-skilling é viável** em ambientes estruturados (Voyager).
2. **Pesquisa automatizada** é possível mas com limites éticos e de qualidade (AI Scientist).
3. **Biblioteca de skills cresce composicionalmente** — capacidades emergem.
4. **Sem governança**, esses sistemas produzem baixa qualidade ou conclusões erradas — HITL é essencial.

## Aplicação prática na Etho

- Agentes de operações que aprendem rotinas úteis (estilo Voyager, em domínio Etho).
- Sistemas de pesquisa interna (estilo AI Scientist, base do Capstone).
- Meta-agentes para otimizar o próprio repositório da Universidade Etho.

## Referências

- Wang, G. et al. *Voyager: An Open-Ended Embodied Agent with LLMs*. arXiv:2305.16291. 2023.
- Lu, C. et al. *The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery*. arXiv:2408.06292. Sakana AI. 2024.
