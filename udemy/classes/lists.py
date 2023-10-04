# Like in JS the list is a array

# Allow many values of all types
list_ = [12, '2', 4.5, True, ['list inside a list']]

print(list_)

new_value = 'New value'

list_[2] = new_value
print('Type of the fist item', type(list_[0]))
print('New value of list: ', list_[2])
print('Type of the last item', type(list_[-1]))
