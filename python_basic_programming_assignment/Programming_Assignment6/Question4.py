'''Question4) Write a program to calculate natural logarithmic of number?'''

import math

n = float(input("Enter a number to find its logarithmic value:"))
def logarithm(number):
    if number<=0:
        print("Enter a valid number for applying log")
    else:
        print(math.log(number))
logarithm(n)
