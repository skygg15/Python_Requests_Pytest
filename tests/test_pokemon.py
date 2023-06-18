import requests
import pytest

host = 'https://pokemonbattle.me:9104'
token = 'b177f67d1f3265acc2dca5c94d856485'

def test_status_code():
    answer = requests.get(f'{host}/trainers', json =
    {
        "name": "Бульбазавр",
         "photo": "https://dolnikov.ru/pokemons/albums/001.png"
          }, headers = {"Content-Type" : "application/json", 'trainer_token' : 'token'})
    assert answer.status_code == 200


    def test_status_code():
      answer_body = requests.get(f'{host}/trainers', params = {'trainer_id' : 4807})
      assert answer_body.json()['trainer_name'] == Assna