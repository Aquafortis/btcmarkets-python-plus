import requests  # pip install requests
import json
import base64
import hashlib
import hmac
import time
from collections import OrderedDict

import config
"""
# Copyright (c) 2018 Aquafortis
# https://github.com/Aquafortis/btcmarkets-python-plus
# {"ordertype": "Limit"}
# {"ordertype": "Market"}
"""
class BTCMarketsBuy(object):
    apiKey = config.apiKey
    apiSecret = config.apiSecret
    nonce = str(int(round(time.time() * 1000)))
    baseUrl = "https://api.btcmarkets.net"
    url = "/order/create"

    # Add your order details here:
    currency = "AUD"
    instrument = "BTC"
    ordertype = "Limit"
    # Price of bid
    rate = 2000
    # Quantity to buy
    quantity = 0.01
    # Retry if order fails
    retries = 3  # 3 = 2 retries
    seconds = 60  # Seconds between retries
    # Don't change anything below this line.

    price = int(rate*1E8)
    volume = int(quantity*1E8)
    trade = rate * quantity
    print("Trade amount:", trade)

    data = OrderedDict([
        ("currency", currency),
        ("instrument", instrument),
        ("price", price),
        ("volume", volume),
        ("orderSide", "Bid"),
        ("ordertype", ordertype),
        ("clientRequestId", nonce)
    ])
    postData = json.dumps(data, separators=(",", ":"))

    def buy_some(self):

        for i in range(0,self.retries):

            try:

                nonce = str(int(round(time.time() * 1000)))
                secret = base64.b64decode(self.apiSecret)
                payload = self.url + "\n" + nonce + "\n" + self.postData

                signature = base64.b64encode(hmac.new(secret, payload.encode(), hashlib.sha512).digest())

                headers = {
                    "accept": "application/json",
                    "Content-Type": "application/json",
                    "User-Agent": "btc markets python client",
                    "accept-charset": "utf-8",
                    "apikey": self.apiKey,
                    "signature": signature,
                    "timestamp": nonce
                }

                #r = requests.post(self.baseUrl + self.url, data=self.postData, headers=headers)
                print("Response Code: " + str(r.status_code))
                data = r.json()
                dat = json.dumps(data, indent=4)
                print(dat)
                # Write to file
                content = open("responses.txt", "a")
                content.write(dat + "\n")
                content.close()

                if r.status_code == 200:
                    break
                else:
                    print("Response Code: " + str(r.status_code))

            except Exception as e:
                print("Error:", e)

            time.sleep(self.seconds)
            continue

BTCMarketsBuy().buy_some()
