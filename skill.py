from abc import ABC, abstractmethod


class Skill(ABC):
  @abstractmethod
  def __init__(self, rating):
    if rating > 0 and rating <= 10:
      self.rating = rating
      self.type = ''
    else:
      raise Exception('value should be between 1 and 10')

  def show(self):
    print(self.type + ' skill: ' + str(self.rating))


class SalesSkill(Skill):
  def __init__(self, rating):
    super().__init__(rating)
    self.type = 'sales'


class BackendSkill(Skill):
  def __init__(self, rating):
    super().__init__(rating)
    self.type = 'backend'
