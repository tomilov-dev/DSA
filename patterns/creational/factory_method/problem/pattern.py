"""
Решение задачи доставки через фабричный метод
В данном решении используются отдельные классы-фабрики для каждого интерфейса IDelivery
Это необходимо лишь в случае, когда для создание экземпляра IDelivery требует сложной логики
В противном случае можно обойтись lambda-функциями или как-то иначе возвращать экземпляры IDelivery
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


class IDelivery:
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


class IDeliveryFactory:
    @abstractmethod
    def create(self) -> IDelivery:
        pass


## В начале у нас было 2 реализации IDelivery и IDeliveryFactory
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


class TransportDeliveryFactory(IDeliveryFactory):
    def create(self) -> IDelivery:
        return TransportDelivery()


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


class RailwayDeliveryFactory(IDeliveryFactory):
    def create(self):
        return RailwayDelivery()


## Мы захотели добавить два дополнительных класса доставки
## Вместе с этим нам требуется реализация двух дополнительных фабричных методов
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


class AirDeliveryFactory(IDeliveryFactory):
    def create(self):
        return AirDelivery()


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


class ShipDeliveryFactory(IDeliveryFactory):
    def create(self):
        return ShipDelivery()


## Мы также создадим класс-селектор в бекенде
## Это поможет нам избавиться от прямых зависимостей в клиентском коде
class DeliveryFactorySelector:
    _factories = {
        DeliveryType.TRANSPORT: TransportDeliveryFactory(),
        DeliveryType.RAILWAY: RailwayDeliveryFactory(),
        DeliveryType.AIR: AirDeliveryFactory(),
        DeliveryType.SHIP: ShipDeliveryFactory(),
    }

    def select(self, delivery_type: DeliveryType) -> IDeliveryFactory:
        factory = self._factories.get(delivery_type)
        if not factory:
            raise NotImplementedError(
                f"Delivery type not implemented yet: {delivery_type.value}"
            )
        return factory


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
    delivery_factory = DeliveryFactorySelector().select(delivery_type)
    delivery = delivery_factory.create()
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
