'''Question3 ) Write a program for array rotation?'''

n = int(input("Enter the number of elements required: "))

array = []

for i in range(0, n):
    element = input("Enter the element: ")
    array.append(element)

print("Before rotation :" , "\narray = ", array)

steps = int(input("Enter a positive number for left rotation and a negative number for right rotation: "))

size = len(array)

def rotate_array(array , steps, size):
    if steps >0:
        array[:] = array[steps:size] + array[0:steps]
    elif steps <0:
        steps = size + steps
        array[:] = array[steps:size] + array[0:steps]

    else:
        array = array    
    return array

print("After rotation :" , "\narray = ", rotate_array(array, steps, size))
