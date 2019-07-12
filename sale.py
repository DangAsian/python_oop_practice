class Whiskey:
    pass

    def __init__(self, price):
        self.price = price

    def tax(self):
        return self.price * 0.5
class Cheese:
    pass

    def __init__(self, price):
        self.price = price

class Toothpaste:
    pass

    def __init__(self, price):
        self.price = price

wild_turkey = Whiskey(40)
gold_label = Whiskey(80)
brie = Cheese(7)
crest = Whiskey(3)


grand_total = 0
items = [wild_turkey, gold_label, brie, crest]
