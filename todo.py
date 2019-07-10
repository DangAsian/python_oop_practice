#let user assign due date for an item
#print out remaining time until due date
#buy groceries due in __

from datetime import date

class ToDo:
    """To Do List"""

    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False
        # self.today_date = date.today()

    def complete(self):
        self.completed = True

    def days_remaining(self):
        days_between = self.due_date - date.today()
        return days_between.days


    def __str__(self):
        return "To do: {} due {} ".format(self.description, self.due_date.humanize())

# print('enter year')
# year = int(input())
#
# print('enter month')
# month = int(input())
#
# print('enter day')
# day = int(input())

# todo = ToDo("buy groceries", date(2019,7,11))

# print(todo.days_remaining())
# print(todo)
