# url: https://pokeapi.co/api/v2/pokemon/<pokemon_number>
# pokemon_number=1 will show results for bulbasaur
# url: https://pokeapi.co/api/v2/pokemon/<pokemon_name>
# make a class with 2 methods for each api calls
# write 3 tests which call the real API and 3 tests which mock the API
import requests


class Pokemon:
  def get_by_number(self, number):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(number))
    content = response.json()
    return content['species']['name']


# pokemon = Pokemon()
# content = pokemon.get_by_number(25)
# print(content)
