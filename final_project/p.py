import requests
import json
import os



def append_data(ticker):
    url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + \
        ticker+'&outputsize=full&apikey=NG9C9EPVYBMQT0C8'
    # url is for creating the request for getting data
    req = requests.get(url)

    req_dct = json.loads(req.text)

    key1 = "Time Series (Daily)"
    key2 = "4. close"

    fil = open(ticker+".csv", "w")
    lines = fil.readlines()
    last_date = lines[-1].split(",")[0]

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


append_data('AAPL')
