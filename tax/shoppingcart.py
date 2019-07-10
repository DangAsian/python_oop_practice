from product import Product

class ShoppingCart:
    """Shopping Cart full of goods"""

    def __init__(self):
        self.products = []

    def __str__(self):
        return "{}".format(self.products)

    def add_item(self, product):
        self.products.append(product)

    def remove_item(self, product):
        self.products.remove(product)

    def before_tax(self):
        total = 0
        for product in self.products:
            if product.quantity > 1:
                total += product.price * product.quantity
            else:
                total += product.price
        return total

    def after_tax(self):
        total = 0
        for product in self.products:
            total += product.product_total_price()
        return total

    def find_expensive(self):
        exp = 0
        for product in self.products:
            print(product)
            if product.price > exp:
                exp = product.price
        return exp

wax = Product("bees wax", 5, 10)
knee = Product("knee wax", 10)
hair = Product("hair wax", 15)

shopper = ShoppingCart()
shopper.add_item(wax)
shopper.add_item(knee)
shopper.add_item(hair)
# print(shopper.products)

print(shopper.before_tax())
# print(shopper.after_tax())
# print(shopper.find_expensive())
