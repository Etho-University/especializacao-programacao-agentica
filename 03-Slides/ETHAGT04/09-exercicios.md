# ETHAGT04 — Exercícios

> Exercícios para aula e para casa.
> Organizados por tipo: em aula, individual, em duplas, projeto.

---

## Exercícios em Aula

### E1 — Plan-and-Execute ou ReAct? (Votação Rápida)
**Slide**: 27
**Tempo**: 2 min
**Formato**: Individual, votação de mão levantada

**Enunciado**: Para cada cenário abaixo, vote: Plan-and-Execute (P) ou ReAct (R)?

1. Planejar e executar uma migração de banco de dados com 15 passos conhecidos
2. Investigar e corrigir um bug intermitente em produção
3. Redigir um relatório trimestral coletando dados de 5 fontes
4. Debugar um teste que falha aleatoriamente
5. Provisionar infraestrutura cloud a partir de um runbook detalhado

**Gabarito**:
1. P (passos conhecidos e estruturados — planejar antes é eficiente)
2. R (debug é imprevisível, cada observação muda o próximo passo)
3. P (coleta é paralelizável e os passos são independentes — ReWOO ideal)
4. R (natureza imprevisível, depende de cada observação)
5. P (runbook = plano pré-existente; Plan-and-Execute segue o script)

---

### E2 — CoT Funciona para TUDO? (Discussão em Duplas)
**Slide**: 17
**Tempo**: 2 min
**Formato**: Duplas, 2 min discussão + 1 min compartilhar

**Enunciado**: Discutam em duplas: Chain-of-Thought melhora quase tudo. Mas para quais problemas CoT não ajuda (ou piora)?

1. Pensem em 2 tipos de problema onde CoT falha.
2. Por que falha nesses casos?

**Gabarito**:
- **Backtracking necessário**: problemas onde você precisa voltar e tentar outro caminho (xadrez, puzzles). CoT é linear — não volta.
- **Erro propagado**: se o passo 2 está errado, o passo 3-10 herdam o erro. Sem validação intermediária.
- **Espaço de busca exponencial**: problemas onde há muitos caminhos possíveis. CoT explora só um.

---

### E3 — Trade-off: Custo vs Qualidade (Duplas)
**Slide**: 77
**Tempo**: 3 min
**Formato**: Duplas, 2 min discussão + 1 min compartilhar

**Enunciado**: Você tem um benchmark de 100 problemas de raciocínio. Seu orçamento é $5. Compare:

| Técnica | Custo/problema | Accuracy esperada |
|---|---|---|
| CoT | $0.002 | 60% |
| Self-Consistency (N=10) | $0.02 | 72% |
| ToT | $0.08 | 85% |
| Reflexion (max 3 tentativas) | $0.02 | 75% |

**Perguntas**:
1. Qual técnica maximiza accuracy dentro do orçamento?
2. Se o orçamento fosse $50, mudaria?

**Gabarito**:
1. **Orçamento $5**: 100 × $0.02 = $2 com Self-Consistency (72%). Ou 100 × $0.02 = $2 com Reflexion (75%). Reflexion vence. Não dá para ToT ($8 > $5).
2. **Orçamento $50**: ToT para todos = $8 (dentro). ToT (85%) vence. Ou estratégia híbrida: ToT para os 30% mais difíceis ($0.08 × 30 = $2.40) + Self-Consistency para o resto ($0.02 × 70 = $1.40) = $3.80, potencial accuracy ~80%.

---

## Exercícios Individuais (para casa)

### E4 — Estratégia para 5 Classes de Problema
**Tempo estimado**: 15 min
**Formato**: Individual, escrito

**Enunciado**: Para cada uma das 5 classes de problema abaixo, indique a estratégia de raciocínio mais adequada e justifique em 2-3 frases:

1. **Aritmética multi-passo** (ex: "Se 3 maçãs custam $2, quanto custam 17 maçãs?")
2. **Planejamento de viagem complexo** (ex: "Roteiro de 7 dias em Tóquio com budget $2000")
3. **Resolução de issue de GitHub** (bug em código desconhecido)
4. **Análise jurídica** (determinar se um contrato viola uma cláusula)
5. **Puzzle de lógica** (ex: 24-game, zebra puzzle)

**Critério de avaliação**:
- Escolha uma técnica apropriada para cada classe ✅
- Justifica com trade-offs (custo, latência, robustez) ✅
- Reconhece quando NÃO usar raciocínio complexo ✅

**Gabarito sugerido**:
1. **CoT** — problema linear, não precisa de busca. Self-Consistency se accuracy é crítica.
2. **Plan-and-Execute** — passos conhecidos (voos, hotéis, atividades), paralelizáveis. ReWOO se fontes são independentes.
3. **ReAct** — imprevisível, depende de cada observação. Reflexion se o modelo falha e tenta de novo.
4. **Plan-and-Execute** — análise estruturada (ler cláusulas, comparar, concluir). ToT se há múltiplas interpretações.
5. **Tree of Thoughts / LATS** — espaço de busca grande, precisa backtracking. ToT para BFS/DFS; LATS para busca mais sofisticada.

---

### E5 — Estrutura de Memória de Reflexion
**Tempo estimado**: 15 min
**Formato**: Individual, código/pseudocódigo

**Enunciado**: Escreva a estrutura de dados da memória episódica de um agente Reflexion. A estrutura deve:

- Armazenar reflexões de tentativas anteriores
- Permitir recuperação eficiente para o prompt da próxima tentativa
- Ter um limite de tamanho (evitar crescimento indefinido)
- Incluir timestamp e status (sucesso/falha) de cada tentativa

