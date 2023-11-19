# Imports
from abc import ABC
import accounts


class Person(ABC):
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age: int):
        self._age = age

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self._name!r}, {self._age!r})'
        return f'{class_name}{attrs}'


class Customer(Person):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.account: accounts.Account | None = None

if __name__ == '__main__':
    c1 = Customer('Kaike', 18)
    c1.account = accounts.CurrentAccount('001', 133, 0, 0)
    print(c1)
    print(c1.account)
