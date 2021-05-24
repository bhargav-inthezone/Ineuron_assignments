'''Question 4) Write a program to swap two variables'''

var1 = input("Enter 1st variable:")
var2 = input("Enter 2nd variable:")
print('Before swapping:\n',"var1 =", var1, "var2 =",var2 )
empty_bucket = var1
var1 = var2
var2 =empty_bucket
print(print('After swapping:\n',"var1 =", var1, "var2 =",var2 ))