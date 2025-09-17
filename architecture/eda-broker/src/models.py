from abc import ABC
from abc import abstractmethod
from typing import Any


class InvalidJsonError(Exception):
    pass


class EventModel(ABC):
    @abstractmethod
    def to_dict(self) -> dict:
        pass

    @staticmethod
    @abstractmethod
    def from_dict(data: dict[str, Any]) -> "EventModel":
        pass


def validate_json(data: dict[str, Any], keys: list[str]) -> None:
    missing = []
    for key in keys:
        if key not in data:
            missing.append(key)
    if len(missing) > 0:
        msg = "Отсутствуют следующие данные:" + ", ".join(missing)
        raise InvalidJsonError(msg)


class Product(EventModel):
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def to_dict(self) -> dict:
        return {"name": self.name, "price": self.price}

    @staticmethod
    def from_dict(data: dict[str, Any]) -> "Product":
        validate_json(data, ["name", "price"])
        return Product(
            name=data["name"],
            price=data["price"],
        )


class OrderItem(EventModel):
    def __init__(self, product: Product, quantity: int) -> None:
        self.product = product
        self.quantity = quantity

    def to_dict(self) -> dict:
        return {"product": self.product.to_dict, "quantity": self.quantity}

    @staticmethod
    def from_dict(data: dict[str, Any]) -> "OrderItem":
        validate_json(data, ["product", "quantity"])
        return OrderItem(
            product=Product.from_dict(data["product"]),
            quantity=data["quantity"],
        )


class Order(EventModel):
    def __init__(self, id: str, items: list[OrderItem]) -> None:
        self.id = id
        self.items = items

    def to_dict(self) -> dict:
        return {"id": self.id, "items": [item.to_dict() for item in self.items]}

    @staticmethod
    def from_dict(data: dict[str, Any]) -> "Order":
        validate_json(data, ["id", "items"])
        return Order(
            id=data["id"],
            items=[OrderItem.from_dict(item) for item in data["items"]],
        )
