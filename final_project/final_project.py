# This is Final Project for course MIS 3500

# Project chosen for the Final project is '1'

# The project is based on Stock Market

# Pre-requisites of the Project
# 1. Getting Data from web JSON API
# 2. Storing data in CSV files
# 3. Auto-update
# 4. Three Analysis on the data
# 5. Results inside results.json
# NG9C9EPVYBMQT0C8

# API Key Generated = 3D9FOUWO02NOZH93

# Library imports
import json
import requests
import time
# json import to handle the json files
# requests imported to handle API key
# wait for 1 sec

def processing_json(ticker):
    url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + \
        ticker+'&outputsize=full&apikey=NG9C9EPVYBMQT0C8'
    request = requests.get(url)
    rqst_dictonary = json.loads(request.text)

    key1 = "Time Series (Daily)"
    # date all  of themn
    key2 = "4. close"

    fil = open(ticker+".csv", "w")
    fil.write("Date,price\n")

    for date in rqst_dictonary[key1]:
        # print(date + "," + rqst_dictonary[key1][date][key2])
        fil.write(date + "," + rqst_dictonary[key1][date][key2]+"\n")
    fil.close()

def data_extraction():
    tickers = ['AAPL', 'CSCO', 'FB', 'GOOGL',
                'JPM', 'MSFT']
    for ticker in tickers:
        processing_json(ticker)
        time.sleep(1)

if __name__ == "__main__":
    data_extraction()