# Write 2 asserts for withdraw
# Write 2 asserts for deposit
# Add a 1ron tax for withdraw and update the test
# Return False if we try to withdraw more than what we have
# Write an assert if we try to withdraw more than what we have

class BankAccount:
  def __init__(self, balance):
    self.balance = balance

  def withdraw(self, amount):
    self.balance -= amount

  def deposit(self, amount):
    self.balance += amount

