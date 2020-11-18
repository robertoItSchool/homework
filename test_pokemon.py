import unittest
from pokemon import Pokemon
import requests
from unittest.mock import patch

# create a subclass of API Response
class OurResponse(requests.Response):
  def json(self):
    return {'species': {'name': 'pikach'}}

class TestPokemon(unittest.TestCase):
  @patch('requests.get', return_value=OurResponse())
  def test_pikachu(self, get):
    #set up
    pokemon = Pokemon()
    #execution
    value = pokemon.get_by_number(25)
    #assertion
    self.assertEqual('pikach', value)

