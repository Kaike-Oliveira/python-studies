# Calculator with while

start_ask = input('Do you like to start? [y] or [n] ')

while True:
    logout = input('Quit? [s] ').lower().startswith('s')
    if logout:
        break

    num_1 = input('Type a number: ')
    num_2 = input('Type other number: ')
    operator = input('Type the operator: ')

    valid_numbers = None

    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        valid_numbers = True
    except Exception as error:
        print(error)
        valid_numbers = None

    if valid_numbers is None:
        print('Invalid number!')
        continue

    if operator == '+':
        print(num_1_float + num_2_float)
    elif operator == '-':
        print(num_1_float - num_2_float)
    elif operator == '*':
        print(num_1_float * num_2_float)
    else:
        print('Invalid operator!')

