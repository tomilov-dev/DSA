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


class MusicPlayer:
    def play(self) -> None:
        print("Включение музыки")

    def stop(self) -> None:
        print("Выключение музыки")


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass


class MacroCommand(Command):
    def __init__(self, commands: list[Command]) -> None:
        self.commands = commands

    def execute(self) -> None:
        for command in self.commands:
            command.execute()

    def undo(self) -> None:
        for command in self.commands[::-1]:
            command.undo()


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


class MusicPlayerCommand(Command):
    def __init__(self, music_player: MusicPlayer) -> None:
        self.music_player = music_player


class MusicOnCommand(MusicPlayerCommand):
    def execute(self) -> None:
        self.music_player.play()

    def undo(self) -> None:
        self.music_player.stop()


class MusicOffCommand(MusicPlayerCommand):
    def execute(self) -> None:
        self.music_player.stop()

    def undo(self) -> None:
        self.music_player.play()


class SmartHomeController:
    def __init__(self) -> None:
        self.command: Command | None = None
        self.history: list[Command] = []
        self.cancelled: list[Command] = []

    def set_command(self, command: Command) -> None:
        self.command = command

    def press_button(self) -> None:
        if self.command:
            self.command.execute()
            self.history.append(self.command)

    def press_redo(self) -> None:
        if self.history:
            command = self.history[-1]
            command.execute()

    def press_undo(self) -> None:
        if self.history:
            command = self.history.pop()
            command.undo()
            self.cancelled.append(command)

    def save_state(self) -> tuple[list[Command], list[Command]]:
        return self.history, self.cancelled

    def load_state(self, history: list[Command], cancelled: list[Command]) -> None:
        self.history = history
        self.cancelled = cancelled
