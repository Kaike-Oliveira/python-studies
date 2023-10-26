# class

# Generate new objects
# Use PascalCase to define the class name

class Person:
    # When we call this inside a class this is a method and not a function
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name


developer = Person('Kaike', 'Oliveira')
user = Person('Luana', 'Alves')

print(developer.name)
print(user.name)
