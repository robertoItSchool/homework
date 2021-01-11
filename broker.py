from datetime import date
import json
from typing import List

from stocks import Stock


class Broker:
  def __init__(self, stocks: List[Stock]):
    self.stocks = stocks

  def save(self):
    file = open('stocks.txt', 'w')
    dict = {}
    for one_stock in self.stocks:
      print(date.today())
      string_today = date.today().strftime("%m/%d/%y")
      dict[one_stock.name] = {
        string_today: one_stock.get_price()
      }
    encoded_dict = json.dumps(dict)
    file.write(encoded_dict)
    file.close()
