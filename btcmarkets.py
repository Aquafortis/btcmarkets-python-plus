import requests  # pip install requests
import json
import base64
import hashlib
import hmac
import time
from collections import OrderedDict

baseUrl = "https://api.btcmarkets.net"

def request(action, key, signature, timestamp, path, postdata):

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
        r = requests.post(baseUrl + path, data=postdata, headers=headers)
        response = r.json()
        resp = json.dumps(response, indent=4)
        # Write to file
        content = open("responses.txt", "a")
        content.write(resp + "\n")
        content.close()
    else:
        r = requests.get(baseUrl + path, headers=headers)
        response = r.json()
        resp = json.dumps(response, indent=4)
        # Write to file
        content = open("responses.txt", "a")
        content.write(resp + "\n")
        content.close()
    return resp

def get_request(key, secret, path):

    nonce = str(int(time.time() * 1000))
    payload = path + "\n" + nonce + "\n"
    signature = base64.b64encode(hmac.new(secret, payload.encode(), hashlib.sha512).digest())

    return request("get", key, signature, nonce, path, None)

def post_request(key, secret, path, postdata):

    nonce = str(int(time.time() * 1000))
    payload = path + "\n" + nonce + "\n" + postdata
    signature = base64.b64encode(hmac.new(secret, payload.encode(), hashlib.sha512).digest())

    return request("post", key, signature, nonce, path, postdata)

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
        postdata = json.dumps(data, separators=(",", ":"))

        return post_request(self.key, self.secret, "/order/trade/history", postdata)

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
        postdata = json.dumps(data, separators=(",", ":"))

        return post_request(self.key, self.secret, "/order/create", postdata)

    def order_history(self, currency, instrument, limit, since):

        data = OrderedDict([
            ("currency", currency),
            ("instrument", instrument),
            ("limit", limit),
            ("since", since)
        ])
        postdata = json.dumps(data, separators=(",", ":"))

        return post_request(self.key, self.secret, "/order/history", postdata)

    def order_open(self, currency, instrument, limit, since):

        data = OrderedDict([
            ("currency", currency),
            ("instrument", instrument),
            ("limit", limit),
            ("since", since)
        ])
        postdata = json.dumps(data, separators=(",", ":"))

        return post_request(self.key, self.secret, "/order/open", postdata)

    def order_detail(self, order_ids):

        data = {
            "orderIds": order_ids
        }
        postdata = json.dumps(data, separators=(",", ":"))

        return post_request(self.key, self.secret, "/order/detail", postdata)

    def order_cancel(self, order_ids):

        data = {
            "orderIds": order_ids
        }
        postdata = json.dumps(data, separators=(",", ":"))

        return post_request(self.key, self.secret, "/order/cancel", postdata)

    def funds_transfer_crypto(self, amount, address, currency):

        data = OrderedDict([
            ("amount", amount),
            ("address", address),
            ("currency", currency)
        ])
        postdata = json.dumps(data, separators=(",", ":"))

        return post_request(self.key, self.secret, "/fundtransfer/withdrawCrypto", postdata)

    def funds_withdraw_fiat(self, name, number, bank, bsb, amount, currency):

        data = OrderedDict([
            ("accountName", name),
            ("accountNumber", number),
            ("bankName", bank),
            ("bsbNumber", bsb),
            ("amount", amount),
            ("currency", currency)
        ])
        postdata = json.dumps(data, separators=(",", ":"))

        return post_request(self.key, self.secret, "/fundtransfer/withdrawEFT", postdata)

    def account_balance(self):

        return get_request(self.key, self.secret, "/account/balance")

    def account_tradingfee(self, instrument, currency):

        return get_request(self.key, self.secret, "/account/"+instrument+"/"+currency+"/tradingfee")

    def get_market_tick(self, instrument, currency):

        return get_request(self.key, self.secret, "/market/"+instrument+"/"+currency+"/tick")

    def get_market_orderbook(self, instrument, currency):

        return get_request(self.key, self.secret, "/market/"+instrument+"/"+currency+"/orderbook")

    def get_market_trades(self, instrument, currency):

        return get_request(self.key, self.secret, "/market/"+instrument+"/"+currency+"/trades")

    def get_market_trades_since(self, instrument, currency, since):

        return get_request(self.key, self.secret, "/market/"+instrument+"/"+currency+"/trades?"+str(since)+"")

# The end (for now)
