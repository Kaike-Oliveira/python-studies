# BMI Calculator

print(20 * '#', 'BMI', 20 * '#')

name = input(str('Type your name: '))
height = input('Type your height: ')
weight = input('Type your weight: ')

bmi = float(weight) / float(height) ** 2

print(f'Based on your height and weight {name}, your BMI is: {bmi}')

if 18.5 > bmi:
    print('You are underweight')
elif 18.5 < bmi < 24.9:
    print('You are normal')
elif 24.9 < bmi < 29.9:
    print('You are overweight')
elif 29.9 < bmi < 34.9:
    print('You are obese')
elif bmi > 35:
    print('You are extremely obese')
