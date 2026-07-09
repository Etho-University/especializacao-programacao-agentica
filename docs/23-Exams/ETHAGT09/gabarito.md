---
password: Etho-Prof-2026
---
# ETHAGT09 — Gabarito da Prova
> Restrito a mentores.

## Parte 1 — Conceitos

**1.** **(a)** Correta. Broadcast = um emissor alcança todos; p2p = comunicação direta 1↔1; pub/sub = desacoplamento via tópicos (inscrição). — *Ref.: Apostila, Cap. 1 — O espectro da comunicação A2A (§1.2 taxonomia).*

**2.** **Falso.** Actor model evita locks: concorrência via troca de mensagens e estado encapsulado. Compartilhar estado exige locks (lentidão, deadlocks). Em cargas distribuídas/paralelas o actor model costuma ser mais rápido e escalável; perde em casos de estado muito compartilhado e mutável. — *Ref.: Cap. 4 — Actor Model (§4.4 "Actor model é mais lento?").*

**3.** **(a)** Correta. Handoff transfere controle + contexto ativo para outro agente; o supervisor roteia como tool calls mantendo posse do fluxo. — *Ref.: Cap. 2 — Padrões de conversação (§2.3 Handoff; §2.4 Supervisor vs handoff vs group chat).*

**4.** **Falso.** No blackboard, especialistas só precisam conhecer o *espaço compartilhado*, não uns aos outros — esse desacoplamento é a vantagem central do padrão. — *Ref.: Cap. 3 — Blackboard (§3.1, §3.3).*

## Parte 2 — Aplicação e trade-off

**5.** Critérios para preferir **blackboard**: (i) problema dinâmico, com contribuições de especialistas que não se conhecem a priori; (ii) muitos produtores/consumidores e baixo acoplamento desejado; (iii) necessidade de estado compartilhado consultável. Prefira **mensagens diretas** quando: fluxo conhecido, baixa latência ponto-a-ponto, poucos agentes com acoplamento explícito. — *Ref.: Cap. 3 (§3.2 Quando o blackboard brilha; §3.3).*

**6.** Causas: (i) falta de condição de parada/termination no seletor ou agente; (ii) ausência de estado de progresso (agentes não sabem que a tarefa acabou). Correções: definir critério de *termination* explícito (ex.: mensagem `FINAL` ou max_turns); usar seletor que detecta repetição/estagnação e força convergência. — *Ref.: Cap. 2 — Padrões de conversação (§2.2 Group chat); Cap. 5 — Negociação (§5.4 Convergência e deadlock).*

**7.** Propriedades: (i) **encapsulamento de estado** (cada actor é isolado, sem memória compartilhada); (ii) **localização transparente** (mensagens a actors locais ou remotos são idênticas → escala natural). Trade-off: overhead de mensagens e modelagem mental mais complexa; latência em coordenação fina. — *Ref.: Cap. 4 — Actor Model (§4.1, §4.2, §4.3).*

**8.** Estratégias: (i) **concessão monotônica** (cada parte cede a cada rodada até zona de acordo); (ii) **BATNA/limite de reserva** conhecido + número máximo de rounds, após o qual aceita-se melhor oferta ou arbitragem. Combinar com *timeouts* e, se necessário, um *mediator*. — *Ref.: Cap. 5 — Negociação e conflito (§5.2 Bargaining/auction; §5.4).*

## Parte 3 — Projeto curto

**9.** Exemplo mínimo:
```json
{
  "version": "1.0",
  "from": "agent://researcher",
  "to": "agent://critic",
  "type": "review_request",
  "payload": { "claim_id": "c-42", "content": "..." }
}
```
O campo `version` permite evolução do protocolo sem quebrar consumidores antigos. — *Ref.: Cap. 1 — O espectro da comunicação A2A (§1.3 Schemas de mensagem).*

**10.** MCP expõe tools/resources/prompts *para um agente* (client↔servidor); A2A orquestra *comunicação entre agentes*. São complementares: cada agente usa MCP para acessar capacidades, e A2A para coordenar com outros. Exemplo: um agente "pesquisador" (MCP: tool de busca) conversa via A2A com um agente "crítico" (MCP: tool de scoring). — *Ref.: Cap. 6 — Protocolos e padrões emergentes (§6.1 A2A; §6.2 MCP vs A2A).*

---

## Erros comuns (parcial/dedução)

- **Q1**: confundir pub/sub com p2p → deduzir metade; marcar (c) mostra visão invertida do broadcast.
- **Q2**: responder "verdadeiro" citando só overhead de mensagens, ignorando custo dos locks e paralelismo → deduzir 50%.
- **Q3**: confundir handoff com delegação reversa (worker devolve ao supervisor) → metade.
- **Q5/Q8**: listar critérios genéricos sem citar convergência/deadlock/limite de reserva → até -40%.
- **Q9**: schema sem `version` → -50% (não atende o enunciado).
- **Q10**: dizer que MCP e A2A "fazem a mesma coisa" → anular (mostra não entendimento da complementaridade).

Crédito parcial: justificativa certa com escolha errada vale até 50% se o raciocínio estiver coerente.

---

## Rubrica por questão (pts)

| Q | Tipo | pts | Aceita parcial |
|---|---|---|---|
| 1 | Múltipla escolha | 10 | 0 |
| 2 | V/F justificado | 10 | 5 se V/F certo, justificativa errada |
| 3 | Múltipla escolha | 10 | 0 |
| 4 | V/F justificado | 10 | 5 |
| 5 | Trade-off (3 critérios) | 10 | 3 pts por critério válido |
| 6 | Debug (2+2) | 10 | 2,5 por item válido |
| 7 | Análise (2+1) | 10 | propriedade/trade-off válidos |
| 8 | Trade-off (2 estratégias) | 10 | 5 por estratégia concreta |
| 9 | Projeto (schema) | 10 | 5 se faltar `version` |
| 10 | Projeto (MCP vs A2A) | 10 | 5 se não der exemplo de uso conjunto |

---

## Nota esperada por perfil

- **5,0**: justifica trade-offs com propriedade, vê quando cada padrão brilha e cita falhas concretas.
- **4,0**: aplica conceitos corretos, justificativas boas com pequenas imprecisões.
- **3,0**: conhece definições mas não diferencia padrões na prática.
- **<3,0**: confunde handoff/supervisor, blackboard/p2p, ou afirma mito do actor model.
