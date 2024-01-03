# Libraries
from uuid import uuid4


class Restaurant:
    def __init__(self, name: str, category: str) -> None:
        self._id = uuid4()
        self._name = name
        self._category = category
        self._status = False

    def __str__(self) -> str:
        return self._name


restaurant = Restaurant('Sushi', 'Japa')
print(restaurant)
