# Main

# Imports
from calculator import sum_number

try:
    print(sum_number(12, '13'))
except AssertionError as error:
    print(f'Invalid operation - {error}')
