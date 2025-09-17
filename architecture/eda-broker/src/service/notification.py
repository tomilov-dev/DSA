from typing import cast

from src.broker import IEventBroker
from src.broker import EmptyQueueError
from src.events import EventType
from src.events import NotificationEvent


class NotificationService:
    def __init__(self, broker: IEventBroker) -> None:
        self._broker = broker

    def notify(self, event: NotificationEvent):
        print("Dicsount:", event.discount, "total:", event.total)

    def listen(self) -> None:
        try:
            event: NotificationEvent = cast(
                NotificationEvent,
                self._broker.pull(EventType.NOTIFICATION),
            )
            print("Process event:", event.id)
            self.notify(event)

        except EmptyQueueError:
            pass
