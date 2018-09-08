Experimental Stop Loss Feature.

USE WITH CAUTION

Read the instructions in the files.

As BTC Markets doesn't currently (September 2018) have a stop-loss setting
we can use this workaround.

This can also be used as an "oco" order type. (one cancels the other)

Usage:

Specify all of your order settings in the settings.py file.

Seconds is the time between api calls to get lastPrice.

300 = 5 minutes - which should suit most swing trades.

There is no need to modify the other files, except for adding your keys
to config.py and uncommenting requests.post in marketbuy.py and
marketsell.py files.

Note that we are using "Market" trades so your order should get filled.

Once you have everything set:

$ cd (path to the stoploss folder)

then run the script:

$ python3 stopbuy.py

or

$ python3 stopsell.py

The script will run until one of the conditions are met,
then it will stop.

You will have to set it again for the next trade.

Keep in mind, this script will need to be running constantly
on your machine until the order is filled.
