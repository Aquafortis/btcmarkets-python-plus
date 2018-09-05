from btcmarkets import BTCMarkets
from converter import Converter
import time

import config
"""
# https://github.com/BTCMarkets/API/wiki/Introduction
# https://github.com/Aquafortis/btcmarkets-python-plus
"""
apiKey = config.apiKey
apiSecret = config.apiSecret

client = BTCMarkets(apiKey, apiSecret)
convert = Converter()

#print(client.trade_history("AUD", "BTC", 10, 2210550224))
#print(client.order_history("AUD", "BTC", 10, 2210550224))
#print(client.order_open("AUD", "BTC", 10, 2210550224))
#print(client.order_detail([2210550224, 2210550235, 2210552825]))
#print(client.order_cancel([2210552825]))
#print(client.account_balance())

print(client.get_market_tick("BTC", "AUD"))
#print(client.get_market_orderbook("BTC", "AUD"))
#print(client.get_market_trades("BTC", "AUD"))
#print(client.get_market_trades_since("BTC", "AUD", 2210550224))

# Using time.sleep between multiple api calls (seconds)
time.sleep(3)

# Price of bid or ask
rate = 2650.50
# Quantity to buy or sell
quantity = 0.01
# Calculations
price = int(rate*1E8)
volume = int(quantity*1E8)
trade = rate * quantity
print("Trade amount:", trade)
# Using timestamp for clientRequestId
cid = str(int(time.time() * 1000))

# Note: price, volume, and cid are generated above
#print(client.order_create("AUD", "BTC", price, volume, "Bid", "Limit", cid))

# Convert timestamp to local time string
# timestamp, multiplier (1000 for 13 digits (milliseconds), 1 for 10 digits)
#print(convert.get_localtime(1535945835, 1))
# Local time now as string
print(convert.get_localtime_now())
# Add or remove requests as needed or just comment out or uncomment.
