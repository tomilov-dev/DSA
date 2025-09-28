from typing import List
from .entity import OrderItem, Customer
from .value_object import Address


class Order:
    def __init__(
        self,
        order_id: int,
        customer: Customer,
        address: Address,
        items: List[OrderItem],
    ):
        self.order_id = order_id
        self.customer = customer
        self.address = address
        self.items = items

    def add_item(self, item: OrderItem) -> None:
        self.items.append(item)

    def change_address(self, new_address: Address) -> None:
        if new_address.is_valid():
            self.address = new_address

    @property
    def total(self) -> int:
        return sum(item.quantity for item in self.items)
