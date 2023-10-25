# Instates methods

class Car:
    def __init__(self, brand: str, year: int, model: str):
        self.brand = brand
        self.year = year
        self.model = model

    def accelerate(self):
        print(f'{self.model} is accelerating!')


tesla = Car('Tesla', 2023, 'Model S')
tesla.accelerate()
