"""
Реализация сервиса для работы с удаленными файлами (наивный подход)
"""

from abc import ABC
from abc import abstractmethod


class ICloudFile(ABC):
    def __init__(self, token: str) -> None:
        self.token = token

    @abstractmethod
    def read(self, path: str) -> str:
        pass


class CloudFile(ICloudFile):
    def read(self, path: str) -> str:
        print(f"Read data for {path}")
        return f"File content by path: {path}"


def client_code():
    cloud = CloudFile("abc")
    data = cloud.read("path")
    data = cloud.read("path")


if __name__ == "__main__":
    client_code()
