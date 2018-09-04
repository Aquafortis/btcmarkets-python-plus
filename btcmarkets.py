import requests  # pip install requests
import json
import base64
import hashlib
import hmac
import time
from collections import OrderedDict

baseUrl = "https://api.btcmarkets.net"

def request(action, key, signature, timestamp, path, postData):

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": "btc markets python client",
        "accept-charset": "utf-8",
        "apikey": key,
        "signature": signature,
        "timestamp": timestamp
    }

    if action == "post":
        r = requests.post(baseUrl + path, data=postData, headers=headers)
        responce = r.json()
        resp = json.dumps(responce, indent=4)
        # Write to file
        content = open("responces.txt", "a")
        content.write(resp + "\n")
        content.close()
    else:
        r = requests.get(baseUrl + path, headers=headers)
        responce = r.json()
        resp = json.dumps(responce, indent=4)
        # Write to file
        content = open("responces.txt", "a")
        content.write(resp + "\n")
        content.close()
    return resp

def get_request(key, secret, path):

    nowInMilisecond = str(int(time.time() * 1000))
    stringToSign = path + "\n" + nowInMilisecond + "\n"
    signature = base64.b64encode(hmac.new(secret, stringToSign.encode(), hashlib.sha512).digest())

    return request("get", key, signature, nowInMilisecond, path, None)

def post_request(key, secret, path, postData):

    nowInMilisecond = str(int(time.time() * 1000))
    stringToSign = path + "\n" + nowInMilisecond + "\n" + postData
    signature = base64.b64encode(hmac.new(secret, stringToSign.encode(), hashlib.sha512).digest())

    return request("post", key, signature, nowInMilisecond, path, postData)

class BTCMarkets:

    def __init__(self, key, secret):
        self.key = key
        self.secret = base64.b64decode(secret)

    def trade_history(self, currency, instrument, limit, since):

        data = OrderedDict([
            ("currency", currency),
            ("instrument", instrument),
            ("limit", limit),
            ("since", since)
        ])
        postData = json.dumps(data, separators=(",", ":"))

        return post_request(self.key, self.secret, "/order/trade/history", postData)

    def order_create(self, currency, instrument, price, volume, side, order_type, client_request_id):

        data = OrderedDict([
            ("currency", currency),
            ("instrument", instrument),
            ("price", price),
            ("volume", volume),
            ("orderSide", side),
            ("ordertype", order_type),
            ("clientRequestId", client_request_id)
        ])
        postData = json.dumps(data, separators=(",", ":"))

        return post_request(self.key, self.secret, "/order/create", postData)

    def order_history(self, currency, instrument, limit, since):

        data = OrderedDict([
            ("currency", currency),
            ("instrument", instrument),
            ("limit", limit),
            ("since", since)
        ])
        postData = json.dumps(data, separators=(",", ":"))

        return post_request(self.key, self.secret, "/order/history", postData)

    def order_open(self, currency, instrument, limit, since):

        data = OrderedDict([
            ("currency", currency),
            ("instrument", instrument),
            ("limit", limit),
            ("since", since)
        ])
        postData = json.dumps(data, separators=(",", ":"))

        return post_request(self.key, self.secret, "/order/open", postData)

    def order_detail(self, order_ids):

        data = {
            "orderIds": order_ids
        }
        postData = json.dumps(data, separators=(",", ":"))

        return post_request(self.key, self.secret, "/order/detail", postData)

    def order_cancel(self, order_ids):

        data = {
            "orderIds": order_ids
        }
        postData = json.dumps(data, separators=(",", ":"))

        return post_request(self.key, self.secret, "/order/cancel", postData)

    def account_balance(self):

        return get_request(self.key, self.secret, "/account/balance")

    def get_market_tick(self, instrument, currency):

        return get_request(self.key, self.secret, "/market/"+instrument+"/"+currency+"/tick")

    def get_market_orderbook(self, instrument, currency):

        return get_request(self.key, self.secret, "/market/"+instrument+"/"+currency+"/orderbook")

    def get_market_trades(self, instrument, currency):

        return get_request(self.key, self.secret, "/market/"+instrument+"/"+currency+"/trades")

    def get_market_trades_since(self, instrument, currency, since):

        return get_request(self.key, self.secret, "/market/"+instrument+"/"+currency+"/trades?"+str(since)+"")

# The end (for now)
