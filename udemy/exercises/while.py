# While

name = input('Type your name: ')

name_size = len(name)

index = 0

while index < name_size:
    print(f'*{name[index]}*')
    index += 1
