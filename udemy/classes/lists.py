# Like in JS the list is a array

# Allow many values of all types
list_ = [12, '2', 4.5, True, ['list inside a list']]

print(list_)

new_value = 'New value'

list_[2] = new_value
print('Type of the fist item', type(list_[0]))
print('New value of list: ', list_[2])
print('Type of the last item', type(list_[-1]))

# Delete a item from a list
list_1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]

print('List before delete an item', list_1)
del list_1[0]
print('List after delete an item', list_1)


# Adding items to list
list_1.append(15)
print('After add an item to list', list_1)

# Delete the last item from list

list_1.pop()
print('List after POP', list_1)
