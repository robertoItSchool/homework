# make a voting system for a company
# there are 30 shareholders with 1%, 10 shareholders with 3%, 1 with 10% and 1 with 20%
# they vote on 3 decisions: increase investments, cut salaries & expand to Asia
# each shareholders can vote YES/NO on every decision or not vote
# a decision is taken if at least 30% shares have voted and if 51% of the votes are YES

class Shareholder:
  def __init__(self, shares):
    self.shares = shares


class OnePercentShareholder(Shareholder):
  def __init__(self):
    # call the parent __init__
    # super().__init__(1)
    # set manually the variable shares
    self.shares = 1


class Decision:
  def __init__(self, name):
    self.name = name
    self.shares_which_voted = 0
    self.shares_which_voted_yes = 0

  def vote(self, shares, option=True):
    self.shares_which_voted += shares
    if option:
      self.shares_which_voted_yes += shares



list_shareholders = []
i = 0
while i < 30:
  i += 1
  list_shareholders.append(OnePercentShareholder())

print(list_shareholders)
