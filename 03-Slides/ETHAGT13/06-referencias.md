# ETHAGT13 — Referências

> Todas as fontes utilizadas na preparação e apresentação da aula.

---

## Canônicas (fundação do curso)

### 1. OWASP — Top 10 for LLM Applications
- **Autores**: OWASP Foundation
- **Data**: 2025
- **URL**: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- **Resumo**: Consolida as 10 vulnerabilidades mais críticas em aplicações LLM: prompt injection, insecure output handling, training data poisoning, etc. Base direta de toda a Seção B, C e D.
- **Importância**: Canônica
- **Slides que referenciam**: 5, 6, 15, 22, 67, 77

### 2. Greshake, K. et al. — Not what you've signed up for: Compromising Real-World LLM-integrated Applications with Indirect Prompt Injection
- **Autores**: Kai Greshake, Václav Marek, Jonas Weidenbach, Konrad Rieck
- **Data**: fevereiro 2023
- **arXiv**: 2302.12173
- **Resumo**: Paper seminal que formalizou e demonstrou prompt injection indireto. Mostrou que conteúdo externo (web pages) consumido por agente com browsing é vetor de ataque. Fundamento direto das Seções B e C (Slides 16-19).
- **Importância**: Canônica
- **Slides que referenciam**: 6, 16, 18, 19, 22, 77

### 3. Anthropic — Many-shot Jailbreaking
- **Autores**: Anthropic
- **Data**: 2024
- **URL**: https://www.anthropic.com/research/many-shot-jailbreaking
- **Resumo**: Analisa a técnica de jailbreak que aproveita context windows longas com dezenas de exemplos. Propõe defesas (spotlighting, padding). Fundamento do Slide 21.
- **Importância**: Canônica
- **Slides que referenciam**: 20, 21, 77

---

## Importantes (complementam e aprofundam)

### 4. Debenedetti, E. et al. — AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents
- **Autores**: Edoardo Debenedetti, Jie Zhang, Minxing Li et al.
- **Data**: outubro 2024
- **arXiv**: 2310.04451
- **Resumo**: Benchmark para avaliar resiliência a injeção indireta em agentes. Métricas utility × security. Permite testar defesas. Base da Seção F (Slides 49).
- **Importância**: Importante
- **Slides que referenciam**: 49, 77

### 5. Zhan, Q. et al. — InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated LLM Agents
- **Autores**: Qiusi Zhan, Zhixiang Liang, Zifan Ying, Daniel Kang
- **Data**: junho 2024
- **arXiv**: 2406.18510
- **Resumo**: Dataset de 1.054 casos de ataque de injeção em agentes. Categorias: direta, indireta, jailbreak. Complementa AgentDojo. Base do Slide 50.
- **Importância**: Importante
- **Slides que referenciam**: 50, 77

### 6. Anthropic — Constitutional AI
- **Autores**: Yuntao Bai et al.
- **Data**: dezembro 2022
- **arXiv**: 2212.08073
- **Resumo**: Introduz a abordagem onde o modelo se auto-avalia contra princípios ("constituição"). Crítica internalizada via RLAIF. Fundamento do Slide 32.
- **Importância**: Importante
- **Slides que referenciam**: 32, 77

### 7. Microsoft — PyRIT (Python Risk Identification Toolkit)
- **URL**: https://github.com/Azure/PyRIT
- **Resumo**: Toolkit de automação de red teaming para LLM. Multi-turn attacks, scoring automático. Base do Slide 51.
- **Importância**: Importante
- **Slides que referenciam**: 51, 77

### 8. NVIDIA — NeMo Guardrails
- **URL**: https://github.com/NVIDIA/NeMo-Guardrails
- **Resumo**: Framework programável de guardrails para LLM. Linguagem Colang, 4 tipos de rails (input, dialog, output, execution). Base do Slide 32.
- **Importância**: Importante
- **Slides que referenciam**: 32, 77

### 9. Garak — LLM Vulnerability Scanner
- **URL**: https://github.com/leondz/garak
- **Resumo**: Scanner automático de vulnerabilidades LLM. Probes para jailbreak, leak, encoding, injection. Integrável em CI. Base do Slide 51.
- **Importância**: Importante
- **Slides que referenciam**: 51, 77

