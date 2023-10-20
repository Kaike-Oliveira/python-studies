# Ordered list
import copy

products = [
    {'name': 'Crusher', 'price': 12600},
    {'name': 'Screen', 'price': 8700},
    {'name': 'Telestacker', 'price': 54300},
    {'name': 'Roll', 'price': 970},
    {'name': 'Washing', 'price': 16530},
]

products_update = [
    {**product, 'price': product['price'] + product['price'] * 10 / 100}
    for product in products
]

price_sorted_products = sorted(copy.deepcopy(products_update), key=lambda product: product['price'])
name_sorted_products = sorted(copy.deepcopy(products_update), key=lambda product: product['name'], reverse=True)


def show_products(items):
    for product in items:
        print(product)


show_products(name_sorted_products)
print()
show_products(price_sorted_products)
