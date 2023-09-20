# BMI Calculator

print(20 * '#', 'BMI', 20 * '#')

name = input(str('Type your name: '))
height = input('Type your height: ')
weight = input('Type your weight: ')

bmi = float(weight) / float(height) ** 2

print(f'Based on your height and weight {name}, your BMI is: {bmi}')
