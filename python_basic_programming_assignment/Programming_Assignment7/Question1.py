'''Question1) Write a program to finf the sum of an array?'''

n = int(input("Enter the number of elements required:"))

array = []
for i in range(0, n):
    element = float(input("Enter number:"))
    array.append(element)

sum_array = sum(array)

print ("Sum of the elements in the array = ",sum_array)