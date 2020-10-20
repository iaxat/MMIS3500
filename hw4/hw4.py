# The following is the homework 4 for course MIS3500
# This assignment is Home Work 4

def file_read():
    add = 0
    counter = 0
    file = open("AAPL.txt", "r")
    lines = file.readlines()
    for line in lines:
        price = float(line)
        print(price)
        add += price
        counter += 1
    
    total_avg = add/counter
    print("Total Average for price is: ", total_avg)

def profit_loss():
    print("We will calculate the profit ")


# The main function goes here
file_read()