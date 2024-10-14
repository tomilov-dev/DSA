from abc import ABC
from abc import abstractmethod


class Visitor(ABC):
    @abstractmethod
    def visit_word_document(self, word_document: "WordDocument") -> None:
        pass

    @abstractmethod
    def visit_pdf_document(self, pdf_document: "PDFDocument") -> None:
        pass

    @abstractmethod
    def visit_excel_document(self, excel_document: "ExcelDocument") -> None:
        pass


class DocumentPrinter(Visitor):
    def visit_word_document(self, word_document: "WordDocument") -> None:
        print("Printing WordDocument")

    def visit_pdf_document(self, pdf_document: "PDFDocument") -> None:
        print("Printing PDFDocument")

    def visit_excel_document(self, excel_document: "ExcelDocument") -> None:
        print("Printing ExcelDocument")


class DocumentSaver(Visitor):
    def visit_word_document(self, word_document: "WordDocument") -> None:
        print("Save WordDocument")

    def visit_pdf_document(self, pdf_document: "PDFDocument") -> None:
        print("Save PDFDocument")

    def visit_excel_document(self, excel_document: "ExcelDocument") -> None:
        print("Save ExcelDocument")


class Document(ABC):
    @abstractmethod
    def accept(self, visitor: "Visitor") -> None:
        pass


class WordDocument(Document):
    def __init__(self, content: str) -> None:
        self.content = content

    def accept(self, visitor: "Visitor") -> None:
        visitor.visit_word_document(self)


class PDFDocument(Document):
    def __init__(self, content: str) -> None:
        self.content = content

    def accept(self, visitor: "Visitor") -> None:
        visitor.visit_pdf_document(self)


class ExcelDocument(Document):
    def __init__(self, data: list[list[int]]) -> None:
        self.data = data

    def accept(self, visitor: "Visitor") -> None:
        visitor.visit_excel_document(self)


def client_code():
    word_document = WordDocument(content="This is a Word document.")
    pdf_document = PDFDocument(content="This is a PDF document.")
    excel_document = ExcelDocument(data=[[1, 2, 3], [4, 5, 6]])

    document_printer = DocumentPrinter()
    document_saver = DocumentSaver()

    word_document.accept(document_printer)
    pdf_document.accept(document_printer)
    excel_document.accept(document_printer)

    word_document.accept(document_saver)
    pdf_document.accept(document_saver)
    excel_document.accept(document_saver)
