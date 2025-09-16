"""
Хороший пример: соблюдение принципа инверсии зависимостей (DIP).
"""

from abc import ABC, abstractmethod


class IRepository(ABC):
    @abstractmethod
    def save(self, data: str) -> None:
        pass


class FileRepository(IRepository):
    def save(self, data: str) -> None:
        print(f"Сохранили в файл: {data}")


class DatabaseRepository(IRepository):
    def save(self, data: str) -> None:
        print(f"Сохранили в базу данных: {data}")


class ReportService:
    def __init__(self, repository: IRepository):
        self.repository = repository

    def save_report(self, data):
        self.repository.save(data)


def main():
    # Теперь можно подставить любую реализацию IRepository:
    repo = FileRepository()
    service_with_file = ReportService(repo)
    service_with_file.save_report("отчёт")

    repo_db = DatabaseRepository()
    service_with_db = ReportService(repo_db)
    service_with_db.save_report("отчёт")


if __name__ == "__main__":
    main()
