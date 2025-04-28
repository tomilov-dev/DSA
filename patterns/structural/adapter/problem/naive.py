"""
Решение задачи интеграции стороннего интерфейса в систему (наивный подход)
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
    def send_message(
        self,
        recipient: str,
        message: str,
    ) -> None:
        pass


## Существует канал, который был реализован специально внутренний интерфейс
class InternalNotificationAPI(INotificationSender):
    def send_message(self, recipient: str, message: str):
        print(f'Sent message "{message}" to {recipient}')


## Необходимо добавить в систему канал, доступ к которому есть через стороннюю библиотеку
class ExternalNotificationAPI:
    def send(self, text: str, to: str) -> None:
        print(f"Message {text} was sent to {to}")


def client_code(messanger_type: MessangerType):
    recipient = "Ivan"
    message = "Hello, World!"
    match messanger_type:
        case MessangerType.INTERNAL:
            client = InternalNotificationAPI()
            client.send_message(recipient, message)

        ## Каждый новый канал требует учета особенностей собственной реализации
        case MessangerType.EXTERNAL:
            client = ExternalNotificationAPI()
            client.send(message, recipient)
        case _:
            raise NotImplementedError(
                f"Messanger not implemented yet: {messanger_type}"
            )


if __name__ == "__main__":
    client_code(MessangerType.INTERNAL)
