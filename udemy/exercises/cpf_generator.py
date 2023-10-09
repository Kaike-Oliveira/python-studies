# CPF generate

cpf = input('Type the CPF here to consult: ')
nine_digit = cpf[:9]

# Validate the first digit of CPF
counter_1 = 10
result_1 = 0

first_digit = 0

for digit in nine_digit:
    first_digit += int(digit) * counter_1

    counter_1 -= 1

digit_1 = (first_digit * 10) % 11
digit_1 = digit_1 if digit_1 <= 9 else 0

# Validate the second digit of CPF
ten_digits = nine_digit + str(digit_1)

counter_2 = 11
second_digit = 0

result_2 = 0

for digit in ten_digits:
    result_2 += int(digit) * counter_2

    counter_2 -= 1

digit_2 = (result_2 * 10) % 11
digit_2 = digit_2 if digit_2 <= 9 else 0

valid_cpf = f'{nine_digit}{digit_1}{digit_2}'

if valid_cpf == cpf:
    print('Valid CPF!')
else:
    print('Invalid CPF!')
