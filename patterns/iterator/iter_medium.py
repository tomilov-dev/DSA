class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year


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


class Library:
    def __init__(self, books: list[Book] | None = None) -> None:
        self.books = books or []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, name: str, author: str, year: int) -> Book | None:
        for book in self.books:
            if book.title == name and book.author == author and book.year == year:
                self.books.remove(book)
                return book

    def __iter__(self):
        return BookIterator(self.books)


def client_code():
    library = Library()
    library.add_book(Book("1984", "George Orwell", 1949))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee", 1960))
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", 1925))

    library.remove_book("1984", "George Orwell", 1949)

    for book in library:
        print(book)
