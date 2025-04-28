class DocumentMemento:
    def __init__(self, state: str) -> None:
        self._state = state

    def get_state(self) -> str:
        return self._state

    def __repr__(self) -> str:
        return self._state


class Document:
    def __init__(self, content: str | None = None) -> None:
        self._content = content or ""

    def add_text(self, text: str) -> None:
        self._content += text

    def get_text(self) -> str:
        return self._content

    def save(self) -> DocumentMemento:
        return DocumentMemento(self._content)

    def restore(self, memento: DocumentMemento) -> None:
        self._content = memento.get_state()


class DocumentHistory:
    def __init__(self, document: Document) -> None:
        self._document = document
        self._history: list[DocumentMemento] = [document.save()]

    def save(
        self,
    ) -> None:
        self._history.append(self._document.save())

    def undo(self) -> None:
        if len(self._history) == 0:
            return

        memento = self._history.pop()
        self._document.restore(memento)


def client_code():
    document = Document()
    history = DocumentHistory(document)

    document.add_text("Hello, ")
    history.save()

    document.add_text("world!")
    history.save()

    print(document.get_text())

    history.undo()
    print(document.get_text())

    history.undo()
    print(document.get_text())

    history.undo()
    print(document.get_text())


if __name__ == "__main__":
    client_code()
