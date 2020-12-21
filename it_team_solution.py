from skill import SalesSkill


class Name:
  # constructor
  def __init__(self, first, last):
    # save values to object
    self.first = first
    self.last = last

  def show(self):
    print('First name: ' + self.first)
    print('Last name: ' + self.last)


class SalesPerson:
  def __init__(self, name, number_of_sales, skill):
    self.name = name
    self.number_of_sales = number_of_sales
    self.skill = skill

  def show(self):
    self.name.show()
    print('Number of sales: ' + str(self.number_of_sales))
    self.skill.show()


class ProductOwner:
  def __init__(self, name, managed_teams):
    self.name = name
    self.managed_teams = managed_teams

  def show(self):
    self.name.show()
    print(self.managed_teams)


# davide = SalesPerson(Name('Davide', 'Ravasi'), 100, SalesSkill(9))
# mircea = ProductOwner(Name('Mircea', 'Pop'), ['syneto-os-backend', 'syneto-os-frontend'])
#
# davide.show()
# mircea.show()
