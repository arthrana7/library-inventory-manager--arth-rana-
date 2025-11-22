class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = 'available'  # By default, the book is available

    def __str__(self):
        # A simple string representation of the book
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {self.status}"

    def to_dict(self):
        # Converts the book object to a dictionary to store in a JSON file
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "status": self.status
        }

    def issue(self):
        if self.status == 'available':
            self.status = 'issued'
        else:
            print(f"The book '{self.title}' is already issued.")

    def return_book(self):
        if self.status == 'issued':
            self.status = 'available'
        else:
            print(f"The book '{self.title}' is already available.")

    def is_available(self):
        return self.status == 'available'