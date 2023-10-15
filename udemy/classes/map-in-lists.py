# Map in lists

# Products
products = [
    {'product': 'Crusher', 'price': 16700},
    {'product': 'Roll', 'price': 340},
    {'product': 'Telestacker', 'price': 23400},
    {'product': 'Screen', 'price': 9800},
]

products_update = [
    {**product, 'price': product['price'] + product['price'] * 10 / 100}
    for product in products
    if product['price'] >= 1000  # filter the product when the price is 1000 or +
]

print(*products_update, sep='\n')
