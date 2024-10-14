class Catalog:
    def __init__(self, books: list[str]) -> None:
        self._store = dict()
        for book in books:
            self._store[book] = self._store.get(book, 0) + 1

    def add_book(self, book: str) -> None:
        self._store[book] = self._store.get(book, 0) + 1

    def remove_book(self, book: str) -> None:
        if book not in self._store:
            raise ValueError("Book not found")
        count = self._store.get(book, 0) - 1
        if count == 0:
            del self._store[book]
        else:
            self._store[book] -= 1

    def search_book(self, book: str) -> int | None:
        return self._store.get(book, None)


class Membership:
    def __init__(self) -> None:
        self._members = dict()

    def add_member(self, member: str, status: str) -> None:
        self._members[member] = status

    def remove_member(self, member: str) -> None:
        if member not in self._members:
            raise ValueError("Member not found")
        del self._members[member]

    def is_active_member(self, member: str) -> bool:
        return self._members.get(member) == "active"


class Borrowing:
    def __init__(
        self,
        catalog: Catalog,
        membership: Membership,
        borrowed: list[tuple[str, str]] = [],
    ) -> None:
        self.catalog = catalog
        self.membership = membership

        self._borrowed = dict()
        for person, book in borrowed:
            bkey = self._bkey(person, book)
            self._borrowed[bkey] = self._borrowed.get(bkey, 0) + 1

    def _bkey(self, person: str, book: str) -> tuple[str, str]:
        return (person, book)

    def borrow_book(self, person: str, book: str) -> str:
        if self.catalog.search_book(book) is None:
            raise ValueError("Book not found")
        if not self.membership.is_active_member(person):
            raise ValueError("Person is not an active member")

        bkey = self._bkey(person, book)
        self._borrowed[bkey] = self._borrowed.get(bkey, 0) + 1
        self.catalog.remove_book(book)
        return book

    def borrow_status(self, person: str, book: str) -> int | None:
        return self._borrowed.get(self._bkey(person, book), None)


class LibraryFacade:
    def __init__(
        self,
        catalog: Catalog,
        membership: Membership,
        borrowing: Borrowing,
    ) -> None:
        self.catalog = catalog
        self.membership = membership
        self.borrowing = borrowing

    def add_book(self, book: str) -> None:
        self.catalog.add_book(book)

    def add_member(self, member: str, status: str) -> None:
        self.membership.add_member(member, status)

    def borrow_book(self, person: str, book: str) -> str:
        return self.borrowing.borrow_book(person, book)

    def check_borrow_status(self, person: str, book: str) -> int | None:
        return self.borrowing.borrow_status(person, book)
