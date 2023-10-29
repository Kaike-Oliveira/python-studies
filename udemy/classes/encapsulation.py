# Encapsulation - public / private / protected

class Foo:
    def __init__(self):
        #  Public
        self.public = 'Public'

        #  Protected
        self._protected = 'Protected'

        #  Private
        self.__private = 'Private'

    def public_method(self):
        self._protected_method()
        return 'Public Method'

    def _protected_method(self):
        print('Protected Method')
        print(f'This come from private method: {self.__private}')
        return 'Protected Method'


f = Foo()
print(f.public)
print(f.public_method())
