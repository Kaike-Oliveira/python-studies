# Try Except

# Show an error if the user or developer pass a wrong data

# TRY - Try to execute the code
# EXCEPT - Find an error

number = input('Type a number: ')

try:
    double_number = float(number) * 2
    print(f'The double of {number} is {double_number}')
except:
    print('This is not a number')

