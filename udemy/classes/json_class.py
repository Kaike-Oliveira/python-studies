# json
import json

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

with open('jsonfile.json', 'w', encoding='utf8') as file:
    json.dump(person, file, ensure_ascii=False, indent=2)


with open('jsonfile.json', 'r', encoding='utf8') as file:
    person_returned = json.load(file)
    print(person_returned)
    