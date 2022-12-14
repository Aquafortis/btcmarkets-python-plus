import requests  # pip install requests
import json
import time

import settings
from marketsell import BTCMarketsSell
"""
# Copyright (c) 2023 Aquafortis
# https://github.com/Aquafortis/btcmarkets-python-plus
"""
# Make all changes in the settings.py file
class StopLossSell(object):

    def stop_sell(self):

        seconds = settings.sellSeconds
        currency = settings.sellCurrency
        instrument = settings.sellInstrument
        stopLoss = settings.sellStopLoss
        sellPrice = settings.sellPrice

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
                        BTCMarketsSell().sell_market()
                        runOnce = 1

                    elif lastPrice > sellPrice:
                        # Sell if market rises above sellPrice
                        BTCMarketsSell().sell_market()
                        runOnce = 1

                    else:
                        # Do nothing if conditions are not met
                        pass
                else:
                    print("Response Code: " + str(r.status_code))

            except Exception as e:
                print("Tick Error:", e)

StopLossSell().stop_sell()
