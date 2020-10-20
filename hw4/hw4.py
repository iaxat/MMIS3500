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
        print(price)
        prices.append(price)
        add += price
        counter += 1

        # Getting back to Moving Average
        i = 0
        for price in prices:
            if i >= 5:
                current_price = price
                moving_average = (prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices[i-5]) / 5
                print("The Moving Average for last 5 days is", moving_average)
                
                if (current_price < .95*moving_average):
                    buy = price
                    print("Buying the Stock",buy)
                    if first_buy == 0:
                        first_buy = buy
                        print("The first buy is at: ", first_buy)

                elif (current_price > 1.5*moving_average):
                    iterative_profit = current_price - buy
                    print("This trade Profit is: ", iterative_profit)
                    total_profit += iterative_profit

                else:
                    print()

            i += 1 # Iteration changes the loop process

    # Now processing the profits
    


# Unrelated but was in the class video so added
    total_avg = add/counter
    print("Total Average for price for the whole list is: ", total_avg)


# The main function goes here
file_read()