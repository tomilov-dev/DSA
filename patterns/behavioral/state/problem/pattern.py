"""
Решение задачи реализации банкомата ATM через паттерн State
"""

from abc import ABC
from abc import abstractmethod


class IState(ABC):
    def __init__(self, bank: "ATMBank") -> None:
        self.bank = bank

    @abstractmethod
    def insert(self, pin: int) -> None:
        pass

    @abstractmethod
    def pin(self, code: int) -> None:
        pass

    @abstractmethod
    def withdraw(self, amount: int) -> None:
        pass

    @abstractmethod
    def eject(self) -> None:
        pass


class NullState(IState):
    def insert(self, pin: int) -> None:
        self.bank.state = CardInserted(self.bank)
        self.bank.set_pin(pin)
        print("Card inserted")

    def pin(self, code: int) -> None:
        print("Card not inserted")

    def withdraw(self, amount: int) -> None:
        print("Card not inserted")

    def eject(self) -> None:
        print("Card not inserted")


class CardInserted(IState):
    def insert(self, pin: int) -> None:
        print("Card already inserted")

    def pin(self, code: int) -> None:
        if self.bank.get_pin() != code:
            print("Pin code is wrong")
            return None

        self.bank.state = PinCodeCorrect(self.bank)
        print("Pin code is correct")

    def withdraw(self, amount: int) -> None:
        print("Pin code not passed")

    def eject(self) -> None:
        self.bank.state = NullState(self.bank)
        print("Card ejected")


class PinCodeCorrect(CardInserted):
    def pin(self, code: int) -> None:
        print("Pin already correct")

    def withdraw(self, amount: int) -> None:
        if self.bank.amount < amount:
            print("Amount is too large")
            return None

        self.bank.amount -= amount
        print("Amount withdrawed")


class ATMBank:
    def __init__(self, amount: int) -> None:
        self.amount = amount
        self.state: IState = NullState(self)
        self._pin: int | None = None

    def set_pin(self, pin: int | None) -> None:
        self._pin = pin

    def get_pin(self) -> int | None:
        return self._pin

    def insert(self, pin: int) -> None:
        self.state.insert(pin)

    def pin(self, code: int) -> None:
        self.state.pin(code)

    def withdraw(self, amount: int) -> None:
        self.state.withdraw(amount)

    def eject(self) -> None:
        self.state.eject()


def client_code():
    bank = ATMBank(10000)

    print("\n--- Попытка снять деньги без карты ---")
    bank.withdraw(100)

    print("\n--- Вставка карты с PIN 1234 ---")
    bank.insert(1234)

    print("\n--- Ввод неправильного PIN ---")
    bank.pin(1111)

    print("\n--- Вставка карты снова (после извлечения) ---")
    bank.insert(1234)

    print("\n--- Ввод правильного PIN ---")
    bank.pin(1234)

    print("\n--- Попытка снять слишком большую сумму ---")
    bank.withdraw(20000)

    print("\n--- Снятие 5000 ---")
    bank.insert(1234)
    bank.pin(1234)
    bank.withdraw(5000)

    print("\n--- Попытка снять ещё 6000 (остаток 5000) ---")
    bank.insert(1234)
    bank.pin(1234)
    bank.withdraw(6000)

    print("\n--- Снятие оставшихся 5000 ---")
    bank.insert(1234)
    bank.pin(1234)
    bank.withdraw(5000)


if __name__ == "__main__":
    client_code()
