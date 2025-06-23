"""
Решение задачи создания текстового редактора с возможностью отмены действий через паттерн Команда
"""

from abc import ABC
from abc import abstractmethod
from collections import deque


class ICommand(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass


class EditorReceiver:
    def __init__(self, content: str = ""):
        self.content = content


class InsertCommand(ICommand):
    def __init__(self, editor: EditorReceiver, to_add: str) -> None:
        self.editor = editor
        self.to_add = to_add
        self.prev = ""

    def execute(self) -> None:
        self.prev = self.editor.content
        self.editor.content += self.to_add

    def undo(self) -> None:
        self.editor.content = self.prev


class DeleteCommand(ICommand):
    def __init__(self, editor: EditorReceiver, symbols: int) -> None:
        self.editor = editor
        self.symbols = symbols
        self.prev = ""

    def execute(self) -> None:
        self.prev = self.editor.content
        self.editor.content = self.editor.content[: -self.symbols]

    def undo(self) -> None:
        self.editor.content = self.prev


class ITextEditor(ABC):
    def __init__(self, content: str | None = None) -> None:
        if not content:
            content = ""
        self.editor = EditorReceiver(content)
        self.commands: list[ICommand] = []
        self.executed: list[ICommand] = []
        self.undone: list[ICommand] = []

    @abstractmethod
    def set_command(self, command: ICommand) -> None:
        pass

    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass

    @abstractmethod
    def redo(self) -> None:
        pass


class TextEditor(ITextEditor):
    def set_command(self, command: ICommand) -> None:
        self.commands.append(command)
        self.undone.clear()

    def execute(self) -> None:
        for command in self.commands:
            command.execute()
            self.executed.append(command)
        self.commands.clear()
        self.undone.clear()

    def undo(self) -> None:
        if not self.executed:
            return None

        command = self.executed.pop()
        command.undo()
        self.undone.append(command)

    def redo(self) -> None:
        if not self.undone:
            return None

        command = self.undone.pop()
        command.execute()
        self.executed.append(command)


def client_code():
    editor = TextEditor()

    editor.set_command(InsertCommand(editor.editor, "Hello"))
    editor.set_command(InsertCommand(editor.editor, ", world"))
    editor.execute()
    print(editor.editor.content)

    editor.set_command(DeleteCommand(editor.editor, 5))
    editor.execute()
    print(editor.editor.content)

    editor.undo()
    print(editor.editor.content)  # Hello, world
    editor.redo()
    print(editor.editor.content)  # Hello


if __name__ == "__main__":
    client_code()
