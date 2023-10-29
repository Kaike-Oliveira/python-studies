# Aggregation

class Cart:
    def __init__(self):
        self._products = []

    def total(self):
        return sum([product.price for product in self._products])

    def list_products(self):
        for product in self._products:
            print(f'Product: {product.name}, Price: {product.price:.2f}')

    def add_to_cart(self, *products):
        self._products += products


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()
rice, bean = Product('Rice', 11.90), Product('Beans', 7.40)
cart.add_to_cart(rice, bean)
cart.list_products()
