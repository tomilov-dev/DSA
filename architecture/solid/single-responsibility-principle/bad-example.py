"""
Пример кода, который нарушает принцип единственной ответственности (Single Responsibility Principle).
"""


class OrderProcessor:
    def __init__(self, order: dict, user: dict) -> None:
        """
        Инициализация процессора заказа с заказом и пользователем.
        """

        self.order = order
        self.user = user

    def validate_order(self) -> None:
        """
        Проверяет корректность заказа.
        """

        if not self.order.get("items"):
            raise ValueError("Заказ пустой")
        if not isinstance(self.order.get("total"), (int, float)):
            raise ValueError("Некорректная сумма заказа")

    def process_payment(self) -> None:
        """
        Обрабатывает оплату заказа.
        """

        print(
            f"Оплата заказа на сумму {self.order['total']} от пользователя {self.user['email']} прошла успешно."
        )

    def save_order(self) -> None:
        """
        Сохраняет заказ в базу данных.
        """

        print(f"Заказ сохранён: {self.order}")

    def send_confirmation_email(self) -> None:
        """
        Отправляет пользователю письмо с подтверждением заказа.
        """

        print(f"Письмо отправлено на {self.user['email']} с подтверждением заказа.")

    def process(self) -> None:
        """
        Полный процесс обработки заказа.
        """

        self.validate_order()
        self.process_payment()
        self.save_order()
        self.send_confirmation_email()


def process() -> None:
    order = {"items": ["яблоко", "банан"], "total": 150}
    user = {"email": "user@example.com", "name": "Иван"}
    processor = OrderProcessor(order, user)
    processor.process()


if __name__ == "__main__":
    process()
