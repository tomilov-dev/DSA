import logging
from abc import ABC
from abc import abstractmethod


ALLOWED_AUTH: set[tuple[str, str]] = set(
    [
        ("admin", "admin"),
    ]
)


class IFileSystem(ABC):
    @abstractmethod
    def read_file(self, path: str) -> str:
        pass

    @abstractmethod
    def write_file(self, path: str, content: str) -> None:
        pass

    @abstractmethod
    def delete_file(self, path: str) -> None:
        pass


class FileSystem(IFileSystem):
    def __init__(self, login: str, password: str) -> None:
        self.login = login
        self.password = password

    def read_file(self, path: str) -> str:
        return f"Reading file from {path}"

    def write_file(self, path: str, content: str) -> None:
        print(f"Write file to {path}")

    def delete_file(self, path: str) -> None:
        print(f"Delete file from {path}")


class FileSystemProxy(IFileSystem):
    def __init__(
        self,
        file_system: FileSystem,
        log: logging.Logger,
    ) -> None:
        self.fs = file_system
        self.log = log

    def check_auth(self) -> bool:
        if (self.fs.login, self.fs.password) not in ALLOWED_AUTH:
            self.log.error("Auth failed")
            return False
        return True

    def read_file(self, path: str) -> str:
        self.log.debug(f"Read file from {path}")
        if self.check_auth():
            return self.fs.read_file(path)
        raise ValueError("Auth failed")

    def write_file(self, path: str, content: str) -> None:
        self.log.debug(f"Write file to {path}")
        if self.check_auth():
            self.fs.write_file(path, content)
        raise ValueError("Auth failed")

    def delete_file(self, path: str) -> None:
        self.log.debug(f"Delete file from {path}")
        if self.check_auth():
            self.fs.delete_file(path)
        raise ValueError("Auth failed")


def client_code():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger("FileSystemProxyLogger")

    real_fs = FileSystem("admin", "admin")
    proxy_fs = FileSystemProxy(real_fs, logger)

    print(proxy_fs.read_file("/path/to/file.txt"))
    proxy_fs.write_file("/path/to/file.txt", "New content")
    proxy_fs.delete_file("/path/to/file.txt")
