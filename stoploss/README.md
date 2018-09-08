**Experimental Stop Loss Feature.**

#### USE WITH CAUTION

Read the instructions in the files.

As BTC Markets doesn't currently have a `stop-loss` setting
we can use this workaround.

This can also be used as an `"oco"` order type. (one cancels the other)

**Usage:**

Set (seconds) to time between api calls for lastPrice.

300 = 5 minutes - which should suit most swing trades.

Make sure the matching `instrument` and `currency` settings are set in both files.

Set your `quantity`.

Note that we are using "Market" trades so your order should be filled.

Even though it is not used for "Market" orders, as a precaution, set the
`price` in `marketbuy.py` and `marketsell.py` files as per instructions.

Once you have everything set:

`$ cd (path to the stoploss folder)`

then run the script:

`$ python3 stopbuy.py`

or

`$ python3 stopsell.py`

The script will run until one of the conditions are met,
then it will stop.

You will have to set it again for the next trade.

Keep in mind, this script will need to be running constantly
on your machine until the order is filled.
