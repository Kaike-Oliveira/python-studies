# Pack and unpack of dicts

# Pack
user = {
    'name': 'Kaike',
    'last_name': 'Oliveira',
}

user_datas = {
    'height': 1.8,
    'age': 18,
}

full_user_datas = {**user, **user_datas}

print(full_user_datas)

# Unpack
for key, value in user.items():
    print(key, value)


# In functions
def show_k_args(*args, **kwargs):
    print('In a function: ')
    print('Args:', args)
    for keys, values in kwargs.items():
        print(keys, values)


show_k_args(1, 2, **user)
