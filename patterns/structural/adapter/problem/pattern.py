"""
Решение задачи интеграции стороннего интерфейса в систему через паттерн Adapter
"""

from enum import Enum
from abc import ABC
from abc import abstractmethod


class MessangerType(str, Enum):
    INTERNAL = "Internal"
    EXTERNAL = "External"


## У нас есть интерфейс отправки уведомлений
class INotificationSender(ABC):
    @abstractmethod
    def send_message(self, recipient: str, message: str) -> None:
        pass


## Существует канал, который был реализован специально внутренний интерфейс
class InternalNotificationAPI(INotificationSender):
    def send_message(self, recipient: str, message: str) -> None:
        print(f'Sent message "{message}" to {recipient}')


## Необходимо добавить в систему канал, доступ к которому есть через стороннюю библиотеку
class ExternalNotificationAPI:
    def send(self, text: str, to: str) -> None:
        print(f"Message {text} was sent to {to}")


## Через Адаптер мы подстраиваем сторонний класс к нашему интерфейсу
class ExternalNotificationAPIAdapter(INotificationSender):
    def __init__(self, api: ExternalNotificationAPI) -> None:
        self.api = api

    def send_message(self, recipient: str, message: str) -> None:
        return self.api.send(message, recipient)


class NotificationSelector:
    def select(self, messanger_type: MessangerType) -> INotificationSender:
        match messanger_type:
            case MessangerType.INTERNAL:
                return InternalNotificationAPI()

            ## Все равно требуется выбор и настройка адаптера
            ## Но адаптер соответствует единому интерфейсу
            case MessangerType.EXTERNAL:
                return ExternalNotificationAPIAdapter(ExternalNotificationAPI())
            case _:
                raise NotImplementedError(
                    f"Messanger not implemented yet: {messanger_type}"
                )


def client_code(messanger_type: MessangerType):
    recipient = "Ivan"
    message = "Hello, World!"

    ## В клиенте теперь используется единый API - здесь ошибок быть не может
    client = NotificationSelector().select(messanger_type)
    client.send_message(recipient, message)


if __name__ == "__main__":
    client_code(MessangerType.EXTERNAL)
