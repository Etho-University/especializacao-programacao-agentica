# Template Visual — Apresentações Universidade Etho

> Padrão visual para todas as apresentações da Especialização em Programação Agêntica.
> Inspirado em: MIT, Stanford, Carnegie Mellon, DeepLearning.AI, Anthropic, Microsoft Learn.

---

## 1. Paleta de Cores

| Token | HEX | Uso |
|---|---|---|
| `etho-primary` | `#1B3A5E` | Cor principal — cabeçalhos, títulos de slide, capa |
| `etho-accent` | `#E85D2F` | Destaques — indicadores, badges, callouts importantes |
| `etho-dark` | `#0F1E2D` | Fundo escuro — slides de seção, diagramas |
| `etho-light` | `#F7F8FA` | Fundo claro — slides de conteúdo |
| `etho-muted` | `#6B7A8F` | Texto secundário, legendas, metadados |
| `etho-success` | `#2D8659` | Boas práticas, "do" |
| `etho-danger` | `#C0392B` | Anti-patterns, "don't" |
| `etho-info` | `#2980B9` | Informação complementar, dicas |
| `etho-warning` | `#D4A017` | Atenção, cuidados |

## 2. Tipografia

| Elemento | Fonte | Tamanho | Peso |
|---|---|---|---|
| Título de slide | Inter / Segoe UI | 32pt | 700 (Bold) |
| Subtítulo | Inter / Segoe UI | 22pt | 600 (SemiBold) |
| Corpo | Inter / Segoe UI | 18pt | 400 (Regular) |
| Código | JetBrains Mono / Consolas | 14pt | 400 |
| Notas de rodapé | Inter / Segoe UI | 12pt | 400 |
| Caption de diagrama | Inter / Segoe UI | 14pt | 400 Italic |

## 3. Layout Base

```
┌──────────────────────────────────────────────────┐
│ [Logo Etho]                        [ETHAGT0X] │ ← Header bar (etho-primary, 8mm)
├──────────────────────────────────────────────────┤
│                                                  │
│  TÍTULO DO SLIDE                                 │ ← 32pt, etho-primary
│  Subtítulo opcional                              │ ← 22pt, etho-muted
│                                                  │
│  ┌────────────────────┐  ┌─────────────────┐    │
│  │                    │  │                 │    │
│  │   CONTEÚDO         │  │  DIAGRAMA /     │    │
│  │   (texto mínimo,   │  │  IMAGEM /       │    │
│  │    bullets curtos) │  │  CÓDIGO         │    │
│  │                    │  │                 │    │
│  └────────────────────┘  └─────────────────┘    │
│                                                  │
├──────────────────────────────────────────────────┤
│ [objetivo do slide]            [tempo · slide X] │ ← Footer (etho-muted, 12pt)
└──────────────────────────────────────────────────┘
```

## 4. Tipos de Slide

| Tipo | Fundo | Layout | Quando usar |
|---|---|---|---|
| **Capa** | `etho-dark` | Logo + título + módulo + professor + data | Início da aula |
| **Seção** | `etho-primary` | Número da seção + título grande | Transição entre blocos |
| **Conteúdo** | `etho-light` | Título + bullets/diagrama | Conceitos, explicações |
| **Comparação** | `etho-light` | Duas colunas (vs) | Trade-offs, do/don't |
| **Diagrama** | `etho-light` ou `etho-dark` | Diagrama em destaque + caption | Arquiteturas, fluxos |
| **Código** | `etho-dark` | Code block + anotações | Demonstração, exemplos |
| **Citação** | `etho-dark` | Quote grande + fonte | Papers, princípios |
| **Exercício** | `etho-light` | Enunciado + caixa de discussão | Atividade em aula |
| **Resumo** | `etho-light` | Checklist visual | Fechamento de seção |
| **Referências** | `etho-light` | Lista numerada com links | Final da aula |

## 5. Padrões Visuais Recorrentes

### Badge de Competência
```
[C1: Programação Agêntica · Nível I]
```
Fundo `etho-accent`, texto branco, 14pt.

### Callout Boxes
- **Boa prática**: borda esquerda `etho-success` (4px), fundo `#E8F5EE`
- **Anti-pattern**: borda esquerda `etho-danger` (4px), fundo `#FDECEA`
- **Dica**: borda esquerda `etho-info` (4px), fundo `#EBF5FB`
- **Atenção**: borda esquerda `etho-warning` (4px), fundo `#FEF9E7`

### Indicador de Tempo
```
⏱ 3 min
```
No canto inferior direito, `etho-muted`, 12pt.

### Numeração
```
Slide 12 / 60
```
No canto inferior direito, `etho-muted`, 12pt.

## 6. Animações Padrão

| Tipo | Quando | Efeito |
|---|---|---|
| **Fade in** | Título de slide | 300ms |
| **Appear** | Bullets de conteúdo | On click, 200ms |
| **Wipe** | Diagramas | Left-to-right, 500ms |
| **Zoom** | Código destacado | 300ms |
| **Morph** | Transição entre slides relacionados | 400ms |

## 7. Estrutura de Notas do Apresentador

Cada slide contém notas no formato:

```
📖 EXPLICAÇÃO COMPLETA:
[texto detalhado do que dizer]

💡 ANALOGIA / HISTÓRIA:
[analogia ou história para ilustrar]

❓ PERGUNTA PARA A TURMA:
[pergunta retórica ou de discussão]

⚠️ ERROS COMUNS:
[o que alunos costumam confundir]

➡️ TRANSIÇÃO:
[como conectar ao próximo slide]
```

## 8. Identidade Visual Etho

- **Logo**: Universidade Etho no canto superior esquerdo de todo slide
- **Código do módulo**: No canto superior direito (ex: `ETHAGT01`)
- **Barra de progresso**: No rodapé, indicando posição na apresentação
- **Consistência**: Mesmo template em todos os 16 módulos + Capstone
