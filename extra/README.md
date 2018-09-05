**The files contained in this folder are experimental.**

#### USE WITH CAUTION

`buyOrderWithErrorHandling.py` and `sellOrderWithErrorHandling.py`
both have the potential to create multiple consecutive orders if
the code is incorrectly altered.

If you want to test them, you will need to add your keys to `config.py`
and uncomment the `requests` line.

It is not recommended to use the `range()` method in the real world.
It would be better to remove this method and call the file from
another file.

It is used here just to give you an idea of how API status code errors
could potentially be handled, and to give you a template to work on.

You will probably want to rename the files to something shorter.

Don't forget to backup your modifications, as they may be overridden
by future updates.
