from models.restaurant import Restaurant

restaurant_praca = Restaurant('Praca', 'Gourmet')
mexican_restaurant = Restaurant('Los Salitos', 'Mexican')
japonese_restaurant = Restaurant('Sakura', 'Japanese')

mexican_restaurant.active_restaurant()

def main():
    Restaurant.show_restaurants()


if __name__ == '__main__':
    main()
