'''Question 4) Write a program to Check Prime number?'''
number = int(input("Enter a number :"))
if number ==0 or number==1:
    print("Entered value is not greater than 1")
rem = 0
for i in range(2,number):
    if number%i ==0:
        rem+=1
if rem>0:
    print("Entered number is not a prime Number")
else:
    print("Entered number is a Prime Number")

