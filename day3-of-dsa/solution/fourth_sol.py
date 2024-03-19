class Book:
    
    def __init__(self, bookid, title, price):
        self.bookid=bookid
        self.title=title
        self.price=price
    def show_book(self):
        return f""" book Id: {self.bookid}\t book Title: {self.title}\t book price {self.price}"""
        
ari=Book("1","arihant class 12th",1500)
print(ari.show_book())