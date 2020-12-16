
import json
import requests
import time
import numpy as np



tickers = ['AAPL', 'CSCO', 'FB', 'GOOGL',
           'JPM', 'MSFT', 'TMUS', 'TSLA', 'TTM', 'XOM']
results_dict = {}


def web_json():
    ticker = 'AAPL'
    url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + \
        ticker+'&outputsize=full&apikey=NG9C9EPVYBMQT0C8'
    # url is for creating the request for getting data
    req = requests.get(url)

    req_dct = json.loads(req.text)
    # Converting to Dictionary
    json.dump(req_dct, open(ticker+".json", "w"))
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
        print(date + "," + req_dct[key1][date][key2])
        # fil.write(date + "," + req_dct[key1][date][key2]+"\n")
        new_lines.append(date + "," + req_dct[key1][date][key2]+"\n")

    new_lines = new_lines[::-1]
    fil = open(ticker + ".csv", "a")
    fil.writelines(new_lines)
    fil.close()

    return fil
# function ends here

web_json()

# append makes data dissapear
# just pick price list from csv
# result.json should be like?
#
