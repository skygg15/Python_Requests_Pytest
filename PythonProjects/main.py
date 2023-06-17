import requests



token = '23f40f63216a35d685ea6783a86e444b'
answer = requests.post('https://pokemonbattle.me:9104/trainers/reg', json = 
{
    "trainer_token": token,
    "email": "skyll15@mail.ru",
    "password": "827696937G"

}, headers = {"Content-Type" : "application/json"})

print(answer.text)


token = '23f40f63216a35d685ea6783a86e444b'
answer = requests.put('https://pokemonbattle.me:9104/pokemons', json = 
{
    "trainer_token": token,
    "email": "skyll15@mail.ru",
    "password": "827696937G"

}, headers = {"Content-Type" : "application/json"})
print(answer.text)


token = '23f40f63216a35d685ea6783a86e444b'
answer = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball', json = 
{
    "trainer_token": token,
    "email": "skyll15@mail.ru",
    "password": "827696937G"

}, headers = {"Content-Type" : "application/json"})
print(answer.text)


