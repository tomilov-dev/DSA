"""
Решение задачи реализации системы умного дома (наивный подход)
"""

from typing import Callable


class AirCondition:
    def on(self) -> None:
        print("AC turned on")

    def off(self) -> None:
        print("AC turned off")

    def ts_callback(self, t: int) -> None:
        if t <= 18:
            self.on()
        else:
            self.off()


class Heater:
    def on(self) -> None:
        print("Heater turned on")

    def off(self) -> None:
        print("Heater turned off")

    def ts_callback(self, t: int) -> None:
        if t <= 18:
            self.off()
        else:
            self.on()


class MobileApp:
    def temperature_notification(self, t: int) -> None:
        print(f"Temperature changed to {t}")

    def ts_callback(self, t: int) -> None:
        self.temperature_notification(t)


class TemperatureSensor:
    def __init__(
        self,
        t: int,
        ac_callback: Callable[[int], None],
        heater_callback: Callable[[int], None],
        app_callback: Callable[[int], None],
    ) -> None:
        self._t = t
        self.ac_callback = ac_callback
        self.heater_callback = heater_callback
        self.app_callback = app_callback

    def get(self) -> int:
        return self._t

    def set(self, value: int) -> None:
        self._t = value
        self.ac_callback(value)
        self.heater_callback(value)
        self.app_callback(value)


def client_code():
    ac = AirCondition()
    heater = Heater()
    app = MobileApp()

    ts = TemperatureSensor(
        20,
        ac.ts_callback,
        heater.ts_callback,
        app.ts_callback,
    )

    ts.set(15)
    ts.set(25)


if __name__ == "__main__":
    client_code()
