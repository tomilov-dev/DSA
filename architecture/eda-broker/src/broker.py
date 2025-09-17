from abc import ABC
from abc import abstractmethod
from collections import deque

from src.events import IEvent
from src.events import EventType


class EmptyQueueError(Exception):
    pass


class IEventBroker(ABC):
    @abstractmethod
    def push(self, event: IEvent) -> None:
        pass

    @abstractmethod
    def pull(self, event_type: EventType) -> IEvent:
        pass


class InMemoryEventBroker(IEventBroker):
    def __init__(self) -> None:
        self._mem: dict[str, deque[IEvent]] = {}

    def _init_deq(self, event_type: EventType) -> None:
        if event_type.value not in self._mem:
            self._mem[event_type.value] = deque([])

    def push(self, event: IEvent) -> None:
        self._init_deq(event.type)
        self._mem[event.type.value].append(event)

    def pull(self, event_type: EventType) -> IEvent:
        self._init_deq(event_type)
        deq = self._mem[event_type.value]
        if not deq:
            raise EmptyQueueError("В очереди нет событий")
        return deq.popleft()