**Exemplo de resposta**:
```python
from dataclasses import dataclass, field
from datetime import datetime
from collections import deque

@dataclass
class ReflexionEntry:
    attempt: int
    status: str  # "success" | "failure"
    reflection: str
    timestamp: datetime = field(default_factory=datetime.now)

class ReflexionMemory:
    def __init__(self, max_entries: int = 5):
        self.entries: deque[ReflexionEntry] = deque(maxlen=max_entries)

    def add(self, attempt: int, status: str, reflection: str):
        self.entries.append(ReflexionEntry(attempt, status, reflection))

    def get_reflections_text(self) -> str:
        if not self.entries:
            return ""
        lines = ["## Reflexões de tentativas anteriores:"]
        for e in self.entries:
            lines.append(f"[Tentativa {e.attempt} — {e.status}] {e.reflection}")
        return "\n".join(lines)

    def all_succeeded(self) -> bool:
        return len(self.entries) > 0 and all(e.status == "success" for e in self.entries)
```

**Poka-yokes aplicados**:
- `maxlen` evita crescimento indefinido (limite rígido)
- `status` permite filtrar só reflexões de falhas
- `get_reflections_text` formata para injeção no prompt

---

### E6 — Verdadeiro/Falso Justificado
**Tempo estimado**: 10 min
**Formato**: Individual, escrito

**Enunciado**: Responda V ou F e justifique em 2-3 frases:

1. "Self-Discover é sempre superior a CoT."
2. "ReWOO reduz custo porque não reenvia o contexto a cada chamada de tool."
3. "Reflexion é equivalente a fine-tuning porque aprende com falhas."
4. "Tree of Thoughts é melhor que CoT porque explora múltiplos caminhos simultaneamente."
5. "Modelos de reasoning nativo (o1/o3) tornam CoT promptado obsoleto."

**Gabarito**:
1. **F** — Self-Discover tem overhead (fase de descoberta). Para problemas que CoT já resolve, é desperdício. Vale para problemas novos e complexos.
2. **V** — ReWOO gera o plano uma vez e executa workers em paralelo sem reenviar histórico. ReAct reenvia TODO o contexto a cada step.
3. **F** — Reflexion aprende em runtime com memória verbal (sem atualizar pesos). Fine-tuning atualiza pesos do modelo. Reflexion é episódico; fine-tuning generaliza.
4. **Parcialmente V** — ToT explora múltiplos caminhos, mas não "simultaneamente" — é uma busca sequencial com poda. E é 10x mais caro. "Melhor" depende do critério (accuracy vs custo).
5. **F** — Reasoning nativo internaliza parte do CoT, mas: (a) não substitui ToT/LATS onde há tools durante a busca; (b) é caixa preta (sem auditorabilidade); (c) é caro. CoT promptado ainda vale para 90% dos casos.

---

### E7 — ReWOO: Por Que Reduz Custo
**Tempo estimado**: 15 min
**Formato**: Individual, análise

**Enunciado**: Compare o custo de tokens entre ReAct e ReWOO para uma tarefa com 5 tools. Considere:

- System prompt: 500 tokens
- Pergunta: 200 tokens
- Cada tool call + observation: 300 tokens
- Histórico cresce linearmente em ReAct

**Perguntas**:
1. Quantos tokens de INPUT o ReAct consome em 5 steps?
2. E o ReWOO (1 chamada de plano + 5 workers paralelos + 1 solver)?
3. Qual a redução percentual?

**Gabarito**:
1. **ReAct**: step 1 = 500+200 = 700. step 2 = 700+300 = 1000. step 3 = 1300. step 4 = 1600. step 5 = 1900. Total input = 700+1000+1300+1600+1900 = **6500 tokens**.
2. **ReWOO**: plano = 500+200 = 700. 5 workers = 5 × (500+100) = 3000 (cada worker recebe só system prompt + a sub-tarefa, não o histórico acumulado). solver = 500+200+(5×300 evidências) = 2200. Total = 700+3000+2200 = **5900 tokens**.

   *(Nota: em implementações otimizadas, workers podem receber prompts menores. A economia real chega a 50-64% conforme o paper original.)*

3. Redução ≈ 9%. Em tarefas com mais steps (10+), a economia do ReWOO cresce porque ReAct é quadrático (histórico acumula) e ReWOO é mais próximo de linear.

---

## Projeto do Módulo

### P1 — GAIA com 3 Padrões de Raciocínio
**Prazo**: 2 semanas
**Formato**: Individual
**Carga**: ~10h

**Descrição**: Implementar um agente que resolve um subconjunto de GAIA (general assistant benchmark) usando pelo menos 3 padrões de raciocínio à escolha. Comparar resultados e justificar.

**Entregáveis**:
- Repositório Git com 3 versões do mesmo agente (diferentes padrões de raciocínio)
- Benchmark: 20 problemas de GAIA executados em cada versão
- ADR (Architecture Decision Record) documentando a escolha de padrão
- Tabela comparativa: success rate, custo, latência, robustez

**Padrões sugeridos (escolher 3)**:
1. ReAct (baseline)
2. Plan-and-Execute
3. Reflexion
4. Tree of Thoughts
5. Self-Discover

**Critério de sucesso**:
- Agente funcional nas 3 versões
- Diferença de success rate entre padrões mensurada e discutida
- ADR justifica escolha com dados concretos
- Tabela comparativa é clara e acionável

**Avaliação** (rubrica de 4 pilares):

| Pilar | Peso | Critério |
|---|---|---|
| Técnico | 40% | Código funcional, benchmark, qualidade da implementação |
| Consultivo | 30% | ADR — clareza da justificativa baseada em dados |
| Comportamental | 20% | Code review de um colega |
| Prático | 10% | Demo ao vivo: padrão escolhido resolvendo um caso |

**Nota mínima de aprovação**: 3.0
