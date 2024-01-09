from abc import ABC, abstractmethod


class MenuItem(ABC):
    def __init__(self, name: str, price: float) -> None:
        self._name = name
        self._price = price

    def __str__(self) -> str:
        return self._name

    @abstractmethod
    def apply_discount(self) -> None: pass
