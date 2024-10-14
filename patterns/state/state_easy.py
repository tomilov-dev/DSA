from abc import ABC
from abc import abstractmethod


class OrderState(ABC):
    @abstractmethod
    def handle(self, context: "OrderContext") -> None:
        pass


class NewOrderState(OrderState):
    def handle(self, context: "OrderContext") -> None:
        print("NewOrderState")
        context.set_state(ProcessingOrderState())


class ProcessingOrderState(OrderState):
    def handle(self, context: "OrderContext") -> None:
        print("ProcessingOrderState")
        context.set_state(ShippedOrderState())


class ShippedOrderState(OrderState):
    def handle(self, context: "OrderContext") -> None:
        print("ShippedOrderState")
        context.set_state(DeliveredOrderState())


class DeliveredOrderState(OrderState):
    def handle(self, context: "OrderContext") -> None:
        print("DeliveredOrderState")


class OrderContext:
    def __init__(self) -> None:
        self._state = None

    def set_state(self, state: OrderState) -> None:
        self._state = state

    def request(self) -> None:
        if not self._state:
            raise ValueError("State is not set")

        self._state.handle(self)


def client_code():
    order = OrderContext()
    order.request()
    order.request()
    order.request()
    order.request()
