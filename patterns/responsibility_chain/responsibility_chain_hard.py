from abc import ABC, abstractmethod
from typing import Optional


class IHandler(ABC):
    def __init__(self) -> None:
        self._next: Optional[IHandler] = None

    def set_next(self, handler: "IHandler") -> None:
        self._next = handler

    @abstractmethod
    def handle(self, request: dict) -> None:
        pass


class OrderValidationHandler(IHandler):
    def handle(self, request: dict) -> None:
        if (
            "order_id" in request
            and "product_id" in request
            and "quantity" in request
            and "user_id" in request
        ):
            print("Order is valid")
            if self._next:
                self._next.handle(request)
        else:
            print("Order validation failed")


class InventoryCheckHandler(IHandler):
    def handle(self, request: dict) -> None:
        if self.check_inventory(request["product_id"], request["quantity"]):
            print("Inventory check passed")
            if self._next:
                self._next.handle(request)
        else:
            print("Inventory check failed")

    def check_inventory(self, product_id: int, quantity: int) -> bool:
        return True


class PaymentProcessingHandler(IHandler):
    def handle(self, request: dict) -> None:
        if request.get("payment_status") == "paid":
            print("Payment processed successfully")
            if self._next:
                self._next.handle(request)
        else:
            print("Payment processing failed")


class ShippingHandler(IHandler):
    def handle(self, request: dict) -> None:
        if self.process_shipping(request):
            print("Shipping processed successfully")
        else:
            print("Shipping processing failed")

    def process_shipping(self, request: dict) -> bool:
        return True


def client_code():
    validation_handler = OrderValidationHandler()
    inventory_handler = InventoryCheckHandler()
    payment_handler = PaymentProcessingHandler()
    shipping_handler = ShippingHandler()

    validation_handler.set_next(inventory_handler)
    inventory_handler.set_next(payment_handler)
    payment_handler.set_next(shipping_handler)

    order1 = {
        "order_id": 1,
        "product_id": 101,
        "quantity": 2,
        "user_id": 1001,
        "payment_status": "paid",
    }
    order2 = {
        "order_id": 2,
        "product_id": 102,
        "quantity": 1,
        "user_id": 1002,
        "payment_status": "unpaid",
    }
    order3 = {
        "order_id": 3,
        "product_id": 103,
        "quantity": 5,
        "user_id": 1003,
        "payment_status": "paid",
    }
    order4 = {
        "order_id": 4,
        "product_id": 104,
        "quantity": 3,
        "user_id": 1004,
        "payment_status": "paid",
    }

    validation_handler.handle(order1)
    validation_handler.handle(order2)
    validation_handler.handle(order3)
    validation_handler.handle(order4)
