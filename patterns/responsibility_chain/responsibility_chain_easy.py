from abc import ABC
from abc import abstractmethod


class IHandler(ABC):
    def __init__(self) -> None:
        self._next: IHandler | None = None

    def set_next(self, handler: "IHandler") -> None:
        self._next = handler

    @abstractmethod
    def handle(self, request: str) -> None:
        pass


class Level1Support(IHandler):
    def handle(self, request: str) -> None:
        if request == "password reset":
            print("Reset Password")
        elif self._next:
            self._next.handle(request)
        else:
            print(f"Request '{request}' could not be handled")


class Level2Support(IHandler):
    def handle(self, request: str) -> None:
        if request == "software installation":
            print("Software Installation")
        elif self._next:
            self._next.handle(request)
        else:
            print(f"Request '{request}' could not be handled")


class Level3Support(IHandler):
    def handle(self, request: str) -> None:
        if request == "network issues":
            print("Network Issues")
        elif self._next:
            self._next.handle(request)
        else:
            print(f"Request '{request}' could not be handled")


def client_code():
    level1 = Level1Support()
    level2 = Level2Support()
    level3 = Level3Support()

    level1.set_next(level2)
    level2.set_next(level3)

    level1.handle("password reset")
    level1.handle("software installation")
    level1.handle("network issues")
    level1.handle("unknown issue")
