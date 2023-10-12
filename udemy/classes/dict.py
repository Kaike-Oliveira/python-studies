# Dict

person = {
    'name': 'Kaike',
    'last_name': 'Oliveira',
    'age': 18,
    'height': 1.81,
    'skills': [
        {'font_end': ['HTML', 'CSS', 'Javascript', 'React', 'Typescript']},
        {'back_end': ['Python', 'MongoDB', 'Postgres']},
    ],
}

for keys in person:
    print(person[keys])

# LEN
print('Show the keys quantity in a dict:', len(person))

# KEYS
print('Show the keys in a dict:', person.keys())

# VALUES
print('Show the value keys in a dict:', person.values())

# ITEMS
print('Show the items and keys in a dict:', person.items())

# GET
print('Get a dict key, if not provided, return None:', person.get('name'))

# POP
print('Remove a specify dict key:', person.pop('name'), person)

# POPITEM
print('Remove the last item in a dict', person.popitem())

# UPDATE
update = person.update({
    'name': 'Cesar',
})
print('Update the dict', person)
