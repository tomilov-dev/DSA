from abc import ABC
from abc import abstractmethod


class Television:
    def turn_on(self) -> None:
        print("Включение телевизора")

    def turn_off(self) -> None:
        print("Выключение телевизора")

    def volume_up(self) -> None:
        print("Увеличение звука телевизора")

    def volume_down(self) -> None:
        print("Уменьшение звука телевизора")


class Command(ABC):
    def __init__(self, television: Television) -> None:
        self.television = television

    @abstractmethod
    def execute(self) -> None:
        pass


class TurnOnCommand(Command):
    def execute(self) -> None:
        self.television.turn_on()


class TurnOffCommand(Command):
    def execute(self) -> None:
        self.television.turn_off()


class VolumeUpCommand(Command):
    def execute(self) -> None:
        self.television.volume_up()


class VolumeDownCommand(Command):
    def execute(self) -> None:
        self.television.volume_down()


class RemoteControl:
    def __init__(self) -> None:
        self.command: Command | None = None

    def set_command(self, command: Command) -> None:
        self.command = command

    def press_button(self) -> None:
        if self.command:
            self.command.execute()


def client_code():
    tv = Television()

    # Создание команд
    turn_on = TurnOnCommand(tv)
    turn_off = TurnOffCommand(tv)
    volume_up = VolumeUpCommand(tv)
    volume_down = VolumeDownCommand(tv)

    # Создание объекта RemoteControl
    remote = RemoteControl()

    # Выполнение команд
    remote.set_command(turn_on)
    remote.press_button()  # Включает телевизор

    remote.set_command(volume_up)
    remote.press_button()  # Увеличивает громкость

    remote.set_command(volume_down)
    remote.press_button()  # Уменьшает громкость

    remote.set_command(turn_off)
    remote.press_button()  # Выключает телевизор
