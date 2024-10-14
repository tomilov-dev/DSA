from abc import ABC
from abc import abstractmethod


class Document(ABC):
    @abstractmethod
    def process(self) -> None:
        pass


class DocumentCreator(ABC):
    @abstractmethod
    def create_document(self) -> Document:
        pass

    def process_document(self, document: Document) -> None:
        return document.process()


class Resume(Document):
    def process(self) -> None:
        print("Process resume")


class ResumeCreator(DocumentCreator):
    def create_document(self) -> Resume:
        return Resume()


class Report(Document):
    def process(self) -> None:
        print("Process report")


class ReportCreator(DocumentCreator):
    def create_document(self) -> Report:
        return Report()


def client_code(creator: DocumentCreator) -> None:
    document = creator.create_document()
    creator.process_document(document)


if __name__ == "__main__":
    print("App: Launched with the ResumeCreator.")
    client_code(ResumeCreator())
    print("\n")

    print("App: Launched with the ReportCreator.")
    client_code(ReportCreator())
