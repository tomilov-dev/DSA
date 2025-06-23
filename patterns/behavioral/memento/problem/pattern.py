"""
Решение задачи сохранения состояния текстового редактора через паттерн Снимок
"""

from abc import ABC
from abc import abstractmethod
from collections import deque
from typing import Any


class IMemento(ABC):
    def __init__(self, state: Any) -> None:
        self._state = state

    @abstractmethod
    def get_state(self) -> Any:
        pass


class IStateManager(ABC):
    def __init__(self, state: Any) -> None:
        self._state = state

    @abstractmethod
    def save(self) -> IMemento:
        pass

    @abstractmethod
    def restore(self, mem: IMemento) -> None:
        pass

    @abstractmethod
    def get(self) -> Any:
        pass

    @abstractmethod
    def update(self, content: Any) -> None:
        pass


class Memento(IMemento):
    def get_state(self) -> Any:
        return self._state


class StateManager(IStateManager):
    def save(self) -> IMemento:
        return Memento(self._state)

    def restore(self, mem: IMemento) -> None:
        self._state = mem.get_state()

    def get(self) -> Any:
        return self._state

    def update(self, content) -> None:
        self._state = content


class ITextEditor(ABC):
    @abstractmethod
    def insert(self, text: str) -> None:
        pass

    @abstractmethod
    def delete(self, symbols: int) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass

    @abstractmethod
    def redo(self) -> None:
        pass

    @property
    @abstractmethod
    def content(self) -> Any:
        pass


class TextEditor(ITextEditor):
    def __init__(
        self,
        max_size: int,
        state_manager: IStateManager,
    ) -> None:
        self.max_size = max_size

        self.state_manager = state_manager
        self.history: deque[IMemento] = deque(
            [self.state_manager.save()],
            maxlen=max_size,
        )
        self.hindex = len(self.history) - 1

    def monitor_state(self) -> None:
        self.history.append(self.state_manager.save())
        self.hindex = len(self.history) - 1

    def insert(self, text: str) -> None:
        self.state_manager.update(self.state_manager.get() + text)
        self.monitor_state()

    def delete(self, symbols: int) -> None:
        self.state_manager.update(self.state_manager.get()[:-symbols])
        self.monitor_state()

    def undo(self) -> None:
        if self.hindex > 0:
            self.hindex -= 1
        self.state_manager.restore(self.history[self.hindex])

    def redo(self) -> None:
        if self.hindex < len(self.history):
            self.hindex += 1
            self.state_manager.restore(self.history[self.hindex])

    @property
    def content(self) -> Any:
        return self.state_manager.get()


def client_code():
    state_manager = StateManager("")
    editor = TextEditor(
        max_size=10,
        state_manager=state_manager,
    )

    editor.insert("Hello")
    print(editor.content)  # Hello

    editor.insert(", world")
    print(editor.content)  # Hello, world

    editor.delete(6)
    print(editor.content)  # Hello

    editor.undo()
    print(editor.content)  # Hello, world

    editor.redo()
    print(editor.content)  # Hello

    editor.undo()
    editor.undo()
    print(editor.content)  # Hello

    editor.insert("!!!")
    print(editor.content)  # Hello!!!

    editor.undo()
    print(editor.content)  # Hello


if __name__ == "__main__":
    client_code()
