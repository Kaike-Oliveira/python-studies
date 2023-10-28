# Class Method

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod  # Factory method - create a new object
    def fix_age(cls, name):
        return cls(name, 24)

    @classmethod  # Factory method - create a new object
    def unknown(cls, age):
        return cls('unknown', age)


person1 = Person.fix_age('Kaike')
person2 = Person.fix_age('Julia')
unknown = Person.unknown(23)
person3 = Person.fix_age('Paulo')

print(vars(person1), vars(person2), vars(person3), vars(unknown))
