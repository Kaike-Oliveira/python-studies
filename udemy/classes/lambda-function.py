# Labda Funtion

users = [
    {'name': 'Luiz', 'last_name': 'miranda'},
    {'name': 'Maria', 'last_name': 'Oliveira'},
    {'name': 'Daniel', 'last_name': 'Silva'},
    {'name': 'Eduardo', 'last_name': 'Moreira'},
    {'name': 'Aline', 'last_name': 'Souza'},
]


# Show the result
def show(users_list):
    for item in users_list:
        print(item)
    print()


# Do a copy of users ordering by name and last name
order_by_name = sorted(users, key=lambda item: item['name'])
order_by_last_name = sorted(users, key=lambda item: item['last_name'])

# Call the show function
show(order_by_name)
show(order_by_last_name)
