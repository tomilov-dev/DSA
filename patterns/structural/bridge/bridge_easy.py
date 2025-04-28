from abc import ABC
from abc import abstractmethod


class ReportFormat(ABC):
    @abstractmethod
    def generate_header(self, content: str) -> str:
        pass

    @abstractmethod
    def generate_body(self, content: str) -> str:
        pass

    @abstractmethod
    def generate_footer(self, content: str) -> str:
        pass


class PDFReport(ReportFormat):
    def generate_header(self, content: str) -> str:
        return f"PDF Header: {content}"

    def generate_body(self, content: str) -> str:
        return f"PDF Body: {content}"

    def generate_footer(self, content: str) -> str:
        return f"PDF Footer: {content}"


class CSVReport(ReportFormat):
    def generate_header(self, content: str) -> str:
        return f"CSV Header: {content}"

    def generate_body(self, content: str) -> str:
        return f"CSV Body: {content}"

    def generate_footer(self, content: str) -> str:
        return f"CSV Footer: {content}"


class Report(ABC):
    def __init__(self, report_format: ReportFormat) -> None:
        self.report_format = report_format

    @abstractmethod
    def generate(self) -> str:
        pass


class SalesReport(Report):
    def generate(self) -> str:
        header = self.report_format.generate_header("Sales Report")
        body = self.report_format.generate_body("Sales Report")
        footer = self.report_format.generate_footer("Sales Report")
        return f"{header}\n{body}\n{footer}"


class InventoryReport(Report):
    def generate(self) -> str:
        header = self.report_format.generate_header("Inventory Report")
        body = self.report_format.generate_body("Inventory Report")
        footer = self.report_format.generate_footer("Inventory Report")
        return f"{header}\n{body}\n{footer}"


def client_code():
    pdf_format = PDFReport()
    csv_format = CSVReport()

    sales_report_pdf = SalesReport(pdf_format)
    sales_report_csv = SalesReport(csv_format)

    inventory_report_pdf = InventoryReport(pdf_format)
    inventory_report_csv = InventoryReport(csv_format)

    print(sales_report_pdf.generate())
    print(sales_report_csv.generate())
    print(inventory_report_pdf.generate())
    print(inventory_report_csv.generate())
