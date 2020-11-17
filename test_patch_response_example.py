import requests
import unittest
from unittest.mock import patch

def call_google():
  response = requests.get('https://google.com')
  return response.status_code

def make_response(status_code):
  response = requests.Response()
  response.status_code = status_code
  return response

class TestRequests(unittest.TestCase):
  @patch('requests.get', return_value=make_response(400))
  def test_400(self, mock_api_call):
    response = call_google()

    self.assertEqual(400, response)
