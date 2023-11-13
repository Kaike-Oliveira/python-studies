# Composition

class Person:
    def __init__(self, name, last_name) -> None:
        self.name = name
        self.last_name = last_name


class Customer(Person):
    super.__init__


customer_1 = Customer('Kaike', 'Oliveira')
