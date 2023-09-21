# Password validate

is_registered = input('Are you already registered? ').strip().lower()
username = ""
registered_password = ""

if is_registered == 'no':
    username = input('Please create a username: ')
    registered_password = input('Please create a password: ')
elif is_registered == 'yes':
    user = input('Please type your username: ')
    if user == username:
        password = input('Please type your password: ')
        if password == registered_password:
            print('Logged in successfully')
        else:
            print('Wrong password')
    else:
        print('Sorry, user not found!')
else:
    print('Invalid input. Please type "yes" or "no".')
