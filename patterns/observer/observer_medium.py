from abc import ABC
from abc import abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, news: str) -> None:
        pass


class Subscriber(Observer):
    def __init__(self, name: str) -> None:
        self.name = name

    def update(self, news: str) -> None:
        print("Subscriber received news:", news)


class NewsPublisher:
    def __init__(self) -> None:
        self.observers: list[Observer] = []

    def publish_news(self, news: str) -> None:
        self.notify_observers(news)

    def register_observer(self, observer: Observer) -> None:
        self.observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        self.observers.remove(observer)

    def notify_observers(self, news: str) -> None:
        for observer in self.observers:
            observer.update(news)


def client_code():
    news_publisher = NewsPublisher()

    subscriber1 = Subscriber("Alice")
    subscriber2 = Subscriber("Bob")

    news_publisher.register_observer(subscriber1)
    news_publisher.register_observer(subscriber2)

    news_publisher.publish_news("Breaking News: New Observer Pattern Example Released!")

    news_publisher.remove_observer(subscriber1)

    news_publisher.publish_news("Update: Observer Pattern Example Improved!")
