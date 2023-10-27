class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price 
        
    def get_book_info(self):
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price}"
    
def get_total_price(books):
    price = 0
    for book in books:
        price += book.price
    return price

description = "This is a module named bookstore."