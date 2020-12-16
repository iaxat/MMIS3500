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
import numpy as np
# json import to handle the json files
# requests imported to handle API key
# wait for 1 sec

def web_json(ticker):
    url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + \
        ticker+'&outputsize=full&apikey=NG9C9EPVYBMQT0C8'
    # url is for creating the request for getting data
    req = requests.get(url)

    req_dct = json.loads(req.text)
    # Converting to Dictionary 
    json.dump(req_dct, open(ticker+".json","w"))
    # Converting to json file format

    key1 = "Time Series (Daily)"
    key2 = "4. close"

    fil = open(ticker+".csv","r")
    lines = fil.readlines()
    last_date = lines[-1].split(",")[0]
    fil = open(ticker+".csv", "w")
    fil.write("Date,price\n")

    new_lines = []

    for date in req_dct[key1]:
        if date == last_date:
            break
        # print(date + "," + req_dct[key1][date][key2])
        new_lines.append(date + "," + req_dct[key1][date][key2]+"\n")
    
    new_lines = new_lines[::-1]
    fil = open(ticker + ".csv", "a")
    fil.writelines(new_lines)
    fil.close()



# Starting Program
tickers = ['AAPL', 'CSCO', 'FB', 'GOOGL',
                 'JPM', 'MSFT', 'TMUS', 'TSLA', 'TTM', 'XOM']

for ticker in tickers:
    time.sleep(13)
    web_json(ticker)
