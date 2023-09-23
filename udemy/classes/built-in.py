# More python types

# Immutable types - str, int, float, bool

string = 'kaike'

# (This can't happen because this is a immutable type!)
# string[4] = 'change'
# To do this we can do this!

second_str = f'{string[:3]}change{string[4:]}'
print(second_str.capitalize())
