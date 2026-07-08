# extraction/02-entity-extraction.md

## objetivo
Prompt para extrair entidades nomeadas (pessoas, organizações, locais, datas) e relações entre elas a partir de texto.

## variáveis
- `{{text}}` — texto fonte
- `{{entity_types}}` — tipos de entidade a extrair (ex.: PERSON, ORG, LOC, DATE, PRODUCT)
- `{{include_relations}}` — se true, extrai também relações entre entidades

## template

```
Extract named entities from the text below.

Text:
{{text}}

Entity types to extract: {{entity_types}}
Include relations: {{include_relations}}

Respond with JSON:
{
  "entities": [
    {
      "name": "<entity text>",
      "type": "<PERSON|ORG|LOC|DATE|PRODUCT|...>",
      "mentions": ["<all mentions, including pronouns resolved>"],
      "attributes": {
        ...optional key-value pairs found in text
      }
    }
  ],
  "relations": [
    {
      "source": "<entity name>",
      "target": "<entity name>",
      "relation": "<relation type>",
      "evidence": "<text snippet supporting this relation>"
    }
  ]
}

If {{include_relations}} is false, omit the "relations" key.
```

## exemplo de uso
Extrair de "João da Silva é CEO da Acme Corp em São Paulo" → entities: `[João da Silva/PERSON, Acme Corp/ORG, São Paulo/LOC]`, relations: `[João da Silva -> Acme Corp: CEO]`.

## trade-offs
- Resolução de pronomes ("ele", "a empresa") é imprecisa sem contexto adicional
- Entidades sobrepostas ("São Paulo" vs "São Paulo, SP") podem gerar duplicatas
- Relações exigem mais capacidade do modelo e são mais propensas a alucinação

## variações
- **Entity resolution**: após extração, normalizar variações ("John" vs "John Doe") para um mesmo ID
- **Nested entities**: extrair entidades dentro de entidades (ex.: "Microsoft's CEO Satya" → ORG contém PERSON)
- **Temporal scoping**: associar cada entidade a um intervalo de tempo quando relevante ("CEO until 2023")
