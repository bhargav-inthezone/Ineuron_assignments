'''Question4) Write a program to split the array and attach its first part to the end?'''



n = int(input("Enter the number of elements required: "))

array = []

for i in range(0, n):
    element = input("Enter the element: ")
    array.append(element)
print("before the split", "\narray = ", array)

array[:] = array[1:] + array[0:1]
print("after the split", "\narray = ", array)
