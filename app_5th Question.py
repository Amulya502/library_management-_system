from flask import Flask, jsonify, request

# Create a Flask web application
app = Flask(__name__)

# Define a class representing a Book
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    # Convert book details to a dictionary
    def to_dict(self):
        return {"title": self.title, "author": self.author, "isbn": self.isbn}

# Define a class representing a Library
class Library:
    def __init__(self):
        self.books = []

    # Add a book to the library
    def add_book(self, book):
        self.books.append(book)

    # Get details of all books in the library
    def get_all_books(self):
        return [book.to_dict() for book in self.books]

    # Remove a book from the library based on ISBN
    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]

# Create an instance of the Library class
library = Library()

# Define a route to add a book to the library
@app.route('/add_book', methods=['POST'])
def add_book():
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    isbn = data.get('isbn')
    new_book = Book(title, author, isbn)
    library.add_book(new_book)
    return jsonify({"message": "Book added successfully"})

# Define a route to list all books in the library
@app.route('/list_books', methods=['GET'])
def list_books():
    return jsonify({"books": library.get_all_books()})

# Define a route to delete a book from the library
@app.route('/delete_book', methods=['DELETE'])
def delete_book():
    data = request.get_json()
    isbn = data.get('isbn')
    library.remove_book(isbn)
    return jsonify({"message": "Book deleted successfully"})

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
