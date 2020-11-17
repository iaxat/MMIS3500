# This project is about HomeWork 5

# libraries imported
import json


mean_reversion_dict = {}
simple_average_dict = {}

# The Mean Reversion Strategy Code Below


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

    mean_reversion_dict[file] = {
        'total profit': total_profit, 'profit percent': final_profit_percent}

    # Unrelated but was in the class video so added
    total_avg = add/counter
    print("Total Average for price for the whole list is: ", total_avg)


# # The main function goes here
# file_read()


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

    simple_average_dict[file] = {
        'total profit': total_profit, 'profit percent': final_profit_percent}


# function to safe results to dict and then to json file
def dict_to_json(dict1, dict2):
    print(dict1)
    print()
    json_object1 = json.dumps(dict1)
    print(json_object1)
    print()
    print(dict2)
    json_object2 = json.dumps(dict2)
    print((json_object2))
    print()
    with open("mean_reversion.json", "w") as outfile:
        json.dump(dict1, outfile)
    with open("simple_average.json", "w") as outfile:
        json.dump(dict2, outfile)


def file_read():
    # Function for mean reversion strategy
    file_names_list = ['AAPL.txt', 'CSCO.txt', 'FB.txt', 'GOOGL.txt',
                       'JPM.txt', 'MSFT.txt', 'TMUS.txt', 'TSLA.txt', 'TTM.txt', 'XOM.txt']
    for file_name in file_names_list:

        price_list = []
        file = open(file_name, "r")
        lines = file.readlines()
        for line in lines:
            price = float(line)
            price_list.append(price)

        meanReversionStrategy(price_list, file_name)
        simpleMovingAverage(price_list, file_name)

    dict_to_json(mean_reversion_dict, simple_average_dict)


# ------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    file_read()
