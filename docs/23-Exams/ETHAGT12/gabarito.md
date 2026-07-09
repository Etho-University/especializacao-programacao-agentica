---
password: Etho-Prof-2026
---
# ETHAGT12 — Gabarito da Prova
> Restrito a mentores.

## Parte 1 — Conceitos

**1.** **(b)** Correta. Traces organizam spans hierárquicos (pai→filho) com contexto/bags e causalidade; logs são eventos isolados, sem estrutura de chamadas. — *Ref.: Cap. 2 — Observabilidade (§2.1 Traces, spans e bags; §2.4 Logs vs traces).*

**2.** **Falso.** Benchmarks têm cobertura limitada, risco de overfit, distribuição diferente do uso real, ausência de integrações reais e possível contaminação. São um *sinal entre vários*, não garantia de produção. — *Ref.: Cap. 4 — Benchmarks canônicos (§4.3 limites/contaminação).*

**3.** **(c)** Não é viés canônico do LLM-as-judge. Vieses típicos: posição, verbosidade, auto-preferência (preferir o próprio modelo), autoridade. "Custo" não é um viés de julgamento inerente. — *Ref.: Cap. 3 — Avaliação automatizada (§3.1 LLM-as-judge: vieses).*

**4.** **Verdadeiro.** Sem medição prévia e pós-mudança num conjunto de regressão, não há como saber se houve regressão. "Você não mediu se não mediu." — *Ref.: Cap. 5 — O ciclo de melhoria (§5.1 Dataset crescente; §5.2 CI para agentes).*

## Parte 2 — Aplicação e trade-off

**5.** Dificuldades específicas de agentes: (i) **não-determinismo** + dependência de **ambiente externo** (tools, web) que muda entre runs; (ii) tarefas **multi-step** onde o caminho importa, não só o resultado; (iii) **custo de runs** (cada execução consome tokens/tools), inviabilizando muita amostragem. — *Ref.: Cap. 1 — Por que agentes são difíceis de avaliar (§1.2 Três fontes de dificuldade).*

**6.** Causas: (i) o judge não tem acesso às **ground-truth facts** e se deixa levar à fluência; (ii) viés de verbosidade/autoridade. Mitigações: fornecer rubrica explícita + referências ao judge; usar *pairwise* com posição aleatorizada; calibrar com golden cases humanos; cross-model judge. — *Ref.: Cap. 3 (§3.1 vieses e mitigações).*

**7.** Métricas de **tarefa**: medem o resultado final (success rate, partial credit, custo/latência). Métricas de **processo**: medem *como* chegou lá (steps, loops, tool misuse, factos alucinados). Ambas importam: um agente pode acertar o resultado por caminho ineficiente (custo) ou errar por loops, e o resultado sozinho esconde regressões de eficiência/segurança. — *Ref.: Cap. 3 (§3.3 Métricas de tarefa vs de processo).*

**8.** Benchmark **canônico**: quando se quer comparabilidade externa/reputação (ex.: relatório para stakeholders, alinhamento com literatura). **Custom**: quando o domínio/uso real não é coberto pelos canônicos ou o ambiente é proprietário (a maioria dos casos de produção). Ideal: um subconjunto canônico para comparabilidade + um custom para regressão do produto. — *Ref.: Cap. 4 (§4.4 SWE-bench vs benchmark custom).*

## Parte 3 — Projeto curto

**9.** Golden case exemplo:
```
input: "Cancele meu pedido #12345"
expected:
  - tool call: cancel_order(order_id="12345")
  - mensagem confirma cancelamento com motivo opcional
critério de sucesso (mensurável):
  - success se pedido #12345 marcado CANCELLED em ≤ 3 steps
    E nenhuma tool destrutiva adicional chamada
  - partial credit se confirma mas em >3 steps
  - fail se não cancela ou chama tool errada
```
Critério deve ser verificável por script ou judge rubricado. — *Ref.: Cap. 3 (§3.2 Golden cases e conjuntos de regressão).*

**10.** Sinais de contaminação: (i) o modelo "sabe" de antemão a resposta/gabarito de itens (memorização do treino); (ii) desempenho anormalmente alto em itens antigos vs novos de mesma dificuldade; (iii) coincidências textuais entre output e o gabarito público. Detecção: itens canários/templated novos; comparar performance em splits temporalmente novos; grep de strings do benchmark no corpus de treino. — *Ref.: Cap. 4 (§4.3 contaminação).*

---

## Erros comuns (parcial/dedução)

- **Q1**: igualar log e trace → anular; (a)/(c) indicam não domínio da observabilidade.
- **Q2**: crer que bom benchmark garante produção → anular (falácia central do módulo).
- **Q3**: marcar (c) como viés — aceitar (a)/(b) como NÃO-viés → anular (são os vieses típicos).
- **Q6**: culpar só o modelo sem citar rubrica/verbosidade/pairwise → até -50%.
- **Q7**: listar métricas sem distinguir tarefa (resultado) vs processo (caminho) → -40%.
- **Q9**: golden case sem critério *mensurável* (ex.: "resposta boa") → -50%.

Crédito parcial: detecção de contaminação conceitual sem exemplo de canário/temporal split vale até 60%.

---

## Rubrica por questão (pts)

| Q | Tipo | pts | Aceita parcial |
|---|---|---|---|
| 1 | Múltipla escolha | 10 | 0 |
| 2 | V/F justificado | 10 | 5 |
| 3 | Múltipla escolha | 10 | 0 |
| 4 | V/F justificado | 10 | 5 |
| 5 | Trade-off (3 motivos) | 10 | ~3 pts por motivo válido |
| 6 | Debug (2 causas + 2 mitigações) | 10 | 2,5 por item |
| 7 | Análise (tarefa vs processo) | 10 | 5 distinção + 5 justificativa "ambas" |
| 8 | Trade-off (canônico vs custom) | 10 | 5 cada, com critério |
| 9 | Projeto (golden case) | 10 | 5 estrutura + 5 critério mensurável |
| 10 | Projeto (3 sinais contaminação) | 10 | ~3 pts por sinal + detecção |

---

## Nota esperada por perfil

- **5,0**: desenha eval reproduzível, distingue tarefa/processo, mitiga vieses de judge, detecta contaminação.
- **4,0**: aplica observabilidade e golden cases com pequenas lacunas.
- **3,0**: conhece ferramentas mas confunde log vs trace ou acredita em benchmark como garantia.
- **<3,0**: aceita "parece bom"/"funcionou uma vez" como evidência.
