# This is Final Project for course MIS 3500
# Project chosen for the Final project is '1'
# The project is based on Stock Market

# Pre-requisites of the Project
# 1. Getting Data from web JSON API
# 2. Storing data in CSV files
# 3. Auto-update
# 4. Three Analysis on the data
# 5. Results inside results.json

from os import path
import time
import requests
import json
API_KEY = 'NG9C9EPVYBMQT0C8'
# Library imports
# json import to handle the json files
# requests imported to handle API key
# wait for 1 sec

mean_reversion_dict = {}
simple_average_dict = {}
bb_dict = {}


def append(ticker):
    url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + \
        ticker+'&outputsize=full&apikey=' + API_KEY
    req = requests.get(url)
    time.sleep(13)

    req_dict = json.loads(req.text)
    print(req_dict.keys())

    key1 = 'Time Series (Daily)'  # dictionary with all prices by date
    key2 = '4. close'

    csv_file = open("/home/ubuntu/environment/final_project/" +
                    ticker + ".csv", "r")
    lines = csv_file.readlines()
    last_date = lines[-1].split(",")[0]

    new_lines = []
    for date in req_dict[key1]:
        if date == last_date:
            break
        print(date + "," + req_dict[key1][date][key2])  # print key, value
        new_lines.append(date + "," + req_dict[key1][date][key2]+"\n")

    new_lines = new_lines[::-1]
    csv_file = open("/home/ubuntu/environment/final_project/" +
                    ticker + ".csv", "a")  # opening the file to append data
    csv_file.writelines(new_lines)  # appending new data
    csv_file.close()

    return csv_file
    # function ends here


def process_json(ticker):

    url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + \
        ticker+'&outputsize=full&apikey=' + API_KEY
    req = requests.get(url)
    time.sleep(13)

    req_dict = json.loads(req.text)

    print(req_dict.keys())

    key1 = 'Time Series (Daily)'  # dictionary with all prices by date
    key2 = '4. close'

    csv_file = open("/home/ubuntu/environment/final_project/" +
                    ticker + ".csv", "w")
    csv_file.write("Date,AAPL\n")
    write_lines = []
    for date in req_dict[key1]:
        print(date + "," + req_dict[key1][date][key2])  # print key, value
        write_lines.append(date + "," + req_dict[key1][date][key2]+"\n")

    write_lines = write_lines[::-1]
    csv_file.writelines(write_lines)
    csv_file.close()

    return csv_file

# --------------------------------------------------------------------------------------------------------------------------------


def meanReversionStrategy(prices, file):
    print("")
    print("\t !!!!!Starting Mean Reversion Strategy for!!!!!", file)
    print("")
    buy = 0
    iterative_profit = 0
    total_profit = 0
    first_buy = 0
    # Getting back to Moving Average
    i = 0
    for price in prices:
        if i >= 5:
            current_price = price
            moving_average = (prices[i-1] + prices[i-2] +
                              prices[i-3] + prices[i-4] + prices[i-5]) / 5
            # print("The Moving Average for last 5 days is", moving_average)

            if (current_price > 0.95*moving_average) and buy == 0:
                if i == len(prices) - 1:
                    print("")
                    print("        YOU SHOULD BUY TODAY")
                    print("")
                buy = current_price
                print("Buying the Stock", buy)
                if first_buy == 0:
                    first_buy = buy

                    print("The first buy is at: ", first_buy)

            elif (current_price < 1.05*moving_average) and buy != 0:
                if i == len(prices) - 1:
                    print("")
                    print("        YOU SHOULD SELL TODAY")
                    print("")
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
    print("For the Ticker: ", file)
    print("The total profit percentage is: ", final_profit_percent)
    print("The total Profit is: ", total_profit)
    print("")
    print("-----------------------------------------------------------------------------------------------------")

    mean_reversion_dict[file] = {
        'total profit': total_profit,
        'profit percent': final_profit_percent}
    return total_profit, final_profit_percent

# //////////////////////////////////////////////////
# Function for simple moving average


def simpleMovingAverage(prices, file):
    print("")
    print("\t !!!!!Starting Simple Moving Average for!!!!!", file)
    print("")
    buy = 0
    iterative_profit = 0
    total_profit = 0
    first_buy = 0

    # Getting back to Moving Average
    i = 0
    for price in prices:
        if i >= 5:
            current_price = price
            moving_average = (
                prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices[i-5]) / 5
            # print("The Moving Average for last 5 days is", moving_average)

            if (current_price > moving_average) and buy == 0:
                if i == len(prices) - 1:
                    print("")
                    print("        YOU SHOULD BUY TODAY")
                    print("")
                buy = current_price
                print("Buying the Stock", buy)
                if first_buy == 0:
                    first_buy = buy
                    print("The first buy is at: ", first_buy)

            elif (current_price < moving_average) and buy != 0:
                if i == len(prices) - 1:
                    print("")
                    print("      YOU SHOULD SELL TODAY")
                    print("")
                print("Selling stock at: ", current_price)
                iterative_profit = current_price - buy
                buy = 0
                print("This trade Profit is: ", iterative_profit)
                total_profit += iterative_profit
                print("")

        i += 1  # Iteration changes the loop process

    # Now processing the profits
    print("-----------------------SIMPLE MOVING AVERAGE total profits earned from the first buy----------------------")
    final_profit_percent = (total_profit/first_buy) * 100
    print("")
    print("For the Ticker: ", file)
    print("The total profit percentage is: ", final_profit_percent)
    print("The total Profit is: ", total_profit)
    print("")
    print("-----------------------------------------------------------------------------------------------------")

    simple_average_dict[file] = {
        'total profit': total_profit,
        'profit percent': final_profit_percent}
    return total_profit, final_profit_percent

