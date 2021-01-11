from stocks import TeslaStock, MicrosoftStock
from broker import Broker

tsla = TeslaStock()
sector = tsla.get_sector()
print(sector)
website = tsla.get_website()
print(website)
price = tsla.get_price()
print(price)

bill = MicrosoftStock()
sector = bill.get_sector()
print(sector)
website = bill.get_website()
print(website)
price = bill.get_price()
print(price)

broker = Broker([tsla, bill])
broker.save()
