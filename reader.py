from book import Book

class Reader:
    """Help Again"""
    def __init__(self, fav_book, current_book):
        self.favourite_book = fav_book
        self.currently_reading = current_book

    def finish_book(self, it_was_the_best_ever):
        if it_was_the_best_ever:
          self.favourite_book = self.currently_reading

        self.currently_reading = None

book1 = Book("Panda Bear, Panda Bear, What Do You See?", "Eric Carle")
book2 = Book("Bear Town", "Fredrik Backman")
print(book1.author)
print(book2)

panda_the_bear = Reader(book1, book2)

print(panda_the_bear)
