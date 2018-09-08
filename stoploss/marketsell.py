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
"""
# Important: rate and quantity are automatically multiplied by 100000000
class BTCMarketsSell(object):
    apiKey = config.apiKey
    apiSecret = config.apiSecret
    nonce = str(int(round(time.time() * 1000)))
    baseUrl = "https://api.btcmarkets.net"
    url = "/order/create"

    # Add your order details here:
    currency = "AUD"
    instrument = "BTC"
    # Actual price much higher than sellPrice
    rate = 40000
    # Actual quantity to sell
    quantity = 0.01
    # Don't change anything below this line.

    # Converts values above into 1E8 integer (x 100000000)
    price = int(rate*1E8)
    volume = int(quantity*1E8)

    data = OrderedDict([
        ("currency", currency),
        ("instrument", instrument),
        ("price", price),
        ("volume", volume),
        ("orderSide", "Ask"),
        ("ordertype", "Market"),
        ("clientRequestId", nonce)
    ])
    postData = json.dumps(data, separators=(",", ":"))

    def sell_some(self):

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

            # Uncomment the line below to go live!
            #r = requests.post(self.baseUrl + self.url, data=self.postData, headers=headers)
            print("Response Code: " + str(r.status_code))
            data = r.json()
            dat = json.dumps(data, indent=4)
            print(dat)
            # Write to file
            content = open("responses.txt", "a")
            content.write("Sell Order\n")
            content.write(dat + "\n")
            content.close()

            if r.status_code == 200:
                print("Sell Order")
            else:
                print("Response Code: " + str(r.status_code))

        except Exception as e:
            print("Error:", e)
