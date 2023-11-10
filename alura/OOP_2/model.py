# Model

class Model:
    def __init__(self, name: str, year: int):
        self._name = name.title()
        self.year = year
        self._likes = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        self._name = new_name.title()

    @property
    def likes(self):
        return self._likes

    def add_like(self):
        self._likes += 1


class Movie(Model):
    def __init__(self, name: str, year: int, time: int):
        super().__init__(name, year)
        self.time = time


class Serie(Model):
    def __init__(self, name: str, year: int, seasons: int):
        super().__init__(name, year)
        self.seasons = seasons


avengers = Movie('avengers - infinite war', 2018, 160)
print(f'{avengers.name} | {avengers.year} | {avengers.time} | {avengers.likes}')

see = Serie('see', 2019, 2)
print(f'{see.name} | {see.year} | {see.seasons} | {see.likes}')
