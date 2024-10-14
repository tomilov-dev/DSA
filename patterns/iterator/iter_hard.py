class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"{self.title} by {self.author}, published in {self.year}"


class BookIterator:
    def __init__(self, books: list[Book]) -> None:
        self.books = books
        self.__pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__pos < len(self.books):
            pos = self.__pos
            self.__pos += 1
            return self.books[pos]

        else:
            raise StopIteration


class FilteredBookIterator:
    def __init__(
        self,
        books: list[Book],
        title: str | None = None,
        author: str | None = None,
        year: int | None = None,
    ) -> None:
        self.books = books
        self.title = title
        self.author = author
        self.year = year
        self.__pos = 0

    def filter(self, book: Book) -> bool:
        check1 = True if not self.title else self.title == book.title
        check2 = True if not self.author else self.author == book.author
        check3 = True if not self.year else self.year == book.year
        return check1 and check2 and check3

    def __iter__(self):
        return self

    def __next__(self):
        while self.__pos < len(self.books):
            if self.filter(self.books[self.__pos]):
                pos = self.__pos
                self.__pos += 1
                return self.books[pos]
            else:
                self.__pos += 1
        raise StopIteration


class Library:
    def __init__(self, books: list[Book] | None = None) -> None:
        self.books = books or []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, title: str, author: str, year: int) -> Book | None:
        for book in self.books:
            if book.title == title and book.author == author and book.year == year:
                self.books.remove(book)
                return book

    def find_books_by_author(self, author: str) -> list[Book]:
        return list(FilteredBookIterator(self.books, author=author))

    def __iter__(self):
        return BookIterator(self.books)


def client_code():
    library = Library()
    library.add_book(Book("1984", "George Orwell", 1949))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee", 1960))
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", 1925))
    library.add_book(Book("Animal Farm", "George Orwell", 1945))

    library.remove_book("1984", "George Orwell", 1949)

    orwell_books = library.find_books_by_author("George Orwell")

    for book in library:
        print(book)

    for book in orwell_books:
        print(book)
