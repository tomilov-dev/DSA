"""
Решение задачи на релаизацию обработчика файлов различных типов через паттер Шаблонный метод
"""

from abc import ABC
from abc import abstractmethod


class IFileHandler(ABC):
    @abstractmethod
    def read(self, path: str) -> list[str]:
        pass

    def process(self, path: str) -> int:
        content = self.read(path)
        print("Rows:", len(content))
        return len(content)


class CSVFileHandler(IFileHandler):
    def read(self, path: str) -> list[str]:
        if not path.endswith(".csv"):
            raise ValueError("Wrong file extension")
        return ["a", "b", "c"]


class ExcelFileHandler(IFileHandler):
    def read(self, path: str) -> list[str]:
        if not path.endswith(".xlsx"):
            raise ValueError("Wrong file extension")
        return ["z", "x", "y", "v"]


def client_code():
    reader = CSVFileHandler()
    reader.process("path.csv")

    reader = ExcelFileHandler()
    reader.process("path.xlsx")


if __name__ == "__main__":
    client_code()
