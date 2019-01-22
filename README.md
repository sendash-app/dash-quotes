# dash-quotes

simple dashboard of stock market prices to demostrate use of [plot.ly]()

## Using this Repo

## Getting Free Stock Prices
Since the rise and fall of the Yahoo! Finance and Google Finance stock prices, the online financial data landscape has changed.

We found ourselves in the age of big data, surrounded by fin-tech startups and online brokers, each craving out their own niche. Each player is eager to gain a foothold and expand their user base. So here's round up of some of the Python libraries I found useful while building this stock price dashboard:

* [iexfinance](https://github.com/addisonlynch/iexfinance): a python wrapper around the [IEX](https://iextrading.com/about/) [Developer API](https://iextrading.com/developer/). They provide historical and **real-time** quotes as well as **corp actions** and **dividend** data.
* [alpha_vantage](https://github.com/RomelTorres/alpha_vantage): offers free **real-time** and historical data on stocks as well, with a well written [API Doc](https://www.alphavantage.co/documentation/). You would need to apply for your own free API for authentication.
* [Robinhood](https://github.com/Jamonek/Robinhood): an unofficial python wrapper of the online broker with its own [unofficial API doc](https://github.com/sanko/Robinhood); **No authentication** is required for getting **real-time** and historic market data.
* [pandas_datareader](https://pandas-datareader.readthedocs.io/en/latest/): as of version `0.6`, Yahoo! Finance data is back. But other `sources` are also available including `IEX` and `Robinhood`. The advantage of using the datareader is that it is natively Pandas but you scarify control over the respective data source's API.  
