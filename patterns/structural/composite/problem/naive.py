"""
Решение задачи системы заказов (наивный подход)
"""

from abc import ABC
from abc import abstractmethod
from typing import Union


## Есть система заказов - от товара до коробки заказов
class Product:
    def __init__(
        self,
        id: str,
        name: str,
        price: int,
    ) -> None:
        self.id = id
        self.name = name
        self.price = price


class ProductSet:
    def __init__(
        self,
        id: str,
        product: Product,
        quantity: int,
        price: int,
    ) -> int:
        self.id = id
        self.product = product
        self.quantity = quantity
        self.price = price

    def discount(self) -> int:
        return (self.product.price * self.quantity) - self.price


class OrderItem:
    def __init__(
        self,
        id: str,
        product: Product,
        quantity: int,
    ) -> None:
        self.id = id
        self.product = product
        self.quantity = quantity

    def total(self) -> int:
        return self.product.price * self.quantity


class Order:
    def __init__(
        self,
        id: str,
        items: list[OrderItem],
        discount_kf: float = 0,
    ) -> None:
        self.id = id
        self.items = items
        self.discount_kf = discount_kf

    def discount(self) -> float:
        if self.discount_kf == 0:
            return 0
        return self.discount_kf * sum(
            i.total() for i in self.items if not isinstance(i.product, ProductSet)
        )

    def total(self) -> float:
        return (1 - self.discount_kf) * sum(
            i.total() for i in self.items if not isinstance(i.product, ProductSet)
        )


class OrderBox:
    def __init__(
        self,
        id: str,
        orders: list[Order],
    ) -> None:
        self.id = id
        self.orders = orders

    def total(self) -> int:
        return sum(o.total() for o in self.orders)


def client_code():
    p1 = Product("P1", "P1", 1)
    p2 = Product("P2", "P2", 6)
    p3 = Product("P3", "P3", 2)
    p4 = Product("P4", "P4", 4)
    ps1 = ProductSet("PS1", p4, 2, 7)

    order1 = Order(
        "O1",
        [
            OrderItem("OI1", p1, 2),
            OrderItem("OI2", p2, 5),
            OrderItem("OI3", p3, 4),
        ],
    )
    order2 = Order(
        "O2",
        [
            OrderItem("OI4", p2, 4),
            OrderItem("OI5", p3, 7),
            OrderItem("OI6", p4, 5),
            OrderItem("OI7", ps1, 1),
        ],
    )

    order_box = OrderBox("OB1", [order1, order2])
    print(order_box.total())


if __name__ == "__main__":
    client_code()
