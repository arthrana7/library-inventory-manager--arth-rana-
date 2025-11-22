import json
from library_manager.book import Book

class LibraryInventory:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
    
    def search_by_title(self, title):
        results = [book for book in self.books if title.lower() in book.title.lower()]
        return results

    def search_by_isbn(self, isbn):
        results = [book for book in self.books if book.isbn == isbn]
        return results

    def display_all(self):
        for book in self.books:
            print(book)

    def save_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                json.dump([book.to_dict() for book in self.books], file, indent=4)
        except Exception as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                books_data = json.load(file)
                self.books = [Book(**book_data) for book_data in books_data]
        except FileNotFoundError:
            print("File not found, starting with an empty library.")
        except json.JSONDecodeError:
            print("Error decoding JSON, the file might be corrupted.")