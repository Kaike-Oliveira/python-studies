from models.restaurant import Restaurant
from models.menu.plate import Plate
from models.menu.drink import Drink

restaurant_praca = Restaurant('Praca', 'Gourmet')
orange_juice = Drink('Orange', 6.50, 750)
pizza = Plate('Pizza', 27.90, 'Cheese pizza')


def main():
    print(pizza)


if __name__ == '__main__':
    main()
