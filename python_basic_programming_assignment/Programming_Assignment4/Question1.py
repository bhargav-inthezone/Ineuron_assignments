'''Question1) Write a program to factorial the Factorial of a number?'''
number = int(input("enter a number:"))
factorial = 1
if number==0:
    print("Factorial of entered number = ", 1)
else:
    for i in range(1,number+1):
        factorial*=i
print(factorial)