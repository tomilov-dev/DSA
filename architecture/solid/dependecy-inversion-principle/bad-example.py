"""
Плохой пример: нарушение принципа инверсии зависимостей (DIP).
"""


class FileRepository:
    def save(self, data: str):
        print(f"Сохранили в файл: {data}")


class DatabaseRepository:
    def save_data(self, data: str):
        print(f"Сохранили в базу данных: {data}")


class ReportService:
    def __init__(self, repository: FileRepository) -> None:
        self.repository = repository  # Жёсткая зависимость от FileRepository
        # self.repository = FileRepository()  # Супер-пупер жёсткая зависимость 0_0

    def save_report(self, data: str):
        self.repository.save(data)


def main():
    file_repo = FileRepository()
    service = ReportService(file_repo)
    service.save_report("отчёт")

    # Мы не можем просто взять и заменить FileRepository на DatabaseRepository
    # Это не сработает, так как ReportService ожидает FileRepository
    # DatabaseRepository не связан никаким контрактом с ReportService
    db_repo = DatabaseRepository()
    service = ReportService(db_repo)
    service.save_report("отчёт")


if __name__ == "__main__":
    main()
