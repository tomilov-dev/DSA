from typing import Callable
from typing import Dict
from typing import List

from src.events import IEvent
from src.events import EventType


class Mediator:
    def __init__(self):
        self._handlers: Dict[
            EventType,
            List[Callable[[IEvent], None]],
        ] = {}

    def subscribe(
        self,
        event_type: EventType,
        handler: Callable[[IEvent], None],
    ) -> None:
        if event_type not in self._handlers:
            self._handlers[event_type] = []
        self._handlers[event_type].append(handler)

    def publish(self, event: IEvent) -> None:
        for handler in self._handlers.get(event.type, []):
            handler(event)
