import json, time, queue, threading
from dataclasses import dataclass, field
from typing import Callable

@dataclass
class Event:
    type: str
    data: dict
    timestamp: float = field(default_factory=time.time)

class EventBus:
    def __init__(self):
        self.subscribers: dict[str, list[Callable]] = {}
        self.queue = queue.Queue()
        threading.Thread(target=self._dispatch_loop, daemon=True).start()

    def subscribe(self, event_type: str, handler: Callable):
        self.subscribers.setdefault(event_type, []).append(handler)

    def publish(self, event: Event):
        self.queue.put(event)

    def _dispatch_loop(self):
        while True:
            event = self.queue.get()
            for handler in self.subscribers.get(event.type, []):
                try:
                    handler(event)
                except Exception as e:
                    print(f"Erro no handler {handler.__name__}: {e}")

bus = EventBus()

def on_research_request(event):
    print(f"[Researcher] Pesquisando: {event.data['query']}")
    bus.publish(Event("research_complete", {"query": event.data["query"], "results": ["resultado1", "resultado2"]}))

def on_synthesize_request(event):
    print(f"[Synthesizer] Sintetizando: {event.data['results']}")
    bus.publish(Event("report_ready", {"report": "Relatório sintetizado"}))

bus.subscribe("research_request", on_research_request)
bus.subscribe("research_complete", on_synthesize_request)

bus.publish(Event("research_request", {"query": "agentes LLM em produção"}))
time.sleep(0.5)
bus.publish(Event("research_request", {"query": "MCP protocol 2025"}))
time.sleep(1)
print("\nSistema event-driven funcionando. Adicione mais handlers para escalar.")
