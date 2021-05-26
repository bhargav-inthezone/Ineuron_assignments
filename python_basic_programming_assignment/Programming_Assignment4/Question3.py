'''Question3) Write a program to print the Fibonacci sequence?'''
f0 =0
f1 =1
fibonacci =[f0,f1]
number = int(input("Enter a whole number:"))
if number ==0:
    print("Fibonacci sequence for the given number = ",[0])
elif number==1:
    print("Fibonacci sequence for the given number = ",[1])
elif number<0:
    print("Incorrect input")
for i in range(2,number+1):
    sum = 0
    sum = (i-1)+(i-2)
    fibonacci.append(sum)
print("Fibonacci sequence for the given number = \n", fibonacci)