'''Question5) Write a program to find cube sum of 1st n natural numbers?'''
n = int(input("Enter a natural number:"))


def cube_sum(num):
    sum = 0
    for i in range(1,num+1):
        sum += i**3
    return sum

if n<=0:
    print("Enter a natural number :")
else:
    print(cube_sum(n))