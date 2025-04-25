from abc import ABC
from abc import abstractmethod


class DocumentState(ABC):
    @abstractmethod
    def publish(self, context: "DocumentContext") -> None:
        pass

    @abstractmethod
    def archive(self, context: "DocumentContext") -> None:
        pass


class DraftState(DocumentState):
    def publish(self, context: "DocumentContext") -> None:
        print("DraftState: Moving to ModerationState")
        context.set_state(ModerationState())

    def archive(self, context: "DocumentContext") -> None:
        print("DraftState: Archiving document")
        context.set_state(ArchivedState())


class ModerationState(DocumentState):
    def publish(self, context: "DocumentContext") -> None:
        print("ModerationState: Moving to PublishedState")
        context.set_state(PublishedState())

    def archive(self, context: "DocumentContext") -> None:
        print("ModerationState: Archiving document")
        context.set_state(ArchivedState())


class PublishedState(DocumentState):
    def publish(self, context: "DocumentContext") -> None:
        print("PublishedState: Already published")

    def archive(self, context: "DocumentContext") -> None:
        print("PublishedState: Archiving document")
        context.set_state(ArchivedState())


class ArchivedState(DocumentState):
    def publish(self, context: "DocumentContext") -> None:
        print("ArchivedState: Cannot publish an archived document")

    def archive(self, context: "DocumentContext") -> None:
        print("ArchivedState: Already archived")


class DocumentContext:
    def __init__(self) -> None:
        self._state: DocumentState | None = None

    def set_state(self, state: DocumentState) -> None:
        self._state = state

    def publish(self) -> None:
        if self._state is None:
            raise ValueError("State is not set")
        self._state.publish(self)

    def archive(self) -> None:
        if self._state is None:
            raise ValueError("State is not set")
        self._state.publish(self)


def client_code():
    document = DocumentContext()

    document.publish()  # DraftState: Moving to ModerationState
    document.publish()  # ModerationState: Moving to PublishedState
    document.archive()  # PublishedState: Archiving document
    document.publish()  # ArchivedState: Cannot publish an archived document
