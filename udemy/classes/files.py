# How to create files in python

with open('file.txt', 'w+') as file:
    file.write('Line one\n')
    file.write('Line two')
    file.seek(0, 0)
    print(file.read())

print('#' * 20)

with open('file.txt', 'r') as file:
    print(file.read())
