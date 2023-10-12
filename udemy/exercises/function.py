# Function

def multiple(*args: int):
    total = 1
    for numbers in args:
        total *= numbers

    return total


result = multiple(1, 5, 3, 8)


def odd_even():
    if result % 2 == 0:
        odd_or_even = f'The number {result} is even!'
    else:
        odd_or_even = f'The number {result} is odd!'
    return odd_or_even


is_odd_or_even = odd_even()
print(is_odd_or_even)


# Multiplication

def create_mult(multplicador):
    def mult(number):
        return number * multplicador

    return mult


double = create_mult(2)
triple = create_mult(3)
quadra = create_mult(4)

print(double(2))
print(triple(2))
print(quadra(2))
