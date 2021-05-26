'''Question5) Write a program to sum of natural numbers?'''
number = int(input("Enter a natural number:"))
sum = 0
for i in range(1,number+1):
    sum = sum+i
print("Sum on Natural numbers for the given number = ", sum)