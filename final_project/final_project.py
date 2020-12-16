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


tickers = ['AAPL', 'CSCO', 'FB', 'GOOGL',
           'JPM', 'MSFT', 'TMUS', 'TSLA', 'TTM', 'XOM']
results_dict = {}


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

    # fil = open(ticker+".csv","r")
    # lines = fil.readlines()
    # last_date = lines[-1].split(",")[0]
    fil = open(ticker+".csv", "w")
    fil.write("Date,price\n")

    new_lines = []

    for date in req_dct[key1]:
        # if date == last_date:
            # break
        # print(date + "," + req_dct[key1][date][key2])
        # fil.write(date + "," + req_dct[key1][date][key2]+"\n")
        new_lines.append(date + "," + req_dct[key1][date][key2]+"\n")
    
    new_lines = new_lines[::-1]
    fil = open(ticker + ".csv", "a")
    fil.writelines(new_lines)
    fil.close()

    return fil
# function ends here

def price_list(file):



def meanReversionStrategy(prices, file):
    add = 0  # variable for adding total
    counter = 0  # counter to understand how many counts are there
    buy = 0
    iterative_profit = 0
    total_profit = 0
    first_buy = 0

    # Getting back to Moving Average
    i = 0
    for price in prices:
        add += price
        counter += 1
        if i >= 5:
            current_price = price
            moving_average = (prices[i-1] + prices[i-2] +
                              prices[i-3] + prices[i-4] + prices[i-5]) / 5
            # print("The Moving Average for last 5 days is", moving_average)

            if (current_price < 0.95*moving_average) and buy == 0:
                buy = current_price
                print("Buying the Stock", buy)
                if first_buy == 0:
                    first_buy = buy
                    print("The first buy is at: ", first_buy)

            elif (current_price > 1.05*moving_average) and buy != 0:
                print("Selling stock at: ", current_price)
                iterative_profit = current_price - buy
                buy = 0
                print("This trade Profit is: ", iterative_profit)
                total_profit += iterative_profit
                print("")

        i += 1  # Iteration changes the loop process

    # Now processing the profits
    print("-----------------------MEAN REVERSION total profits earned from the first buy----------------------")
    final_profit_percent = (total_profit/first_buy) * 100
    print("")
    print("The total profit percentage is: ", final_profit_percent)
    print("")

    results_dict[file] = {
        'total profit': total_profit, 'profit percent': final_profit_percent}

    # Unrelated but was in the class video so added
    total_avg = add/counter
    print("Total Average for price for the whole list is: ", total_avg)


# Function for simple moving average
def simpleMovingAverage(prices, file):
    add = 0  # variable for adding total
    counter = 0  # counter to understand how many counts are there
    buy = 0
    iterative_profit = 0
    total_profit = 0
    first_buy = 0

    # Getting back to Moving Average
    i = 0
    for price in prices:
        add += price
        counter += 1
        if i >= 5:
            current_price = price
            moving_average = (
                prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices[i-5]) / 5
            # print("The Moving Average for last 5 days is", moving_average)

            if (current_price > moving_average) and buy == 0:
                buy = current_price
                print("Buying the Stock", buy)
                if first_buy == 0:
                    first_buy = buy
                    print("The first buy is at: ", first_buy)

            elif (current_price < moving_average) and buy != 0:
                print("Selling stock at: ", current_price)
                iterative_profit = current_price - buy
                buy = 0
                print("This trade Profit is: ", iterative_profit)
                total_profit += iterative_profit
                print("")

        i += 1  # Iteration changes the loop process

    # Now processing the profits
    print("-----------------------SIMPLE MOVING total profits earned from the first buy----------------------")
    final_profit_percent = (total_profit/first_buy) * 100
    print("")
    print("The total profit percentage is: ", final_profit_percent)
    print("")

    # Unrelated but was in the class video so added
    total_avg = add/counter
    print("Total Average for price for the whole list is: ", total_avg)

    results_dict[file] = {
        'total profit': total_profit, 'profit percent': final_profit_percent}


# Program Running
for ticker in tickers:
    time.sleep(13)
    price_list(web_json(ticker))


# append makes data dissaoear
# just pick price list from csv
# result.json should be like?
# 