"""
Решение задачи связывания UI-компонентов (наивный метод)

Преимущества:
1. Компоненты друг о друге не знают. Меньше связанность.
2. Логика взаимодействия компонентов строго централизована.
"""

from abc import ABC
from abc import abstractmethod
from typing import Any


class IMediator(ABC):
    def __init__(
        self,
        input: "Input",
        checkbox: "Checkbox",
        button: "Button",
    ) -> None:
        self.input = input
        self.checkbox = checkbox
        self.button = button

        self.input.mediator = self
        self.checkbox.mediator = self
        self.button.mediator = self

    @abstractmethod
    def notify(
        self,
        sender: "IUIComponent",
        **kwargs,
    ) -> None:
        pass


class DialogMediator(IMediator):
    def notify(
        self,
        sender: "IUIComponent",
        **kwargs,
    ) -> None:
        if isinstance(sender, Button):
            if not self.input.state:
                raise ValueError("Input must be filled")
            if not self.checkbox.state:
                raise ValueError("Checkbox must be confirmed")


class IUIComponent(ABC):
    def __init__(
        self,
        state: Any = None,
        mediator: IMediator | None = None,
    ) -> None:
        self.state = state
        self._mediator = mediator

    @property
    def mediator(self) -> IMediator:
        if self._mediator is None:
            raise ValueError("Mediator is not setuped")
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: IMediator) -> None:
        self._mediator = mediator

    @abstractmethod
    def set(self, **kwargs) -> None:
        pass


class Input(IUIComponent):
    def set(self, name: str) -> None:
        print(f"Input name: {name}")
        self.state = name
        self.mediator.notify(self)


class Checkbox(IUIComponent):
    def set(self) -> None:
        if not self.state:
            print(f"Checkbox activated")
            self.state = True
        else:
            print(f"Checkbox deactivated")
            self.state = False

        self.mediator.notify(self)


class Button(IUIComponent):
    def set(self, inp: IUIComponent, checkbox: IUIComponent) -> None:
        print("Button is clicked. Render...")
        self.mediator.notify(self)


def client_code():
    input = Input()
    checkbox = Checkbox()
    button = Button()
    mediator = DialogMediator(input, checkbox, button)

    input.mediator = mediator
    checkbox.mediator = mediator
    button.mediator = mediator

    input.set("Ivan")
    checkbox.set()
    button.set(input, checkbox)


if __name__ == "__main__":
    client_code()
