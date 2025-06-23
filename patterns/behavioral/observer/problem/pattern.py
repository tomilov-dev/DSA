"""
Решение задачи реализации системы умного дома через паттерн Observer
"""

from abc import ABC
from abc import abstractmethod


class ITemperatureSensorSubscriber(ABC):
    @abstractmethod
    def temperature_update(self, value: int) -> None:
        pass


class TemperatureSensor:
    def __init__(self, t: int, subs: list[ITemperatureSensorSubscriber]) -> None:
        self.subs = subs
        self._t = t

    def subscribe(self, sub: ITemperatureSensorSubscriber) -> None:
        self.subs.append(sub)

    def unsubscribe(self, sub: ITemperatureSensorSubscriber) -> None:
        self.subs.pop(self.subs.index(sub))

    def get(self) -> int:
        return self._t

    def set(self, value: int) -> None:
        self._t = value
        for sub in self.subs:
            sub.temperature_update(value)


class AirCondition(ITemperatureSensorSubscriber):
    def on(self) -> None:
        print("AC turned on")

    def off(self) -> None:
        print("AC turned off")

    def temperature_update(self, t: int) -> None:
        if t <= 18:
            self.on()
        else:
            self.off()


class Heater(ITemperatureSensorSubscriber):
    def on(self) -> None:
        print("Heater turned on")

    def off(self) -> None:
        print("Heater turned off")

    def temperature_update(self, t: int) -> None:
        if t <= 18:
            self.off()
        else:
            self.on()


class MobileApp(ITemperatureSensorSubscriber):
    def temperature_notification(self, t: int) -> None:
        print(f"Temperature changed to {t}")

    def temperature_update(self, t: int) -> None:
        self.temperature_notification(t)


def client_code():
    ac = AirCondition()
    heater = Heater()
    app = MobileApp()

    ts = TemperatureSensor(20, [ac, heater, app])
    ts.set(15)
    ts.set(25)


if __name__ == "__main__":
    client_code()
