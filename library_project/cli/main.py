import logging
from library_manager.book import Book
from library_manager.inventory import LibraryInventory

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    inventory = LibraryInventory()

    # Load inventory from file
    inventory.load_from_file("books.json")

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book by Title")
        print("6. Search Book by ISBN")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        try:
            if choice == '1':
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                isbn = input("Enter book ISBN: ")
                book = Book(title, author, isbn)
                inventory.add_book(book)
                logger.info(f"Added book: {book}")
            
            elif choice == '2':
                isbn = input("Enter ISBN of the book to issue: ")
                books = inventory.search_by_isbn(isbn)
                if books:
                    books[0].issue()
                    logger.info(f"Issued book: {books[0]}")
                else:
                    print("Book not found.")
            
            elif choice == '3':
                isbn = input("Enter ISBN of the book to return: ")
                books = inventory.search_by_isbn(isbn)
                if books:
                    books[0].return_book()
                    logger.info(f"Returned book: {books[0]}")
                else:
                    print("Book not found.")
            
            elif choice == '4':
                inventory.display_all()
            
            elif choice == '5':
                title = input("Enter title to search: ")
                results = inventory.search_by_title(title)
                if results:
                    for book in results:
                        print(book)
                else:
                    print("No books found.")
            
            elif choice == '6':
                isbn = input("Enter ISBN to search: ")
                results = inventory.search_by_isbn(isbn)
                if results:
                    for book in results:
                        print(book)
                else:
                    print("No books found.")
            
            elif choice == '7':
                # Save to file before exiting
                inventory.save_to_file("books.json")
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")
        
        except Exception as e:
            print(f"Error: {e}")
            logger.error(f"Error: {e}")

if __name__ == "__main__":
    main()