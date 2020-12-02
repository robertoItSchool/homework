class Consumption:
  def __init__(self, units, name):
    # save the value to the object
    self.units = units
    self.name = name


class ConsumptionBelow100(Consumption):
  def get_price(self):
    return self.units * 0.06


class ConsumptionBelow200(Consumption):
  def get_price(self):
    return 6 + 0.08 * (self.units - 100)


class ConsumptionBelow300(Consumption):
  def get_price(self):
    return 6 + 8 + 0.09 * (self.units - 200)


class ConsumptionAbove300(Consumption):
  def get_price(self):
    return 6 + 8 + 9 + 0.1 * (self.units - 300)
