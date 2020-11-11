class GameCollection:
  @staticmethod
  def get():
    return [
      {'name': 'Cyberpunk', 'price': 60, 'voucher': 'ADA'},
      {'name': 'Minecraft', 'price': 30, 'voucher': ''},
      {'name': 'Yaga', 'price': 15, 'voucher': 'Romania'},
      {'name': 'Fifa 21', 'price': 70, 'voucher': 'ADA'},
      {'name': 'Kingdom Come Deliverance', 'price': 40, 'voucher': ''},
      {'name': 'Spiderman', 'price': 70, 'voucher': ''},
      {'name': 'Fortnite', 'price': 0, 'voucher': ''},
      {'name': 'Sims', 'price': 10, 'voucher': 'DAD'},
      {'name': 'Cities Skyline', 'price': 26, 'voucher': 'DAD'},
      {'name': 'Witcher', 'price': 20, 'voucher': ''},
      {'name': 'Prince of Persia', 'price': 10, 'voucher': ''},
    ]

class Client:
  def __init__(self, username):
    self.username = username
    self.money = 0

  # make tests for it, return False if he tries to add more than 500
  def add_money(self, ammount):
    self.money += ammount

  # give a list of games, if the user has enough money buy them (substract money)
  # if the voucher code applies to a game, reduce the price by 10%
  # write at least 6 tests
  def buy_games(self, list_of_games, voucher=''):
    pass

# write a subclass of Client, PremiumClient
# every game is 20% cheaper
# vouchers do not work
# every ammount of money added is taxed with 10%
# write the same test cases as for Client


