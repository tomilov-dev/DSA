from abc import ABC
from abc import abstractmethod
from enum import Enum


class OrderStatus(Enum, str):
    NEW = "new"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"


class EmptyOrderError(Exception):
    pass


class IProduct(ABC):
    def __init__(
        self,
        id: str,
        name: str,
        price: float,
    ) -> None:
        self.id = id
        self.name = name
        self.price = price


class Product(IProduct):
    pass


class IOrderItem(ABC):
    def __init__(
        self,
        product: IProduct,
        quantity: int,
    ) -> None:
        self.product = product
        self.quantity = quantity


class OrderItem(IOrderItem):
    pass


class IOrder(ABC):
    def __init__(
        self,
        order_id: str,
        items: list[IOrderItem],
    ) -> None:
        self.order_id = order_id
        self.items = items
        self.status = OrderStatus.NEW

    @abstractmethod
    def confirm(self) -> None:
        pass

    @abstractmethod
    def cancel(self) -> None:
        pass


class Order(IOrder):
    def confirm(self) -> None:
        if not self.items:
            raise EmptyOrderError("В заказе должна быть хотя бы одна позиция")
        self.status = OrderStatus.CONFIRMED

    def cancel(self) -> None:
        self.status = OrderStatus.CANCELLED
