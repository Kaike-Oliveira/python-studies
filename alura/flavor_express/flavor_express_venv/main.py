from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    return {'Hello':'World'}

@app.get('/api/restaurants/')
def get_restaurants(restaurant: str = Query(None)):
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        json_datas = response.json()
        if restaurant is None:
            return {'Dados':json_datas}

        restaurant_datas = []
        for item in json_datas:
            if item['Company'] == restaurant:
                restaurant_datas.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
                })
        return {'Restaurant': restaurant, 'Cardapio': restaurant_datas}
    else: 
        return {'Error':f'{response.status_code} - {response.text}'}
    