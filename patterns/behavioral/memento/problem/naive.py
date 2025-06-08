"""
Решение задачи сохранения состояния текстового редактора (наивный подход)
"""

from abc import ABC
from abc import abstractmethod
from collections import deque


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


class TextEditor(ITextEditor):
    def __init__(
        self,
        max_size: int,
        content: str | None = None,
    ) -> None:
        self.max_size = max_size
        self.content = content if content else ""
        self.states = deque([self.content], maxlen=max_size)
        self.state_index = len(self.states) - 1

    def monitor_state(self) -> None:
        self.states.append(self.content)
        self.state_index = len(self.states) - 1

    def insert(self, text: str) -> None:
        self.content += text
        self.monitor_state()

    def delete(self, symbols: int) -> None:
        self.content = self.content[:-symbols]
        self.monitor_state()

    def undo(self) -> None:
        if self.state_index > 0:
            self.state_index -= 1
        self.content = self.states[self.state_index]

    def redo(self) -> None:
        if self.state_index < len(self.states):
            self.state_index += 1
        self.content = self.states[self.state_index]


def client_code():
    editor = TextEditor(max_size=10)

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
