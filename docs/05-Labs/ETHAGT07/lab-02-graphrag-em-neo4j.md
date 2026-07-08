# ETHAGT07 — Lab 2: GraphRAG em Neo4j

> Curso: Knowledge Graphs & Vector Databases para Agentes · Carga: 30h · Pré-req: ETHAGT07 Lab 1

## Objetivo
Construir um Knowledge Graph a partir de um corpus textual usando extração de entidades/relações com LLM, indexar em Neo4j, e responder perguntas multi-hop que o vector RAG não consegue resolver.

## Preparação
- Ambiente: Python 3.11+, `pip install neo4j openai langchain-experimental`, Docker
- Dados/recursos: Neo4j local (Docker); corpus de 5-10 artigos sobre um tema interligado (ex.: história de tecnologia, com pessoas, empresas e produtos)
- Leitura prévia: Apostila ETHAGT07, Unidade 3 (Knowledge Graphs) e Unidade 4 (GraphRAG)

## Roteiro
### Passo 1 — Subir o Neo4j
```bash
docker run --name neo4j -p 7474:7474 -p 7687:7687 \
  -e NEO4J_AUTH=neo4j/password -d neo4j:5
```

**Checkpoint:** Neo4j Browser acessível em `http://localhost:7474`.

### Passo 2 — Conectar ao Neo4j
```python
from neo4j import GraphDatabase
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))
driver.verify_connectivity()
```

**Checkpoint:** conexão estabelecida sem erro.

### Passo 3 — Extração de entidades e relações
Use LLM para extrair triplas (sujeito, relação, objeto) de cada documento:

```python
def extract_triples(text):
    prompt = f"""Extract knowledge triples from this text as JSON:
    [{{"subject": "...", "relation": "...", "object": "...", "s_type": "Person", "o_type": "Company"}}]
    Text: {text}"""
    response = call_llm(prompt)
    return json.loads(response)
```

**Checkpoint:** extração produz triplas válidas para um documento de teste.

### Passo 4 — Inserir triplas no Neo4j
Crie nós e relacionamentos com tipagem:

```python
import re

def _safe_label(value: str) -> str:
    """Valida label/tipo de relação do Cypher (apenas [A-Za-z_]) para evitar injeção."""
    cleaned = re.sub(r"[^A-Za-z_]", "_", value.upper().replace(" ", "_"))
    if not cleaned or not cleaned[0].isalpha():
        raise ValueError(f"Label inválido: {value}")
    return cleaned

def insert_triples(tx, triples):
    for t in triples:
        s_type = _safe_label(t["s_type"])
        o_type = _safe_label(t["o_type"])
        rel = _safe_label(t["relation"])
        # Labels/tipos de relação NÃO podem ser parametrizados no Cypher:
        # interpolam-se via f-string APÓS validação estrita (whitelist).
        cypher = (
            f"MERGE (s:{s_type} {{name: $subject}}) "
            f"MERGE (o:{o_type} {{name: $object}}) "
            f"MERGE (s)-[:{rel}]->(o)"
        )
        tx.run(cypher, subject=t["subject"], object=t["object"])

with driver.session() as session:
    for doc in corpus:
        triples = extract_triples(doc)
        session.execute_write(insert_triples, triples)
```

**Checkpoint:** grafo tem nós e relacionamentos visíveis no Neo4j Browser.

### Passo 5 — Query Cypher para pergunta multi-hop
Escreva queries Cypher que atravessam o grafo para responder perguntas multi-hop:

```python
def graph_query(question):
    # Ex: "Quais empresas foram fundadas por pessoas que trabalharam na Apple?"
    cypher = """
    MATCH (p:Person)-[:WORKED_AT]->(a:Company {name: 'Apple'})
    MATCH (p)-[:FOUNDED]->(c:Company)
    RETURN DISTINCT c.name as company
    """
    with driver.session() as session:
        return session.run(cypher).data()
```

**Checkpoint:** query Cypher retorna resultados corretos para uma pergunta de teste.

### Passo 6 — Geração automática de Cypher
Implemente LLM-to-Cypher: o agente traduz a pergunta natural em Cypher:

```python
def natural_to_cypher(question, schema):
    prompt = f"""Convert this question to a Cypher query.
    Schema: {schema}
    Question: {question}
    Output only the Cypher query."""
    return call_llm(prompt).strip()
```

**Checkpoint:** LLM gera Cypher válido para 3 perguntas de teste diferentes.

### Passo 7 — Comparar GraphRAG vs Vector RAG
Prepare 5 perguntas multi-hop e compare GraphRAG com vector RAG (do Lab 1):

| Pergunta | Vector RAG | GraphRAG | Hops |
|---|---|---|---|
| "Quem fundou a empresa que adquiriu o produto X?" | Incorreto | Correto | 3 |
| "Liste todos os colaboradores em comum entre A e B" | Parcial | Correto | 2 |

**Checkpoint:** GraphRAG supera vector RAG em pelo menos 4 das 5 perguntas multi-hop.

### Passo 8 — Análise de custo de construção
Documente o custo de construir o KG vs o benefício:

```markdown
## Custo de construção do KG
- Tokens para extração de triplas: ~X
- Tempo de indexação: ~Y min
- Manutenção (atualização incremental): ?

## Quando GraphRAG vale o custo
- Perguntas multi-hop (≥2 hops): SIM
- Perguntas factuais simples: NÃO (vector RAG basta)
```

**Checkpoint:** análise de custo-benefício documentada em `cost_analysis.md`.

## Desafios extras
- Implemente local search e global search do Microsoft GraphRAG
- Adicione sumarização hierárquica de comunidades
- Construa um pipeline híbrido: agente escolhe entre vector RAG e GraphRAG por pergunta
- Implemente atualização incremental do grafo (novo documento → diff de triplas)

## Entrega
- Repositório com `graph_builder.py`, `graphrag_query.py`, `comparison.md`, `cost_analysis.md`
- Commit no padrão `ETHAGT07: lab-2 implementar graphrag em neo4j`

## Rubrica
Avaliado pela rubrica em `08-Assignments/ETHAGT07/assignment-01.md` (Pilar Comportamental 20%: colaboração em labs).
