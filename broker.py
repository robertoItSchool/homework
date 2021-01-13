from datetime import date
from typing import List

from stocks import Stock
from persistance import StocksFile


class Broker:
  def __init__(self, stocks: List[Stock]):
    self.stocks = stocks

  def save(self):
    stocks_file = StocksFile()
    dict = stocks_file.read()
    for one_stock in self.stocks:
      string_today = date.today().strftime("%m/%d/%y")
      dict[one_stock.name][string_today] = one_stock.get_price()
    stocks_file.write(dict)

