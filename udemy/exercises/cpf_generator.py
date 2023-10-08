# CPF generate

cpf = '92316489001'
nine_digit_1s = cpf[:9]

# Calculate the first digit in CPF
counter_1 = 10
result_1 = 0

first_digit = 0

for digit_1 in nine_digit_1s:
    first_digit += int(digit_1) * counter_1

    counter_1 -= 1

digit_1 = (first_digit * 10) % 11
digit_1 = digit_1 if digit_1 <= 9 else 0
