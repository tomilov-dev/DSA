from abc import ABC
from abc import abstractmethod


class IReportElement(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


class Header(IReportElement):
    pass


class Footer(IReportElement):
    pass


class Content(IReportElement):
    pass


class PDFHeader(Header):
    def render(self) -> str:
        return "PDF Header"


class PDFFooter(Footer):
    def render(self) -> str:
        return "PDF Footer"


class PDFContent(Content):
    def render(self) -> str:
        return "PDF Content"


class HTMLHeader(Header):
    def render(self) -> str:
        return "HTML Header"


class HTMLFooter(Footer):
    def render(self) -> str:
        return "HTML Footer"


class HTMLContent(Content):
    def render(self) -> str:
        return "HTML Content"


class ReportFactory(ABC):
    @abstractmethod
    def create_header(self) -> Header:
        pass

    @abstractmethod
    def create_footer(self) -> Footer:
        pass

    @abstractmethod
    def create_content(self) -> Content:
        pass


class PDFReportFactory(ReportFactory):
    def create_header(self) -> Header:
        return PDFHeader()

    def create_footer(self) -> Footer:
        return PDFFooter()

    def create_content(self) -> Content:
        return PDFContent()


class HTMLReportFactory(ReportFactory):
    def create_header(self) -> Header:
        return HTMLHeader()

    def create_footer(self) -> Footer:
        return HTMLFooter()

    def create_content(self) -> Content:
        return HTMLContent()


def client_code(report_factory: ReportFactory) -> None:
    header = report_factory.create_header()
    content = report_factory.create_content()
    footer = report_factory.create_footer()

    doc = f"{header.render()}{content.render()}{footer.render()}"
