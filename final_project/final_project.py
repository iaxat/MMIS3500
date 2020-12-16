# This is Final Project for course MIS 3500
# Project chosen for the Final project is '1'
# The project is based on Stock Market

# Pre-requisites of the Project
# 1. Getting Data from web JSON API
# 2. Storing data in CSV files
# 3. Auto-update
# 4. Three Analysis on the data
# 5. Results inside results.json


# API Key = NG9C9EPVYBMQT0C8

# Library imports
import json
import requests
import time
# json import to handle the json files
# requests imported to handle API key
# wait for 1 sec

def web_json(ticker):
    # ticker = 'AAPL'
    url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + \
        ticker+'&outputsize=full&apikey=NG9C9EPVYBMQT0C8'
    req = requests.get(url)

    req_dct = json.loads(req.text)
    json.dump(req_dct, open(ticker+".json","w"))

    key1 = "Time Series (Daily)"
    key2 = "4. close"

    fil = open(ticker+".csv", "w")
    fil.write("Date,price\n")

    for date in req_dct[key1]:
        # print(date + "," + req_dct[key1][date][key2])
        fil.write(date + "," + req_dct[key1][date][key2]+"\n")
    fil.close()


tickers = ['AAPL', 'CSCO', 'FB', 'GOOGL',
                 'JPM', 'MSFT', 'TMUS', 'TSLA', 'TTM', 'XOM']


for ticker in tickers:
    time.sleep(30)
    web_json(ticker)



