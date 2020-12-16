# Web JSON API

import requests
import json

ticker = 'AAPL'
url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + \
    ticker+'&outputsize=full&apikey=NG9C9EPVYBMQT0C8'

print('The json process')

request = requests.get(url)
print(request.text)

rqst_dict = json.loads(request.text)
print(rqst_dict)


json.dump(rqst_dict,open(ticker+".csv", "w"))