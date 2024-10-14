from abc import ABC
from abc import abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate_discount(self, order_total: float) -> float:
        pass


class NoDiscountStrategy(DiscountStrategy):
    def calculate_discount(self, order_total: float) -> float:
        return 0


class PercentageDiscountStrategy(DiscountStrategy):
    def __init__(self, percentage: float) -> None:
        self._percentage = percentage

    def calculate_discount(self, order_total: float) -> float:
        return order_total * (self._percentage / 100)


class FixedAmountDiscountStrategy(DiscountStrategy):
    def __init__(self, amount: float) -> None:
        self._amount = amount

    def calculate_discount(self, order_total: float) -> float:
        return self._amount if order_total >= 1000 else 0


class TieredDiscountStrategy(DiscountStrategy):
    def calculate_discount(self, order_total: float) -> float:
        if order_total < 100:
            return order_total * 0.05
        if order_total < 500:
            return order_total * 0.10
        if order_total < 1000:
            return order_total * 0.15
        return order_total * 0.20


class DiscountCalculator:
    def __init__(self, strategy: DiscountStrategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: DiscountStrategy) -> None:
        self._strategy = strategy

    def calculate_discount(self, order_total: float) -> float:
        return self._strategy.calculate_discount(order_total)


def client_code():
    calculator = DiscountCalculator(NoDiscountStrategy())

    discount = calculator.calculate_discount(order_total=150)
    print(discount)

    calculator.set_strategy(PercentageDiscountStrategy(percentage=10))
    discount = calculator.calculate_discount(order_total=150)
    print(discount)

    calculator.set_strategy(FixedAmountDiscountStrategy(amount=20))
    discount = calculator.calculate_discount(order_total=150)
    print(discount)

    discount = calculator.calculate_discount(order_total=1200)
    print(discount)

    calculator.set_strategy(TieredDiscountStrategy())
    discount = calculator.calculate_discount(order_total=150)
    print(discount)