# ///////////////////////////////////////////////////////////


def bb(prices, file):
    print("")
    print("\t !!!!!!Starting Bollinger Bands Strategy for!!!!!!", file)
    print("")
    buy = 0
    iterative_profit = 0
    total_profit = 0
    first_buy = 0

    # Getting back to Moving Average
    i = 0
    for price in prices:
        if i >= 5:
            current_price = price
            moving_average = (prices[i-1] + prices[i-2] +
                              prices[i-3] + prices[i-4] + prices[i-5]) / 5
            # print("The Moving Average for last 5 days is", moving_average)

            if (current_price < 0.95*moving_average) and buy == 0:
                if i == len(prices) - 1:
                    print("")
                    print("       YOU SHOULD BUY TODAY")
                    print("")
                buy = current_price
                print("Buying the Stock", buy)
                if first_buy == 0:
                    first_buy = buy
                    print("The first buy is at: ", first_buy)

            elif (current_price > 1.05*moving_average) and buy != 0:
                if i == len(prices) - 1:
                    print("")
                    print("      YOU SHOULD SELL TODAY")
                    print("")
                print("Selling stock at: ", current_price)
                iterative_profit = current_price - buy
                buy = 0
                print("This trade Profit is: ", iterative_profit)
                total_profit += iterative_profit
                print("")

        i += 1  # Iteration changes the loop process

    # Now processing the profits
    print("-----------------------BOLLINGER BANDS total profits earned from the first buy----------------------")
    final_profit_percent = (total_profit/first_buy) * 100
    print("")
    print("For the Ticker: ", file)
    print("The total profit percentage is: ", final_profit_percent)
    print("The total Profit is: ", total_profit)
    print("")
    print("-----------------------------------------------------------------------------------------------------")

    bb_dict[file] = {
        'total profit': total_profit,
        'profit percent': final_profit_percent}
    return total_profit, final_profit_percent


# /////////////////////////////////////////////////
def results():
    final_result = {}
    high_returns = 0
    high_returns_ticker = ""
    high_returns_strategy = ""
    high_returns_percent = 0
    print("")
    print("")
    print("!!!The final project API requests are at an interval of 13 seconds each!!!")
    print("")
    tickers = ['AAPL', 'CSCO', 'FB', 'GOOGL',
               'JPM', 'MSFT', 'TMUS', 'TSLA', 'TTM', 'XOM']
    for ticker in tickers:
        # if path.isfile(ticker + ".csv"):
        #     append(ticker)
        # else:
        #     process_json(ticker)

        file = open(ticker+".csv")
        lines = file.readlines()[1:]
        prices = [float(line.split(",")[1]) for line in lines]

        total_profit, final_profit_percent = simpleMovingAverage(
            prices, "/home/ubuntu/environment/final_project/"+ticker+".csv")
        if total_profit > high_returns:
            high_returns = total_profit
            high_returns_ticker = ticker
            high_returns_percent = final_profit_percent
            high_returns_strategy = "Simple Moving Average"

        total_profit, final_profit_percent = meanReversionStrategy(
            prices, "/home/ubuntu/environment/final_project/"+ticker+".csv")
        if total_profit > high_returns:
            high_returns = total_profit
            high_returns_ticker = ticker
            high_returns_percent = final_profit_percent
            high_returns_strategy = "Mean Reversion"

        total_profit, final_profit_percent = bb(
            prices, "/home/ubuntu/environment/final_project/"+ticker+".csv")
        if total_profit > high_returns:
            high_returns = total_profit
            high_returns_ticker = ticker
            high_returns_percent = final_profit_percent
            high_returns_strategy = "Simple Moving Average"

    final_result["simpleMovingAverage"] = simple_average_dict
    final_result["meanReversionStrategy"] = mean_reversion_dict
    final_result["bb"] = bb_dict

    final_result["MAX PROFIT"] = {"ticker": high_returns_ticker,
                                  "strategy": high_returns_strategy,
                                  "returns": high_returns,
                                  "percent": high_returns_percent}

    print("")

    print("")

    print("")
    print(final_result)


results()
