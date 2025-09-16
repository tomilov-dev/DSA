"""
Плохой пример: нарушение OCP — старый способ получения данных закомментирован, новый добавлен прямо в класс.
"""


class DataFetcher:
    # def fetch(self) -> dict:
    #     # Старый способ — получение данных из базы данных
    #     print("Получаем данные из базы данных...")
    #     return {"source": "database", "data": 5}

    def fetch(self) -> dict:
        # Новый способ — получение данных по API
        print("Получаем данные через API...")
        return {"source": "api", "data": 10}


class DataProcessor:
    def __init__(self, fetcher: DataFetcher) -> None:
        self.fetcher = fetcher

    def process(self) -> None:
        data = self.fetcher.fetch()
        print(f"Обработали данные: {data['data'] ** 2}")


def main():
    fetcher = DataFetcher()
    processor = DataProcessor(fetcher)
    processor.process()


if __name__ == "__main__":
    main()
