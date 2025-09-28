from typing import Dict, Optional
from src.domain.aggregate import Order
from src.domain.repository import IOrderRepository


class InMemoryOrderRepository(IOrderRepository):
    def __init__(self):
        self._orders: Dict[int, Order] = {}

    def save(self, order: Order) -> None:
        self._orders[order.order_id] = order

    def get_by_id(self, order_id: int) -> Optional[Order]:
        return self._orders.get(order_id)
