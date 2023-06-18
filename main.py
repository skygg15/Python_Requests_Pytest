import requests

token = 'b177f67d1f3265acc2dca5c94d856485'
answer = requests.post('https://pokemonbattle.me:9104//pokemons', json =
{

    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"


}, headers = {"Content-Type" : "application/json", 'trainer_token' : 'b177f67d1f3265acc2dca5c94d856485'})

print(answer.text)


answer = requests.put('https://pokemonbattle.me:9104/pokemons', json = 
{
  
    "pokemon_id": "13722",
    "name": "New Name",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"

}, headers = {"Content-Type" : "application/json", 'trainer_token' : 'b177f67d1f3265acc2dca5c94d856485'})
print(answer.text)


answer = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball', json = 
{
    
    "pokemon_id": "13722"


}, headers = {"Content-Type" : "application/json", 'trainer_token' : 'b177f67d1f3265acc2dca5c94d856485'})
print(answer.text)


