from abc import ABC
from abc import abstractmethod


class OrderContext:
    def __init__(self) -> None:
        self._state: OrderState = NewOrderState()  # Устанавливаем начальное состояние

    def set_state(self, state: "OrderState") -> None:
        self._state = state

    def process(self) -> None:
        self._state.process(self)

    def ship(self) -> None:
        self._state.ship(self)

    def deliver(self) -> None:
        self._state.deliver(self)

    def return_order(self) -> None:
        self._state.return_order(self)

    def cancel(self) -> None:
        self._state.cancel(self)


class OrderState(ABC):
    @abstractmethod
    def process(self, context: OrderContext) -> None:
        pass

    @abstractmethod
    def ship(self, context: OrderContext) -> None:
        pass

    @abstractmethod
    def deliver(self, context: OrderContext) -> None:
        pass

    @abstractmethod
    def return_order(self, context: OrderContext) -> None:
        pass

    @abstractmethod
    def cancel(self, context: OrderContext) -> None:
        pass


class BaseOrderState(OrderState):
    def reason(self) -> str:
        return ""

    def process(self, context: OrderContext) -> None:
        print("Cannot process order because", self.reason())

    def ship(self, context: OrderContext) -> None:
        print("Cannot ship order because", self.reason())

    def deliver(self, context: OrderContext) -> None:
        print("Cannot deliver order because", self.reason())

    def return_order(self, context: OrderContext) -> None:
        print("Cannot return order order because", self.reason())

    def cancel(self, context: OrderContext) -> None:
        print("Order cancelled")
        context.set_state(CancelledOrderState())


class NewOrderState(BaseOrderState):
    def reason(self) -> str:
        return "it state is new"

    def process(self, context: OrderContext) -> None:
        print("Process order")
        context.set_state(ProcessingOrderState())

    def ship(self, context: OrderContext) -> None:
        print("Ship order")
        context.set_state(ShippedOrderState())

    def deliver(self, context: OrderContext) -> None:
        print("Deliver order")
        context.set_state(DeliveredOrderState())

    def return_order(self, context: OrderContext) -> None:
        print("Return order")
        context.set_state(ReturnedOrderState())


class ProcessingOrderState(BaseOrderState):
    def reason(self) -> str:
        return "it state is new"

    def ship(self, context: OrderContext) -> None:
        print("Ship order")
        context.set_state(ShippedOrderState())

    def deliver(self, context: OrderContext) -> None:
        print("Deliver order")
        context.set_state(DeliveredOrderState())

    def return_order(self, context: OrderContext) -> None:
        print("Return order")
        context.set_state(ReturnedOrderState())


class ShippedOrderState(BaseOrderState):
    def reason(self) -> str:
        return "it state is shipped"

    def deliver(self, context: OrderContext) -> None:
        print("Deliver order")
        context.set_state(DeliveredOrderState())

    def return_order(self, context: OrderContext) -> None:
        print("Return order")
        context.set_state(ReturnedOrderState())


class DeliveredOrderState(BaseOrderState):
    def reason(self) -> str:
        return "it state is delivered"

    def return_order(self, context: OrderContext) -> None:
        print("Return order")
        context.set_state(ReturnedOrderState())

    def cancel(self, context: OrderContext) -> None:
        print("Cannot cancel order because", self.reason())


class CancelledOrderState(BaseOrderState):
    def reason(self) -> str:
        return "it state is delivered"

    def cancel(self, context: OrderContext) -> None:
        print("Cannot cancel order because", self.reason())


class ReturnedOrderState(BaseOrderState):
    def reason(self) -> str:
        return "it state is returned"

    def return_order(self, context: OrderContext) -> None:
        print("Cannot cancel order because", self.reason())

    def cancel(self, context: OrderContext) -> None:
        print("Cannot cancel order because", self.reason())


def client_code():
    order = OrderContext()

    print("Initial state: NewOrderState")
    order.process()
    order.ship()
    order.deliver()
    order.return_order()
    order.cancel()
