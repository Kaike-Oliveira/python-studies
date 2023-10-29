# Composition

class Customer:
    def __init__(self, name):
        self.name = name
        self.address = []

    def add_address(self, number, street):
        self.address.append(Address(number, street))

    def show_address(self):
        for address in self.address:
            print(address.number, address.street)


class Address:
    def __init__(self, number, street):
        self.number = number
        self.street = street


customer1 = Customer('Maria')
customer1.add_address(234, 'Av. Brasil')
customer1.add_address(345, 'Av. Pio XII')

customer1.show_address()

del customer1
