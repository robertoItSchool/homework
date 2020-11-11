import json
import os


class Warehouse:
  @staticmethod
  def add(product):
    # remove try/except and use os.path.exists
    # tests should still pass
    try:
      # read from the file if it exists
      f = open('warehouse', 'r')
      items = f.read()
      decoded_items = json.loads(items)
      f.close()
    except:
      # if no file, the structure is empty
      decoded_items = {}

    decoded_items[product.name] = product.__dict__

    # write the new item structure to the file
    encoded_items = json.dumps(decoded_items)

    # open the file for writing
    f = open('warehouse', 'w')
    f.write(encoded_items)
    f.close()

  @staticmethod
  def show():
    if os.path.exists('warehouse'):  # we check the file exists
      f = open('warehouse')  # open the file for read
      encoded_items = f.read()  # we read the JSON
      items = json.loads(encoded_items)  # we decode the JSON
      f.close()
      return items
    return {}

  # implement method to remove a product
  # make tests for it
  #   test nr 1, if we do not have a file
  #   test nr 2, if we have a file but no products in it
  #   test nr 3, if we have a file but not the specified product
  #   test nr 4, if we have only the specified product and it succesfully removes it
  #   test nr 5, we have 2 products and the specified one
  @staticmethod
  def remove(product):
    pass


class Product:
  def __init__(self, name, price, number):
    self.name = name
    self.price = price
    self.number = number

