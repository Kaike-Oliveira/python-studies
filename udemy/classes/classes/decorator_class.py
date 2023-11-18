# Decorator classes

class Multiply:
    def __init__(self, func):
        self.func = func
        self._multiplier = 10

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        return result * self._multiplier


@Multiply
def sum_numbers(x, y):
    return x + y


sum_1 = sum_numbers(2, 5)
print(sum_1)
