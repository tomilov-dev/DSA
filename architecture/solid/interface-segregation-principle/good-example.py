"""
Хороший пример: отдельные интерфейсы для каждого типа уведомлений.
"""

from abc import ABC
from abc import abstractmethod


class IEmailSender(ABC):
    @abstractmethod
    def send_email(self, to: str, message: str) -> None:
        pass


class ISmsSender(ABC):
    @abstractmethod
    def send_sms(self, to: str, message: str) -> None:
        pass


class IPushSender(ABC):
    @abstractmethod
    def send_push(self, to: str, message: str) -> None:
        pass


class EmailService(IEmailSender):
    def send_email(self, to: str, message: str) -> None:
        print(f"Отправили email на {to}: {message}")


class SmsService(ISmsSender):
    def send_sms(self, to: str, message: str) -> None:
        print(f"Отправили SMS на {to}: {message}")


class PushService(IPushSender):
    def send_push(self, to: str, message: str) -> None:
        print(f"Отправили push на {to}: {message}")
