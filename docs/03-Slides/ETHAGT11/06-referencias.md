# ETHAGT11 — Referências

> Todas as fontes utilizadas na preparação e apresentação da aula.

---

## Canônicas (fundação do curso)

### 1. Temporal.io — Durable Execution
- **Autor**: Temporal Technologies
- **URL**: https://docs.temporal.io/develop/python/durable-execution
- **Resumo**: Documentação e primer oficial sobre durable execution. Define os conceitos de workflow, activity, worker, replay, signals e timers. Fundamento direto das Seções D e E (slides 28-46).
- **Importância**: Canônica
- **Slides que referenciam**: 30, 31, 32, 38, 40, 41, 42, 43, 44, 75

### 2. Kafka: The Definitive Guide
- **Autores**: Neha Narkhede, Gwen Shapira, Todd Palino
- **Editora**: O'Reilly Media
- **Resumo**: Referência canônica sobre Kafka. Cobre arquitetura de tópicos, partições, consumer groups, replicação, ordering e produção. Base direta da Seção C (slides 14-27).
- **Importância**: Canônica
- **Slides que referenciam**: 15, 16, 17, 18, 21, 22, 75

### 3. Kreps, J. — The Log: What every software engineer should know
- **Autor**: Jay Kreps (co-criador do Kafka)
- **URL**: https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unified
- **Resumo**: Essay seminal sobre o log como abstração central em sistemas distribuídos. Fundamento conceitual de todo o paradigma event-driven. Base do Slide 15 e conceito permeante.
- **Importância**: Canônica
- **Slides que referenciam**: 6, 9, 15, 75

### 4. Richards, M. & Ford, N. — Fundamentals of Software Architecture
- **Editora**: O'Reilly Media
- **Resumo**: Capítulo sobre arquitetura event-driven. Define o estilo arquitetural, trade-offs (complexidade, eventual consistency, debugging) e quando aplicar. Base da Seção B (slides 7-13).
- **Importância**: Canônica
- **Slides que referenciam**: 8, 9, 11, 12

---

## Importantes (complementam e aprofundam)

### 5. Microsoft — Cloud Design Patterns
- **URL**: https://learn.microsoft.com/azure/architecture/patterns/
- **Resumo**: Catálogo de padrões de nuvem. Especialmente relevantes: Saga, CQRS, Circuit Breaker, Retry, Health Endpoint Monitoring. Base direta dos Slides 23 (CQRS), 24 (saga), 51-53 (resiliência).
- **Importância**: Importante
- **Slides que referenciam**: 23, 24, 48, 51, 52, 53, 75

### 6. NATS Documentation — JetStream
- **URL**: https://docs.nats.io/nats-concepts/jetstream
- **Resumo**: Documentação oficial do NATS JetStream. Cobre streams, consumers duráveis, modelos de delivery (at-least-once, exactly-once com dedup window). Base do Slide 20.
- **Importância**: Importante
- **Slides que referenciam**: 20, 21, 22

### 7. RabbitMQ Documentation
- **URL**: https://www.rabbitmq.com/documentation.html
- **Resumo**: Documentação oficial do RabbitMQ. Cobre modelo AMQP (exchanges, bindings, queues), tipos de exchange (direct, topic, fanout, headers), ACK manual, dead letter exchange. Base do Slide 19.
- **Importância**: Importante
- **Slides que referenciam**: 19, 21, 22

### 8. CloudEvents Specification (CNCF)
- **URL**: https://cloudevents.io/
- **Resumo**: Especificação CNCF para descrição de eventos em formato comum. Campos: id, source, type, specversion, time, data, subject. Padrão emergente para interoperabilidade. Base do Slide 25.
- **Importância**: Importante
- **Slides que referenciam**: 6, 25, 75

### 9. Prefect Documentation
- **URL**: https://docs.prefect.io/
- **Resumo**: Documentação do Prefect. Cobre @flow e @task decorators, retries, persistência de estado. Alternativa mais simples ao Temporal. Base do Slide 33.
- **Importância**: Importante
- **Slides que referenciam**: 33, 35

### 10. Apache Airflow Documentation
- **URL**: https://airflow.apache.org/docs/
- **Resumo**: Documentação do Airflow. Cobre DAGs, agendamento, operators. Posicionamento como ferramenta de batch vs orquestração em tempo real. Base do Slide 34.
- **Importância**: Importante
- **Slides que referenciam**: 34, 35

---

## Complementares (leitura opcional)

### 11. Restate — Durable RPC
- **URL**: https://docs.restate.dev/
- **Resumo**: Alternativa moderna a Temporal. Durable RPC com menor overhead. Referência para comparação de abordagens.
- **Slides que referenciam**: 31

### 12. OpenTelemetry — Distributed Tracing
- **URL**: https://opentelemetry.io/docs/
- **Resumo**: Padrão CNCF para observabilidade. Cobre spans distribuídos, context propagation, Trace ID em headers de mensagem. Base do Slide 58; aprofundamento em ETHAGT12.
- **Slides que referenciam**: 58

### 13. Konieczny — Exactly-once is impossible
- **Resumo**: Argumento técnico sobre por que exactly-once delivery verdadeiro não existe na presença de falhas. Fundamento do Slide 56.
- **Importância**: Complementar (conceitual)
- **Slides que referenciam**: 56

### 14. Temporal Web UI
- **URL**: https://docs.temporal.io/web-ui
- **Resumo**: Interface web do Temporal para visualizar execuções, histórico, replay. Usada nas DEMOS (Slides 44).
- **Slides que referenciam**: 41, 44

### 15. DBOS — Durable Execution
- **URL**: https://docs.dbos.dev/
- **Resumo**: Alternativa acadêmica a Temporal. Durable execution via banco de dados transacional. Referência para comparação.
- **Slides que referenciam**: 31

---

## Ficha de Pesquisa

- **Arquivo**: `20-Research/ETHAGT11-pesquisa.md`
- **Última consulta**: Julho 2026
- **Revalidação**: Janeiro 2027 (estado da arte em orquestração e workflow engines evolui rapidamente)
