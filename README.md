# BTC Markets python plus
## Optimised for Python 3x
Originally forked from [BTCMarkets / api-client-python](https://github.com/BTCMarkets/api-client-python) v1 API
### What's new?
* Using `requests` instead of `urllib`
* Added `/order/cancel`
* Added `since` parameter to `/market/BTC/AUD/trades?since=trade_id`
* Indented responses for easy reading
* Responses logged in backup file
* Includes a 1E8 converter for price and volume
* Includes a timestamp and datetime string converter
* Added standalone buy and sell order files
* Added Fund Transfer API requests
* Added `stop-loss` or `oco` order type files

**Only using stable v1 API** (for now)

Tested on Python 2.7.15

Tested on Python 3.7.0

### Important!
**All `rate` and `quantity` fields are automatically multiplied by 100000000**

Type in the **Actual** price, volume, or amount you want to trade or send.

**Usage**

See `main.py` file with examples.

`$ python3 main.py`

`$ python main.py`

To use `buyorder.py` and `sellorder.py` files:

Uncomment the `requests.post` line in the file.

`$ python3 buyorder.py`

`$ python3 sellorder.py`

**Points of interest**

You'll need `requests` and `calendar` modules installed.

`$ pip install requests`

`$ pip install calendar`

If you want to programmatically clean out your response backups from the text file, just run these next few lines in the `main.py` file.

`content = open("responses.txt", "w")`  
`content.truncate()`  
`content.close()`

Don't forget to add your keys to the `config.py` file.

TODO list:
* ~~Fund Transfer API requests~~
* ~~Sample standalone `/order/create` files for use with a trading bot~~

LICENSE: [MIT License](https://github.com/Aquafortis/btcmarkets-python-plus/blob/master/LICENSE.txt)
