# Decorators

def decorator(func):
    print('decorate 1')

    def node(*args, **kwargs):
        print('node')
        response = func(*args, **kwargs)
        return response
    return node


@decorator
def sum_1(x, y):
    return x + y


sum_1(10, 4)
