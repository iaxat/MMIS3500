# This project is about HomeWork 5

# libraries imported
import json

# nested Functions
def file_read():
    # Function for mean reversion strategy
    file_names_list = ['AAPL.txt','CSCO.txt','FB.txt','GOOGL.txt','JPM.txt','MSFT.txt','TMUS.txt','TSLA.txt','TTM.txt','XOM.txt']
    for file in file_names_list:
        price_list = []
        file = open(file,"r")
        lines = file.readlines()
        
    
        # The Mean Reversion Strategy Code Below
        def meanReversionStrategy():
            add = 0 # variable for adding total
            counter = 0 # counter to understand how many counts are there
            prices = price_list
            buy = 0
            iterative_profit = 0
            total_profit = 0
            first_buy = 0
            mean_reversion_dict = {}

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


        # # The main function goes here
        # file_read()


        # Function for simple moving average
        def simpleMovingAverage():
            moving_average_dict = {}
            print('Simple Moving Average')



    # function to safe results to dict and then to json file
    def saveResults():
        print('Save Result')


    # print('Main Function Here')
    # meanReversionStrategy()
    # simpleMovingAverage()
    # saveResults()
