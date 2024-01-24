class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        print("Title: {}".format(self.title))
        print("Author: {}".format(self.author))
        print("ISBN: {}".format(self.isbn))

# Example usage:
book1 = Book("The Python Programming Language", "Guido van Rossum", "978-0-13-407643-0")
book2 = Book("Introduction to Machine Learning", "Andrew Ng", "978-1-119-54556-0")

# Display book information
book1.display_info()
print("\n")
book2.display_info()
