# Imports
from models.menu.menu_item import MenuItem


class Drink(MenuItem):
    def __init__(self, name: str, price: float, size: int) -> None:
        super().__init__(name, price)
        self._size = size

    def apply_discount(self) -> None:
        self._price -= (self._price * 0.08)
