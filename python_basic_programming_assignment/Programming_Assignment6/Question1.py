'''Question1) Write a program to find the Fibonacci sequence using Recursion?'''


# Python program to display the Fibonacci sequence

def fibonacci(n):
   if n == 1:
       return 1
   elif n==2:
       return 1
   elif n>2:
       return(fibonacci(n-1) + fibonacci(n-2))

nterms = int(input("Enter a whole number term:"))

list=[]
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(1,nterms):
       list.append(fibonacci(i))
print(list)