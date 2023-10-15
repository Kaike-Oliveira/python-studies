# Try except, else and finally

try:
    print('Before exception')
    a = 18
    # b = 0
    c = a / b
    print('After exception')
except ZeroDivisionError:
    print('You cannot divide by zero!')
except NameError:
    print('Name is not defined!')

print('Continue...')
