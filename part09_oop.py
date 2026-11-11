# Ahmad, Roll No: __________, 2026-11-11
"""Classes, objects, inheritance and composition."""


class Student:
    def __init__(self, name: str, roll_number: int, marks: list[float] | None = None) -> None:
        self.name, self.roll_number, self.marks = name, roll_number, marks or []

    def add_mark(self, mark: float) -> None:
        self.marks.append(mark)

    def average(self) -> float:
        return sum(self.marks) / len(self.marks) if self.marks else 0.0

    def __str__(self) -> str:
        return f"{self.name} (Roll {self.roll_number}): avg {self.average():.1f}"


class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner, self.balance = owner, balance
        self.history: list[str] = []

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount
        self.history.append(f"Deposit: {amount:.2f}")

    def withdraw(self, amount: float) -> None:
        if amount <= 0 or amount > self.balance:
            raise ValueError("Invalid withdrawal")
        self.balance -= amount
        self.history.append(f"Withdraw: {amount:.2f}")


class Book:
    def __init__(self, title: str, author: str, available: bool = True) -> None:
        self.title, self.author, self.available = title, author, available

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: float, available: bool = True) -> None:
        super().__init__(title, author, available)
        self.file_size = file_size

    def __str__(self) -> str:
        return f"{super().__str__()} ({self.file_size} MB)"


class Library:
    def __init__(self) -> None:
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def borrow(self, title: str) -> bool:
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                return True
        return False

    def return_book(self, title: str) -> bool:
        for book in self.books:
            if book.title == title and not book.available:
                book.available = True
                return True
        return False

    def available_books(self) -> list[Book]:
        return [book for book in self.books if book.available]


if __name__ == "__main__":
    account = BankAccount("Ali", 1000)
    account.deposit(250)
    account.withdraw(100)
    print(account.balance, account.history)
