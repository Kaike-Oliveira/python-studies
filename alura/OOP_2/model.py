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

    def __str__(self):
        return f'{show.name} | {show.year} | {show.likes}'


class Movie(Model):
    def __init__(self, name: str, year: int, time: int):
        super().__init__(name, year)
        self.time = time

    def __str__(self):
        return f'{show.name} | {show.year} | {self.time} | {show.likes}'


class Serie(Model):
    def __init__(self, name: str, year: int, seasons: int):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f'{show.name} | {show.year} | {self.seasons} | {show.likes}'


class Playlist(list):
    def __init__(self, name, shows):
        self.__name = name
        super().__init__(shows)


avengers = Movie('avengers - infinite war', 2018, 160)
see = Serie('see', 2019, 2)
the_last_of_us = Serie('The last of us', 2023, 1)
the_pope_exorcist = Movie('The pope exorcist', 2023, 103)

playlist = [avengers, see, the_last_of_us, the_pope_exorcist]

favorites = Playlist('Favorites', playlist)

for show in favorites:
    print(show)
