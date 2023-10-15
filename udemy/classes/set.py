# Set

# Empty set
set_1 = set()

# Set with value
set_2 = {1, 2, 3, 'Name', 3}

# Can remove duplicate values, but the order is lost and don't allow index
print(set_2)

# ****** Methods ****** #
print('# ****** Methods ****** #')

# add
set_2.add(6)
print('add:', set_2)

# update
set_2.update(('Hello World', 1, 7, 4))
print('update: ', set_2)

# discard
set_2.discard('Hello World')
print('discard:', set_2)

# clear
set_2.clear()
print('clear:', set_2)

# ****** Operators ****** #
print('# ****** Operators ****** #')
set_3 = {1, 2, 3}
set_4 = {2, 3, 4}

# union
union = set_3 | set_4
print('union: ', union)

# intersections
intersections = set_3 & set_4
print('intersections:', intersections)

# difference
difference = set_3 - set_4
print('difference:', difference)

# symmetric difference
symmetric_difference = set_3 ^ set_4
print('symmetric difference:', symmetric_difference)