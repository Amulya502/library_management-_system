class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        print("Title: {}".format(self.title))
        print("Author: {}".format(self.author))
        print("ISBN: {}".format(self.isbn))


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book '{}' added to the library.".format(book.title))

    def display_all_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("All Books in the Library:")
            for book in self.books:
                book.display_info()
                print("---------------------")

    def search_by_title(self, title):
        found_books = [book for book in self.books if book.title.lower() == title.lower()]

        if not found_books:
            print("No books with the title '{}' found in the library.".format(title))
        else:
            print("Books with the title '{}':".format(title))
            for book in found_books:
                book.display_info()
                print("---------------------")

# Example usage:
library = Library()

book1 = Book("The Python Programming Language", "Guido van Rossum", "978-0-13-407643-0")
book2 = Book("Introduction to Machine Learning", "Andrew Ng", "978-1-119-54556-0")

library.add_book(book1)
library.add_book(book2)

# Display all books in the library
library.display_all_books()

# Search for a book by title using user input
search_title = input("Enter the title of the book you want to search: ")
library.search_by_title(search_title)
