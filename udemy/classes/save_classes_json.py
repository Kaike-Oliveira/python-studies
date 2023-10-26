# JSON

# Imports
import json

PATH = 'save-classes-a.json'


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


customer = Person('Clara Trindade', 23)
developer = Person('Kaike Cesar', 18)
user = Person('Sam Smith', 32)

body = [vars(customer), vars(developer), vars(user)]


def generate_json_person():
    with open(PATH, 'w', encoding='utf8') as people:
        json.dump(body, people, indent=2)
