import unittest
from bills_repository import ConsumptionRepository
from compute_bill import compute_price


class TestBill(unittest.TestCase):
  def test_bills(self):
    repo = ConsumptionRepository()
    consumptions = repo.get()

    actual_message = compute_price(consumptions[0])
    self.assertEqual('Billy has to pay 4.8$', actual_message)

    actual_message = compute_price(consumptions[5])
    self.assertEqual('Jeff has to pay 43.0$', actual_message)


if __name__ == '__main__':
  unittest.main()
