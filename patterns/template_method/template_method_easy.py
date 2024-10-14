from abc import ABC
from abc import abstractmethod


class DocumentProcessor(ABC):
    def process_document(self, input_path: str, output_file: str) -> None:
        self.read_document(input_path)
        self.process_content()
        self.save_document(output_file)

    @abstractmethod
    def read_document(self, file_path: str) -> None:
        pass

    @abstractmethod
    def process_content(self) -> None:
        pass

    @abstractmethod
    def save_document(self, file_path: str) -> None:
        pass


class TextDocumentProcessor(DocumentProcessor):
    def read_document(self, file_path: str) -> None:
        print("Read text document")

    def process_content(self) -> None:
        print("Process text document")

    def save_document(self, file_path: str) -> None:
        print("Save text document")


class PdfDocumentProcessor(DocumentProcessor):
    def read_document(self, file_path: str) -> None:
        print("Read PDF document")

    def process_content(self) -> None:
        print("Process PDF document")

    def save_document(self, file_path: str) -> None:
        print("Save PDF document")


def client_code():
    text_processor = TextDocumentProcessor()
    text_processor.process_document("example.txt", "output.txt")

    pdf_processor = PdfDocumentProcessor()
    pdf_processor.process_document("example.pdf", "output.pdf")
