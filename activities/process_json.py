import requests
import json

ticker = 'AAPL'
url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + \
    ticker+'&outputsize=full&apikey=NG9C9EPVYBMQT0C8'
request = requests.get(url)
rqst_dictonary = json.loads(request.text)

key1 = "Time Series (Daily)"
# date all  of themn
key2 = "4. close"

fil = open(ticker+".csv","w")
fil.write("Date,price\n")

for date in rqst_dictonary[key1]:
    print(rqst_dictonary[key1][date][key2])
