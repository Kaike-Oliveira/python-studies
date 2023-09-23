# Show if is odd or even

number = input('Type a integer number: ')
try:
    # Convert the str number to int
    converted_num = int(number)

    # Check if the number is even or odd
    number_value = converted_num % 2

    # Show the result
    if number_value % 2 == 0:
        print('This number is even')
    else:
        print('This number is odd')
except:
    print('This is not a integer number')
