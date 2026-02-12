import random

class User:
    _id_counter = 1000   # Class variable for unique IDs

    def __init__(self, name):
        self._name = name                      # Encapsulation
        self._user_id = User._id_counter
        User._id_counter += 1
        self._borrowed_books = []  

    def get_user_id(self):
        return self._user_id
        
    def get_user_name(self):
        return self._name

    def get_borrowed_books(self):
        return self._borrowed_books

    def borrow_book(self, book):
        if book.is_available:
            self._borrowed_books.append(book)
            book.set_availability(False)
            print(f"{self._name} borrowed '{book.get_title()}'")
        else:
            print("Book not available")

    def return_book(self, book):
        if book in self._borrowed_books:
            self._borrowed_books.remove(book)
            book.set_availability(True)
            print(f"{self._name} returned '{book.get_title()}'")
        else:
            print("This book was not borrowed by the user.")

    def display_info(self):
        return f"User ID: {self._user_id}, Name: {self._name}"

    def __str__(self):
        return self.display_info()      

    
# Inheritance
class Student(User):
    def display_info(self):  # Polymorphism
        return f"[Student] ID: {self._user_id}, Name: {self._name}"


class Librarian(User):
    def display_info(self):  # Polymorphism
        return f"[Librarian] ID: {self._user_id}, Name: {self._name}"  