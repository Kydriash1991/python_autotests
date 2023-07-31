import requests

token = '8aaf21304b123d11e1b674e00c1944f5' # Токен для покемонов
host = 'https://api.pokemonbattle.me:9104' # Хост для покемонов

response = requests.post(f'{host}/pokemons', json = {
    "name": "kydiroma",
    "photo": "https://dolnikov.ru/pokemons/albums/843.png"
}, headers = {'Content-Type' : 'application/json', 'trainer_token' : token} )

print(response.text) 

response_new_name = requests.put(f'{host}/pokemons', json = {
    "pokemon_id": "5749",
    "name": "bymbam",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})

print(response.text) 

response_add_pokeball = requests.post(f'{host}/trainers/add_pokeball', json = {
    "pokemon_id": "5749"
}, headers = {'Content-Type' : 'application/json', 'trainer_token' : token} )

print(response.text) 