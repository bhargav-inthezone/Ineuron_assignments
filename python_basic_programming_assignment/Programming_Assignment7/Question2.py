'''Question2) Write a program to find the largest element in the array?'''

n = int(input("Enter the number of elements required in the array"))
array = []

for i in range(0, n):
    element = float(input("Enter the element"))
    array.append(element)

max_ele = max(array)

print("Largest element in the array = ", max_ele)