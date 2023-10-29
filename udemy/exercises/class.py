# Class car

class Car:
    def __init__(self, name):
        self.name = name
        self._brand = None
        self._engine = None

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, value):
        self._engine = value

    def show_infos(self):
        print(f'Car: {self.name}')
        print(f'Brand: {self.brand.__dict__}')
        print(f'Engine: {self.engine.__dict__}')

    def build_car(self, car_brand, car_engine):
        print('Building Car')
        self._brand = car_brand
        self._engine = car_engine


class Engine:
    def __init__(self, car_engine):
        self.engine = car_engine


class Brand:
    def __init__(self, car_brand):
        self.brand = car_brand


car = Car('Fusca')
brand = Brand('Volkswagen')
engine = Engine('1.6')

car.brand = brand
car.engine = engine

car.build_car(brand, engine)
car.show_infos()
