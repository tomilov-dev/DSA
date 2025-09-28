from .aggregate import Order


class OrderService:
    @staticmethod
    def can_place_order(order: Order) -> bool:
        return order.address.is_valid() and len(order.items) > 0
