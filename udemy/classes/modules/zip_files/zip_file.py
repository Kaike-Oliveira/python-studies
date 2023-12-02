# ZIP 

import os
import shutil
from pathlib import Path
from zipfile import ZipFile

# Paths
DEFAULT_PATH = Path(__file__).parent
ZIP_DIR = DEFAULT_PATH / 'zip_directory'
PACK_PATH = DEFAULT_PATH / 'zipped_file.zip'
UNPACK_PATH = DEFAULT_PATH / 'unzipped_file'

shutil.rmtree(ZIP_DIR, ignore_errors=True)
Path.unlink(PACK_PATH, missing_ok=True)
shutil.rmtree(str(PACK_PATH).replace('.zip', ''), ignore_errors=True)
shutil.rmtree(UNPACK_PATH, ignore_errors=True)

ZIP_DIR.mkdir(exist_ok = True)

# Create files
def create_files(quantity: int, zip_dir: Path):
    for _file in range(quantity):
        text = 'file_%s' % _file
        with open(zip_dir / f'{text}.txt', 'w') as file:
            file.write(text)
            
create_files(10, ZIP_DIR)

# Unpack file in folders
with ZipFile(PACK_PATH, 'w') as _zip:
    for root, dirs, files in os.walk(ZIP_DIR):
        for file in files:
            _zip.write(os.path.join(root, file), file)

# Reading file with python
with ZipFile(PACK_PATH, 'r') as _zip:
    for _file in _zip.namelist():
        print(_file)

# Unpacking files
with ZipFile(PACK_PATH, 'r') as _zip:
    _zip.extractall(UNPACK_PATH)
