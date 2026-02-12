class Book:
    _id_counter = 1

    def __init__(self, title, author):
        self._book_id = Book._id_counter
        Book._id_counter += 1
        self._title = title
        self._author = author
        self._is_available = True

    # Getters (Encapsulation)
    def get_book_id(self):
        return self._book_id

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def is_available(self):
        return self._is_available

    def set_availability(self, status):
        self._is_available = status

    # Magic Methods
    def __str__(self):
        status = "Available" if self._is_available else "Not Available"
        return f"ID: {self._book_id}, Title: {self._title}, Author: {self._author}, Status: {status}"

    def __eq__(self, other):
        return self._book_id == other._book_id

    def __len__(self):
        return len(self._title)
