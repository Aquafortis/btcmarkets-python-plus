import requests  # pip install requests
import json
import time

import settings
from marketbuy import BTCMarketsBuy
"""
# Copyright (c) 2018 Aquafortis
# https://github.com/Aquafortis/btcmarkets-python-plus
"""
# Make all changes in the settings.py file
class StopLossBuy(object):

    def stop_buy(self):

        seconds = settings.buySeconds
        currency = settings.buyCurrency
        instrument = settings.buyInstrument
        stopLoss = settings.buyStopLoss
        buyPrice = settings.buyPrice

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
                        BTCMarketsBuy().buy_market()
                        runOnce = 1

                    elif lastPrice < buyPrice:
                        # Buy if market falls below buyPrice
                        BTCMarketsBuy().buy_market()
                        runOnce = 1

                    else:
                        # Do nothing if conditions are not met
                        pass
                else:
                    print("Response Code: " + str(r.status_code))

            except Exception as e:
                print("Tick Error:", e)

StopLossBuy().stop_buy()
