# Web JSON API

import requests
import json

ticker = 'AAPL'
url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + \
    ticker+'&outputsize=full&apikey=NG9C9EPVYBMQT0C8'


