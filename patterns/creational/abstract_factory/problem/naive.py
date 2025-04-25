"""
Решение задачи системы пользовательских интерфейсов (наивный подход)
"""

from functools import wraps
from enum import Enum
from abc import ABC
from abc import abstractmethod


class PlatformType(str, Enum):
    WINDOWS = "Windows"
    LINUX = "Linux"
    MACOS = "macOS"
    NEW_PLATFORM = "NewPlatform"


## С помощью глобальной переменной обозначим запуск на "Платформе"
PLATFORM = PlatformType.WINDOWS


## Мы используем строгую проверку платформы
## Потому что компоненты между платформами не совместимы
def check_platform(
    target: PlatformType,
    component: str,
):
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            global PLATFORM

            if PLATFORM.value != target.value:
                err = f"{component} {target.value} not compatible with platfrom {PLATFORM.value}"
                raise SystemError(err)
            return func(*args, **kwargs)

        return wrapper

    return deco


class IButton(ABC):
    @abstractmethod
    def click(self) -> None:
        pass


class ITextField(ABC):
    @abstractmethod
    def fill(self, text: str) -> None:
        pass


## На старте у нас есть две реализации пары интерфейсов
## Для Windows и для Linux
class WindowsButton(IButton):
    @check_platform(PlatformType.WINDOWS, "Button")
    def click(self) -> None:
        print("Windows button clicked")


class WindowsTextField(ITextField):
    @check_platform(PlatformType.WINDOWS, "TextField")
    def fill(self, text: str) -> None:
        print(f"Windows text field filled with {text}")


class LinuxButton(IButton):
    @check_platform(PlatformType.LINUX, "Button")
    def click(self):
        print("Linux button clicked")


class LinuxTextField(ITextField):
    @check_platform(PlatformType.LINUX, "TextField")
    def fill(self, text):
        print(f"Linux text field filled with {text}")


## Нам необходимо добавить еще одну платформу (masOC)
class MacOSButton(IButton):
    @check_platform(PlatformType.MACOS, "Button")
    def click(self):
        print("macOS button clicked")


class MacOSTextField(ITextField):
    @check_platform(PlatformType.MACOS, "TextField")
    def fill(self, text):
        print(f"macOS text field filled with {text}")


def client_code(platform_type: PlatformType):
    global PLATFORM

    PLATFORM = platform_type

    match platform_type:
        ## На старте мы имеем две реализации платформенных компонент
        case PlatformType.WINDOWS.value:
            button = WindowsButton()
            text_field = WindowsTextField()
        case PlatformType.LINUX.value:
            button = LinuxButton()
            text_field = LinuxTextField()

        ## Добавляем новую платформу и случайно допускаем ошибку
        ## FIXME: имеем сильную зависимость от реализаций в клиентском коде
        case PlatformType.MACOS.value:
            button = MacOSButton()
            text_field = WindowsTextField()
        case _:
            raise NotImplementedError(
                f"Platform not implemented yet: {platform_type.value}"
            )

    button.click()
    text_field.fill("Hello world")


if __name__ == "__main__":
    client_code(PlatformType.WINDOWS)
