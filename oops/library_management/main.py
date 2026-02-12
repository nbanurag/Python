from library import Library

def main():
    library = Library()
    library.load_books()

    while True:
        print("\n===== LIBRARY MENU =====")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Register Student")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            library.add_book(title, author)

        elif choice == "2":
            library.display_books()

        elif choice == "3":
            name = input("Enter student name: ")
            library.register_student(name)

        elif choice == "4":
            user_id = int(input("Enter user ID: "))
            book_id = int(input("Enter book ID: "))

            user = library.find_user(user_id)
            book = library.find_book(book_id)

            if user and book:
                user.borrow_book(book)
            else:
                print("Invalid user or book ID.")

        elif choice == "5":
            user_id = int(input("Enter user ID: "))
            book_id = int(input("Enter book ID: "))

            user = library.find_user(user_id)
            book = library.find_book(book_id)

            if user and book:
                user.return_book(book)
            else:
                print("Invalid user or book ID.")

        elif choice == "6":
            library.save_books()
            print("Data saved. Exiting...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
