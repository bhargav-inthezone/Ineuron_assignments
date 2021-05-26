'''Question4)Write a program to Check Armstrong Number?'''
number = int(input("Enter a natural number:"))
n = str(number)
s = list(n)
count = len(s)
sum = 0
for i in s:
    x = int(i)
    sum = sum + (x**count)
if sum==number:
    print("Entered number is an Armstrong Number:")
else:
    print("Entered number is not an Armstrong Number")
    
