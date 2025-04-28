import copy
from abc import ABC
from abc import abstractmethod


class Document(ABC):
    @abstractmethod
    def clone(self) -> "Document":
        pass


class Author:
    def __init__(
        self,
        name: str,
        email: str,
    ) -> None:
        self.name = name
        self.email = email

    def __repr__(self) -> str:
        return f"{self.name}:{self.email}"


class Report(Document):
    def __init__(
        self,
        author: Author,
        title: str,
        content: str,
    ) -> None:
        self.author = author
        self.title = title
        self.content = content

    def clone(self) -> "Report":
        return copy.deepcopy(self)


class Invoice(Document):
    def __init__(
        self,
        author: Author,
        number: int,
        amount: float,
    ) -> None:
        self.author = author
        self.number = number
        self.amount = amount

    def clone(self) -> "Invoice":
        return copy.deepcopy(self)


def client_code():
    auth1 = Author("John", "john@gmail.ru")
    auth2 = Author("Jenny", "jenny@gmail.ru")

    rep1 = Report(auth1, title="Report 1", content="Content 1")
    rep2 = rep1.clone()

    print("Original Report Author:", rep1.author)
    print("Cloned Report Author:", rep2.author)

    rep2.author = auth2

    print("After changing cloned report author:")
    print("Original Report Author:", rep1.author)
    print("Cloned Report Author:", rep2.author)

    inv1 = Invoice(auth1, number=12345, amount=1000.0)
    inv2 = inv1.clone()

    print("Original Invoice Author:", inv1.author)
    print("Cloned Invoice Author:", inv2.author)

    inv2.author.email = "bob.clone@example.com"

    print("After changing cloned invoice author email:")
    print("Original Invoice Author:", inv1.author)
    print("Cloned Invoice Author:", inv2.author)


if __name__ == "__main__":
    client_code()
