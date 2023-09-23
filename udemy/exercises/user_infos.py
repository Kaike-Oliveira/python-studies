# User Infos

# Receive the user data
name = input('Please type your name: ')
age = input('Type your age: ')

if name and age:
    print(f'Your name is: {name}')
    print(f'Your reverse name is: {name[::-1]}')

    # Check if name has space
    if ' ' in name:
        print('Your name has spaces')
    else:
        print('Your name has not spaces')

    print(f'Your name has {len(name)} characters')
    print(f'The first letter of your name is {name[0]}')
    print(f'The last letter of your name is {name[-1]}')
else:
    print('Sorry, any field is empty!')
