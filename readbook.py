class Library:
    books = []
    @classmethod
    def how_many_books(cls):
        return "There are {} books in the library".format(len(cls.books))
class Book:
    pass

    def __init__(self, pages, name, ):
        self.pages = pages
        self.name = name
        self.current_page = 1
        Library.books.append(self)

    def turn_page_forward(self):
        self.current_page += 1

    def turn_page_backward(self):
        self.current_page -= 1





bird = Book( 250, "To Kill a Mocking Bird")
it = Book(250, "it")

print(bird)
print(it.turn_page_forward())
print(it.turn_page_forward())
print(it.turn_page_forward())
print(it.turn_page_forward())
print(it.current_page)
print(Library.how_many_books())
