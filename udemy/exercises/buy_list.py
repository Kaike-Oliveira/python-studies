# Buy list

# Imports
import os

buy_list = []

while True:
    print('Select an option')
    option = input('add[A] delete[D] show[S]: ').lower()

    if option == 'a':
        os.system('cls')
        item = input('Item: ')
        buy_list.append(item)

    elif option == 'd':
        os.system('cls')
        index = input('Select an index to delete: ')

        try:
            int_index = int(index)
            del buy_list[int_index]

        except ValueError and IndexError:
            print('Was not possible delete the index')

    elif option == 's':
        os.system('cls')
        if len(buy_list) == 0:
            print('Empty list')

        for i, value in enumerate(buy_list):
            print(i, value)

    else:
        print('This option do not exist')
