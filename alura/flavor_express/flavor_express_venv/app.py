import json
import requests

source = 'https://guilhermeonrails.github.io/api-restaurants/restaurants.json'
response = requests.get(source)
print(response)

if response.status_code == 200:
    json_data = response.json()
    restaurant_data = {}
    for item in json_data:
        restaurant_name = item['Company']
        if restaurant_name not in restaurant_data:
            restaurant_data[restaurant_name] = []

        restaurant_data[restaurant_name].append({
            "item": item['Item'],
            "price": item["price"],
            "description": item['description'],
        })

else:
    print(f'Sorry, there was an error {response.status_code}')


for restaurant_name, datas in restaurant_data.items():
    file_name = f'{restaurant_name}.json'
    with open(file_name, 'w') as restaurant_menu:
        json.dump(datas, restaurant_menu, indent=2)