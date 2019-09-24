class Book:
    def __init__(self, title, author, publisher):
        self.title = title
        self.author = author
        self.publisher = publisher
    def __str__(self):
        return "This book is %s by %s, published by %s." % (self.title, self.author, self.publisher)


'''  Unit Test '''
if __name__ == "__main__":
    book = Book("The Cat in the Hat", "Dr. Seuss", "Random House")
    print(book)
