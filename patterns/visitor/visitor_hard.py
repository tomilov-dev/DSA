from abc import ABC
from abc import abstractmethod


class Visitor(ABC):
    @abstractmethod
    def visit_text_file(self, text_file: "TextFile") -> None:
        pass

    @abstractmethod
    def visit_csv_file(self, csv_file: "CSVFile") -> None:
        pass

    @abstractmethod
    def visit_json_file(self, json_file: "JSONFile") -> None:
        pass

    @abstractmethod
    def visit_xml_file(self, xml_file: "XMLFile") -> None:
        pass


class FileCompressor(Visitor):
    def visit_text_file(self, text_file: "TextFile") -> None:
        print(f"Compress text file: {text_file.content}")

    def visit_csv_file(self, csv_file: "CSVFile") -> None:
        print(f"Compress csv file: {csv_file.data}")

    def visit_json_file(self, json_file: "JSONFile") -> None:
        print(f"Compress json file: {json_file.data}")

    def visit_xml_file(self, xml_file: "XMLFile") -> None:
        print(f"Compress xml file: {xml_file.data}")


class FileEncryptor(Visitor):
    def visit_text_file(self, text_file: "TextFile") -> None:
        print(f"Encrypt text file: {text_file.content}")

    def visit_csv_file(self, csv_file: "CSVFile") -> None:
        print(f"Encrypt csv file: {csv_file.data}")

    def visit_json_file(self, json_file: "JSONFile") -> None:
        print(f"Encrypt json file: {json_file.data}")

    def visit_xml_file(self, xml_file: "XMLFile") -> None:
        print(f"Encrypt xml file: {xml_file.data}")


class FileUploader(Visitor):
    def visit_text_file(self, text_file: "TextFile") -> None:
        print(f"Upload text file: {text_file.content}")

    def visit_csv_file(self, csv_file: "CSVFile") -> None:
        print(f"Upload csv file: {csv_file.data}")

    def visit_json_file(self, json_file: "JSONFile") -> None:
        print(f"Upload json file: {json_file.data}")

    def visit_xml_file(self, xml_file: "XMLFile") -> None:
        print(f"Upload xml file: {xml_file.data}")


class File(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass


class TextFile(File):
    def __init__(self, content: str) -> None:
        self.content = content

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_text_file(self)


class CSVFile(File):
    def __init__(self, data: list[list[str]]) -> None:
        self.data = data

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_csv_file(self)


class JSONFile(File):
    def __init__(self, data: dict) -> None:
        self.data = data

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_json_file(self)


class XMLFile(File):
    def __init__(self, data: str) -> None:
        self.data = data

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_xml_file(self)


def client_code():
    text_file = TextFile(content="This is a text file.")
    csv_file = CSVFile(data=[["Name", "Age"], ["Alice", "30"], ["Bob", "25"]])
    json_file = JSONFile(data={"name": "Alice", "age": 30})
    xml_file = XMLFile(data="<person><name>Alice</name><age>30</age></person>")

    file_compressor = FileCompressor()
    file_encryptor = FileEncryptor()
    file_uploader = FileUploader()

    text_file.accept(file_compressor)
    csv_file.accept(file_compressor)
    json_file.accept(file_compressor)
    xml_file.accept(file_compressor)

    text_file.accept(file_encryptor)
    csv_file.accept(file_encryptor)
    json_file.accept(file_encryptor)
    xml_file.accept(file_encryptor)

    text_file.accept(file_uploader)
    csv_file.accept(file_uploader)
    json_file.accept(file_uploader)
    xml_file.accept(file_uploader)
