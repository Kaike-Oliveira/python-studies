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

    def show_details(self):
        print(f'{show.name} | {show.year} | {show.likes}')


class Movie(Model):
    def __init__(self, name: str, year: int, time: int):
        super().__init__(name, year)
        self.time = time

    def show_details(self):
        print(f'{show.name} | {show.year} | {self.time} | {show.likes}')


class Serie(Model):
    def __init__(self, name: str, year: int, seasons: int):
        super().__init__(name, year)
        self.seasons = seasons

    def show_details(self):
        print(f'{show.name} | {show.year} | {self.seasons} | {show.likes}')


avengers = Movie('avengers - infinite war', 2018, 160)
see = Serie('see', 2019, 2)

favorites = [avengers, see]

for show in favorites:
    show.show_details()
