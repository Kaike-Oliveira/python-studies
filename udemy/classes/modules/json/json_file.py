#  Json

#  Imports
import json
from typing import TypedDict
import os

FILE_NAME = 'json_file.json'
ABSOLUTE_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        FILE_NAME
    )
)


class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None | float


movie: Movie = {
    "title": "O Senhor dos Anéis: A Sociedade do Anel",
    "original_title": "The Lord of the Rings: The Fellowship of the Ring",
    "is_movie": True,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
    "budget": None
}

with open(ABSOLUTE_PATH, 'w', encoding='utf8') as file_:
    json.dump(movie, file_, indent=2, ensure_ascii=False)

with open(ABSOLUTE_PATH, 'r', encoding='utf8') as file_:
    json_movie = json.load(file_)
    print(json_movie)
