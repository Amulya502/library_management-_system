# Define a class representing a Book
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    # Method to display book information
    def display_info(self):
        print("Title: {}".format(self.title))
        print("Author: {}".format(self.author))
        print("ISBN: {}".format(self.isbn))


# Define a subclass EBook that inherits from the Book class
class EBook(Book):
    def __init__(self, title, author, isbn, file_format):
        super().__init__(title, author, isbn)
        self.file_format = file_format

    # Override the display_info method to include file format
    def display_info(self):
        super().display_info()
        print("File Format: {}".format(self.file_format))


# Define a class representing a Library
class Library:
    def __init__(self):
        self.books = []

    # Method to add a book to the library
    def add_book(self, book):
        self.books.append(book)
        print("Book '{}' added to the library.".format(book.title))

    # Method to display information about all books in the library
    def display_all_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("All Books in the Library:")
            for book in self.books:
                book.display_info()
                print("---------------------")

    # Method to search for a book by title
    def search_by_title(self, title):
        found_books = [book for book in self.books if book.title.lower() == title.lower()]

        if not found_books:
            print("No books with the title '{}' found in the library.".format(title))
        else:
            print("Books with the title '{}':".format(title))
            for book in found_books:
                book.display_info()
                print("---------------------")

    # Method to search for an ebook by title
    def search_ebook_by_title(self, title):
        found_ebooks = [book for book in self.books if isinstance(book, EBook) and book.title.lower() == title.lower()]

        if not found_ebooks:
            print("No ebooks with the title '{}' found in the library.".format(title))
        else:
            print("EBooks with the title '{}':".format(title))
            for ebook in found_ebooks:
                ebook.display_info()
                print("---------------------")


# Example usage:
library = Library()

book1 = Book("The Python Programming Language", "Guido van Rossum", "978-0-13-407643-0")
book2 = Book("Introduction to Machine Learning", "Andrew Ng", "978-1-119-54556-0")
ebook1 = EBook("Learn Python the Hard Way", "Zed Shaw", "978-0-321-88491-6", "PDF")
ebook2 = EBook("Dive into Python 3", "Mark Pilgrim", "978-1-59059-356-1", "EPUB")

library.add_book(book1)
library.add_book(book2)
library.add_book(ebook1)
library.add_book(ebook2)

# Display all books in the library
library.display_all_books()

# Search for a book by title using user input
search_title = input("Enter the title of the book you want to search: ")
library.search_by_title(search_title)

# Search for an ebook by title using user input
search_title_ebook = input("Enter the title of the ebook you want to search: ")
library.search_ebook_by_title(search_title_ebook)
