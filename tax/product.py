
class Product:
    """Product class"""

    def __init__(self, name, price, quantity=1, tax_rate=1.13):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.tax_rate = tax_rate

    def __str__(self):
        return "name: {} price: {} tax_rate: {}".format(self.name,self.price,self.tax_rate)

    def product_total_price(self):
        return self.price * self.tax_rate

wax = Product("bees wax", 10)
# print(wax)
