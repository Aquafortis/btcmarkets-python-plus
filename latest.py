import requests  # pip install requests
import json
import time
"""
# Copyright (c) 2019 Aquafortis
# https://github.com/Aquafortis/btcmarkets-python-plus
# "https://api.btcmarkets.net/market/BTC/AUD/tick"
# timeinseconds 300 = 5 minutes
# $ python3 latest.py
"""
class BTCMarkets(object):

    instrument = "BTC"
    currency = "AUD"

    def get_latest(self):
        timeinseconds = 300
        while True:
            time.sleep(timeinseconds)
            try:

                url = "https://api.btcmarkets.net/market/"+self.instrument+"/"+self.currency+"/tick"
                r = requests.get(url)
                data = r.json()
                dat = json.dumps(data, indent=4)
                a = json.loads(dat)
                #print(dat)
                if r.status_code == 200:
                    c0 = a["bestBid"]
                    c1 = a["bestAsk"]
                    c2 = a["lastPrice"]
                    c6 = a["volume24h"]
                    print("Bid:", c0)
                    print("Ask:", c1)
                    print("Last:", c2)
                    #print("Vol24h:", c6)
                    print("----------")

                else:
                    print("Response Code: " + str(r.status_code))

            except Exception as e:
                print("Error:", e)

BTCMarkets().get_latest()
# Type "control C" to exit loop in Terminal
