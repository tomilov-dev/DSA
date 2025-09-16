from abc import ABC
from abc import abstractmethod


class IAlertManager(ABC):
    @abstractmethod
    def alert(self, msg: str) -> None:
        pass
