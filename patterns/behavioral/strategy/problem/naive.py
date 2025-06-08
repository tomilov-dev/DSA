"""
Реализация калькулятора стоимости доставки в интернет магазине (наивный подход)
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


class IDelivery(ABC):
    @abstractmethod
    def calculate(
        self,
        items: list[Item],
        delivery_method: DeliveryType,
    ) -> float:
        pass


class Delivery(IDelivery):
    def delivery_cost(
        self,
        weight: float,
        delivery_method: DeliveryType,
    ) -> float:
        if delivery_method == DeliveryType.COURIER:
            return max(10, weight * 1)
        elif delivery_method == DeliveryType.PICKUP:
            return max(10, weight * 0.5)
        elif delivery_method == DeliveryType.POST:
            return 10
        else:
            raise ValueError(f"DeliveryType is not implemented: {delivery_method}")

    def calculate(
        self,
        items: list[Item],
        delivery_method: DeliveryType,
    ) -> float:
        total = 0
        weight = 0
        for i in items:
            total += i.cost
            weight += i.weight
        return total + self.delivery_cost(weight, delivery_method)


def client_code():
    i1 = Item(10, 100)
    i2 = Item(15, 150)
    i3 = Item(3, 400)

    delivery = Delivery()
    cost = delivery.calculate(
        [i1, i2, i3],
        DeliveryType.PICKUP,
    )
    print(cost)


if __name__ == "__main__":
    client_code()
