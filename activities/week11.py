# Week 11

# Content Videos
# Files Section 9.3
file1 = open("output1.txt",'w')
file1.write('hello\n')
file1.write('goodbye\n')

with open('output2.txt','w') as file2:
    file2.write('hello goodbye')



# File OS Module 9.4
import os

os.rename('output1.txt', 'output_rename.txt')



# JSON Section 9.5
import json

my_hobbies = {}

my_hobbies['sports'] = ['rugby','basketball','football','soccer']
my_hobbies['arts'] = ['music','painting']
my_hobbies['tv_shows'] = ['the office','press your luck']

print(my_hobbies)

json.dump(my_hobbies,open('my_hobbies.json', 'w'))

d1 = json.load(open('my_hobbies.json','r'))
print(d1)



# Handling Exceptions 9.8
try:
    open('this file')
except:
    print('this file does not exist')

try:
    print(0/5)
    print(5/0)
except:
    print('throw denominator')

print('still running')



# Pandas Module 9.12
import csv
import pandas
import numpy

# Section 9.12.2
df = pandas.read_csv("AAPL.csv")
# print(df)
print(df.keys())

print(df["Adj Close"])

for price in df["Adj Close"]:
    print(price)

# print(df.head())



# ZOOM SESSION 11.1 PROGRAMMING ACTIVITIES

