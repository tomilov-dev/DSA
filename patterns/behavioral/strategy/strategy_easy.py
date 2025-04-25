from abc import ABC
from abc import abstractmethod


class DeliveryCostStrategy(ABC):
    @abstractmethod
    def calculate_cost(self, order_weight: float) -> float:
        pass


class PickupStrategy(DeliveryCostStrategy):
    def calculate_cost(self, order_weight: float) -> float:
        return 0


class StandardDeliveryStrategy(DeliveryCostStrategy):
    def calculate_cost(self, order_weight: float) -> float:
        return order_weight * 1.2


class ExpressDeliveryStrategy(DeliveryCostStrategy):
    def calculate_cost(self, order_weight: float) -> float:
        return order_weight * 1.5


class DeliveryCostCalculator:
    def __init__(self, strategy: DeliveryCostStrategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: DeliveryCostStrategy) -> None:
        self._strategy = strategy

    def calculate_cost(self, order_weight: float) -> float:
        return self._strategy.calculate_cost(order_weight)


def client_code():
    calculator = DeliveryCostCalculator(PickupStrategy())

    cost = calculator.calculate_cost(order_weight=5)
    print(cost)

    calculator.set_strategy(StandardDeliveryStrategy())
    cost = calculator.calculate_cost(order_weight=5)
    print(cost)

    # Установка стратегии экспресс-доставки
    calculator.set_strategy(ExpressDeliveryStrategy())
    cost = calculator.calculate_cost(order_weight=5)
    print(cost)
