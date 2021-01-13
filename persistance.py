import json


class StocksFile:
  def read(self):
    # open for read
    file = open('stocks.txt')
    content = file.read()
    # close the file as soon as we do not need it
    file.close()
    # decode the content of the file, from str to json
    dict = json.loads(content)
    return dict

  def write(self, dict):
    # encode the python dictionary to JSON, so we can write it to the file
    json_dict = json.dumps(dict)
    file = open('stocks.txt', 'w')
    file.write(json_dict)
    file.close()

# file = StocksFile()
# stocks = file.read()
# print(stocks)
# print(stocks['MSFT'])
