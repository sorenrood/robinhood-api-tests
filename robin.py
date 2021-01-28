import robin_stocks as r
import os

r.login(os.getenv('SOREN_EMAIL'), os.getenv('SOREN_ROBINHOOD_PASSWORD'))
x = r.order_buy_limit("AAPL", 1, 300)
print(x)