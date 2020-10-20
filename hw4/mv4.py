file = open("AAPL.txt", "r")
lines = file.readlines()
prices = []

for line in lines:
    price = float(line)
    prices.append(price)
    print(price)
print(prices)