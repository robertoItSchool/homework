import unittest
import requests
from bitcoin import get_value_in_euro
from unittest.mock import patch
import json

# create a requests.Response object with our data
class OurResponse(requests.Response):
  def json(self):
    return {'rates': {'eur': {'value': 100}}}

def get_response():
  return OurResponse()

class TestBitcoin(unittest.TestCase):
  @patch('requests.get', return_value=get_response())
  def test_eur(self, get):
    actual_value = get_value_in_euro()
    # compare the value from the API with what we expect
    self.assertEqual(100, actual_value)