# The following is the homework 4 for course MIS3500
# This assignment is Home Work 4

def file_read():
    add = 0 # variable for adding total
    counter = 0 # counter to understand how many counts are there
    prices = []
    buy = 0
    iterative_profit = 0
    total_profit = 0
    first_buy = 0

    file = open("AAPL.txt", "r")
    lines = file.readlines() # This line reads the lines in the file
    
    for line in lines:

        price = float(line)
        prices.append(price)
        add += price
        counter += 1

        # Getting back to Moving Average
    i = 0
    for price in prices:
        if i >= 5:
            current_price = price
            moving_average = (prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices[i-5]) / 5
            # print("The Moving Average for last 5 days is", moving_average)
            
            if (current_price < 0.95*moving_average) and buy == 0:
                buy = current_price
                print("Buying the Stock",buy)
                if first_buy == 0:
                    first_buy = buy
                    print("The first buy is at: ", first_buy)

            elif (current_price > 1.05*moving_average) and buy!=0:
                print("Selling stock at: ", current_price)
                iterative_profit = current_price - buy
                buy = 0
                print("This trade Profit is: ", iterative_profit)
                total_profit += iterative_profit
                print("")


        i += 1 # Iteration changes the loop process

    # Now processing the profits
    print("-----------------------We will see the total profits earned from the first buy----------------------")
    final_profit_percent = (total_profit/first_buy) * 100
    print("")
    print("The total profit percentage is: ", final_profit_percent)
    print("")


# Unrelated but was in the class video so added
    total_avg = add/counter
    print("Total Average for price for the whole list is: ", total_avg)


# The main function goes here
file_read()