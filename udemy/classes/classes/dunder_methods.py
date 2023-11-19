# Dunder Methods


class Coordinate:
    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f'{class_name}(x={self._x}, y={self._y})'


coordinate_1 = Coordinate(22, 15)
coordinate_2 = Coordinate(564, 8293)

print(coordinate_1)
print(coordinate_2)
