#  CSV (Comma Separator Values)

#  Imports
from pathlib import Path
import csv


CSV_PATH = Path(__file__).parent / 'csv_file.csv'


with open(CSV_PATH, 'r', encoding='utf8') as file_:
    file_reader = csv.reader(file_)

    for line in file_reader:
        print(line)
