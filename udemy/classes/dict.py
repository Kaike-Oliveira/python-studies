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
