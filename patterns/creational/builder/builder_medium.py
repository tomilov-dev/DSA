from abc import ABC
from abc import abstractmethod


class SaleItem:
    def __init__(self, sku: str, price: float, quantity: int) -> None:
        self.sku = sku
        self.price = price
        self.quantity = quantity


class SalesReport:
    def __init__(self) -> None:
        self.title: str | None = None
        self.period: str | None = None
        self.items: list[SaleItem] = []
        self.comments: list[str] = []

        self.total_sales: float | None = None
        self.average_price: float | None = None

    def set_title(self, title: str) -> None:
        self.title = title

    def set_period(self, period: str) -> None:
        self.period = period

    def add_item(self, item: SaleItem) -> None:
        self.items.append(item)

    def add_comment(self, comment: str) -> None:
        self.comments.append(comment)

    def count_total_sales(self) -> float:
        self.total_sales = sum(item.price * item.quantity for item in self.items)
        return self.total_sales

    def count_avg_price(self) -> float | None:
        if self.total_sales is None:
            return None

        self.average_price = self.total_sales / len(self.items)
        return self.average_price


class SalesReportBuilder(ABC):
    def __init__(self) -> None:
        self.report = SalesReport()

    @abstractmethod
    def build_title(self, title: str) -> None:
        pass

    @abstractmethod
    def build_period(self, period: str) -> None:
        pass

    @abstractmethod
    def build_items(self, items: list[SaleItem]) -> None:
        pass

    @abstractmethod
    def build_comments(self, comments: list[str]) -> None:
        pass

    @abstractmethod
    def build_total_sales(self) -> float:
        pass

    @abstractmethod
    def build_avg_price(self) -> float | None:
        pass


class DetailedSalesReportBuilder(SalesReportBuilder):
    def build_title(self, title: str) -> None:
        self.report.set_title(title)

    def build_period(self, period: str) -> None:
        self.report.set_period(period)

    def build_items(self, items: list[SaleItem]) -> None:
        for item in items:
            self.report.add_item(item)

    def build_comments(self, comments: list[str]) -> None:
        for comment in comments:
            self.report.add_comment(comment)

    def build_total_sales(self) -> float:
        return self.report.count_total_sales()

    def build_avg_price(self) -> float | None:
        return self.report.count_avg_price()


class SalesReportDirector:
    def __init__(self, builder: SalesReportBuilder) -> None:
        self._builder = builder

    def construct_report(
        self,
        title: str,
        period: str,
        items: list[SaleItem],
        comments: list[str],
    ) -> None:
        self._builder.build_title(title)
        self._builder.build_period(period)
        self._builder.build_items(items)
        self._builder.build_comments(comments)
        self._builder.build_total_sales()
        self._builder.build_avg_price()


def client_code():
    # Пример данных для отчета о продажах
    title = "Отчет о продажах за Q1 2023"
    period = "01.01.2023 - 31.03.2023"
    items = [
        SaleItem("Товар 1", 1000.0, 5),
        SaleItem("Товар 2", 2000.0, 3),
        SaleItem("Товар 3", 1500.0, 4),
    ]
    comments = ["Продажи выросли на 10% по сравнению с предыдущим кварталом."]

    # Создание строителя и директора
    builder = DetailedSalesReportBuilder()
    director = SalesReportDirector(builder)

    # Конструирование отчета о продажах
    director.construct_report(title, period, items, comments)
    report = builder.report

    # Отображение деталей отчета о продажах
    print(f"Title: {report.title}")
    print(f"Period: {report.period}")
    print(
        f"Items: {[f'{item.sku}: {item.price} x {item.quantity}' for item in report.items]}"
    )
    print(f"Total Sales: {report.total_sales}")
    print(f"Average Price: {report.average_price}")
    print(f"Comments: {report.comments}")
