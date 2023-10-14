# List comprehension

# Default form to add items in a list
number_list = []

for number in range(10):
    number_list.append(number)


# Using list comprehension
number_list = [number ** 2 for number in range(8)]
print(number_list)
