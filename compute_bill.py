# import the class BillRepository
from bills_repository import ConsumptionRepository
from consumption import ConsumptionBelow100, ConsumptionBelow200, ConsumptionBelow300, ConsumptionAbove300


# def compute_bill(consumption):
#   if consumption < 100:
#     return consumption * 0.06
#   price = 100 * 0.06
#   if consumption < 200:
#     return price + consumption * 0.08
#   price += 100 * 0.08
#   if consumption < 300:
#     return price + consumption * 0.09
#   price += 100 * 0.09
#   price += 0.1 * (consumption - 300)
#   return price


# create an object BillRepository
# repo = BillRepository()
# bills = repo.get()


def compute_price(consumption):
  return consumption.name + ' has to pay ' + str(consumption.get_price()) + '$'


# print(bills)
# go through all the dicts (bills) and compute the price
# for bill in bills:
  # access the value, make it int
  # print(compute_price(bill))