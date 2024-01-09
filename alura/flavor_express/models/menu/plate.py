# Imports
from models.menu.menu_item import MenuItem


class Plate(MenuItem):
    def __init__(self, name: str, price: float, description: str) -> None:
        super().__init__(name, price)
        self._description = description

    def apply_discount(self) -> None:
        self._price -= (self._price * 0.05)
