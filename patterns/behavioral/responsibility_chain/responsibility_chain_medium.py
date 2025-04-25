from abc import ABC
from abc import abstractmethod


class Handler(ABC):
    def __init__(self) -> None:
        self._next: Handler | None = None

    def set_next(self, handler: "Handler") -> None:
        self._next = handler

    @abstractmethod
    def handle(self, order: dict) -> None:
        pass


class PhysicalProductHandler(Handler):
    def handle(self, order: dict) -> None:
        if order["type"] == "physical":
            print("PhysicalProductHandler")
        elif self._next:
            self._next.handle(order)
        else:
            print(f"Order type '{order['type']}' could not be handled")


class DigitalProductHandler(Handler):
    def handle(self, order: dict) -> None:
        if order["type"] == "digital":
            print("DigitalProductHandler")
        elif self._next:
            self._next.handle(order)
        else:
            print(f"Order type '{order['type']}' could not be handled")


class SubscriptionHandler(Handler):
    def handle(self, order: dict) -> None:
        if order["type"] == "subscription":
            print("SubscriptionHandler")
        elif self._next:
            self._next.handle(order)
        else:
            print(f"Order type '{order['type']}' could not be handled")


def client_code():
    physical_handler = PhysicalProductHandler()
    digital_handler = DigitalProductHandler()
    subscription_handler = SubscriptionHandler()

    physical_handler.set_next(digital_handler)
    digital_handler.set_next(subscription_handler)

    order1 = {"type": "physical", "details": "Order details for physical product"}
    order2 = {"type": "digital", "details": "Order details for digital product"}
    order3 = {"type": "subscription", "details": "Order details for subscription"}
    order4 = {"type": "unknown", "details": "Order details for unknown product"}

    physical_handler.handle(order1)
    physical_handler.handle(order2)
    physical_handler.handle(order3)
    physical_handler.handle(order4)
