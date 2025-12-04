# how to connect to api using python : https://youtu.be/JVQNywo4AbU

# Step-1: to import requests library to request to the api
import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)     # .get() will give us a response object
    
    if response.status_code == 200:
        pokemon_data = response.json()  # this will convert our response object into python dictionary --> key : value pair
        return pokemon_data
    else:
        print(f"Failed to retrived data {response.status_code}")
 
pokemon_name = "pikachu"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info["name"].capitalize()}")
    print(f"Id: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")
