from src.events import EventType
from src.events import NotificationEvent
from src.mediator import Mediator


class NotificationService:
    def __init__(self, mediator: Mediator):
        self._mediator = mediator
        self._mediator.subscribe(
            EventType.NOTIFICATION,
            self.process_notification,  # type:ignore
        )

    def process_notification(self, event: NotificationEvent) -> None:
        print("Discount:", event.discount, "total:", event.total)
