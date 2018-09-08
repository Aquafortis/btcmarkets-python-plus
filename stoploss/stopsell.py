import requests  # pip install requests
import json
import time

from marketsell import BTCMarketsSell
"""
# Copyright (c) 2018 Aquafortis
# https://github.com/Aquafortis/btcmarkets-python-plus
"""
class StopLossSell(object):

    def stop_sell(self):
        # Set matching instrument and currency in marketsell.py
        # Set quantity in marketsell.py
        seconds = 300
        instrument = "BTC"
        currency = "AUD"
        stopLoss = 9000
        sellPrice = 10200
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

                    if lastPrice < stopLoss:
                        # Sell if market falls below stopLoss
                        BTCMarketsSell().sell_some()
                        runOnce = 1

                    elif lastPrice > sellPrice:
                        # Sell if market rises above sellPrice
                        BTCMarketsSell().sell_some()
                        runOnce = 1

                    else:
                        # Do nothing if conditions are not met
                        pass
                else:
                    print("Response Code: " + str(r.status_code))

            except Exception as e:
                print("Tick Error:", e)

StopLossSell().stop_sell()
