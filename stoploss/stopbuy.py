import requests  # pip install requests
import json
import time

from marketbuy import BTCMarketsBuy
"""
# Copyright (c) 2018 Aquafortis
# https://github.com/Aquafortis/btcmarkets-python-plus
"""
class StopLossBuy(object):

    def stop_buy(self):
        # Set matching instrument and currency in marketbuy.py
        # Set quantity in marketbuy.py
        seconds = 300
        instrument = "BTC"
        currency = "AUD"
        stopLoss = 9080
        buyPrice = 7800
        # Don't change anything below this line.
        runOnce = 0
        while runOnce < 1:
            time.sleep(seconds)
            try:

                url = "https://api.btcmarkets.net/market/"+instrument+"/"+currency+"/tick"
                r = requests.get(url)
                data = r.json()
                dat = json.dumps(data, indent=4)
                #print(dat)
                a = json.loads(dat)
                lastPrice = a["lastPrice"]
                #print("Last price:", lastPrice)

                if r.status_code == 200:

                    if lastPrice > stopLoss:
                        # Buy if market rises above stopLoss
                        BTCMarketsBuy().buy_some()
                        runOnce = 1

                    elif lastPrice < buyPrice:
                        # Buy if market falls below buyPrice
                        BTCMarketsBuy().buy_some()
                        runOnce = 1

                    else:
                        # Do nothing if conditions are not met
                        pass
                else:
                    print("Response Code: " + str(r.status_code))

            except Exception as e:
                print("Tick Error:", e)

StopLossBuy().stop_buy()
