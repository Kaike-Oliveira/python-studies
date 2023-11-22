#  Check the file size

#  Imports
import math


def format_size(size_in_bytes: int, base: int = 1024) -> str:
    if size_in_bytes <= 0:
        return '0B'

    sizes_abreviation = 'B', 'KB', 'MB', 'GB', 'TB', 'PB'

    sizes_index = int(math.log(size_in_bytes, base))
    print(sizes_index)

    pow_ = base ** sizes_index

    final_size = size_in_bytes / pow_

    abb_size = sizes_abreviation[sizes_index]
    return f'{final_size} {abb_size}'


print(format_size(10000000))
