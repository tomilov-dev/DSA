"""
Реализация калькулятора стоимости доставки в интернет магазине через паттерн Стратегия
"""

from enum import Enum
from abc import ABC
from abc import abstractmethod


class DeliveryType(str, Enum):
    COURIER = "courier"
    POST = "post"
    PICKUP = "pickup"


class Item:
    def __init__(self, weight: float, cost: int) -> None:
        self.weight = weight
        self.cost = cost


class IDeliveryStrategy(ABC):
    @abstractmethod
    def calculate(self, weight: float) -> float:
        pass


class DeliveryCourier(IDeliveryStrategy):
    def calculate(self, weight: float) -> float:
        return max(10, weight * 1)


class DeliveryPickup(IDeliveryStrategy):
    def calculate(self, weight: float) -> float:
        return max(10, weight * 0.5)


class DeliveryPost(IDeliveryStrategy):
    def calculate(self, weight: float) -> float:
        return 10


class IDelivery(ABC):
    def __init__(self, delivery: IDeliveryStrategy | None = None) -> None:
        if not delivery:
            delivery = DeliveryPost()
        self._delivery = delivery

    def set_delivery_method(self, delivery: IDeliveryStrategy) -> None:
        self._delivery = delivery

    @abstractmethod
    def calculate(
        self,
        items: list[Item],
        delivery_method: DeliveryType,
    ) -> float:
        pass


class Delivery(IDelivery):
    def delivery_cost(self, weight: float) -> float:
        return self._delivery.calculate(weight)

    def calculate(self, items: list[Item]) -> float:
        total = 0
        weight = 0
        for i in items:
            total += i.cost
            weight += i.weight
        return total + self.delivery_cost(weight)


def client_code():
    i1 = Item(10, 100)
    i2 = Item(15, 150)
    i3 = Item(3, 400)
    items = [i1, i2, i3]

    delivery = Delivery()
    cost = delivery.calculate(items)
    print(cost)

    delivery.set_delivery_method(DeliveryCourier())
    cost = delivery.calculate(items)
    print(cost)


if __name__ == "__main__":
    client_code()
