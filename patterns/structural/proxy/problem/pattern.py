"""
Реализация сервиса для работы с удаленными файлами через паттерн Прокси

Следует учесть, что кэш-прокси наследуется от ICloudFile интерфейса, чтобы соблюдать дальнейшую совместимость классов.
"""

from abc import ABC
from abc import abstractmethod


class ICloudFile(ABC):
    def __init__(self, token: str) -> None:
        self._token = token

    @abstractmethod
    def read(self, path: str) -> str:
        pass


class CloudFile(ICloudFile):
    def read(self, path: str) -> str:
        print(f"Read data for {path}")
        return f"File content by path: {path}"


class CloudFileCache(ICloudFile):
    def __init__(
        self,
        token: str,
        service: ICloudFile,
    ) -> None:
        super().__init__(token)
        self.service = service
        self._cache = {}

    def read(self, path: str) -> str:
        if path not in self._cache:
            self._cache[path] = self.service.read(path)
        return self._cache[path]


def client_code():
    cloud_service = CloudFile("abc")
    cloud = CloudFileCache("abc", cloud_service)

    data = cloud.read("path")
    data = cloud.read("path")


if __name__ == "__main__":
    client_code()
