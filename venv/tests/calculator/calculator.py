# Simple calculator

def sum_number(x: float, y: float) -> float:
    assert isinstance(x, (int, float)), 'x should be int of float'
    assert isinstance(y, (int, float)), 'y should be int of float'
    return x + y
