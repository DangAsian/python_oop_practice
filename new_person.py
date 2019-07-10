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

class Cat:
    """Class about Cat"""

    def __init__(self, name, preffered_food, meal_time):
        self.name = name
        self.preffered_food = preffered_food
        self.meal_time = meal_time

    def __str__(self):
        return "{} is eating {} at {}".format(self.name, self.preffered_food, self.eat_at())

    def eat_at(self):
        if self.meal_time > 12:
            return "{} PM".format(self.meal_time - 12)
        # elif

cat1 = Cat("pebbles", "meat", 10)
cat2 = Cat("stone", "veg", 12)

print(cat1)
print(cat2.eat_at)

class Player:
    """Class for vid game"""

    def __init__(self, gold_coins = 5, health_points = 10, lives = 5):
        self.gold_coins = gold_coins
        self.health_points = health_points
        self.lives = lives

    def __str__(self):
        return "You have gold: {}, health: {}, lives: {}".format(self.gold_coins, self.health_points, self.lives)

    def level_up(self, level=1):
        self.health_points += level

    def collect_tressure(self):
        if self.gold_coins % 10 != 0:
            self.gold_coins +=1
        else:
            self.level_up()
            self.gold_coins +=1

    def do_battle(self, damage):
        self.health_points -= damage

        if self.health_points < 1:
            self.lives -= 1
            self.health_points = 10

        if self.lives < 1:
            self.restart()

    def restart(self):
        self.gold_coins = 5
        self.health_points = 10
        self.lives = 5
        return "help"

warrior = Player()
# print(warrior.level_up(2))
print(warrior.collect_tressure())
print(warrior)
print(warrior.do_battle(10))
print(warrior)
print(warrior.do_battle(10))
print(warrior)
print(warrior.do_battle(10))
print(warrior)
print(warrior.do_battle(10))
print(warrior)
print(warrior.do_battle(10))
# print(warrior.do_battle(10))
print(warrior)
