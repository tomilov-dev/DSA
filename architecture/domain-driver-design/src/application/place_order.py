from src.domain.aggregate import Order
from src.domain.service import OrderService
from src.domain.event import OrderPlacedEvent
from src.infrastructure.in_memory_repository import InMemoryOrderRepository
from datetime import datetime


class PlaceOrderUseCase:
    def __init__(self, repository: InMemoryOrderRepository):
        self.repository = repository

    def execute(self, order: Order) -> OrderPlacedEvent:
        if not OrderService.can_place_order(order):
            raise ValueError("Order is not valid")
        self.repository.save(order)
        return OrderPlacedEvent(order_id=order.order_id, occurred_on=datetime.now())
