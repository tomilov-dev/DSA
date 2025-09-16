"""
Хороший пример: соблюдение OCP — добавление нового способа получения данных без изменения существующего кода.
"""

from abc import ABC
from abc import abstractmethod


class IDataFetcher(ABC):
    @abstractmethod
    def fetch(self) -> dict:
        pass


class DatabaseDataFetcher(IDataFetcher):
    def fetch(self) -> dict:
        print("Получаем данные из базы данных...")
        return {"source": "database", "data": 5}


class APIDataFetcher(IDataFetcher):
    def fetch(self) -> dict:
        print("Получаем данные через API...")
        return {"source": "api", "data": 10}


class DataProcessor:
    def __init__(self, fetcher: IDataFetcher) -> None:
        self.fetcher = fetcher

    def process(self) -> None:
        data = self.fetcher.fetch()
        print(f"Обработали данные: {data['data'] ** 2}")


def main():
    fetchers = [DatabaseDataFetcher(), APIDataFetcher()]
    for fetcher in fetchers:
        processor = DataProcessor(fetcher)
        processor.process()


if __name__ == "__main__":
    main()
