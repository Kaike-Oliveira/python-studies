# Meta class

class Meta(type):
    def __new__(mcs, name, bases, dct):
        print('--New MetaClass--')
        cls = super().__new__(mcs, name, bases, dct)
        return cls


class Person(metaclass=Meta):  # Parent class (object)
    def __new__(cls, *args, **kwargs):
        print('--New--')
        instance = super().__new__(cls)
        return instance

    def __init__(self, name):
        print('--Init--')
        self.name = name


p1 = Person('Kaike Cesar')
