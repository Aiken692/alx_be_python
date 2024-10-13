# Base class - Book
class Book:
    def __init__(self, title, author):
        """Constructor to initialize the common attributes for a book."""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation of a book."""
        return f"Book: {self.title} by {self.author}"


# Derived class - EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        """Constructor to initialize the attributes of an EBook."""
        super().__init__(title, author)  # Call the base class constructor
        self.file_size = file_size  # Additional attribute specific to EBook

    def __str__(self):
        """String representation of an EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


# Derived class - PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Constructor to initialize the attributes of a PrintBook."""
        super().__init__(title, author)  # Call the base class constructor
        self.page_count = page_count  # Additional attribute specific to PrintBook

    def __str__(self):
        """String representation of a PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Composition - Library
class Library:
    def __init__(self):
        """Constructor to initialize the library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Method to add a book (Book, EBook, or PrintBook) to the library."""
        self.books.append(book)

    def list_books(self):
        """Method to list all books in the library."""
        for book in self.books:
            print(book)  # Will call the __str__ method of the respective class
