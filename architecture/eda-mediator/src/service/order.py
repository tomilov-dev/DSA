from uuid import uuid4

from src.events import EventType
from src.events import OrderEvent
from src.events import BillingEvent
from src.mediator import Mediator


class OrderService:
    def __init__(self, mediator: Mediator):
        self._mediator = mediator
        self._mediator.subscribe(
            EventType.ORDER,
            self.process_order,  # type: ignore
        )

    def process_order(self, event: OrderEvent) -> None:
        order = event.order
        for item in order.items:
            print("Need to sell item", item.product.name, "in quantity", item.quantity)
        billing_event = BillingEvent(
            id=uuid4().hex,
            type=EventType.BILLING,
            order=order,
        )
        self._mediator.publish(billing_event)
