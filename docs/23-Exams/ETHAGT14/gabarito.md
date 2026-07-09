---
password: Etho-Prof-2026
---
# ETHAGT14 — Gabarito da Prova
> Restrito a mentores.

## Parte 1 — Conceitos

**1.** **(b)** Correta. O LLM é tipicamente o gargalo dominante: latência alta por chamada e custo crescendo com o tamanho do contexto (mais tools = mais tokens). — *Ref.: Cap. 1 — Onde agentes esbarram em escala (§1.2, §1.3).*

**2.** **Falso.** Streaming reduz a **latência percebida** (time-to-first-token), mas não a latência total (o trabalho do modelo é o mesmo). Pode até adicionar pequeno overhead. — *Ref.: Cap. 3 — Model routing e otimização (§3.3 Speculative decoding e streaming).*

**3.** **(a)** Correta. Cache semântico usa embedding para casar perguntas semanticamente equivalentes (não só strings idênticas), com um limiar de similaridade. Não é "sempre mais rápido" e serve para prompts e tool results. — *Ref.: Cap. 2 — Caching (§2.2 exact match; §2.3 Cache semântico).*

**4.** **Falso.** Stateless facilita réplica/escala, mas agentes com estado de conversa/checkpoint longo precisam de workers stateful (ou estado externalizado). A escolha depende do caso; stateful não é automaticamente pior. — *Ref.: Cap. 4 — Distribuição (§4.1; §4.5 "Stateless é sempre preferível?").*

## Parte 2 — Aplicação e trade-off

**5.** Falhas do cache semântico: (i) **falso-positivo de similaridade** — perguntas parecidas com respostas diferentes (ex.: "saldo em jan" vs "saldo em fev") casam e devolvem resposta errada; (ii) **stale** — dado subjacente mudou (cotação, status) mas o cache ainda serve o antigo. Mitigações: TTL/invalidação por evento; incorporar chaves de contexto/tempo na chave de cache; baixar limiar para itens sensíveis; verificar idempotência antes de reusar. — *Ref.: Cap. 2 — Caching (§2.5 Invalidação e consistência).*

**6.** Diagnóstico: cada tool adiciona descrição/schema ao prompt → crescimento do contexto pago em **todas** as chamadas (custo ∝ tokens de input). Correções: (a) **tool lazy-loading** — carregar só as tools relevantes via roteamento/ retrieval; (b) **reduzir/podar descrições** e schemas, e usar *tool result caching*; (c) **model routing** (modelos baratos para a maioria das chamadas). — *Ref.: Cap. 1 (§1.3); Cap. 2 (§2.4 Cache de tool results); Cap. 3 (§3.1 Roteamento).*

**7.** Medir complexidade: (i) **classificador leve** (modelo pequeno/regras/heurística) que rotula simples/difícil — risco: erro de classificação degrada qualidade; (ii) **métricas do prompt** (tamanho, nº de entidades, nº de tools envolvidas) — risco: sinais grosseiros, subestimam casos sutis. Combinar com fallback: se modelo barato falhar, escalar para o caro. — *Ref.: Cap. 3 (§3.1 Roteamento por complexidade).*

**8.** Trade-off: mais qualidade geralmente custa mais (modelo maior) e/ou mais latência (mais steps/tools). Alavanca que move custo favoravelmente: **model routing + cache** — 80% das perguntas fáceis vão para modelo barato (Haiku) com cache semântico, reduzindo custo 5-7× mantendo qualidade percebida. — *Ref.: Cap. 6 — FinOps (§6.4 Otimização e trade-offs).*

## Parte 3 — Projeto curto

**9.** Esqueleto de orçamento com circuit breaker:
```python
class Budget:
    def __init__(self, limit_usd): self.spent = 0; self.limit = limit_usd
    def charge(self, usd):
        self.spent += usd
        if self.spent > self.limit:
            raise BudgetExceeded(f"spent {self.spent} > {self.limit}")  # circuit breaker
# cada tool/LLM call chama budget.charge(custo) antes/depois; ao estourar, a execução aborta.
```
Idealmente o orçamento é por execução/usuário/tenant e monitorado com alertas. — *Ref.: Cap. 6 — FinOps (§6.2 Orçamento; §6.3 Medição granular).*

**10.** Sharding por tenant: particionar pelo `tenant_id` (cada tenant roteado a um shard/worker pool); estado persistente por tenant em armazenamento isolado (schema ou namespace por tenant, ou prefixo por tenant); cache com chaves prefixadas por tenant; tools com allowlist por tenant. Isolamento: nunca compartilhar memória/cache entre tenants, logs segregados, rate limits por tenant. — *Ref.: Cap. 4 — Distribuição (§4.2 Sharding por usuário/sessão/domínio).*

---

## Erros comuns (parcial/dedução)

- **Q1**: marcar rede/disco como gargalo → anular; o LLM é dominante (latência + custo com contexto).
- **Q2**: crer que streaming reduz latência *total* → anular (reduz só a percebida/TTFT).
- **Q3**: descrever cache semântico como "sempre mais rápido" ou só para tools → até -50%.
- **Q4**: defender "stateless sempre" sem qualificar → anular (ignora estado de conversa/checkpoint).
- **Q6**: sugerir "adicionar modelo maior" sem tocar em tool lazy-loading/poda de contexto → -50%.
- **Q9**: budget sem circuit breaker (não aborta ao estourar) → -50%.
- **Q10**: sharding sem isolamento de estado/cache por tenant → -40%.

Crédito parcial: roteamento descrito sem medir complexidade ou sem fallback vale até 60%.

---

## Rubrica por questão (pts)

| Q | Tipo | pts | Aceita parcial |
|---|---|---|---|
| 1 | Múltipla escolha | 10 | 0 |
| 2 | V/F justificado | 10 | 5 |
| 3 | Múltipla escolha | 10 | 0 |
| 4 | V/F justificado | 10 | 5 |
| 5 | Trade-off (2 falhas) | 10 | 5 por falha + mitigação |
| 6 | Debug (diagnóstico + 2 correções) | 10 | 4 diagnóstico + 3 por correção concreta |
| 7 | Análise (2 abordagens + risco) | 10 | 4 por abordagem + 2 riscos |
| 8 | Trade-off (3 eixos + alavanca) | 10 | 4 trade-off + 6 alavanca justificada |
| 9 | Projeto (budget + breaker) | 10 | 5 budget + 5 breaker que aborta |
| 10 | Projeto (sharding por tenant) | 10 | 5 particionamento + 5 isolamento |

---

## Nota esperada por perfil

- **5,0**: diagnostica gargalos, aplica cache + routing + FinOps com medição granular e justifica stateless vs stateful.
- **4,0**: aplica caching/routing com pequenas lacunas em invalidação.
- **3,0**: conhece ferramentas mas confunde latência percebida com total.
- **<3,0**: afirma que stateless é sempre melhor ou que streaming reduz latência total.
