# Libraries
from uuid import uuid4

# Imports
from alura.flavor_express.models.menu.drink import Drink
from alura.flavor_express.models.menu.menu_item import MenuItem
from alura.flavor_express.models.menu.plate import Plate
from models.rate import Rate


class Restaurant:
    restaurants = []

    def __init__(self, name: str, category: str) -> None:
        self._id = uuid4()
        self._name = name.title()
        self._category = category
        self._status = False
        self._rate = []
        self._menu = []
        Restaurant.restaurants.append(self)

    def __str__(self) -> str:
        return self._name

    @property
    def status(self):
        return 'Active' if self._status else 'Inactive'

    def active_restaurant(self):
        self._status = not self._status

    @classmethod
    def show_restaurants(cls):
        for restaurant in cls.restaurants:
            print(f'Name: {restaurant._name} | Category: {restaurant._category} '
                  f'| Status: {restaurant.status} | Rate: {restaurant.rate_average}')

    def rate_restaurante(self, grade: float, customer: str):
        rate = Rate(customer, grade)
        self._rate.append(rate)

    @property
    def rate_average(self) -> float:
        if not self._rate:
            return 0

        sum_grades = sum(
            rate._grade for rate in self._rate if rate._grade is not None)
        total_grades = len(
            [rate for rate in self._rate if rate._grade is not None])

        if total_grades == 0:
            return 0

        average = round(sum_grades / total_grades, 1)

        return average

    def add_menu_item(self, item):
        if isinstance(item, MenuItem):
            self._menu.append(item)

    @property
    def show_menu(self):
        print(f"{self._name}'s Menu")
        for index, item in enumerate(self._menu, start=1):
            if hasattr(item, 'description'):
                print(f'{index}. Name: {item._name} | Price: {item._price} | Description: {item._description}')
            elif hasattr(item, 'size'):
                print(f'{index}. Name: {item._name} | Price: {item._price} | Size: {item._size}')
