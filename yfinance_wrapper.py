import yfinance


class YahooFinanceStock:
  # the constructor
  def __init__(self, name):
    # create an object to communicate with the Yahoo API
    self.ticker = yfinance.Ticker(name)
    # we only initialize the variable info, but without a value (or value None)
    self.info = None

  def get_info(self):
    if not self.info:
      # if we do not have the variable, we initialize it
      self.info = YahooFinanceStockInfo(self.ticker.info)
    return self.info


class YahooFinanceStockInfo:
  def __init__(self, dict_info):
    self.dict_info = dict_info

  def get_sector(self):
    return self.__get_value('sector')

  def get_website(self):
    return self.__get_value('website')

  def get_price(self):
    return self.__get_value('regularMarketPrice')

  def __get_value(self, key):
    try:
      # try to access the key
      return self.dict_info[key]
    except KeyError:
      # we get here if the key does not exist
      return key + ' info not available'
