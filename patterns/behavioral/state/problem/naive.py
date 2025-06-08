"""
Решение задачи реализации банкомата ATM (наивный подход)
"""


class ATMBank:
    def __init__(self, amount: int) -> None:
        self.amount = amount

        self._inserted: bool = False
        self._inserted_pin: int | None = None
        self._pin_passed: bool = False

    def null_state(self) -> None:
        self._inserted = False
        self._inserted_pin = False
        self._pin_passed = False

    def insert(self, pin: int) -> None:
        if self._inserted:
            print("Card already inserted")
            self.eject()
        else:
            print("Card inserted")
            self._inserted = True
            self._inserted_pin = pin

    def pin(self, code: int) -> None:
        if not self._inserted:
            print("Card not inserted")
            self.null_state()
        elif not self._inserted_pin:
            print("Error: card has not pin")
            self.eject()
        elif self._inserted_pin != code:
            print("Error: wrong pin")
            self.eject()
        else:
            self._pin_passed = True

    def withdraw(self, amount: int) -> None:
        if not self._inserted:
            print("Card not inserted")
            self.null_state()
        elif not self._pin_passed:
            print("Pin not passed")
            self.eject()
        elif self.amount < amount:
            print("Amount too large")
            self.eject()
        else:
            self.amount -= amount
            self.eject()

    def eject(self) -> None:
        if not self._inserted:
            print("Card not inserted yet")
        else:
            print("Card ejected")
        self.null_state()


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
