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

#print(client.order_detail([2210550224, 2210550235, 2210552825]))

#print(client.order_cancel([2210550235]))

#print(client.account_balance())

print(client.get_market_tick("BTC", "AUD"))

#print(client.get_market_trades_since("BTC", "AUD", 2210550224))

# Using time.sleep between multiple api calls (seconds)
time.sleep(3)

# Price amount of bid or ask
amount = 2650.50
# Quantity to buy or sell
quantity = 0.01
# Calculations
price = int(amount*1E8)
print("Price:", price)
volume = int(quantity*1E8)
print("Volume:", volume)
# Using timestamp for clientRequestId
cid = str(int(time.time() * 1000))
print("CID:", cid)
trade = amount * quantity
print("Trade:", trade)

# Note: price, volume, and cid are generated above
#print(client.order_create("AUD", "BTC", price, volume, "Bid", "Limit", cid))

# Convert datetime to millisecond timestamp (GMT only)
# year, month, day, hour, minutes, seconds, multiplier
print(convert.get_timestamp(2018, 9, 3, 0, 0, 0, 1000))
# Convert timestamp to local time string
# timestamp, multiplier (1000 for 13 digits (milliseconds), 1 for 10 digits)
print(convert.get_localtime(1535945835, 1))
# Local time now as string
print(convert.get_localtime_now())
# Add or remove requests as needed or just comment them out.
