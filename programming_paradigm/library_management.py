class Book:
    def __init__(self, title, author):
        self.title = title            # Public attribute
        self.author = author          # Public attribute
        self._is_checked_out = False  # Private attribute

    def check_out(self):
        """Check out the book, marking it as unavailable."""
        if self._is_checked_out:
            return False  # Already checked out
        self._is_checked_out = True
        return True

    def return_book(self):
        """Return the book, making it available again."""
        if not self._is_checked_out:
            return False  # Already returned
        self._is_checked_out = False
        return True

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out

class Library:
    def __init__(self):
        self._books = []  # Private list to store books

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Checked out '{title}' successfully.")
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"'{title}' not found in the library.")

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned '{title}' successfully.")
                else:
                    print(f"'{title}' was not checked out.")
                return
        print(f"'{title}' not found in the library.")

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No available books.")

