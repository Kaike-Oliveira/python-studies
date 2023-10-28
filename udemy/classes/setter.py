# Setter

class Pen:
    def __init__(self, color):
        # private -> _color
        self._color = color  # can't be used out of the class
        self._brand = None

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value: str):
        if value.lower() == 'pink':
            raise ValueError('Not allowed color!')
        self._color = value

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value


pen = Pen('Blue')  # Start the pen with this value
print(f'Before setter: {pen.color}')

pen.color = 'Dark Blue'  # Modify the color pen
print(f'After setter: {pen.color}')

pen.brand = 'Bic'
print(pen.brand)

pen.color = 'Pink'
print(f'Pink color pen {pen.color}')
