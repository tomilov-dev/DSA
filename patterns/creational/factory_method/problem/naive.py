"""
Решение задачи доставки (наивный подход)
"""

from enum import Enum
from abc import ABC
from abc import abstractmethod


class DeliveryType(str, Enum):
    TRANSPORT = "Transport"
    RAILWAY = "Railway"
    AIR = "Air"
    SHIP = "Ship"


class Product:
    def __init__(
        self,
        name: str,
        price: float,
        weight: float,
    ) -> None:
        self.name = name
        self.price = price
        self.weight = weight


class OrderItem:
    def __init__(
        self,
        product: Product,
        quantity: int,
    ) -> None:
        self.product = product
        self.quantity = quantity


class IDelivery(ABC):
    @abstractmethod
    def cost(
        self,
        subtotal: float,
        weight: float,
        dist: float,
    ) -> float:
        pass

    @abstractmethod
    def time(
        self,
        dist: float,
    ) -> float:
        pass


## В начале у нас есть 2 класса доставки
class TransportDelivery(IDelivery):
    def cost(
        self,
        subtotal: float,
        weight: float,
        dist: float,
    ) -> float:
        if subtotal >= 1000:
            return 0
        return weight * dist * 2 / 100

    def time(
        self,
        dist: float,
    ) -> float:
        return dist * 1 / 24


class RailwayDelivery(IDelivery):
    def cost(
        self,
        subtotal: float,
        weight: float,
        dist: float,
    ) -> float:
        if subtotal >= 500:
            return 0
        return weight * dist * 1.5 / 100

    def time(
        self,
        dist: float,
    ) -> float:
        return dist * 2 / 24


## Через какое-то время мы хотим добавить еще два типа доставки
## Мы делаем это, просто добавляя две новые реализации интерфейса IDelivery
class AirDelivery(IDelivery):
    def cost(
        self,
        subtotal: float,
        weight: float,
        dist: float,
    ) -> float:
        return weight * dist * 3.5 / 100

    def time(
        self,
        dist: float,
    ) -> float:
        return dist * 1 / 24


class ShipDelivery(IDelivery):
    def cost(
        self,
        subtotal: float,
        weight: float,
        dist: float,
    ) -> float:
        return weight * dist * 2.5 / 100

    def time(
        self,
        dist: float,
    ) -> float:
        return dist * 1.5 / 24


## В корзине нет изменений, связанных с добавлением новых реализаций
## Потому что мы работаем через интерфейс
class Cart:
    def __init__(
        self,
        delivery: IDelivery,
        distance: float,
    ) -> None:
        self.delivery = delivery
        self.distance = distance

    def total(
        self,
        items: list[OrderItem],
    ) -> float:
        subtotal = 0
        weight = 0
        for item in items:
            subtotal += item.product.price * item.quantity
            weight += item.product.weight * item.quantity

        delivery = self.delivery.cost(subtotal, weight, self.distance)
        return subtotal + delivery


def client_code(
    distance: float,
    delivery_type: DeliveryType,
) -> None:
    match delivery_type.value:
        ## В начале мы имели 2 switch-case выражения
        case DeliveryType.TRANSPORT.value:
            delivery = TransportDelivery()
        case DeliveryType.RAILWAY.value:
            delivery = RailwayDelivery()

        ## После добавления новых доставок, мы вмешиваемся в клиентский код (2 новых выражения)
        ## Потому что в клиентском коде мы имеем прямую зависимость от классов доставок
        ## FIXME: зависимость в клиентском коде
        case DeliveryType.AIR.value:
            delivery = AirDelivery()
        case DeliveryType.SHIP.value:
            delivery = ShipDelivery()

        case _:
            raise NotImplementedError(
                f"Delivery type not implemented yet: {delivery_type.value}"
            )

    cart = Cart(delivery, distance)

    ## Товары были созданы для иллюстрации
    p1 = Product("1", 1, 1)
    p2 = Product("2", 2, 2)
    p3 = Product("3", 3, 3)
    items = [
        OrderItem(p1, 3),
        OrderItem(p2, 2),
        OrderItem(p3, 1),
    ]

    total = cart.total(items)
    print(total)


if __name__ == "__main__":
    client_code(100, DeliveryType.AIR)
