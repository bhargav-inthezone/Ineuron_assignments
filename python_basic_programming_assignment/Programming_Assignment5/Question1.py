'''Question1) Write a program to find the LCM?'''
import math

x1 = int(input("enter 1st number:"))
x2 = int(input("enter 2nd number:"))
gcd = math.gcd(x1,x2)
LCM = (x1*x2)/gcd
print("LCM of given numbers = ",LCM)
