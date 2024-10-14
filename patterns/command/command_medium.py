from abc import ABC
from abc import abstractmethod


class Light:
    def turn_on(self) -> None:
        print("Включение света")

    def turn_off(self) -> None:
        print("Выключение света")


class Thermostat:
    def set_temperature(self, temperature: float) -> None:
        print(f"Установка температуры: {temperature}°C")


class DoorLock:
    def lock(self) -> None:
        print("Закрытие двери")

    def unlock(self) -> None:
        print("Открытие двери")


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass


class LightCommand(Command, ABC):
    def __init__(self, light: Light) -> None:
        self.light = light


class LightOnCommand(LightCommand):
    def execute(self) -> None:
        self.light.turn_on()

    def undo(self) -> None:
        self.light.turn_off()


class LightOffCommand(LightCommand):
    def execute(self) -> None:
        self.light.turn_off()

    def undo(self) -> None:
        self.light.turn_on()


class ThermostatCommand(Command, ABC):
    def __init__(self, thermostat: Thermostat, temperature: float) -> None:
        self.thermostat = thermostat
        self.temperature = temperature


class SetTemperatureCommand(ThermostatCommand, ABC):
    def execute(self) -> None:
        self.thermostat.set_temperature(self.temperature)

    def undo(self) -> None:
        self.thermostat.set_temperature(20.0)


class DoorCommand(Command, ABC):
    def __init__(self, door_lock: DoorLock) -> None:
        self.door_lock = door_lock


class DoorLockCommand(DoorCommand):
    def execute(self) -> None:
        self.door_lock.lock()

    def undo(self) -> None:
        self.door_lock.unlock()


class DoorUnlockCommand(DoorCommand):
    def execute(self) -> None:
        self.door_lock.unlock()

    def undo(self) -> None:
        self.door_lock.lock()


class SmartHomeController:
    def __init__(self) -> None:
        self.command: Command | None = None
        self.history: list[Command] = []

    def set_command(self, command: Command) -> None:
        self.command = command

    def press_button(self) -> None:
        if self.command:
            self.command.execute()

    def press_undo(self) -> None:
        if self.history:
            command = self.history.pop()
            command.undo()


def client_code():
    light = Light()
    thermostat = Thermostat()
    door_lock = DoorLock()

    turn_on_light = LightOnCommand(light)
    turn_off_light = LightOffCommand(light)
    set_temperature = SetTemperatureCommand(thermostat, 22.5)
    lock_door = DoorLockCommand(door_lock)
    unlock_door = DoorUnlockCommand(door_lock)

    controller = SmartHomeController()

    controller.set_command(turn_on_light)
    controller.press_button()

    controller.set_command(set_temperature)
    controller.press_button()

    controller.set_command(lock_door)
    controller.press_button()

    controller.press_undo()
