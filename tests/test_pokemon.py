import requests
import pytest

host = 'https://pokemonbattle.me:9104'
token = '23f40f63216a35d685ea6783a86e444b'

def test_part_of_answer():
    answer = requests.get(f'{host}/trainers'),


def test_part_of_answer():
  answer = requests.get(f'{host}/trainers', params = {'trainer_id' : 4710})