from abc import ABC
from abc import abstractmethod


class TaxStrategy(ABC):
    @abstractmethod
    def calculate_tax(self, price: float) -> float:
        pass


class FoodTaxStrategy(TaxStrategy):
    def calculate_tax(self, price: float) -> float:
        return price * 0.05


class ElectronicsTaxStrategy(TaxStrategy):
    def calculate_tax(self, price: float) -> float:
        return price * 0.08


class ClothingTaxStrategy(TaxStrategy):
    def calculate_tax(self, price: float) -> float:
        return price * 0.03


class TaxCalculator:
    def __init__(self, strategy: TaxStrategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: TaxStrategy) -> None:
        self._strategy = strategy

    def calculate_tax(self, price: float) -> float:
        return self._strategy.calculate_tax(price)


def client_code():
    calculator = TaxCalculator(FoodTaxStrategy())

    tax = calculator.calculate_tax(price=100)
    print(tax)

    calculator.set_strategy(ElectronicsTaxStrategy())
    tax = calculator.calculate_tax(price=100)
    print(tax)

    # Установка стратегии налога на одежду
    calculator.set_strategy(ClothingTaxStrategy())
    tax = calculator.calculate_tax(price=100)
    print(tax)
