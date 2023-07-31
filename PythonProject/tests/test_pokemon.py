import requests
import pytest

token = '8aaf21304b123d11e1b674e00c1944f5' 
host = 'https://api.pokemonbattle.me:9104'

def test_status_code():
    response = requests.get(f'{host}/trainers', params = {'trainer_id' : 1895})
    assert response.status_code == 200

def test_part_of_answer():
    response = requests.get(f'{host}/trainers', params = {'trainer_id' : 1895})
    assert response.json()['trainer_name'] == 'Очко' 