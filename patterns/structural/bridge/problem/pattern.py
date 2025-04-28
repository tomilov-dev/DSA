"""
Решение задачи управления девайсами через паттерн Bridge
"""

from abc import ABC
from abc import abstractmethod


class IDevice(ABC):
    def __init__(self):
        self.volume = 10

    @abstractmethod
    def turn_on(self) -> None:
        pass

    @abstractmethod
    def turn_off(self) -> None:
        pass

    @abstractmethod
    def set_volume(self, volume: float) -> None:
        pass


## Мы имеем два устройства
class TV(IDevice):
    def turn_on(self) -> None:
        print("TV is now ON")

    def turn_off(self) -> None:
        print("TV is now OFF")

    def set_volume(self, volume: float) -> None:
        print(f"TV volume set to {volume}")


class Radio(IDevice):
    def turn_on(self) -> None:
        print("Radio is now ON")

    def turn_off(self) -> None:
        print("Radio is now OFF")

    def set_volume(self, volume: float) -> None:
        print(f"Radio volume set to {volume}")


## Теперь мы имеем также два устройства управления
class RemoteController:
    def __init__(self, device: IDevice) -> None:
        self.device = device

    def on(self) -> None:
        return self.device.turn_on()

    def off(self) -> None:
        return self.device.turn_off()

    def add_volume(self) -> None:
        cur_volume = self.device.volume
        return self.device.set_volume(cur_volume + 1)

    def down_volume(self) -> None:
        cur_volume = self.device.volume
        return self.device.set_volume(cur_volume - 1)


## Мы расширяем функционал управления, добавляя новый класс
class AdvancedRemoteController(RemoteController):
    def mute(self) -> None:
        self.device.set_volume(0)


def client_code():
    ## Теперь для управления устройством нам не нужно работать с ним напрямую
    tv = TV()
    remote_control = RemoteController(tv)
    remote_control.on()
    remote_control.add_volume()
    remote_control.off()

    ## Мы можем расширять функционал управления, никак не изменяя само устройство
    radio = Radio()
    advanced_control = AdvancedRemoteController(radio)
    advanced_control.on()
    advanced_control.add_volume()
    advanced_control.mute()
    advanced_control.off()


if __name__ == "__main__":
    client_code()
