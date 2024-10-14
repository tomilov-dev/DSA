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


class PDFReportFormat(ReportFormat):
    def generate_header(self, content: str) -> str:
        return f"PDF Header: {content}"

    def generate_body(self, content: str) -> str:
        return f"PDF Body: {content}"

    def generate_footer(self, content: str) -> str:
        return f"PDF Footer: {content}"


class HTMLReportFormat(ReportFormat):
    def generate_header(self, content: str) -> str:
        return f"HTML Header: {content}"

    def generate_body(self, content: str) -> str:
        return f"HTML Body: {content}"

    def generate_footer(self, content: str) -> str:
        return f"HTML Footer: {content}"


class ExcelReportFormat(ReportFormat):
    def generate_header(self, content: str) -> str:
        return f"Excel Header: {content}"

    def generate_body(self, content: str) -> str:
        return f"Excel Body: {content}"

    def generate_footer(self, content: str) -> str:
        return f"Excel Footer: {content}"


class DeliveryChannel(ABC):
    @abstractmethod
    def send(self, report: str, recipient: str) -> None:
        pass


class EmailChannel(DeliveryChannel):
    def send(self, report: str, recipient: str) -> None:
        print(f"Sending report through Email to {recipient} with content: {report}")


class FTPChannel(DeliveryChannel):
    def send(self, report: str, recipient: str) -> None:
        print(f"Sending report through FTP to {recipient} with content: {report}")


class APIChannel(DeliveryChannel):
    def send(self, report: str, recipient: str) -> None:
        print(f"Sending report through API to {recipient} with content: {report}")


class SalesReport(ABC):
    def __init__(
        self,
        report_format: ReportFormat,
        delivery_channel: DeliveryChannel,
    ) -> None:
        self.report_format = report_format
        self.delivery_channel = delivery_channel

    @abstractmethod
    def generate_and_send(self, recipient: str) -> None:
        pass


class DailySalesReport(SalesReport):
    def generate_and_send(self, recipient: str) -> None:
        header = self.report_format.generate_header("Daily Sales Report")
        body = self.report_format.generate_body("Daily Sales Report")
        footer = self.report_format.generate_footer("Daily Sales Report")
        report = f"{header}\n{body}\n{footer}"
        self.delivery_channel.send(report, recipient)


class WeeklySalesReport(SalesReport):
    def generate_and_send(self, recipient: str) -> None:
        header = self.report_format.generate_header("Weekly Sales Report")
        body = self.report_format.generate_body("Weekly Sales Report")
        footer = self.report_format.generate_footer("Weekly Sales Report")
        report = f"{header}\n{body}\n{footer}"
        self.delivery_channel.send(report, recipient)


class MonthlySalesReport(SalesReport):
    def generate_and_send(self, recipient: str) -> None:
        header = self.report_format.generate_header("Monthly Sales Report")
        body = self.report_format.generate_body("Monthly Sales Report")
        footer = self.report_format.generate_footer("Monthly Sales Report")
        report = f"{header}\n{body}\n{footer}"
        self.delivery_channel.send(report, recipient)


def client_code():
    pdf_format = PDFReportFormat()
    excel_format = ExcelReportFormat()
    html_format = HTMLReportFormat()

    email_channel = EmailChannel()
    ftp_channel = FTPChannel()
    api_channel = APIChannel()

    daily_report = DailySalesReport(pdf_format, email_channel)
    weekly_report = WeeklySalesReport(excel_format, ftp_channel)
    monthly_report = MonthlySalesReport(html_format, api_channel)

    daily_report.generate_and_send("user@example.com")
    weekly_report.generate_and_send("ftp://example.com/reports")
    monthly_report.generate_and_send("https://api.example.com/reports")
