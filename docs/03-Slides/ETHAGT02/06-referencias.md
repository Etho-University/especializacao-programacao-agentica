# ETHAGT02 — Referências

> Todas as fontes utilizadas na preparação e apresentação da aula.

---

## Canônicas (fundação do curso)

### 1. Anthropic — Building Effective Agents, Appendix 2 ("Prompt Engineering Your Tools")
- **Autores**: Erik Schluntz, Barry Zhang
- **Data**: dezembro 2024
- **URL**: https://www.anthropic.com/engineering/building-effective-agents
- **Resumo**: Formula a analogia ACI :: HCI e os princípios de design de tools (poka-yoke, descrições ricas, paths absolutos, formato próximo ao natural). Base direta das Seções B, C, D e E da aula.
- **Importância**: 🏛 Canônica
- **Slides que referenciam**: 6, 8, 17, 18, 19, 20, 21, 22, 25, 26, 46, 47, 57

### 2. Toolformer: Language Models Can Teach Themselves to Use Tools
- **Autores**: Tim Schick et al.
- **Venue**: NeurIPS 2023
- **arXiv**: 2302.04761
- **Resumo**: Primeira demonstração de que LLMs podem aprender tool use com treino self-supervised. Contexto histórico do mecanismo de function calling moderno. Base do Slide 8.
- **Importância**: 🏛 Canônica
- **Slides que referenciam**: 6, 8

### 3. OpenAI — Function Calling Guide e Structured Outputs
- **Data**: 2024
- **URL**: https://platform.openai.com/docs/guides/function-calling
- **Resumo**: Documentação de referência do mecanismo de function calling (tools API), structured outputs e constrained decoding via JSON Schema. Base técnica dos Slides 9, 10, 14.
- **Importância**: 🏛 Canônica
- **Slides que referenciam**: 9, 10, 11, 14

---

## Importantes (complementam e aprofundam)

### 4. Gorilla: Large Language Model Connected with Massive APIs
- **Autores**: Shishir Patil et al.
- **arXiv**: 2305.15334
- **Resumo**: Treina LLM para usar 1.700+ APIs. Mostra degradação de performance com muitas tools disponíveis — contexto direto para o trade-off "tokens de descrição vs benefício" do Slide 12.
- **Importância**: Importante
- **Slides que referenciam**: 12, 13

### 5. ToolLLM: Facilitating LLMs to Master 16000+ Real-world APIs
- **Autores**: Yujia Qin et al.
- **arXiv**: 2307.16789
- **Resumo**: Benchmark de tool use em larga escala (16k+ APIs). Referência para avaliação de tools e prepara ETHAGT12 (AgentOps).
- **Importância**: Importante
- **Slides que referenciam**: 12, 42, 43

### 6. Reflexion: Language Agents with Verbal Reinforcement Learning
- **Autores**: Noah Shinn et al.
- **Venue**: NeurIPS 2023
- **arXiv**: 2303.11366
- **Resumo**: Usa tools em loop com auto-crítica e memória de falhas. Referência para tratamento de erro em tools — quando o modelo se recupera sozinho.
- **Importância**: Importante
- **Slides que referenciam**: 30

### 7. Anthropic — Writing Effective Tools for AI Agents
- **Data**: 2025
- **URL**: https://www.anthropic.com/engineering/writing-tools-for-agents
- **Resumo**: Guia prático de design de tools (ACI), aprofundando poka-yoke, schemas e examples. Expande o Appendix 2.
- **Importância**: Importante
- **Slides que referenciam**: 18, 19, 20, 21, 46

### 8. Pydantic AI Documentation
- **URL**: https://ai.pydantic.dev/
- **Resumo**: Padrões modernos de schema/validação com Pydantic para tool definitions. Referência prática para os Slides 9, 28.
- **Importância**: Importante
- **Slides que referenciam**: 9, 28

### 9. instructor (jxnl) — Structured Outputs com Pydantic
- **URL**: https://github.com/jxnl/instructor
- **Resumo**: Biblioteca para structured outputs usando Pydantic com OpenAI/Anthropic. Referência prática para o Slide 10.
- **Importância**: Importante
- **Slides que referenciam**: 10, 28

---

## Complementares (leitura opcional)

### 10. Pat McGuinness — Design Patterns for Effective AI Agents
- **Fonte**: Substack
- **Resumo**: Reflexão prática sobre padrões de design de agentes e tools. Perspectiva de engenharia de produção.
- **Slides que referenciam**: 46, 47

### 11. Patterson, D. — Tools, not Agents
- **Resumo**: Reflexão sobre quando ferramentas (sem loop agêntico) bastam. Contraponto à complexidade.
- **Slides que referenciam**: 33

### 12. LangChain — Tool Calling Guide
- **URL**: https://python.langchain.com/docs/concepts/tool_calling/
- **Resumo**: Implementação de referência de tool calling em framework. Comparação de abordagens.
- **Slides que referenciam**: 14, 28

### 13. SWE-bench: Can Language Models Resolve Real-World GitHub Issues?
- **Autores**: Carlos Jimenez et al.
- **arXiv**: 2310.06770
- **Resumo**: Benchmark que fundamenta o caso de estudo (Anthropic coding agent, paths relativos → absolutos).
- **Importância**: Importante
- **Slides que referenciam**: 25, 48

### 14. Coda / Notion / Replit — Relatos de produção com tools
- **Resumo**: Relatos de engenharia sobre design de tools em agentes de produção.
- **Slides que referenciam**: 46, 47

---

## Ficha de Pesquisa

- **Arquivo**: `20-Research/ETHAGT02-pesquisa.md`
- **Última consulta**: Julho 2026
- **Revalidação**: Janeiro 2027 (estado da arte de tool calling evolui rápido)
