from abc import ABC
from abc import abstractmethod


class TradingSignal:
    def __init__(self, call: str, share_name: str, price: float) -> None:
        self.call = call
        self.share_name = share_name
        self.price = price

    def __str__(self) -> str:
        return f"{self.call} - {self.share_name} - {self.price}"


class Observer(ABC):
    @abstractmethod
    def update(self, signal: TradingSignal) -> None:
        pass


class TradingSignalPublisher:
    def __init__(self) -> None:
        self.observers: list[Observer] = []

    def publish_signal(self, signal: TradingSignal) -> None:
        self.notify_observers(signal)

    def register_observer(self, observer: Observer) -> None:
        self.observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        self.observers.remove(observer)

    def notify_observers(self, signal: TradingSignal) -> None:
        for observer in self.observers:
            observer.update(signal)


class Trader(Observer):
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name

    def update(self, signal: TradingSignal) -> None:
        print("Trader received signal:", signal)


class TradingStrategy(Observer):
    def __init__(self, name: str) -> None:
        self.name = name

    def update(self, signal: TradingSignal) -> None:
        print("TradingStrategy received signal:", signal)


def client_code():
    signal_publisher = TradingSignalPublisher()

    trader1 = Trader(1, "Alice")
    trader2 = Trader(2, "Bob")
    strategy1 = TradingStrategy("Strategy A")

    signal_publisher.register_observer(trader1)
    signal_publisher.register_observer(trader2)
    signal_publisher.register_observer(strategy1)

    signal = TradingSignal("BUY", "AAPL", 150.0)
    signal_publisher.publish_signal(signal)

    signal_publisher.remove_observer(trader1)

    signal = TradingSignal("SELL", "GOOGL", 2800.0)
    signal_publisher.publish_signal(signal)
