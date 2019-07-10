class Person:
    """ This is a Person class """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return "Hello my name is {}".format(self.name)


daniel = Person("Daniel", 26)

print(daniel.introduce())

#Recipe will have title, description, min
class Recipe:
    """Class for a recipe"""

    def __init__(self, title, description, min):
        self.title = title
        self.description = description
        self.min = min

    def __str__(self):
        return "{} {}".format(self.title, self.description)



taco = Recipe("Taco Bell", "Taco Yummy", 30)
print(taco)

class BankAccount:
    """Bank Account class"""

    def __init__(self, balance=0, interest_rate=1.13):
        self.balance = balance
        self.interest_rate = interest_rate

    def __str__(self):
        return "Your balance: {} that has a interest_rate of {}".format(self.balance, self.interest_rate)

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def gain_interest(self):
        self.balance *= self.interest_rate
        return self.balance

account1 = BankAccount()
print(account1.deposit(20))
print(account1.deposit(20))
print(account1.gain_interest())
# print(account1.)
