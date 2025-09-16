"""
Лучший пример: один интерфейс для всех видов уведомлений.
"""

from abc import ABC
from abc import abstractmethod


class INotifier(ABC):
    @abstractmethod
    def send(self, to: str, message: str) -> None:
        pass


class EmailService(INotifier):
    def send(self, to: str, message: str) -> None:
        print(f"Отправили email на {to}: {message}")


class SmsService(INotifier):
    def send(self, to: str, message: str) -> None:
        print(f"Отправили SMS на {to}: {message}")


class PushService(INotifier):
    def send(self, to: str, message: str) -> None:
        print(f"Отправили push на {to}: {message}")


class CompositeNotifier(INotifier):
    def __init__(self, notifiers: list[INotifier]) -> None:
        self._notifiers = notifiers

    def send(self, to: str, message: str) -> None:
        for notifier in self._notifiers:
            notifier.send(to, message)
