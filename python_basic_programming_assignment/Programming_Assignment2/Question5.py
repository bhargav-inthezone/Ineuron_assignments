'''Question 5) Write a Python program to swap two variables without temp variable?'''
var1 = input("Enter 1st variable:")
var2 = input("Enter 2nd variable:")
print ("before swapping:","\nvar1 =", var1, "var2 =", var2)
var1, var2 = var2, var1
print ("after swapping:","\nvar1 =", var1, "var2 =", var2)