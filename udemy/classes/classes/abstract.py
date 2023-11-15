# Abstract

# Imports
from abc import ABC, abstractmethod


class Abstract(ABC):
    def __init__(self, name) -> None:
        self.name = name

    @property
    def name(self): ...

    @name.setter
    def name(self, name): ...


class AbstractChild(Abstract):
    def __init__(self, name) -> None:
        super().__init__(name)
