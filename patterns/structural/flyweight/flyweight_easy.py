class Book:
    def __init__(
        self,
        name: str,
        author: str,
        genre: str,
    ) -> None:
        self.__name = name
        self.__author = author
        self.__genre = genre

    def display(self) -> None:
        print(f"Book: {self.__name}, Author: {self.__author}, Genre: {self.__genre}")


class BookFactory:
    def __init__(self) -> None:
        self.__cache = dict()

    def get_book(self, name: str, author: str, genre: str) -> Book:
        key = (name, author, genre)
        if key not in self.__cache:
            self.__cache[key] = Book(name, author, genre)
        return self.__cache[key]


class BookContext:
    def __init__(
        self,
        book_info: Book,
        location: str,
    ) -> None:
        self.book_info = book_info
        self.location = location

    def display(self) -> None:
        self.book_info.display()
        print(f"Location: {self.location}")


def client_code():
    factory = BookFactory()

    context1 = BookContext(
        factory.get_book("1984", "George Orwell", "Dystopian"), "Shelf 1, Row 3"
    )
    context2 = BookContext(
        factory.get_book("To Kill a Mockingbird", "Harper Lee", "Fiction"),
        "Shelf 2, Row 1",
    )
    context3 = BookContext(
        factory.get_book("1984", "George Orwell", "Dystopian"), "Shelf 1, Row 4"
    )

    context1.display()
    context2.display()
    context3.display()
