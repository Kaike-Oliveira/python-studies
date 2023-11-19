# Data Classes

# Imports
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    last_name: str

    @property
    def full_name(self):
        return f'{self.name} {self.last_name}'


if __name__ == '__main__':
    p1 = Person('Kaike', 'Oliveira')
    print(p1.full_name())
