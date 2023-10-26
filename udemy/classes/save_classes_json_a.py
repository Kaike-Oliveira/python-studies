# JSON

# Imports
import json
from save_classes_json import PATH, generate_json_person

generate_json_person()

with open(PATH, 'r') as file:
    people = json.load(file)

    for person in people:
        print(person['name'])
