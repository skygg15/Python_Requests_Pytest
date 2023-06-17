import requests
import pytest

host = 'https://pokemonbattle.me:9104'
token = '23f40f63216a35d685ea6783a86e444b'
def test_status_code():
    answer = requests.post(f'{host}/pokemons', json = 
    
            {
        "name": "ass1",
        "photo": "https://dolnikov.ru/pokemons/albums/001.png"
    }, headers= {'Content-Type' : 'application/json', 'trainer_token' : token})
    assert answer.status_code == 201


def test_status1code():
    answer = requests.put(f'{host}/pokemons', json = 
        
            {
            "name": "ass1",
            "photo": "https://dolnikov.ru/pokemons/albums/001.png"
    }, headers= {'Content-Type' : 'application/json', 'trainer_token' : token})
    assert answer.status_code == 201