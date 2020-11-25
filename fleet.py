# import the classes we need
from transportation import Minivan, Car, Morgan, Bus, Motorcycle, Bicycle
import math


class Fleet:
  def __init__(self):
    self.list = [
      Bus(), Bus(),
      Car(), Car(), Car(), Car(),
      Minivan(),
      Motorcycle(), Motorcycle(), Motorcycle()
    ]
    i = 0
    # add 6 bicycles
    while i < 6:
      self.list.append(Bicycle())
      i += 1

  def get_capacity(self):
    capacity = 0
    # go through all the transport objects
    for transport in self.list:
      # add the capacity of the transport object
      capacity += transport.capacity
    return capacity

  def get_electronics_capacity(self):
    capacity = 0
    for transport in self.list:
      if transport.type == 'electronics':
        capacity += transport.capacity
    return capacity

  #    - a function to compute how many food orders it can deliver from 9am to 6pm
  #        - bicycle takes 20min for an order, motorcycle takes 10min
  #        - drivers need to take 10min break after 1h and have 1h lunch break
  def get_number_of_orders(self):
    actual_time = 400  # in minutes
    number_of_orders = 0
    # go through all the transport objects
    for transport in self.list:
      # check it transports food
      if transport.type == 'food':
        number_of_orders += actual_time / transport.delivery_time
    return number_of_orders


fleet = Fleet()
cap = fleet.get_capacity()
print(cap)
cap_el = fleet.get_electronics_capacity()
print(cap_el)
orders = fleet.get_number_of_orders()
print(orders)
