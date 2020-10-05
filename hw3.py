# This is the homework 3 from exersies from chapter 3

# Problem 3.4
# The problem is for printing @ in two rows
def function34():
    print("This is Problem 3.4")
    print()
    x = range(0,2) # The range is defined here for row
    y = range(0,7)# The 2nd range for column
    for i in x: # First loop for iterating the row
        for j in y: # The second loop for iterating the column
            print("@",end="") # end used for not changing the line
        print() # The print statement to change the line
    
    print() # to give a space before another problem runs
# Running the function for problem 3.4
function34()

#------------------------------------------------------------------------------------------------------------------------------------------------
# Problem 2.11 and Problem 3.9

# Problem 3.9
# The problem is related to exercise 2.11
# In this homework to solve problem 3.9, I have also mentioned problem 2.11 so the code changes can be seen and understood

# First Problem 2.11
def function211():
    print("This is problem 2.11 for reference to 3.9 which is just below this problem")
    print()
    data = int(input("Enter number: ")) # The 
    a = data // 10000 # The division floor function does remove other digits
    b = data % 10000 // 1000 # Modulous function is for dividing to get the decimal value
    c = data % 10000 % 1000 // 100
    d = data % 10000 % 1000 % 100 // 10
    e = data % 10000 % 1000 % 100 % 10 // 1
    
    print(a,' ',b,' ',c,' ',d,' ',e)
    print()

function211()
# Now with the changes the problem 3.9 is mentioned:

# PROBLEM 3.9
def function39():
    print("This is Problem 3.9")
    print()
    x = int(input("Enter number: "))
    arr = [] # This creates an array which will hold the digits after seperation
    while True:
        a = x // 10000
        arr.append(a) # The array append function adds the seperated digit 
        b = x % 10000 // 1000
        arr.append(b)
        c = x % 10000 % 1000 // 100
        arr.append(c)
        d = x % 10000 % 1000 % 100 // 10
        arr.append(d)
        e = x % 10000 % 1000 % 100 % 10 // 1
        arr.append(e)
        break # The break function is here to get out from the while condition
    
    for i in range(0, len(arr)): # This loop is for iterating around the array
        print(arr[i])
    print()
    
function39()
#------------------------------------------------------------------------------------------------------------------------------------------------
# Problem 3.11
def function311():
    print("This is Problem 3.11")
    print()
    # we will take input of the gallon and miles on it
    fuel = []
    miles = []
    
    while True:
        fuel1 = float(input("Enter the fuel: "))
        mile1 = float(input("Enter the miles in "))
        fuel.append(fuel1)
        miles.append(mile1)
        ask = input("Do you want to enter Fuel and Miles y/n: ")
        if ask == "n":
            break
    print()
    x = len(fuel)
    y = len(miles)
    
    for i in range(0,x):
        avg = miles[i]/fuel[i]
        print("Average for ", miles[i]," miles in ",fuel[i]," fuel is ",avg)
    print()    
    print("Calculating total average of total miles per total gallon of fuel :-D :-P :-) :-|")
    print("Got it...Coming up!!!")
    print()
    totalfuel = 0
    totalmile = 0
    for i in range(0,x):
        totalfuel += float(fuel[i])
        totalmile += float(miles[i])
    
    totalavg = totalmile/totalfuel
    print("The average for total-miles:",totalmile,"in total-fuel:",totalfuel,"is",totalavg)
    print()

# Running the function for Problem 3.11
function311()

#------------------------------------------------------------------------------------------------------------------------------------------------
# Problem 3.12
# This is a palindrom problem
def function312():
    print("This is problem 3.12")
    print()
    data = input("Enter the digits/letters: ")
    arr = list(data)
    x = len(arr)
    counter = 0
    for i in range(0,x):
        if (arr[i] == arr[x-i-1]):
            counter += 0
        else:
            counter += 1
    if (counter == 0):
        print("The input", data,"is Palindrome")
    elif (counter >= 1):
        print("The input", data,"is not Palindrome")
    print()

# Running Problem 3.12
function312()
#------------------------------------------------------------------------------------------------------------------------------------------------
# Problem 3.14
# Finding the value of pi using infinite series
# Leibniz Formula to be used to understand the pi value
# The value to be found is till 3.14
# Program to be run till the number of iterations for 3.14 is two times
def function314():
    print("This is problem 3.14")
    pi = 0
    iterate = 3000
    counter = 0
    times_pi = 0
    for i in range(0, iterate):
        pi += ((4.0 * (-1)**i) / (2i + 1))
        print(,pi)
        counter += 1
        if pi == 3.14:
            times_pi += 1
            if times_pi == 2:
                break
    
    print()
    print("The value of pi has been 3.14 2 times till now")
    print("The number of iterations is:", counter,"before the value of pi till 2 decimal value could be achieved")
        
# The function for problem 3.14 runs here

function314()
#------------------------------------------------------------------------------------------------------------------------------------------------
