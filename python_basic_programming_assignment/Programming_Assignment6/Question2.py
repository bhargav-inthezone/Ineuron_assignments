'''Question 2) Write a program to find the factorial using Recursion?'''
def factorial(number):
    if number==0 or number==1:
        return 1
    else:
        return number*factorial(number-1)
n = int(input("Enter a number to find its factorial:"))
print(factorial(n))