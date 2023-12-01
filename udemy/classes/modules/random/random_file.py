#  Random

# Imports
import random

random_number = random.randrange(10, 120, 2)  # Generate random numbers 0 - 120
print(f'randrange -> {random_number}')

int_random_number = random.randint(2, 25)  # Generate integers numbers 2 - 25
print(f'randint -> {int_random_number}')

float_random_number = random.uniform(2, 25)
print(f'uniform -> {float_random_number}')
