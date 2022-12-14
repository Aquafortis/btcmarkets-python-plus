"""
# Copyright (c) 2023 Aquafortis
# https://github.com/Aquafortis/btcmarkets-python-plus
# OCO (one cancels the other)
# Specify all of your order settings below
# Run the desired script - or run both
# $ cd (path to stoploss folder)
"""

# Buy Order with Stop (OCO)
buySeconds = 300
buyCurrency = "AUD"
buyInstrument = "BTC"
buyStopLoss = 9050
buyPrice = 7800
buyQuantity = 0.01
# Run $ python3 stopbuy.py

# Sell Order with Stop (OCO)
sellSeconds = 300
sellCurrency = "AUD"
sellInstrument = "BTC"
sellStopLoss = 9050
sellPrice = 10800
sellQuantity = 0.01
# Run $ python3 stopsell.py
