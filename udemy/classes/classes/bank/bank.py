# Imports
from abc import ABC


class Person(ABC):
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age


class Account(ABC):
    def __init__(self, number: int, balance: float):
        self._branch = '0001'
        self._number = number
        self._balance = balance

    def withdraw(self, value):
        return self._balance - value

    def deposit(self, value):
        return self._balance + value

    def extract(self):
        return self._balance


class Customer(Person, Account):
    pass
