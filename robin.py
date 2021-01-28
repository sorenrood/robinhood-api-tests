import robin_stocks as r
import os
login = r.login(os.getenv('SOREN_EMAIL'), os.getenv('SOREN_ROBINHOOD_PASSWORD'))
pos = r.get_all_watchlists()
print(pos)
