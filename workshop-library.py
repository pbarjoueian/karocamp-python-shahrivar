class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow_book(self):
        if self.is_borrowed:
            raise Exception(f"The book '{self.title}' is already borrowed.")
        self.is_borrowed = True

    def return_book(self):
        if not self.is_borrowed:
            raise Exception(f"The book '{self.title}' was not borrowed.")
        self.is_borrowed = False


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow(self, book):
        if book in self.borrowed_books:
            raise Exception(
                f"The book '{book.title}' is already borrowed by {self.name}."
            )
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book not in self.borrowed_books:
            raise Exception(f"The book '{book.title}' is not borrowed by {self.name}.")
        self.borrowed_books.remove(book)


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def borrow_book(self, isbn, member_id):
        book = None
        for b in self.books:
            if isbn == b.isbn:
                book = b
        member = next((m for m in self.members if m.member_id == member_id), None)

        if not book:
            raise Exception(f"No book with ISBN {isbn} found in the library.")
        if not member:
            raise Exception(f"No member with ID {member_id} found.")
        if book.is_borrowed:
            raise Exception(f"The book '{book.title}' is already borrowed.")

        book.borrow_book()
        member.borrow(book)

    def return_book(self, isbn, member_id):
        book = next((b for b in self.books if b.isbn == isbn), None)
        member = next((m for m in self.members if m.member_id == member_id), None)

        if not book:
            raise Exception(f"No book with ISBN {isbn} found in the library.")
        if not member:
            raise Exception(f"No member with ID {member_id} found.")

        book.return_book()
        member.return_book(book)

    def list_available_books(self):
        available_books = [book for book in self.books if not book.is_borrowed]
        return available_books


# مثال استفاده
library = Library()

# افزودن کتاب‌ها
book1 = Book("1984", "George Orwell", "12345")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "67890")
library.add_book(book1)
library.add_book(book2)

# ثبت اعضا
member1 = Member("Alice", "001")
member2 = Member("Bob", "002")
library.register_member(member1)
library.register_member(member2)

# امانت‌گیری کتاب
library.borrow_book("12345", "001")

# لیست کتاب‌های موجود
for book in library.list_available_books():
    print(f"Available Book: {book.title}")

# بازگرداندن کتاب
library.return_book("12345", "001")
