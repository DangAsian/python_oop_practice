import random
from datetime import datetime

class Book:
    on_shelf = []
    on_loan  = []

    @classmethod
    def create(cls, title, author, ISBN):
        new_book = Book(title, author, ISBN)
        cls.on_shelf.append(new_book)
        return new_book

    @classmethod
    def current_due_date(cls):
        now = datetime.now()
        two_weeks = 60 * 60 * 24 * 14
        future_timestamp = now.timestamp() + two_weeks
        return datetime.fromtimestamp(future_timestamp)

    @classmethod
    def overdue_books(cls):
        overdue = []
        now = datetime.now()
        for book in cls.on_loan:
            if book.due < now:
                overdue.append(book)
        return overdue


    @classmethod
    def browse(cls):
        return random.choice(cls.on_shelf)

    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN

    def __repr__(self):
        return "{}".format(self.title)


    def borrow(self):
        lent_out = self.lent_out()
        if lent_out == False:
            due = Book.current_due_date()
            self.due = due
            Book.on_shelf.remove(self)
            Book.on_loan.append(self)

            return True

    def return_to_library(self):
        lent_out = self.lent_out()
        if lent_out == True:
            Book.on_loan.remove(self)
            Book.on_shelf.append(self)
            self.due = "None"
            return True
        else:
            return False

    def lent_out(self):
        if len(Book.on_loan) == 0:
            return False

        for book in Book.on_loan:
            if self.title == book.title:
                return True
            else:
                return False


book1 = Book.create("Dan's book", "Daniel", "129412587")
book2 = Book.create("Molly's book", "Daniel", "129412587")
# print(book1)
# print(Book.on_shelf)
# print(Book.browse())
print(Book.on_shelf)
print(book1.borrow())
print(Book.on_shelf)

print(Book.overdue_books())
# print(book1.return_to_library())
