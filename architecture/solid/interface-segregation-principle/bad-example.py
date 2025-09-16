"""
Плохой пример: один интерфейс для всех видов уведомлений.
"""

from abc import ABC
from abc import abstractmethod


class INotifier(ABC):
    @abstractmethod
    def send_email(self, to: str, message: str) -> None:
        pass

    @abstractmethod
    def send_sms(self, to: str, message: str) -> None:
        pass

    @abstractmethod
    def send_push(self, to: str, message: str) -> None:
        pass


class EmailService(INotifier):
    def send_email(self, to: str, message: str) -> None:
        print(f"Отправили email на {to}: {message}")

    def send_sms(self, to: str, message: str) -> None:
        print("Ошибка: EmailService не поддерживает отправку SMS")
        raise NotImplementedError()

    def send_push(self, to: str, message: str) -> None:
        print("Ошибка: EmailService не поддерживает push-уведомления")
        raise NotImplementedError()


class SmsService(INotifier):
    def send_email(self, to: str, message: str) -> None:
        print("Ошибка: SmsService не поддерживает отправку email")
        raise NotImplementedError()

    def send_sms(self, to: str, message: str) -> None:
        print(f"Отправили SMS на {to}: {message}")

    def send_push(self, to: str, message: str) -> None:
        print("Ошибка: SmsService не поддерживает push-уведомления")
        raise NotImplementedError()


class PushService(INotifier):
    def send_email(self, to: str, message: str) -> None:
        print("Ошибка: PushService не поддерживает отправку email")
        raise NotImplementedError()

    def send_sms(self, to: str, message: str) -> None:
        print("Ошибка: PushService не поддерживает отправку SMS")
        raise NotImplementedError()

    def send_push(self, to: str, message: str) -> None:
        print(f"Отправили push на {to}: {message}")
