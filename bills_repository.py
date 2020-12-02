import json

from consumption import ConsumptionBelow100, ConsumptionBelow200, ConsumptionBelow300, ConsumptionAbove300


class Bill:
  # define the constructor
  def __init__(self, name, consumption):
    self.name = name
    self.consumption = int(consumption)


class ConsumptionRepository:
  def get(self):
    bills = self.read_from_file()
    # make an empty list
    consumption_objects = []
    for bill_dict in bills:
      # create an object Consumption
      new_consumption = self.make_consumption(bill_dict['consumption'], bill_dict['name'])
      # add a Consumption object to the list
      consumption_objects.append(new_consumption)
    return consumption_objects

  def make_consumption(self, units, name):
    units = int(units)
    if units < 100:
      return ConsumptionBelow100(units, name)
    if units < 200:
      return ConsumptionBelow200(units, name)
    if units < 300:
      return ConsumptionBelow300(units, name)
    return ConsumptionAbove300(units, name)

  def read_from_file(self):
    # create a File object (handler)
    file = open('electricity_bills.json')
    # read the content of the file, we get a string
    encoded_json = file.read()
    # close the reading channel
    file.close()
    # decode the json
    bills = json.loads(encoded_json)
    return bills