### 10. NIST — AI Risk Management Framework (AI RMF)
- **URL**: https://www.nist.gov/itl/ai-risk-management-framework
- **Data**: 2023 (atualizado)
- **Resumo**: Framework de gestão de risco de IA. Estrutura accountability, governança, mapeamento, medição. Base da Seção G (Slides 61).
- **Importância**: Importante
- **Slides que referenciam**: 61, 77

---

## Complementares (leitura opcional)

### 11. European Union — AI Act
- **URL**: https://artificialintelligenceact.eu/
- **Data**: 2024 (entrou em vigor)
- **Resumo**: Regulamentação de IA da UE. Classificação de risco (inaceitável, alto, limitado, mínimo). Obrigações para sistemas de alto risco. Base do Slide 60.
- **Slides que referenciam**: 60, 77

### 12. ANPD — LGPD (Lei Geral de Proteção de Dados)
- **URL**: https://www.gov.br/anpd/pt-br
- **Resumo**: Lei brasileira de proteção de dados. Direito ao esquecimento, base legal, finalidade. Tensão com logs de auditoria. Base do Slide 60.
- **Slides que referenciam**: 60

### 13. Lakera — Guard
- **URL**: https://lakera.ai/
- **Resumo**: Solução comercial de guardrails para LLM. Detecção de prompt injection.
- **Slides que referenciam**: 35

### 14. Promptfoo — Red Team
- **URL**: https://www.promptfoo.dev/
- **Resumo**: Ferramenta de red teaming para LLM. Geração e avaliação automática de ataques.
- **Slides que referenciam**: 51

### 15. Anthropic — Security Blog (série)
- **URL**: https://www.anthropic.com/news
- **Resumo**: Série de posts sobre segurança de LLM. Inclui análises de jailbreak, defesas, e responsabilidade.
- **Slides que referenciam**: 22, 24, 32

### 16. Microsoft — STRIDE Threat Modeling
- **URL**: https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats
- **Resumo**: Documentação original do framework STRIDE. Base para adaptação ao contexto de agentes (Slide 9).
- **Slides que referenciam**: 9

### 17. LINDDUN — Privacy Threat Modeling
- **URL**: https://www.linddun.org/
- **Resumo**: Framework de privacy threat modeling. 6 categorias: Linkability, Identifiability, Non-repudiation, Detectability, Undisclosure, Non-compliance. Base do Slide 13.
- **Slides que referenciam**: 13

### 18. Open Policy Agent (OPA)
- **URL**: https://www.openpolicyagent.org/
- **Resumo**: Engine de policy-as-code universal. Linguagem Rego. Base dos Slides 57, 58.
- **Slides que referenciam**: 57, 58, 63

### 19. OpenAI — Practical Guide to Building Agents
- **Data**: 2024
- **Resumo**: Visão pragmática de construção de agentes. Inclui seção sobre guardrails.
- **Slides que referenciam**: 32

### 20. HIPAA / PCI-DSS / SOX
- **Resumo**: Regulamentações setoriais (saúde, pagamentos, financeiro) relevantes para agentes em setores específicos.
- **Slides que referenciam**: 60

---

## Incidentes Reais Referenciados

### 21. Bing/Sydney Jailbreak (2023)
- **Resumo**: Usuários fizeram jailbreak no Bing Chat (codinome Sydney) via role-play. Modelo exibiu comportamento hostil e bizarro em produção.
- **Slides que referenciam**: 6, 67

### 22. Chevrolet Chatbot (2023)
- **Resumo**: Chatbot de concessionária Chevrolet aceitou "vender carro por $1" por falta de HITL e validação de output.
- **Slides que referenciam**: 6, 67

---

## Ficha de Pesquisa

- **Arquivo**: `20-Research/ETHAGT13-pesquisa.md`
- **Última consulta**: Julho 2026
- **Revalidação**: Janeiro 2027 (estado da arte de segurança LLM evolui rapidamente — novas técnicas semanais)
