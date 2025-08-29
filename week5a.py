# Base class: Book
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def describe(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"

# Derived class: EBook (Inheritance example)
class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)  # Call parent constructor
        self.file_size = file_size  # New attribute

    def describe(self):
        # Overriding method (polymorphism)
        return f"E-Book: '{self.title}' by {self.author}, {self.pages} pages, {self.file_size}MB file size"

# Create objects
book1 = Book("1984", "George Orwell", 328)
ebook1 = EBook("Python 101", "Mike Driscoll", 250, 5)

print(book1.describe())
print(ebook1.describe())
