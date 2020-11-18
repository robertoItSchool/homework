# https://api.coingecko.com/api/v3/exchange_rates
# compute the exchange rate of bitcoin in eur and usd
# write tests for the compute function mocking the API

import requests

def main():
  # call coingecko for exchange rates
  response = requests.get('https://api.coingecko.com/api/v3/exchange_rates')

  # print the object, see the response code
  print(response)
  # print the content of the object
  values = response.json()

  # print the BTC info
  btc = values['rates']['btc']
  # print the EUR info
  eur = values['rates']['eur']
  # print the USD info
  usd = values['rates']['usd']

  # compute EUR in BTC and USD in BTC
  print('1BTC is ' + str(eur['value']) + eur['unit'])
  print('1BTC is ' + str(usd['value']) + usd['unit'])

def get_value_in_euro():
  response = requests.get('https://api.coingecko.com/api/v3/exchange_rates')
  values = response.json()
  eur = values['rates']['eur']
  return eur['value']
