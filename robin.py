import robin_stocks as r
import os

r.login(os.getenv('SOREN_EMAIL'), os.getenv('SOREN_ROBINHOOD_PASSWORD'))
price = r.stocks.get_latest_price('AAPL', includeExtendedHours=True)
price = float(price[0])
print(f"The current price of AAPL is {price}")