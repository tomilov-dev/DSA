from abc import ABC
from abc import abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, message: str) -> None:
        pass


class User(Observer):
    def __init__(self, name: str, chat_room: "ChatRoom") -> None:
        self.name = name
        self.chat_room = chat_room

    def update(self, message: str) -> None:
        print(f"{self.name} received message: {message}")

    def send_message(self, message: str) -> None:
        self.chat_room.send_message(message)


class ChatRoom:
    def __init__(self) -> None:
        self.observers: list[Observer] = []

    def send_message(self, message: str) -> None:
        self.notify_observers(message)

    def register_observer(self, observer: Observer) -> None:
        self.observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        self.observers.remove(observer)

    def notify_observers(self, message: str) -> None:
        for observer in self.observers:
            observer.update(message)


def client_code():
    chat_room = ChatRoom()

    user1 = User("Alice", chat_room)
    user2 = User("Bob", chat_room)

    chat_room.register_observer(user1)
    chat_room.register_observer(user2)

    user1.send_message("Hello, everyone!")

    chat_room.remove_observer(user1)

    user2.send_message("Goodbye, Alice!")
