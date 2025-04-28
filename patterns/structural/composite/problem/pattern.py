"""
Решение задачи системы заказов через паттерн Composite
"""

from abc import ABC
from abc import abstractmethod
from typing import Union


class IOrderComponent(ABC):
    @abstractmethod
    def total(self) -> float:
        pass

    @abstractmethod
    def discount(self) -> float:
        pass


class Product(IOrderComponent):
    def __init__(
        self,
        id: str,
        price: float,
        discount_kf: float,
    ) -> None:
        self.id = id
        self.price = price
        self.discount_kf = discount_kf

    def total(self) -> float:
        return self.price * (1 - self.discount_kf)

    def discount(self) -> float:
        return self.price - self.total()


class ProductSet(IOrderComponent):
    def __init__(
        self,
        id: str,
        product: Product,
        quantity: int,
        price: float,
        discount_kf: float,
    ) -> None:
        self.id = id
        self.product = product
        self.quantity = quantity
        self.price = price
        self.discount_kf = discount_kf

    def total(self) -> float:
        return self.price * (1 - self.discount_kf)

    def discount(self) -> float:
        return (self.product.price * self.quantity) - self.total()


class OrderItem(IOrderComponent):
    def __init__(
        self,
        id: str,
        product: Product | ProductSet,
        quantity: int,
    ) -> None:
        self.id = id
        self.product = product
        self.quantity = quantity

    def total(self) -> float:
        return self.product.total() * self.quantity

    def discount(self) -> float:
        return self.product.discount() * self.quantity


class Order(IOrderComponent):
    def __init__(
        self,
        id: str,
        items: list[OrderItem],
    ) -> None:
        self.id = id
        self.items = items

    def add(self, item: OrderItem) -> None:
        self.items.append(item)

    def remove(self, id: str) -> OrderItem | None:
        search = [i for i, oi in enumerate(self.items) if oi.id == id]
        if search:
            return self.items.pop(search[0])
        return None

    def total(self) -> float:
        return sum(i.total() for i in self.items)

    def discount(self) -> float:
        return sum(i.discount() for i in self.items)


class OrderBox(IOrderComponent):
    def __init__(
        self,
        id: str,
        orders: list[Order],
    ) -> None:
        self.id = id
        self.orders = orders

    def add(self, order: Order) -> None:
        self.orders.append(order)

    def remove(self, id: str) -> Order | None:
        search = [i for i, o in enumerate(self.orders) if o.id == id]
        if search:
            return self.orders.pop(search[0])
        return None

    def total(self) -> float:
        return sum(o.total() for o in self.orders)

    def discount(self) -> float:
        return sum(o.discount() for o in self.orders)


def client_code():
    product1 = Product(id="p1", price=100.0, discount_kf=0.1)
    product2 = Product(id="p2", price=200.0, discount_kf=0.2)

    product_set = ProductSet(
        id="ps1",
        product=product1,
        quantity=3,
        price=270.0,
        discount_kf=0.1,
    )

    order_item1 = OrderItem(
        id="oi1",
        product=product1,
        quantity=2,
    )
    order_item2 = OrderItem(
        id="oi2",
        product=product_set,
        quantity=1,
    )
    order_item3 = OrderItem(
        id="oi3",
        product=product2,
        quantity=3,
    )

    order1 = Order(id="o1", items=[order_item1, order_item2])
    order2 = Order(id="o2", items=[order_item3])

    order_box = OrderBox(id="box1", orders=[order1, order2])

    print(f"Total: {order_box.total()}")
    print(f"Discount: {order_box.discount()}")


if __name__ == "__main__":
    client_code()
