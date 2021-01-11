# We will use Yahoo financial API to query info of companies publicly traded
# We will not call directly, we will use a library(piece of code)
# import yfinance, you will need to install it (hover with the mouse over it & click install)
# yfinance github repo: https://github.com/ranaroussi/yfinance

# create 4 stock classes, 4 different companies
# use class Ticker from yfinance and initialize it with a stock option (MSFT - Microsoft, TSLA - Tesla)
# class Ticker has a variable info, it will be a dictionary with a lot of information
# Stock class should contain the sector, website, industry, city, market

# create a class broker, it has multiple stocks
# he saves his stock info in a file, so it is faster for him to access the info
# he has a method check the price indicators and save it with the current date, previous prices remain in the file
# info about the price in Ticker.info, previousClose & regularMarketPrice are good indicators
# can return from the file the stock objects
