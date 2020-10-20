# The following is the homework 4 for course MIS3500
# This assignment is Home Work 4

def file_read():
    add = 0 # variable for adding total
    counter = 0 # counter to understand how many counts are there
    prices = []
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
                current_price = prices[i]
                moving_average = (prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices[i-5]) / 5
                print("The Moving Average for last 5 days is", moving_average)
                if (current_price < )
            i += 1




    total_avg = add/counter
    print("Total Average for price is: ", total_avg)

    # Now we will get back on the HW4




# The main function goes here
file_read()