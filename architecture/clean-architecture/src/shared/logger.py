from abc import ABC
from abc import abstractmethod


class ILogger(ABC):
    @abstractmethod
    def debug(self, msg: str) -> None:
        pass

    @abstractmethod
    def info(self, msg: str) -> None:
        pass

    @abstractmethod
    def warning(self, msg: str) -> None:
        pass

    @abstractmethod
    def error(self, msg: str) -> None:
        pass

    @abstractmethod
    def critical(self, msg: str) -> None:
        pass
