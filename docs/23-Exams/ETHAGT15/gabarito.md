# ETHAGT15 — Gabarito da Prova
> Restrito a mentores.

## Parte 1 — Conceitos

**1.** **(b)** Correta. Meta-agente opera *sobre* agentes: gera prompts/tools/agentes, otimiza-os ou os evolui (strategies: synthesis, evolution, optimization). — *Ref.: Cap. 1 — O que é meta-agência (§1.1, §1.3 Três estratégias).*

**2.** **Falso.** Auto-aprendizado pode introduzir drift, overfit ao histórico, memória contaminada/errada e regressões. Requer avaliação contínua, sandbox e capacidade de "esquecer". — *Ref.: Cap. 4 — Auto-aprendizado contínuo (§4.5 "sempre melhora?").*

**3.** **(a)** Correta. DSPy compila chamadas declarativas de LLM, otimizando prompts (e às vezes tools) programaticamente. — *Ref.: Cap. 3 — Otimização automatizada (§3.1 Otimização de prompts: DSPy).*

**4.** **Verdadeiro.** Goal drift = a métrica otimizada diverge do objetivo real (Goodhart); o sistema melhora o que mede mas degrada o que importa. — *Ref.: Cap. 5 — Riscos e governança (§5.2 Goal drift).*

## Parte 2 — Aplicação e trade-off

**5.** Vale otimizar automaticamente quando: (i) há **métrica de avaliação reproduzível** (golden cases/benchmark) para guiar a otimização — sem ela, é cego; (ii) o domínio é **estável e volumoso** o suficiente para o ganho amortizar o custo de otimização. Prefira manual quando o domínio muda rápido, o volume é baixo, ou a qualidade é subjetiva/difícil de medir. — *Ref.: Cap. 3 (§3.4 Quando otimizar automaticamente).*

**6.** Riscos: (i) **recursão/explosão de agentes** (overhead, custo, complexidade); (ii) **drift de qualidade** (agentes gerados pioram o sistema). Fences: (a) **meta-governor com veto** e cota de agentes gerados; (b) **validação obrigatória (eval) em sandbox** antes de qualquer deploy, com confiança incremental. — *Ref.: Cap. 5 — Riscos e governança (§5.1 Recursão; §5.3 Meta-governor e vetos; §5.4 Confiança incremental).*

**7.** Sem meta-governor, um sistema auto-evolutivo pode entrar em loops de auto-modificação, drift ou gerar agentes que contornam regras. O governor mantém invariantes de segurança (vetos), audita mudanças e força sandbox/escalada de confiança. Sem ele, falta uma entidade "fora" do loop evolutivo que freie derivas. — *Ref.: Cap. 5 (§5.3 Meta-governor e vetos; §5.5 Segurança).*

**8.** Riscos de guardar tudo: (i) **contaminação/drift** (falhas ou vieses antigos influenciam decisões); (ii) **explosão de memória/custo** e lentidão. Estratégia de esquecimento: TTL/decaimento de memórias por relevância, retenção só de sucessos *validados recentemente*, e re-avaliação periódica do que ainda faz sentido. — *Ref.: Cap. 4 — Auto-aprendizado contínuo (§4.4 Quando esquecer/drift).*

## Parte 3 — Projeto curto

**9.** Veto (regra de segurança):
```python
def meta_governor_veto(action):
    if action.target == "meta_governor" and action.kind in ("edit_code","edit_policy","edit_veto"):
        return DENY  # o governor é imutável por agentes sob sua governança
    return ALLOW
```
Princípio: o governor e suas regras de veto estão fora do conjunto editável pelos agentes que ele governa. — *Ref.: Cap. 5 (§5.3 Meta-governor e vetos; §5.5).*

**10.** Pipeline:
```
1. meta-agente lê a tarefa e gera (prompt + tools + config) do especialista.
2. especialista é executado num sandbox contra um eval daquela tarefa.
3. se eval ≥ limiar e meta-governor aprova → deploy em canary.
4. monitora; se regredir, rollback automático.
```
Confiança incremental: nada vai a produção sem eval + aprovação. — *Ref.: Cap. 2 — Geração de agentes (§2.1, §2.3 Validação do agente gerado); Cap. 5 (§5.4).*

---

## Erros comuns (parcial/dedução)

- **Q1**: confundir meta-agente com agente qualquer que use memória → anular.
- **Q2**: defender "auto-aprendizado sempre melhora" → anular (ignora drift/overfit/contaminação).
- **Q3**: confundir DSPy com orquestração/cache → anular (erro de identificação da ferramenta).
- **Q5**: recomendar otimização automática sem métrica de avaliação → -50% (otimização cega).
- **Q6**: propor fences "mais agentes" em vez de veto/quota/sandbox → até -40%.
- **Q7**: não reconhecer a necessidade de uma entidade *fora* do loop evolutivo → -50%.
- **Q9**: veto editável pelo próprio agente governado → anular (veto deve ser imutável).

Crédito parcial: pipeline (Q10) sem etapa de validação/eval antes do deploy → -40%.

---

## Rubrica por questão (pts)

| Q | Tipo | pts | Aceita parcial |
|---|---|---|---|
| 1 | Múltipla escolha | 10 | 0 |
| 2 | V/F justificado | 10 | 5 |
| 3 | Múltipla escolha | 10 | 0 |
| 4 | V/F justificado | 10 | 5 |
| 5 | Trade-off (2 critérios) | 10 | 5 por critério (métrica/volume) |
| 6 | Debug (2 riscos + 2 fences) | 10 | 2,5 por item |
| 7 | Análise (meta-governor) | 10 | 5 necessidade + 5 o que falha |
| 8 | Trade-off (2 riscos + esquec.) | 10 | 4 por risco + 2 estratégia esquecer |
| 9 | Projeto (veto) | 10 | 5 regra + 5 imutabilidade do governor |
| 10 | Projeto (pipeline 4 passos) | 10 | 2,5 por passo (gerar→validar→aprovar→deploy) |

---

## Nota esperada por perfil

- **5,0**: justifica meta-governança, detecção de drift, sandbox e confiança incremental com propriedade.
- **4,0**: aplica otimização/validação com pequenas lacunas em fences de segurança.
- **3,0**: conhece DSPy/Voyager mas trata auto-aprendizado como sempre benéfico.
- **<3,0**: aceita recursão sem governança ou não reconhece goal drift.
