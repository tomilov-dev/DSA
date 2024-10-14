from abc import ABC
from abc import abstractmethod


class FileProcessor(ABC):
    def process_file(self, path: str) -> None:
        self.open_file(path)
        self.read_data()
        self.process_data()
        self.close_file()

    @abstractmethod
    def open_file(self, path: str) -> None:
        pass

    @abstractmethod
    def read_data(self) -> None:
        pass

    @abstractmethod
    def process_data(self) -> None:
        pass

    @abstractmethod
    def close_file(self) -> None:
        pass


class CSVFileProcessor(FileProcessor):
    def open_file(self, path: str) -> None:
        print("Open CSV File")

    def read_data(self) -> None:
        print("Read CSV File")

    def process_data(self) -> None:
        print("Process CSV File")

    def close_file(self) -> None:
        print("Close CSV File")


class JSONFileProcessor(FileProcessor):
    def open_file(self, path: str) -> None:
        print("Open JSON File")

    def read_data(self) -> None:
        print("Read JSON File")

    def process_data(self) -> None:
        print("Process JSON File")

    def close_file(self) -> None:
        print("Close JSON File")


def client_code():
    csv_processor = CSVFileProcessor()
    csv_processor.process_file("data.csv")

    json_processor = JSONFileProcessor()
    json_processor.process_file("data.json")
