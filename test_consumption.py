import unittest
from consumption import ConsumptionBelow100, ConsumptionBelow300

class TestConsumption(unittest.TestCase):
  def test_below_100(self):
    # set up
    consumption = ConsumptionBelow100(50, 'name')
    # execution
    actual_price = consumption.get_price()
    # assertion
    self.assertEqual(3, actual_price)

  def test_below_300(self):
    # set up
    consumption = ConsumptionBelow300(290, 'name')
    # execution
    actual_price = consumption.get_price()
    # assertion
    self.assertEqual(22.1, actual_price)