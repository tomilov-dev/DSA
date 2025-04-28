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


class IComponentsFactory(ABC):
    @abstractmethod
    def create_button(self) -> IButton:
        pass

    @abstractmethod
    def create_text_field(self) -> ITextField:
        pass


## На старте у нас есть две реализации пары интерфейсов
## Для платформ Windows и для Linux
## А также абстрактных фабрики для каждой платформы
class WindowsButton(IButton):
    @check_platform(PlatformType.WINDOWS, "Button")
    def click(self) -> None:
        print("Windows button clicked")


class WindowsTextField(ITextField):
    @check_platform(PlatformType.WINDOWS, "TextField")
    def fill(self, text: str) -> None:
        print(f"Windows text field filled with {text}")


class WindowsComponentsFactory(IComponentsFactory):
    def create_button(self):
        return WindowsButton()

    def create_text_field(self):
        return WindowsTextField()


class LinuxButton(IButton):
    @check_platform(PlatformType.LINUX, "Button")
    def click(self):
        print("Linux button clicked")


class LinuxTextField(ITextField):
    @check_platform(PlatformType.LINUX, "TextField")
    def fill(self, text):
        print(f"Linux text field filled with {text}")


class LinuxComponentsFactory(IComponentsFactory):
    def create_button(self):
        return LinuxButton()

    def create_text_field(self):
        return LinuxTextField()


## Нам необходимо добавить еще одну платформу (masOC)
## Вместе с этим нам нужно добавить новую абстрактную фабрику
class MacOSButton(IButton):
    @check_platform(PlatformType.MACOS, "Button")
    def click(self):
        print("macOS button clicked")


class MacOSTextField(ITextField):
    @check_platform(PlatformType.MACOS, "TextField")
    def fill(self, text):
        print(f"macOS text field filled with {text}")


class MacOSComponentsFactory(IComponentsFactory):
    def create_button(self):
        return MacOSButton()

    def create_text_field(self):
        return MacOSTextField()


class PlatformComponentsSelector:
    _factories = {
        PlatformType.WINDOWS: WindowsComponentsFactory(),
        PlatformType.LINUX: LinuxComponentsFactory(),
        PlatformType.MACOS: MacOSComponentsFactory(),
    }

    def select(self, platform_type: PlatformType) -> IComponentsFactory:
        factory = self._factories.get(platform_type)
        if not factory:
            raise NotImplementedError(
                f"Platform not implemented yet: {platform_type.value}"
            )
        return factory


def client_code(platform_type: PlatformType):
    global PLATFORM

    PLATFORM = platform_type

    factory = PlatformComponentsSelector().select(platform_type)
    button = factory.create_button()
    text_field = factory.create_text_field()

    button.click()
    text_field.fill("Hello world")


if __name__ == "__main__":
    client_code(PlatformType.MACOS)
