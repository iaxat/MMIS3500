# The following is the homework 4 for course MIS3500
# This assignment is Home Work 4

def file_read():
    file = open("AAPL.txt", "r")
    lines = file.readlines()
    for line in lines:
        price = float(line)
        print("The file read prints following: ")
        print(price)

def profit_loss():
    print("We will calculate the profit ")


# The main function goes here
file_read()

