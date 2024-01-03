from gettext import find
from typing import List, Dict
import os
from uuid import uuid4

def show_name():
    print('Flavor Express')

restaurants: List[Dict] = [
    {'id': '1234', 'name': 'La Bella Trattoria', 'category': 'Italiano', 'is_active': False},
    {'id': uuid4(), 'name': 'Churrascaria do Sul', 'category': 'Churrascaria', 'is_active': False},
    {'id': uuid4(), 'name': 'Sushi Palace', 'category': 'Sushi', 'is_active': False},
    {'id': uuid4(), 'name': 'MexiCuisine', 'category': 'Mexicano', 'is_active': False},
    {'id': uuid4(), 'name': 'Verde Vida', 'category': 'Vegetariano', 'is_active': False}
]

# Options
register = '1. Register restaurant'
show = '2. Show restaurants'
activate = '3. Activate restaurant'
logout = '4. Logout'

def show_options():
    print(register, show, activate, logout, sep='\n')

def back_to_menu():
    input('Press [Enter] to back to menu ')
    main()

def selected_action(title: str) -> None:
    os.system('cls')
    print(20 * '-', title, 20 * '-')

def register_restaurant() -> None:
    selected_action('Register a new restaurant')
    id = uuid4()
    name = input('Type the restaurant name: ').title()
    category = input('What is the restaurant category? ')
    is_active = False
    restaurant = {
        'id': id,
        'name': name,
        'category': category,
        'is_active': is_active
    }
    restaurants.append(restaurant)
    print(f'The restaurant {name} registered successfully\n')
    back_to_menu()

def show_restaurants() -> None:
    selected_action('Restaurant List')
    for index, restaurant in enumerate(restaurants):
        print(f'{index}. ', end='')
        for key, value in restaurant.items():
            print(f'{key}: {value}', end=' ')
        print()
    back_to_menu()

def activate_restaurant() -> None:
    selected_action('Activate a restaurant')
    id = input('Type the restaurant id: ')
    selected_restaurant = False
    for restaurant in restaurants:
        if id == restaurant['id']:
            selected_restaurant = True
            restaurant['is_active'] = True
            print(f'The restaurant {restaurant["name"]} was activated successfully')
    
    if not selected_restaurant:
        print('The restaurant was not found')

    back_to_menu()

def end_app() -> None:
    os.system('cls')
    print('Ending app...')

def invalid_option() -> None:
    print('Invalid option\n')
    back_to_menu()

def choose_option() -> None:
    try:
        selected_option = int(input('Select an option: '))
        if selected_option == 1:
            register_restaurant()
        elif selected_option == 2:
            show_restaurants()
        elif selected_option == 3:
            activate_restaurant()
        elif selected_option == 4:
            end_app()
        else:
            invalid_option()
    except:
        invalid_option()


def main() -> None:
    os.system('cls')
    show_name()
    show_options()
    choose_option()

if __name__ == '__main__':
    main()