from book import Book
from user import Student, Librarian


class Library:
    def __init__(self):
        self._books = []
        self._users = []

    # ---------------- BOOK METHODS ----------------

    def add_book(self, title, author):
        book = Book(title, author)
        self._books.append(book)
        print("Book added successfully.")

    def remove_book(self, book_id):
        for book in self._books:
            if book.get_book_id() == book_id:
                self._books.remove(book)
                print("Book removed.")
                return
        print("Book not found.")

    def search_book(self, title):
        for book in self._books:
            if book.get_title().lower() == title.lower():
                print(book)
                return
        print("Book not found.")

    def display_books(self):
        for book in self._books:
            print(book)

    # ---------------- USER METHODS ----------------

    def register_student(self, name):
        student = Student(name)
        self._users.append(student)
        print("Student registered successfully.")

    def register_librarian(self, name):
        librarian = Librarian(name)
        self._users.append(librarian)
        print("Librarian registered successfully.")

    def find_user(self, user_id):
        for user in self._users:
            if user.get_user_id() == user_id:
                return user
        return None

    def find_book(self, book_id):
        for book in self._books:
            if book.get_book_id() == book_id:
                return book
        return None

    # ---------------- FILE HANDLING ----------------

    def save_books(self):
        with open("books.txt", "w") as file:
            for book in self._books:
                file.write(f"{book.get_book_id()},{book.get_title()},{book.get_author()},{book.is_available()}\n")

    def load_books(self):
        try:
            with open("books.txt", "r") as file:
                for line in file:
                    book_id, title, author, status = line.strip().split(",")
                    book = Book(title, author)
                    book._book_id = int(book_id)
                    book.set_availability(status == "True")
                    self._books.append(book)
        except FileNotFoundError:
            pass
