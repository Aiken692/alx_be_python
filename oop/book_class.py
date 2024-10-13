class Book:
    def __init__(self, title, author, year):
        """Constructor to initialize Book attributes"""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor to clean up when a Book object is deleted"""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation for the Book object"""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation that can recreate the Book object"""
        return f"Book('{self.title}', '{self.author}', {self.year})"
