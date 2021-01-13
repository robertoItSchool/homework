import unittest
from stocks import Stock
from yfinance_wrapper import YahooFinanceStockInfo


class MockYahooFinanceStock:
  def __init__(self, dict_info: dict):
    self.dict_info = dict_info

  def get_info(self):
    return YahooFinanceStockInfo(self.dict_info)


class MyTestCase(unittest.TestCase):
  def test_sector(self):
    # set up
    mock_yahoo_finance_stock = MockYahooFinanceStock({'sector': 'Technology'})
    stock = Stock(mock_yahoo_finance_stock)
    # execution
    sector = stock.get_sector()
    # assertion (verify the result)
    self.assertEqual('Technology', sector)

  def test_sector_not_available(self):
    # set up
    mock_yahoo_finance_stock = MockYahooFinanceStock({})
    stock = Stock(mock_yahoo_finance_stock)
    # execution
    sector = stock.get_sector()
    # assertion (verify the result)
    self.assertEqual('sector info not available', sector)


if __name__ == '__main__':
  unittest.main()
