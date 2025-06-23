"""
Решение задачи связывания UI-компонентов (наивный метод)

Проблемы:
1. Каждый компонент должен знать о других компонентах (если это требуется) - более сильная связанность
2. Если потребуется изменять логику взаимодействия между компонентами, тогда нужно будет нарушать OCP-принцип
3.
"""

from abc import ABC
from abc import abstractmethod
from typing import Any


class IUIComponent(ABC):
    def __init__(self, state: Any = None) -> None:
        self.state = state

    @abstractmethod
    def set(self, **kwargs) -> None:
        pass


class Input(IUIComponent):
    def set(self, name: str) -> None:
        print(f"Input name: {name}")
        self.state = name


class Checkbox(IUIComponent):
    def set(self) -> None:
        if not self.state:
            print(f"Checkbox activated")
            self.state = True
        else:
            print(f"Checkbox deactivated")
            self.state = False


class Button(IUIComponent):
    def set(self, inp: IUIComponent, checkbox: IUIComponent) -> None:
        if not inp.state:
            raise ValueError("Input must be filled")
        if not checkbox.state:
            raise ValueError("Checkbox must be confirmed")

        print("Button is clicked. Render...")


def client_code():
    inp = Input()
    checkbox = Checkbox()
    button = Button()

    inp.set("Ivan")
    checkbox.set()
    button.set(inp, checkbox)


if __name__ == "__main__":
    client_code()
