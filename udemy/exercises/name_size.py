# Name Size

name = input('Type your name: ')

short_name = 4
medium_name = 5 or 6
long_name = 6

name_size = len(name)

if name_size <= short_name:
    print('Your name is short!')
elif name_size is medium_name:
    print('Your name is medium!')
elif name_size > long_name:
    print('Your name is long!')
