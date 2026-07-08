# τ-bench: A Benchmark for Tool-Agent-User Interaction

> **Autores**: Yao et al.  
> **Venue/Ano**: arXiv, Abril 2024 · arXiv:2404.44529  
> **URL**: https://arxiv.org/abs/2404.44529

## TL;DR
τ-bench mede a qualidade de **tool use** em agentes, simulando interações agente-cliente em domínios como varejo e bancos, com métricas de sucesso, eficiência e segurança.

## Contribuições
- Benchmark focado em tool use (não raciocínio geral)
- Métricas separadas: sucesso da tarefa, eficiência (passos), segurança (violações)
- Simulação de interação agente-usuário realista

## Método
Ambientes simulados (retail, banking) com APIs documentadas. Agente deve completar tarefas de cliente (ex.: "transferir dinheiro entre contas") usando tools. Avaliação: tarefa completa? Passos mínimos? Violou regras?

## Resultados
- Modelos state-of-the-art: ~40-60% task success
- Violações de segurança comuns (agentes executam ações sem verificação)
- Eficiência: agentes usam mais passos que necessário

## Limitações
- Domínios limitados (retail, banking)
- Simulação simplificada vs interação humana real
- Ferramentas predefinidas (não testa descoberta de tools)

## Relação com a Especialização
**Benchmark de ETHAGT12 e ETHAGT13**. τ-bench é o benchmark mais relevante para tool use com segurança. Usado nos labs de ETHAGT13 (red team de tool agents). Métrica de violações é referência para guardrails.
