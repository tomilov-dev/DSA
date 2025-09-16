"""
Пример кода, который соблюдает принцип единственной ответственности (Single Responsibility Principle).
"""

from abc import ABC
from abc import abstractmethod


class IOrderValidator(ABC):
    @abstractmethod
    def validate(self, order: dict) -> None:
        """
        Проверяет корректность заказа.
        """

        pass


class BaseOrderValidator(IOrderValidator):
    def validate(self, order: dict) -> None:
        if not order.get("items"):
            raise ValueError("Заказ пустой")
        if not isinstance(order.get("total"), (int, float)):
            raise ValueError("Некорректная сумма заказа")


class ExtendedOrderValidator(BaseOrderValidator):
    def validate(self, order: dict) -> None:
        super().validate(order)
        if order["total"] <= 0:
            raise ValueError("Сумма заказа должна быть больше нуля")


class OtherOrderValidator(IOrderValidator):
    def validate(self, order: dict) -> None:
        print(order)
        if not order.get("items-column"):
            raise ValueError("Заказ пустой")
        if not isinstance(order.get("total"), (int, float)):
            raise ValueError("Некорректная сумма заказа")
        if order["total"] <= 0:
            raise ValueError("Сумма заказа должна быть больше нуля")


class IPaymentProcessor(ABC):
    @abstractmethod
    def process(self, order: dict) -> None:
        """
        Обрабатывает оплату заказа.
        """

        pass


class PaymentProcessor(IPaymentProcessor):
    def process(self, order: dict) -> None:
        print(f"Оплата заказа на сумму {order['total']} прошла успешно.")


class IOrderRepository(ABC):
    @abstractmethod
    def save(self, order: dict) -> None:
        """
        Сохраняет заказ в базу данных.
        """

        pass


class OrderRepository(IOrderRepository):
    def save(self, order: dict) -> None:
        print(f"Заказ сохранён: {order}")


class IEmailSender(ABC):
    @abstractmethod
    def send_confirmation(self, user: dict, order: dict) -> None:
        """
        Отправляет пользователю письмо с подтверждением заказа.
        """

        pass


class EmailSender(IEmailSender):
    def send_confirmation(self, user: dict, order: dict) -> None:
        print(f"Письмо отправлено на {user['email']} с подтверждением заказа.")


class OrderService:
    def __init__(
        self,
        validator: IOrderValidator,
        payment_processor: IPaymentProcessor,
        repository: IOrderRepository,
        email_sender: IEmailSender,
    ) -> None:
        """
        Сервис для обработки заказа.
        """

        self.validator = validator
        self.payment_processor = payment_processor
        self.repository = repository
        self.email_sender = email_sender

    def process(self, order: dict, user: dict) -> None:
        """
        Обрабатывает заказ: проверяет, оплачивает, сохраняет и отправляет подтверждение.
        """

        self.validator.validate(order)
        self.payment_processor.process(order)
        self.repository.save(order)
        self.email_sender.send_confirmation(user, order)


def process1() -> None:
    order = {"items": ["яблоко", "банан"], "total": 150}
    user = {"email": "user@example.com", "name": "Иван"}

    validator = BaseOrderValidator()
    # validator = ExtendedOrderValidator()

    payment_processor = PaymentProcessor()
    repository = OrderRepository()
    email_sender = EmailSender()
    service = OrderService(validator, payment_processor, repository, email_sender)
    service.process(order, user)


def process2() -> None:
    order = {"items-column": ["яблоко", "банан"], "total": 150}
    user = {"email": "user@example.com", "name": "Иван"}

    validator = OtherOrderValidator()
    payment_processor = PaymentProcessor()
    repository = OrderRepository()
    email_sender = EmailSender()
    service = OrderService(validator, payment_processor, repository, email_sender)
    service.process(order, user)


if __name__ == "__main__":
    process1()
    process2()
