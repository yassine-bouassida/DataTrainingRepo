# In order to send HTTP requests and receive responses we need the requests module
# We gotta pip install it first (MAKE SURE YOU ARE IN A VIRTUAL ENVIRONMENT)
import requests

# Unlike other languages (i.e. Java or C#, we don't have to do things like... set up 
# some sort of HTTP client object, we don't need a model for the return, etc)
# We can just send the request and work with the response (assuming its a JSON)

print("Enter a pokemon to find (either name or dex number): ")
query = input()

found_pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/645")

print(found_pokemon.json())