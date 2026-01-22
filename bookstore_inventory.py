#Developer Identification
DEVELOPER_NAME = "Eweje Ayomide Francis "
DEVELOPER_MATRIC = "24/24439"
DEVELOPER_DEPARTMENT = "Computer Science"

class Book:
    def __init__(self, book_isbn, book_title, book_author, stock_quantity):
        self.book_isbn = book_isbn
        self.book_title = book_title
        self.book_author = book_author
        self.stock_quantity = stock_quantity

class InventoryManager:
    def __init__(self):
        self.inventory = {}

    def add_book(self, book):
        self.inventory[book.book_isbn] = book
        print(f"Added: {book.book_title}")

    def update_stock(self, book_isbn, amount):
        if book_isbn in self.inventory:
            self.inventory[book_isbn].stock_quantity += amount
            print(f"Updated {self.inventory[book_isbn].book_title} stock to {self.inventory[book_isbn].stock_quantity}")

# Implementation Instance
manager = InventoryManager()
new_book = Book("978-0132350884", "Clean Code", "Robert C. Martin", 10)
manager.add_book(new_book)