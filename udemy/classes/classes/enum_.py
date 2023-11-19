# Imports
import enum

# Directions = enum.Enum('Directions', ['LEFT', 'RIGHT'])

class Directions(enum.Enum):
    LEFT = 1
    RIGHT = 2
    BOTTOM = 3
    TOP = 4


def move(direction: Directions):
    if not isinstance(direction, Directions):
        raise ValueError(f'Invalid directions please use {direction}')
    print(f'Moving to {direction.name.title()}')


move(Directions.LEFT)
move(Directions.RIGHT)
move('BOTTOM')
