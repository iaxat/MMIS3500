import requests
import json

ticker = 'AAPL'
url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + \
    ticker+'&outputsize=full&apikey=NG9C9EPVYBMQT0C8'
request = requests.get(url)
rqst_dictonary = json.loads(request.text)
json.dump(rqst_dictonary,open("results.json","w"))
