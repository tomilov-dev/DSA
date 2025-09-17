from uuid import uuid4
from typing import cast

from src.broker import IEventBroker
from src.broker import EmptyQueueError
from src.events import EventType
from src.events import OrderEvent
from src.events import BillingEvent
from src.models import Order


class OrderService:
    def __init__(self, broker: IEventBroker) -> None:
        self._broker = broker

    def make(self, event: OrderEvent) -> None:
        order = event.order
        for item in order.items:
            print("Need to sell item", item.product.name, "in quantity", item.quantity)

        billing_event = BillingEvent(
            id=uuid4().hex,
            type=EventType.BILLING,
            order=order,
        )
        self._broker.push(billing_event)

    def listen(self) -> None:
        try:
            event: OrderEvent = cast(
                OrderEvent,
                self._broker.pull(EventType.ORDER),
            )
            print("Process event:", event.id)
            self.make(event)

        except EmptyQueueError:
            pass
