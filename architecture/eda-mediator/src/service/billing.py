from uuid import uuid4
from abc import ABC
from abc import abstractmethod

from src.events import EventType
from src.events import BillingEvent
from src.events import NotificationEvent
from src.models import Order
from src.mediator import Mediator


class IDiscountStrategy(ABC):
    @abstractmethod
    def discount(self, order: Order, total: float) -> float:
        pass


class BasicDiscountStrategy(IDiscountStrategy):
    def discount(self, order: Order, total: float) -> float:
        if total >= 100:
            return total * 0.01
        return total


class BillingService:
    def __init__(self, mediator: Mediator, discount_strategy: IDiscountStrategy):
        self._mediator = mediator
        self._discount_strategy = discount_strategy
        self._mediator.subscribe(
            EventType.BILLING,
            self.process_billing,  # type:ignore
        )

    def process_billing(self, event: BillingEvent) -> None:
        order = event.order
        total = sum(item.product.price * item.quantity for item in order.items)
        discount = self._discount_strategy.discount(order, total)
        notification_event = NotificationEvent(
            id=uuid4().hex,
            type=EventType.NOTIFICATION,
            order=order,
            total=total,
            discount=discount,
        )
        self._mediator.publish(notification_event)
