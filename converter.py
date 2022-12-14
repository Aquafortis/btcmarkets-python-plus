import time
import calendar  # pip install calendar
"""
# calendar module also imports datetime module
# Copyright (c) 2023 Aquafortis
# https://github.com/Aquafortis/btcmarkets-python-plus
"""
class Converter:

    # Convert gmt datetime to timestamp (Not available in local time)
    def get_timestamp(self, year, month, day, hour, minutes, seconds, multiple):

        return calendar.timegm((year,month,day,hour,minutes,seconds)) * multiple

    # Convert timestamp to datetime string
    def get_localtime(self, mts, div):

        return time.strftime("%a %b %d %H:%M:%S %Y", time.localtime(mts/div))

    # Convert timestamp to datetime string
    def get_gmttime(self, mts, div):

        return time.strftime("%a %b %d %H:%M:%S %Y", time.gmtime(mts/div))

    # Convert time now to timestamp
    def get_timenow(self, multiple):

        return int(round(time.time() * multiple))

    # Local time now datetime as string
    def get_localtime_now(self):

        return time.asctime(time.localtime(time.time()))

    # Convert price or volume to 1E8 integer (max 2 decimal places)
    def price_integer(self, rate):

        return int(rate*1E8)

    # Convert 1E8 integer to actual price or volume (rounded)
    def integer_price(self, integer):

        return int(integer/1E8)

##convert = Converter()
# Usage (copy from below to main.py)
#print(convert.get_timestamp(2018, 9, 3, 0, 0, 0, 1000))
#print(convert.get_localtime(1535932800000, 1000))
#print(convert.get_localtime(1535945835, 1))
#print(convert.get_gmttime(1535932800000, 1000))
#print(convert.get_timenow(1000))
#print(convert.get_localtime_now())
#print(convert.price_integer(2650.50))
#print(convert.integer_price(265050000000))
