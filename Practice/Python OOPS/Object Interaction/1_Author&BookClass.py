# Create Author and Book class (Book has Author object).

class Author:
    def __init__(self, name):
        self.name = name

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author   #Author Object

    def show_book(self):
        print("Book Title:", self.title)
        print("Author:", self.author.name)

#Creating Author Object
author1 = Author("J.k Rowling")

#passing author object into Book
book1 = Book("Harry Potter",author1)

book1.show_book()