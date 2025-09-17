from abc import ABC
from abc import abstractmethod
from uuid import uuid4
from typing import cast

from src.broker import IEventBroker
from src.broker import EmptyQueueError
from src.models import Order
from src.events import EventType
from src.events import BillingEvent
from src.events import NotificationEvent


class IDiscountStrategy(ABC):
    @abstractmethod
    def discount(self, order: Order, total: float) -> float:
        pass


class BasicDiscountStrategy(IDiscountStrategy):
    def discount(self, order: Order, total: float) -> float:
        if total >= 100:
            return total * 0.01
        return total


class BillingSerivce:
    def __init__(
        self,
        broker: IEventBroker,
        discount_strategy: IDiscountStrategy,
    ) -> None:
        self._broker = broker
        self._discount_strategy = discount_strategy

    def bill(self, event: BillingEvent) -> None:
        order = event.order
        total = 0
        for item in order.items:
            total += item.product.price * item.quantity

        discount = self._discount_strategy.discount(order, total)
        notification_event = NotificationEvent(
            id=uuid4().hex,
            type=EventType.NOTIFICATION,
            order=order,
            total=total,
            discount=discount,
        )
        self._broker.push(notification_event)

    def listen(self) -> None:
        try:
            event: BillingEvent = cast(
                BillingEvent,
                self._broker.pull(EventType.BILLING),
            )
            print("Process event:", event.id)
            self.bill(event)

        except EmptyQueueError:
            pass
